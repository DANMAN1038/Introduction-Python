import random
choice = input("Would you like to go first?(y/n)")
pile = 21
if choice == 'n':
    while pile > 0:
        remove = pile % 4
        pile -= remove
        print("The pile is now: ",pile)
        print('')
        remove_player = int(input("Enter the number to remove: 1, 2, or 3 "))
        if 1 <= remove_player <= 3:
            pile -= remove_player
            print("The pile is now: ",pile)
            print('')
        else:
            print("Not a valid number")
elif choice == 'y':
    while pile > 0:
        player_remove = int(input("Enter the number to remove: 1, 2, or 3 "))
        if 1 <= player_remove <= 3:
            print("The pile is now: ",pile)
            print('')
        else:
            print("Not a valid number")
        remove = pile % 4
        if remove == 0:
            remove = 1
        pile -= remove
        print("The pile is now: ", pile)
        print('')
else:
    print("Number must be 1 or 2")
        
    
