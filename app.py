from constants import PLAYERS, TEAMS
import random
import string

def clean_data():
    new_players_data = []
    for player in PLAYERS:
        working_dict = {}
        working_dict["name"] = player["name"]
        working_height = player["height"].split(" ")[0]
        working_dict["height"] = int(working_height)
        if player["experience"] == "NO":
            working_dict["experience"] = False
        else:
            working_dict["experience"] = True
        working_list = player["guardians"].split(" and ")
        working_dict["guardians"] = working_list
        new_players_data.append(working_dict)  
    return new_players_data


def balance_teams():
    num_players_per_team = len(PLAYERS) / len(TEAMS)
    unchosen_player_list = clean_data()
    team_player_dict = {}
    for team in TEAMS:
        working_player_list = []
        player_count = 0
        while True:
            if len(unchosen_player_list) != 1:
                random_num = random.randint(0, len(unchosen_player_list) - 1)
            else:
                random_num = 0
            random_player = unchosen_player_list[random_num]
            if player_count < num_players_per_team:
                working_player_list.append(random_player)
                unchosen_player_list.pop(random_num)
                player_count += 1
            else:
                team_player_dict[team] = working_player_list
                break
    return team_player_dict


def stats_tool():
    list_of_balanced_teams = balance_teams()

    main_menu = True
    sub_menu = False

    print("Basketball Team Stats Tool")
    print("----Menu----")
    print("\nHere are your choices:")
    print(" A) Display Team Stats")
    print(" B) Exit")
    
    while main_menu:
        choice = input("Enter an option: ")
        if choice != "A" or choice != "a" or choice != "B" or choice != "b":
            print("Please choose either A or B.")
            continue
        elif choice == "A" or choice == "a":
            sub_menu = True
            break
        else:
            break

    if sub_menu:
        letter_list = list(string.ascii_uppercase)
        chooseable_dict = {}
        chooseable_letter_list = []
        for team in TEAMS:
                print(letter_list[0] + ") " + team)
                chooseable_dict[letter_list[0]] = team
                chooseable_letter_list.append(letter_list[0])
                letter_list.pop(0)
        while True:
            sub_menu_choice = input("\nEnter an option: ")
            if sub_menu_choice not in chooseable_letter_list:
                print("Please choose from the given teams.")
                continue
            else:
                chosen_team = chooseable_dict[sub_menu_choice]
                print("Team: " + chosen_team + " Stats")
                print("-------------------------------")
                total_players = len(list_of_balanced_teams[chosen_team])
                chosen_team_players = list_of_balanced_teams[chosen_team]
                num_experienced = 0
                num_unexperienced = 0
                average_height = 0.0
                total_height = 0.0
                player_list = []
                guardian_list = []
                for player in chosen_team_players:
                    if player["experience"]:
                        num_experienced += 1
                    else:
                        num_unexperienced += 1
                    total_height = total_height + player["height"]
                    player_list.append(player["name"])
                    for guardian in player["guardians"]:
                        guardian_list.append(guardian)
                average_height = total_height / total_players
                player_list_string = ", ".join(player_list)
                guardian_list_string = ", ".join(guardian_list)
                print("\nTotal playres: " + total_players)
                print("Number of experienced playres: " + num_experienced)
                print("Number of unexperienced playres: " + num_unexperienced)
                print("Average height: " + average_height)
                print("\nPlayer list:")
                print(player_list_string)
                print("\nGuardian list:")
                print(guardian_list_string)
                end_program = input("\nPress ENTER to continue")


if __name__ == "__main__":
    stats_tool()