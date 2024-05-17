import constants
import random
from constants import PLAYERS, TEAMS

def clean_data(players):
    cleaned = []
    for player in players:
        fixed = {}
        fixed["name"] = player["name"]
        guardians = player["guardians"].split(" and ")
        fixed["first_guardian"] = guardians[0]
        if len(guardians) > 1:
            fixed["second_guardian"] = guardians[1]
        else:
            fixed["second_guardian"] = None
        fixed["experience"] = player["experience"] == "YES"
        fixed["height"] = int(player["height"].split(" ")[0])
        cleaned.append(fixed)
    return cleaned


def balance_teams(players):
    experienced_players = [player for player in players if player["experience"]]
    inexperienced_players = [player for player in players if not player["experience"]]

    teams = {team: [] for team in TEAMS}
    random.shuffle(experienced_players)
    random.shuffle(inexperienced_players)

    while experienced_players:
        for team_name in TEAMS:
            if experienced_players:
                player = experienced_players.pop()
                teams[team_name].append(player)

    while inexperienced_players:
        for team_name in TEAMS:
            if inexperienced_players:
                player = inexperienced_players.pop()
                teams[team_name].append(player)

    while True:
        for index, team in enumerate(TEAMS, start=1):
            print(f"{index}. {team}")
        choice = input("Please choose a team (1-3) or enter 0 to exit:\n")
        if choice == '0':
            print("\n")
            print("Exiting program...")
            break
        try:
            choice = int(choice)
            if choice < 1 or choice > 3:
                print("Invalid choice.")
                continue
        except ValueError:
            print("Invalid choice.")
            continue

        selected_team_index = choice - 1
        selected_team = TEAMS[selected_team_index]

        team_players = teams[selected_team]
        team_players.sort(key=lambda player: player["height"])
        all_guardians = []
        total_height = 0

        for player in team_players:
            guardians = [player['first_guardian']]
            if player['second_guardian']:
                guardians.append(player['second_guardian'])
            guardians_string = " and ".join(guardians)
            all_guardians.extend(guardians)
            total_height += player["height"]

        average_height = total_height / len(team_players) if team_players else 0
        player_names = [player['name'] for player in team_players]
        player_names_string = ", ".join(player_names)
        player_guardians_string = ", ".join(all_guardians)
        print("\n")
        print(f"<------ {selected_team} Stats: ------>")
        print(f"Team Size: {len(team_players)}")
        print(f"Players: {player_names_string}")
        print(f"# Experienced Players: {len([p for p in team_players if p['experience']])}")
        print(f"# Inexperienced Players: {len([p for p in team_players if not p['experience']])}")
        print(f"Average Height: {average_height:.2f} inches")
        print(f"Guardians: {player_guardians_string}")
        print("\n")

        quit_request = input("Enter '1' to select another team, or '0' to exit:\n")
        print("\n")
        if quit_request == '0':
            print("Exiting program...")
            break

def welcome_message(players):
    if __name__ == "__main__":
        print(" BASKETBALL TEAM STATS TOOL \n")
        print(" -----  MAIN MENU  ----- \n")
        print(" Here are your choices: ")
        print(" A) Display Stats ")
        print(" B) Quit \n")

        quit_request = False
        while not quit_request:
            choice = input(" Please choose below: A OR B \n").upper()
            print("\n")
            if choice == "A":
                balance_teams(players)
                if quit_request == 0:
                    break
            elif choice == "B":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please choose either 'A' or 'B'.")


players = clean_data(constants.PLAYERS)
welcome_message(players)