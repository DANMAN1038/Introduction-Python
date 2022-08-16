import random
#This function randomly assigns who is odds and evens as well as the numbers player 1 and 2 choose
#No parameters since everything is random
#The evaluated values that are printed are the scores of either player and the winner
def play_odds_evens():
     #randomly assigns which player is odds or evens
     choice = random.randint(1,2)
     player_1_score = 0
     player_2_score = 0
     #starts on first turn, not 0 since that would equate to 6 rounds
     rounds = 1
     if choice == 1:
          player_1 = 'odds'
          player_2 = 'evens'
     else:
          player_1 = 'evens'
          player_2 = 'odds'
     #This function keeps going through until the number of rounds is past 5
     while rounds <= 5:
          #Randomly assigning which number each player chooses
          player_1_draw = random.randint(1,3)
          player_2_draw = random.randint(1,3)
          #Calculates the sum of both cards drawn
          total = player_1_draw + player_2_draw
          #Conditional if statements that determine who wins
          if total % 2 == 0 and player_1 == 'evens':
               player_1_score += 1
          elif total % 2 == 0 and player_2 == 'evens':
               player_2_score += 1
          elif total % 2 == 1 and player_1 == 'odds':
               player_1_score += 1
          #We can use an else assigned with a valid outcome here since there are no possibility of errors as the numbers are not inputed
          else:
               player_2_score += 1
          rounds += 1
     if player_1_score > player_2_score:
          winner = "Player 1"
     #Once again, there is no chance at a draw, since there are an odd number of rounds and the sum will always be either odd or even
     else:
          winner = "Player 2"
     #\n print new lines which allow me to organize the scores and winner
     print('Player 1','(',player_1,'):',player_1_score, '\nPlayer 2','(',player_2,'):',player_2_score, "\nThe winner is:",winner)
#Calls function
play_odds_evens()
