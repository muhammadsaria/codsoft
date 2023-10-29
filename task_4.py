import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        else:
            return False
    elif comp == 's':
        if you == 'r':
            return True
        else:
            return False
    elif comp == 'p':
        if you == 's':
            return True
        else:
            return False
        

        
while True:
    print("Comp's turn: Enter rock(r), paper(p), or scissor(s)? ")
    r = random.randint(1, 3)
    if r == 1:
        comp = 'r'
    elif r == 2:
        comp = 's'
    elif r == 3:
        comp = 'p'

    you = input("Your turn: rock(r), paper(p), or scissor(s)? ")

    result = game(comp, you)
    print(f"Comp chose: {comp}")
    print(f"You chose: {you}")

    if result == None:
        print("The game is a tie")
    elif result:
        print("You won!")
    else:
        print("You lose")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break





