import time

def intro():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious place...")
    time.sleep(2)
    print("You see two paths in front of you.")
    time.sleep(2)
    print("Which path will you choose? (1 or 2)")

def choice():
    choice = input("Enter your choice: ")
    if choice == "1":
        path_one()
    elif choice == "2":
        path_two()
    else:
        print("Invalid choice!")
        choice()

def path_one():
    print("You chose path 1.")
    time.sleep(2)
    print("You encounter a fierce dragon!")
    time.sleep(2)
    print("What will you do? (1: Fight, 2: Run)")

    action = input("Enter your action: ")
    if action == "1":
        print("You bravely fight the dragon!")
        time.sleep(2)
        print("Congratulations! You defeated the dragon and won the game!")
    elif action == "2":
        print("You cowardly run away!")
        time.sleep(2)
        print("You stumble into a dark cave and get lost...")
        time.sleep(2)
        print("Game over!")
    else:
        print("Invalid choice!")
        path_one()

def path_two():
    print("You chose path 2.")
    time.sleep(2)
    print("You find a treasure chest!")
    time.sleep(2)
    print("Do you open it? (1: Yes, 2: No)")

    action = input("Enter your action: ")
    if action == "1":
        print("You open the chest and find a pile of gold!")
        time.sleep(2)
        print("Congratulations! You become rich and win the game!")
    elif action == "2":
        print("You decide not to open the chest.")
        time.sleep(2)
        print("You continue on your journey...")
        time.sleep(2)
        print("Game over!")
    else:
        print("Invalid choice!")
        path_two()

def main():
    intro()
    choice()

if __name__ == "__main__":
    main()