#CFG Final Project by Hannah and Ari
#Top Trumps
#This is a small game using the Pokemon API, where players compare stats, similar to the Top Trumps card game.
# The basic flow of the games is:
# 1. You are given 3 random cards with different stats
# 2. You select one card and one of the stats
# 3. Another random card is selected for your opponent (the computer)
# 4. The stats of the two cards are compared
# 5. The player with the stat higher than their opponent wins

#-----------CODE----------
#Import the libraries needed for the program
import random
import requests
import time

#Function to get a random pokemon and its stats from the Poke on API
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
}

#Function to print random Pokemons
def print_stats(user, selected_pokemon):
    print('{}'.format(user),'pokemon name is {}'.format(selected_pokemon['name']))
    print('{}'.format(user),'pokemon ID is {}'.format(selected_pokemon['id']))
    print('{}'.format(user),'pokemon height is {}'.format(selected_pokemon['height']),'cm')
    print('{}'.format(user),'pokemon weight is {}'.format(selected_pokemon['weight']),'kg')

#Program gets the name of the user and asks for the number of rounds
name_user=input("Whats your name: ")
number_of_rounds=input("How many rounds do you want to play?: ")

#If the input of the user is not a number, it outputs error and asks again
while number_of_rounds.isnumeric() != True:
    print("Invalid Option, try again")
    number_of_rounds = input("How many rounds do you want to play? (You must enter a number): ")

#Variable declaration
number_of_rounds = int(number_of_rounds)
number=0
user_winning_counter=0
opponent_winning_counter=0

#For loop to repeat the contents for the selected number of rounds
for number in range(number_of_rounds):
    round_number=number+1
    #Generates 3 random pokemon and prints them on the screen, so the user can see their options
    print("THIS IS ROUND {}".format(round_number))
    my_pokemon1 = random_pokemon()
    print("-----This is your first choice-----")
    print_stats('Your first choice', my_pokemon1)
    my_pokemon2 = random_pokemon()
    print("-----This is your second choice-----")
    print_stats('Your second choice', my_pokemon2)
    my_pokemon3 = random_pokemon()
    print("-----This is your third choice-----")
    print_stats('Your third choice', my_pokemon3)

    #Let the user choose one of the pokemons, outputs an error if none of the options is written and asks again
    choose_pokemon = input("Choose your pokemon (Options: pokemon 1, pokemon 2, pokemon 3): ")
    while (choose_pokemon != "pokemon 1") and (choose_pokemon != "pokemon 2") and (choose_pokemon != "pokemon 3"):
        print('Error, choose again')
        choose_pokemon = input("Choose your pokemon (You must enter one of these options: pokemon 1, pokemon 2, pokemon 3): ")

    #If statement to store the selection in a variable, which will be used in the rest of the program
    if choose_pokemon == "pokemon 1":
        my_pokemon = my_pokemon1
        print("-----You chose Pokemon 1-----")
    elif choose_pokemon == "pokemon 2":
        my_pokemon = my_pokemon2
        print("-----You chose Pokemon 2-----")
    elif choose_pokemon == "pokemon 3":
        my_pokemon = my_pokemon3
        print("-----You chose Pokemon 3-----")

    #Print chosen pokemon again
    print_stats('Your chosen', my_pokemon)

    #Asks the user for the stat to use, outputs an error if a different option is written and asks again
    stat_choice= input("Choose your stat (Options: id, weight, height): ")
    while stat_choice != "weight" and stat_choice != "height" and stat_choice != "id":
        print("Invalid Option, try again")
        stat_choice= input("Choose your stat (You must enter one of these options: id, weight, height): ")

    #Generates a random pokemon for the opponent (computer) and prints it on the screen
    opponents_pokemon = random_pokemon()
    print_stats("Opponent", opponents_pokemon)

    #If statement to compare the players stats and select the winner
    if my_pokemon[stat_choice] > opponents_pokemon[stat_choice]:
        print('Your opponents stat is less than yours. You WIN this round')
        user_winning_counter += 1
        round_winner = "------The winner of this round is " + name_user + "------" + "\n"
    elif my_pokemon[stat_choice] < opponents_pokemon[stat_choice]:
        print('Your opponents stat is greater than yours. You LOSE this round')
        opponent_winning_counter += 1
        round_winner = "------The winner of this round is the Computer------" + "\n"
    else:
        print('Your opponents stat is equal than yours. Its a DRAW in this round')
        round_winner = "------This round ends in a Draw------" + "\n"

    #The code used from line 111 to line 119, allows the program to save the results of eacn round in a file
    #the user can review the contents of the file "pokemon.txt" at the end of the game

    text_round_number= "ROUND " + str(round_number) + "\n"
    user_pokemon_choice_name= name_user + 's pokemon name is ' + my_pokemon['name'] + "\n"
    user_stat_choice = "The stat chosen was " + str(stat_choice) + " with a value of " + str(my_pokemon [stat_choice]) + "\n"
    opponents_pokemon_name = "Opponents" + ' pokemon name is ' + opponents_pokemon['name'] + "\n"
    opponent_stat_choice = "The stat chosen was " + str(stat_choice) + " with a value of " + str(opponents_pokemon[stat_choice]) + "\n"

    with open('pokemon_game.txt', 'a') as pokemon_file:
        text = text_round_number + user_pokemon_choice_name + user_stat_choice + opponents_pokemon_name + opponent_stat_choice + round_winner
        pokemon_file.write(text)

    #This command gives a pause in between rounds
    time.sleep (5)

#If statement that determines the overall winner of the game
if user_winning_counter > opponent_winning_counter:
    print("The final score is {}".format(user_winning_counter), "to {}.".format(opponent_winning_counter), "CONGRATULATIONS! YOU ARE THE WINNER OF THE GAME")
    winner_statement = "-----------END-----------" + "\n" + "The winner of the game is " + name_user
elif user_winning_counter < opponent_winning_counter:
    print("The final score is {}".format(user_winning_counter), "to {}.".format(opponent_winning_counter), "YOU LOST THIS TIME, TRY AGAIN")
    winner_statement = "-----------END-----------" + "\n" + "The winner of the game is the Computer"
else:
    print("The final score is {}".format(user_winning_counter), "to {}.".format(opponent_winning_counter), "THE GAME ENDS IN A DRAW")
    winner_statement = "-----------END-----------" + "\n" + "The game ended in a Draw"

    #This command allows the program to save the winner of the game in a file
    #the user can review the contents of the file "pokemon.txt" at the end of the game

with open('pokemon_game.txt', 'a') as pokemon_file:
    text = winner_statement
    pokemon_file.write(text)

print("THANKS FOR PLAYING :)")





