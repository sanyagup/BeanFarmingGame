import random

starting_cards_names = ['Red Bean', 'Blue Bean', 'Cocoa Bean', 'Garden Bean', 'Black-Eyed Bean', 'Soy Bean', 'Wax Bean', 'Coffee Bean', 'Chili Bean', 'Stink Bean', 'Green Bean']
starting_cards_values = [(2,3,4,5), (4,6,8,10), (2,3,4), (2,3), (2,4,5,6), (2,4,6,7), (4,7,9,11), (4,7,10,12), (3,6,8,9), (3,5,7,8), (3,5,6,7)]
starting_cards_numbers = [8,20,4,6,10,12,22,24,18,16,14]
intital_number_of_cards = 154

# # Initialize the list with a tuple
# my_list = [1, 2, (5, 6), 3, 4]

# # Access the tuple at index 2
# tuple_at_index_2 = my_list[2]

# # Access the elements within the tuple
# element_5 = tuple_at_index_2[0]
# element_6 = tuple_at_index_2[1]

# # Print the elements
# print("Element 5:", element_5)
# print("Element 6:", element_6)

number_of_players = int(input("Welcome to the game!! (Max amount of players 7, minimum 2) Enter the amount of players you want: "))
#assign 5 cards to each player
player1=['','','','','']
player2=['','','','','']
player3=['','','','','']
player4=['','','','','']
player5=['','','','','']
player6=['','','','','']
player7=['','','','','']

player1_farm= [('',0),('',0)]
player2_farm=[('',0),('',0)]
player3_farm=[('',0),('',0)]
player4_farm=[('',0),('',0)]
player5_farm=[('',0),('',0)]
player6_farm=[('',0),('',0)]
player7_farm=[('',0),('',0)]

adding_cards = starting_cards_names
if number_of_players == 2:
    for i in range(5):
        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player1[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player2[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

if number_of_players == 3:
    for i in range(5):
        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player1[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player2[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player3[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

if number_of_players == 4:
    for i in range(5):
        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player1[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player2[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player3[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player4[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

if number_of_players == 5:
    for i in range(5):
        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player1[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player2[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player3[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player4[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player5[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

    
if number_of_players == 6:
    for i in range(5):
        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player1[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player2[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player3[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player4[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player5[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player6[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

if number_of_players == 7:
    for i in range(5):
        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player1[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player2[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player3[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player4[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player5[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player6[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

        index = random.randint(0,len(adding_cards)-1)
        if starting_cards_numbers[index] > 0:
            player7[i] = adding_cards[index]
            starting_cards_numbers[index] -= 1

counter = 1

print(f'Round {counter}')
print(player1)
print(player2)
print()
answer = input('Player 1. Do you want to take one or two of these cards into your farm? (type yes), else do you want to trade? (type no if this is the case): ')
if answer == 'yes':
    answer1 = int(input('Player 1 only one or two? (Type value): '))
    print(player1)
    if answer1 == 1:
        card_type = input('Enter card type: ')
        index = starting_cards_names.index(card_type)
        starting_cards_numbers[index] -= 1
        farm_number = int(input("Which farm do you want to add it to?: "))
        print(farm_number)
        if farm_number == 1:
            print(player1_farm[0][0]+' here')

        elif farm_number == 2:
             # Access the tuple at index 2
            tuple_at_index_2 = player1_farm[0]

            # Access the elements within the tuple
            element_5 = tuple_at_index_2[0]
            element_6 = tuple_at_index_2[1]
        else: 
            # Access the tuple at index 2
            tuple_at_index_2 = player1_farm[0]

            # Access the elements within the tuple
            element_5 = tuple_at_index_2[0]
            element_6 = tuple_at_index_2[1]

