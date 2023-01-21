#
# Game: Adventure Deluxe
# Type: Text-Adventure RPG
# Date: January 21, 2023
# Utilizing local saving of accounts and the usage of object-oriented programming.


import os
import time
import random

ALL_STAGE_FINISHED = False
def start_program():

    # Accounts
    accounts = {
        # Test account
        "demo": {
            "password": "demopassword1234",
            "status": {
                'hp': 99999,
                'damage': 99999,
                'gold': 99999,
            },
        }
    }

    # Data or Information of NPC/Mobs
    enemies = {
            "Goblin" : {"hp" : 500, "damage" : [5, 6]},
            "Troll" : {"hp" : 900, "damage" : [5, 15]},
            "Evil King" : {"hp" : 3000, "damage" : [25, 50]},
        }

    # Main brain for the game
    # Requires the parameter of logged-in account
    def adventure(logged_in_account):
        animations("game-title", True, .05)
        # Copy player stats
        thisPlayer = accounts[logged_in_account]
        # Plot
        def stages():
            def showStats():
                print("\n")
                print("PLAYER:","Mr. Knight")
                print("HP: ", thisPlayer.get('status').get('hp'))
                print("Damage: ", thisPlayer.get('status').get('damage'))
                print("Gold: ", thisPlayer.get('status').get('gold'))
            def showMobStats(mob):
                print("\n")
                print("MOB:", mob)
                print("HP: ", enemies[mob].get("hp"))
                print("Damage: ", enemies[mob].get('damage'))
            def checkIfPlayerDied(hp):
                if hp <= 0:
                    return True
                else:
                    return False
            def checkIfMobDied(hp):
                if hp <= 0:
                    return True
                else:
                    return False

            # Stage 1
            showStats()
            print("\n[STORY]")
            time.sleep(1)
            print("As you've started your adventure, you've encountered a hostile Goblin")
            time.sleep(1)
            print("You tried to run away from the monster but its manner is not that easily can be fend off.")
            time.sleep(1)
            print("Now you have no choice but to fight it.")
            # Create new object for NPC
            mob_1 = enemies["Goblin"]
            while True:
                # prompt
                print("[1] Sword Fight")
                print("[2] Run Away")
                input_move = input(">> ")
                if input_move == "1":
                    animations('sword-fight', False, 0.005)
                    # Make randomize damage
                    mob_damage = random.randint(mob_1.get('damage')[0], mob_1.get('damage')[1]) # min, max
                    player_damage = random.randint(thisPlayer.get('status').get('damage')[0], thisPlayer.get('status').get('damage')[1]) # min, max
                    mob_new_hp = mob_1.get('hp') - player_damage
                    player_new_hp = thisPlayer.get('status').get('hp') - mob_damage

                    thisPlayer.get('status')['hp'] = player_new_hp
                    mob_1['hp'] = mob_new_hp
                    print("oof! that was a good fight.")
                    if checkIfPlayerDied(player_new_hp):
                        print("Game Over")
                        print("You died in miserable way.")
                        print("Try again in next life.")
                        exit()
                    if checkIfMobDied(mob_new_hp):
                        print("You've successfully killed the Goblin!")
                        print("25 Gold is added to your wallet. Congratulations!")
                        thisPlayer.get('status')['gold'] = thisPlayer.get('status').get('gold') + 25 # Increment gold
                        break # end fight
                    else:
                        showStats()
                        showMobStats("Goblin")
                elif input_move == "2":
                    print("Running away is not considered a strength of a knight. Disgraceful.")
                    print("The Goblin seems looking at you fiercely, quick choose your move!")
            # Stage 2
            print("\n\n")
            print("[STORY]")
            time.sleep(1)
            print("As you wander the world and by using the map, you come accross the house of the giants")
            time.sleep(1)
            print("Trolls who stinks, and with high HP faced upon you way.")
            time.sleep(1)
            print("Let's see who wins this fight.")
            # Create NPC
            mob_2 = enemies["Troll"]
            while True:
                # prompt
                print("[1] Sword Fight")
                print("[2] Run Away")
                input_move = input(">> ")
                if input_move == "1":
                    animations('sword-fight', False, 0.005)
                    # Make randomize damage
                    mob_damage = random.randint(mob_2.get('damage')[0], mob_2.get('damage')[1]) # min, max
                    player_damage = random.randint(thisPlayer.get('status').get('damage')[0], thisPlayer.get('status').get('damage')[1]) # min, max
                    mob_new_hp = mob_2.get('hp') - player_damage
                    player_new_hp = thisPlayer.get('status').get('hp') - mob_damage

                    thisPlayer.get('status')['hp'] = player_new_hp
                    mob_2['hp'] = mob_new_hp
                    print("oof! that was a good fight.")
                    if checkIfPlayerDied(player_new_hp):
                        print("Game Over")
                        print("You died in miserable way.")
                        print("Try again in next life.")
                        exit()
                    if checkIfMobDied(mob_new_hp):
                        print("You've successfully killed the Troll!")
                        print("55 Gold is added to your wallet. Congratulations!")
                        thisPlayer.get('status')['gold'] = thisPlayer.get('status').get('gold') + 55 # Increment gold
                        break # end fight
                    else:
                        showStats()
                        showMobStats("Troll")
                elif input_move == "2":
                    print("Running away is not considered a strength of a knight. Disgraceful.")
                    print("The Troll seems looking at you fiercely, quick choose your move!")
            # Stage 3 (Final)
            print("\n\n")
            print("[STORY]")
            time.sleep(1)
            print("You're now in the tip of your destination.")
            time.sleep(1)
            print("You also can feel it, the menacing gaze of an aura.")
            time.sleep(1)
            print("You've been swallowed up by the darkness.")
            time.sleep(1)
            print("Loading...")
            time.sleep(5)
            print("You've fallen through the dungeon of the Evil King. He's laughing at you.")
            time.sleep(1)
            print("You proked him, and it works.")
            time.sleep(1)
            print("Now, your final goal is in your palm.")
            time.sleep(1)
            print("The show must go on!")
            time.sleep(1)
            print("Save the queen and survive!")
            # Create NPC
            mob_3 = enemies["Evil King"]
            while True:
                # prompt
                print("[1] Sword Fight")
                print("[2] Run Away")
                input_move = input(">> ")
                if input_move == "1":
                    animations('sword-fight', False, 0.005)
                    # Make randomize damage
                    mob_damage = random.randint(mob_3.get('damage')[0], mob_3.get('damage')[1]) # min, max
                    player_damage = random.randint(thisPlayer.get('status').get('damage')[0], thisPlayer.get('status').get('damage')[1]) # min, max
                    mob_new_hp = mob_3.get('hp') - player_damage
                    player_new_hp = thisPlayer.get('status').get('hp') - mob_damage

                    thisPlayer.get('status')['hp'] = player_new_hp
                    mob_3['hp'] = mob_new_hp
                    print("oof! that was a good fight.")
                    if checkIfPlayerDied(player_new_hp):
                        print("Game Over")
                        print("You died in miserable way.")
                        print("Try again in next life.")
                        exit()
                    if checkIfMobDied(mob_new_hp):
                        print("You've successfully killed the Evil King!")
                        print("You got the Evil King's ring. It seems you can use this in the future.")
                        print("1500 Gold is added to your wallet. Congratulations!")
                        thisPlayer.get('status')['gold'] = thisPlayer.get('status').get('gold') + 1500 # Increment gold
                        break # end fight
                    else:
                        showStats()
                        showMobStats("Evil King")
                elif input_move == "2":
                    print("Running away is not considered a strength of a knight. Disgraceful.")
                    print("The Evil King seems looking at you fiercely, quick choose your move!")

        stages()
        # Ending
        print("\n\n[STORY]")
        time.sleep(1)
        print("You've found the prison room of the Princess.")
        time.sleep(1)
        print("She was thankfull")
        time.sleep(1)
        print("Both of you escaped the place of the Evil King")
        time.sleep(1)
        print("The Kingdom did a celebration for saving the Princess.")
        time.sleep(1)
        print("3 years later... ")
        time.sleep(3)
        print("The Princess fell in love with you and now you both are married.")
        time.sleep(1)
        print("And the story goes by. you both went to happily ever after.")
        exit()


        
    # Register
    def registerAccount():
        while True:
            print("\nREGISTRATION FORM")
            input_username = input("Enter username: ")
            input_password = input("Enter password: ")
            if not input_username in accounts:
                # Create default values
                accounts[input_username] = {
                    "password" : input_password,
                    "status" : {
                        "hp" : 1500,
                        "damage" : [35, 150],
                        "gold" : 10, # poor :D
                    }
                }
                break
            else:
                print("It seems the username", input_username, "is already taken. Try again.")
        startGame()

    # Verify the player account
    def checkAccount(username, password):
        if username in accounts and accounts[username].get("password") == password:
            return True
        else:
            return False

    # Necessary, I guess?
    def tutorials():
        print("\n\nTUTORIAL & INFO: ")
        time.sleep(1)
        print("* In this game, you will be the main character!")
        time.sleep(1)
        print("* Your task is to save the princess of emerald which has been kidnapped by the evil king.")
        time.sleep(1)
        print("* This game is basically an adventure text game based.")
        time.sleep(1)
        print("* A selection of to-do will be shown in you're going to choose each of options so that your adventure progress.")
        time.sleep(1)
        print("* So... Goodluck with your adventure Mr. Knight!")
        time.sleep(1)
        while True:
            restart = input("Type 'y' to restart: ")
            if restart.lower() == "y":
                startGame()
                break
            else:
                print("Invalid input. Try again.")

    # Main
    def startGame():
        animations("game-title", True, .105)
        print("═══════════════════════════════════════════════════════════")
        print("[1] Login")
        print("[2] Register")
        print("[3] Tutorial (Recommended)")
        print("[4] Exit")
        # Used a while-loop so that we can check if the input are valid vice-versa.
        while True:
            if ALL_STAGE_FINISHED == False:
                input_1 = input(">> ")
                if input_1 == "1":
                    while True:
                        print("")
                        input_username = input("Enter username: ")
                        input_password = input("Enter password: ")
                        # Invoking/Calling the function so that we can check if the account inputted is in the accounts stored.
                        if checkAccount(input_username, input_password):
                            adventure(input_username)
                            break
                        else:
                            # Self-explanatory logic here.
                            print("\nInvalid username or password. Would you like to try again? or register?")
                            print("[1] Try again")
                            print("[2] Register")
                            input_tryAgain = input(">> ")
                            if input_tryAgain != "1":
                                # Shortcut to registering account function.
                                registerAccount()
                elif input_1 == "2":
                    registerAccount()
                    break
                elif input_1 == "3":
                    # Calling the tutorial function
                    tutorials()
                    break
                elif input_1 == "4":
                    # Kill the entire program.
                    exit()
                else:
                    # Detect the input if it result as invalid.
                    print("Invalid input, Try again.")
            else:
                print("You've succeeded saving the princess. I guess this is the moment for once upon a time that ends with happily ever after right?")
                print("Thanks for playing the game.")
                exit()
    
    # Call function
    startGame()

# This function utilize the usage of terminal of the operating system
# so that the program can clear the command screen for visual representation.
def clearscreen():
    command = ""
    if os.name in ("nt", "dos"):
        command = "cls"
    else:
        command = "clear"
    os.system(command) # Call the computer's terminal and execute the command.

# This function manages the "animation" frame-by-frame of some panels.
def animations(request, clear : bool, speedVertical : int):
    frames = []
    if request.lower() == "sword-fight":
        frames.clear()
        frame_1 = [
                    "---------------------------------",
                    "|      /\               /\      |",
                    "|     /  \             /  \     |",
                    "|     |  |             |  |     |",
                    "|     |  |             |  |     |",
                    "|     |  |             |  |     |",
                    "|     |  |             |  |     |",
                    "|     |  |             |  |     |",
                    "|    Oo--oO           Oo--oO    |",
                    "|      ||               ||      |",
                    "|      ||               ||      |",
                    "|     (__)             (__)     |",
                    "---------------------------------",
                ]
        frame_2 = [
                    "---------------------------------",
                    "|      /\               /\      |",
                    "|     /  \             /  \     |",
                    "|     |  |             |  |     |",
                    "|     |  |             |  |     |",
                    "|     |  |             |  |     |",
                    "|     |  |             |  |     |",
                    "|     /  /             \  \     |",
                    "|   Oo--oO             Oo--oO   |",
                    "|    / /                 \ \    |",
                    "|   / /                   \ \   |",
                    "|  (__)                   (__)  |",
                    "---------------------------------",
                ]
        frame_3 = [
                    "---------------------------------",
                    "|           ^       ^           |",
                    "|          / \     / \          |",
                    "|         /  /     \  \         |",
                    "|        /  /       \  \        |",
                    "|       /  /         \  \       |",
                    "|      /  /           \  \      |",
                    "|     /  /             \  \     |",
                    "|   Oo--oO             Oo--oO   |",
                    "|    / /                 \ \    |",
                    "|   / /                   \ \   |",
                    "|  (__)                   (__)  |",
                    "---------------------------------",
                ]
        frame_4 = [
                    "---------------------------------",
                    "|             ^   ^             |",
                    "|            / \ / \            |",
                    "|           /  / \  \           |",
                    "|          /  /   \  \          |",
                    "|         /  /     \  \         |",
                    "|        /  /       \  \        |",
                    "|       /  /         \  \       |",
                    "|     Oo--oO         Oo--oO     |",
                    "|      / /             \ \      |",
                    "|     / /               \ \     |",
                    "|    (__)               (__)    |",
                    "---------------------------------",
                ]
        frame_5 = [
                    "---------------------------------",
                    "|             ^   ^             |",
                    "|            / \ / \            |",
                    "|    -----------------------    |",
                    "|    |   CLANG     CLANG   |    |",
                    "|    |   CLANG     CLANG   |    |",
                    "|    |   CLANG     CLANG   |    |",
                    "|    -----------------------    |",
                    "|     Oo--oO         Oo--oO     |",
                    "|      / /             \ \      |",
                    "|     / /               \ \     |",
                    "|    (__)               (__)    |",
                    "---------------------------------",
                ]
        frames.append(frame_1)
        frames.append(frame_2)
        frames.append(frame_3)
        frames.append(frame_4)
        frames.append(frame_5)
    elif request.lower() == "game-title":
        frame_1 = [
                    "                                                  ",                                
                    " █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗",    
                    "██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝",   
                    "███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  ",  
                    "██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  ",    
                    "██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗",    
                    "╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝",    
                    "                                                  ",                                
                    "██████╗ ███████╗██╗     ██╗   ██╗██╗  ██╗███████╗",                                
                    "██╔══██╗██╔════╝██║     ██║   ██║╚██╗██╔╝██╔════╝",                                
                    "██║  ██║█████╗  ██║     ██║   ██║ ╚███╔╝ █████╗",                                  
                    "██║  ██║██╔══╝  ██║     ██║   ██║ ██╔██╗ ██╔══╝",                                  
                    "██████╔╝███████╗███████╗╚██████╔╝██╔╝ ██╗███████╗",                                
                    "╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝",                                                                                 
                    "                                                  ",                                
                ]
        frames.append(frame_1)
    # Start animating
    for frame in frames:
        if clear: 
            clearscreen()

        for vertical_pixels in frame:
            if speedVertical >= 0 and not speedVertical < 0:
                time.sleep(speedVertical)
            print(vertical_pixels)
        # Delay per frame
        time.sleep(1)
    return


# Starts here.
start_program()