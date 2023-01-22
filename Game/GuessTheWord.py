import os
import random

def game_data():
    answers = {
        "word-length-2": [
            ["hi", ["A kid waving to another", "A man waving towards you", "A kid waving across the door", "A couple waving to someone on the phone"]],
            ["tv", ["A family celebrating to a sport game", "A family watching something", "A guy getting entertained in his sofa", "A couple eating popcorn"]],
            ["ai", ["A human and robot hand pointing at each other", "A robot thinking", "A headless humanoid with glowing brain", "A woman getting facial recognition"]],
            ["go", ["A woman walking", "An athlete in ready stance before running", "Green light indication for racing", "A person in ready for running stance"]],
            ["me", ["A kid pointing himself", "A woman pointing to herself", "Two friends pointing at themselves", "A person pointing to themselves in the mirror"]],
        ],
        "word-length-3": [
            ["tie", ["A well suited man", "A man preparing his wear for neck", "A knot of rope", "A red ribbon"]],
            ["key", ["A locked doorknob", "A selfie of an elephant", "An unique characteristic of an elf", "Something you can insert"]],
            ["dot", ["A dice rolling around", "A dress with point design", "Something with URL to complete the address link", "That"]],
            ["dip", ["A strawberry with chocolate partner", "Touching your dry foot in a pond", "Nachos with guacamole", "Dry brush about to touch the paint"]],
            ["net", ["World Wide Web", "Global", "A boundary for separate team", "A middle wall"]],
        ],
        "word-length-4": [
            ["baby", ["A newborn human", "A duckling", "A group of kittens", "A cute newborn kitty"]],
            ["tool", ["A heavy duty pliers", "A hammer smashin a nail", "A mobile drilling machine", "A Screw driver and clamp"]],
            ["gift", ["Kids getting presents", "A box with ribbons", "12am of December 25", "Santa's delivery"]],
            ["toast", ["A fire yellow warning sign", "A bonfire", "A bread whose overcooked", "Red color of human for warning"]],
            ["star", ["A rating system", "A red carpet event", "Constellations", "A VIP"]],
        ],
        "word-length-5": [
            ["mouse", ["A hardware device that allows to move the cursor", "A rat", "A trap with cheese", "Logitech"]],
            ["horse", ["A rocking toy chair for kids", "A knight in chess", "A cowboys partner", "Unicorn"]],
            ["italy", ["Pizza", "Eiffell Tower", "Venice Canal", "Leaning tower"]],
            ["round", ["A globe", "A pregnant woman's tummy", "A basketball", "A shiny marble"]],
            ["queen", ["An important member of bee hive", "Bohemian Rhapsody", "Important piece of a chess", "Royalty"]],
        ],
        "word-length-6": [
            ["animal", ["A herd of Elepants", "A cute kitten and puppy", "A herd of sheeps looking at you", "A squirrel jumping to each tree"]],
            ["cowboy", ["A typical county hat", "A catching rope", "A horse", "Good old clapping boots"]],
            ["circus", ["Tiger and Rabbit on a colorful ball", "A typically red and white tent", "A host performing with lion", "A clown juggling colorful balls"]],
            ["statue", ["Statue of Liberty", "Christ the redeemer", "A Golden Buddha", "Eastern islands Maoi"]],
            ["strike", ["A bowling game getting all pins down", "A kid punching", "A group of workers doing protest", "A fighter jet intercepting"]],
        ],
    }
    return answers

def start_program():
    ALL_STAGE_FINISHED = False
    
    # Accounts
    accounts = {
        # Test account
        "demo": {
            "password": "pass1234",
            "points": 9999,
        }
    }

    def registerAccount():
        while True:
            print("\nREGISTRATION FORM")
            input_username = input("Enter username: ")
            input_password = input("Enter password: ")
            if not input_username in accounts:
                # Create default values
                accounts[input_username] = {
                    "password" : input_password,
                    "points" : 0,
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

    def text_content(request):
        game_title = [
            
            "============================================================================",
            "   _______  __   __  _______  _______  _______    _______  __   __  _______ ",
            "  |       ||  | |  ||       ||       ||       |  |       ||  | |  ||       |",
            "  |    ___||  | |  ||    ___||  _____||  _____|  |_     _||  |_|  ||    ___|",
            "  |   | __ |  |_|  ||   |___ | |_____ | |_____     |   |  |       ||   |___ ",
            "  |   ||  ||       ||    ___||_____  ||_____  |    |   |  |       ||    ___|",
            "  |   |_| ||       ||   |___  _____| | _____| |    |   |  |   _   ||   |___ ",
            "  |_______||_______||_______||_______||_______|    |___|  |__| |__||_______|",
            "   _     _  _______  ______    ______                                       ",
            "  | | _ | ||       ||    _ |  |      |                                      ",
            "  | || || ||   _   ||   | ||  |  _    |                                     ",
            "  |       ||  | |  ||   |_||_ | | |   |                                     ",
            "  |       ||  |_|  ||    __  || |_|   |                                     ",
            "  |   _   ||       ||   |  | ||       |                                     ",
            "  |__| |__||_______||___|  |_||______|                                      ",
            "                                                                            ",
            "============================================================================",
            "\n",
        ]
        if request.lower() == "show-gt":
            for x in game_title:
                print(x)

    def showContext(difficulty, stage):
        if difficulty in game_data():
            print("\n[STAGE " + str(stage) + "] (" + difficulty + ")")
            print("Here's your hint:")
            index = 0
            for hint in game_data()[difficulty][stage-1][1]:
                index+=1
                print("Hint-"+ str(index) +":", hint)
            return game_data()[difficulty][stage-1][0] # answer
            exit()
        else:
            print("Difficulty ", difficulty, "not found in the game data.")
            return exit() # Exit code because of error

    def checkPlayerAnswer(answer, username):
        while True:
            user_input = input(">> ")
            if answer == user_input:
                print("You got that right! Awesome!")
                
                get_random_points = random.randint(15, 100)
                player_points = accounts[username]["points"] = accounts[username].get("points") + get_random_points # reward

                print("You got " + str(get_random_points) + " points!")
                return True
            else:
                print("Input is not right at all, try again.")
    
    def gameEnded(username):
        # Game ended
        print("\n\nCONGRATULATIONS ON WINNING!")
        print("You earn " + str(accounts[username].get("points")) + " points while playing.")
        print("\n Would you like to try again?")
        print("[1] Yes")
        print("[2] No")
        while True:
            tryAgain = input(">> ")
            if tryAgain == "1":
                startGame()
            elif tryAgain == "2":
                print("\nThanks for playing!")
                exit()
            else:
                print("Invalid input try again.")

    def startGame():
        clearscreen()
        text_content("show-gt")
        print("[1] Login")
        print("[2] Register")
        print("[3] Tutorials (Recommended)")
        while True:
            first_prompt = input(">> ")
            if first_prompt == "1":
                # login
                while True:
                    print("\n[LOGIN FORM]")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    if checkAccount(username, password):
                        print("\nYour task is to guess the word by using the 4 given sentence/word given by the game.\n")
                        print("Choose what difficulty:")
                        print("[1] 2-word length")
                        print("[2] 3-word length")
                        print("[3] 4-word length")
                        print("[4] 5-word length")
                        print("[5] 6-word length")
                        while True:
                            difficulty = input(">> ")
                            if difficulty == "1":
                                # 2 word
                                answer = showContext('word-length-2', 1)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-2', 2)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-2', 3)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-2', 4)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-2', 5)
                                checkPlayerAnswer(answer, username)
                                gameEnded(username)
                            elif difficulty == "2":
                                # 4 word
                                answer = showContext('word-length-3', 1)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-3', 2)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-3', 3)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-3', 4)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-3', 5)
                                checkPlayerAnswer(answer, username)
                                gameEnded(username)
                            elif difficulty == "3":
                                # 6 word
                                answer = showContext('word-length-4', 1)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-4', 2)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-4', 3)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-4', 4)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-4', 5)
                                checkPlayerAnswer(answer, username)
                                gameEnded(username)
                            elif difficulty == "4":
                                # 6 word
                                answer = showContext('word-length-5', 1)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-5', 2)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-5', 3)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-5', 4)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-5', 5)
                                checkPlayerAnswer(answer, username)
                                gameEnded(username)
                            elif difficulty == "5":
                                # 6 word
                                answer = showContext('word-length-6', 1)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-6', 2)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-6', 3)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-6', 4)
                                checkPlayerAnswer(answer, username)
                                answer = showContext('word-length-6', 5)
                                checkPlayerAnswer(answer, username)
                                gameEnded(username)
                            else:
                                print("\nInvalid input, try again.")
                    else:
                        print("\nInvalid username or password.")
                        print("[1] Try again")
                        print("[2] Register")
                        while True:
                            invalid = input(">> ")
                            if invalid == "2":
                                registerAccount()
                            elif invalid == "1":
                                break
                            else:
                                print("Invalid input, try again.")
                                
            elif first_prompt == "2":
                # register
                registerAccount()
            elif first_prompt == "3":
                # tutorials
                print("\n\n[TUTORIAL]")
                print("* Your task is to guess the word with the help of hints and the number of letter it requires.")
                print("* Example:")
                print("*\tHint-1: Tophat with Bunny")
                print("*\tHint-2: A fantasy power")
                print("*\tHint-3: The talent of a well-suited man with white gloves")
                print("*\tAnswer: magic")
                while True:
                    print()
                    if input("Enter 'y' to exit: "):
                        startGame()
                    else:
                        print("Invalid input, try again.")
            else:
                print("Invalid input, try again.")
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


start_program()