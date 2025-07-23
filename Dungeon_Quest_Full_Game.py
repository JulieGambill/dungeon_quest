print("Welcome to Dungeon Quest!  Find treasure and escape traps through 5 dungeon rooms to win!")
print("Enter your player name:")
player_name = input()
print()
print(f"Hello,", player_name + "!", "Good luck on your quest!")
print("Your health starts at 10.")
player_health = 10 #Initial Health Status
player_inventory = []
player_points = 0
print()

#Treaure Dictionary
treasures = {
    'plate': 5,
    'goblet': 10,
    'vase': 20,
    'book': 35,
    'helmet': 50,
    'sword': 60,
    'sheild': 75,
    'necklace': 100
}

#Traps Dictionary
traps = {
    'arrows': 2,
    'monster': 2,
    'rockslide': 2,
    'acidic fog': 2,
    'snare': 2
}
#game play
import random  
dungeon_room = 1
max_rooms = 5
while dungeon_room <= max_rooms and player_health > 0:
    print()
    print('You have entered room:', dungeon_room)
    print('What would you like to do?')
    print('1. Search for treasure.')
    print('2. Move to the next room.')
    print('3. Check health and inventory.')
    print('4. Quit the game.')
    player_choice = input('Enter: 1, 2, 3, or 4: ')
    print()
#player choice
    if player_choice == '1':
        outcome = random.choice(['treasure', 'trap'])
        if outcome == 'trap':
            trap = random.choice(list(traps.keys()))
            player_health -= 2
            print('You encountered:', trap + '!')
            print('You lost 2 health points!')
            print()
        elif outcome == 'treasure':
            treasure = random.choice(list(treasures.keys()))
            player_inventory.append(treasure)
            print('You found ' + treasure + '!')
            print('It is worth ' + str(treasures[treasure]) + ' points!')
            player_points += (treasures[treasure])
            print()
    elif player_choice == '2':
        dungeon_room += 1
        if dungeon_room > max_rooms:
            print('You have completed all rooms! You won!')
            print("Final player stats:")
            print("Health:", player_health)
            print(f"Inventory: {", ".join(items for items in player_inventory)}")
            print("Points:", player_points)
            print()
            break
    elif player_choice == '3':
        print("Current player stats:")
        print("Health:", player_health)
        print(f"Inventory: {", ".join(items for items in player_inventory)}")
        print("Points:", player_points)
        print()
    elif player_choice == '4':
        print('Thank you for playing!')
        print("Final player stats:")
        print("Health:", player_health)
        print(f"Inventory: {", ".join(items for items in player_inventory)}")
        print("Points:", player_points)
        break
    else:
        print('Please enter a choice of 1 - 4.')
if player_health == 0:
    print('You ran out of health! Game Over!')
    print("Final player stats:")
    print("Health:", player_health)
    print(f"Inventory: {", ".join(items for items in player_inventory)}")
    print("Points:", player_points)