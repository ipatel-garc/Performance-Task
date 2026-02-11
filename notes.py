

all_entries = [] #Empty List
jokes = {
        "robbers": ["Robbers ", "Calder police – I've been robbed!"],
        "tanks": ["Tanks ", "You are welcome!"],
        "pencils": ["Pencils ", "Nevermind, it's pointless!"]
    }
def joke_game(player_name):  #Parameter
    print(f"Welcome, {player_name}") #Argument

    add_joke = input("Do you want to make your own joke? yes or no:")
    if add_joke == "yes":
        new_joke = input("Enter a joke topic: ")
        joke_start = input("How do you start it?: ")
        punchline = input("Enter punchline: ")

        jokes[new_joke] = [joke_start, punchline]
        print("Now your joke is made and added.")
    
    answer = input("Do you want to hear a joke? yes or no. ")
    print("Available joke topics: ", list(jokes.keys()))
    if answer == "no":
        print("Okay suit yourself!")
        return None, None, None
    
    while answer == "yes":
        choice_question = input("Choose a joke topic. ")

        if choice_question in jokes:
            input("Knock Knock ")
            input(jokes[choice_question][0])
            print(jokes[choice_question][1])
        else:
            print("That’s not an option.")

        answer = input("Do you want to hear another joke or are you finished? ")

    if answer == "finished":
        rate_game = int(input("Rate the game 1–10: "))
        print(str(rate_game * 10) + "% satisfaction rate")

        friend_question = input("Would you recommend this game to a friend? ")
        if friend_question in ("yes", "no"):
            print("Thanks, we appreciate it.")
        else:
            print("Sorry you did not enjoy it.")

        return choice_question, rate_game, friend_question

    return None, None, None


player_name= input("What is your name?")
choice_question, rate_game, friend_question = joke_game(player_name)


if rate_game is not None and friend_question is not None:
    all_entries.append([choice_question, rate_game, friend_question])

print("\n--- List of all entries so far ---")
for entry in all_entries:
    print(entry)
    print("-------------------------------\n")