#Danial Syed
import random
def play_cards():
    computer_cards = random.sample(range(0,9),3)
    player_cards = random.sample(range(0,9),3)
    print("Let the games begin!")
    print("Player's cards:",player_cards)
    computer_score = 0
    player_score = 0
    index_identity = []
    for i in range(3):
        print()
        print("Round", i+1,":")
        card_choose_a = int(input("Enter the index of the card you would like to play: "))
        if card_choose_a == index_identity:
            print("Invalid. You cannot play the same card twice")
        elif card_choose_a <= 0 or card_choose_a > 3:
            print("Invalid. You are only allowed to be an index between 1-3")
        else:
            index_identity.append(card_choose_a)
            print("You played: ",player_cards[card_choose_a - 1],"Computer played: ", computer_cards[i])
            if player_cards[card_choose_a - 1] > computer_cards[i]:
                player_score += 1
            elif player_cards[card_choose_a - 1] < computer_cards[i]:
                computer_score += 1
            else:
                computer_score += 1
                player_score += 1
        print("Scores: Player", player_score,"Computer", computer_score)
    if computer_score < player_score:
        print("Players Wins!")
    elif computer_score > player_score:
        print("Computer Wins!")
    else:
        print("Draw")
play_cards()
