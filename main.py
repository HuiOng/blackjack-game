############### Blackjack Project #####################
from replit import clear
from art import logo
import random

starting = input("Do you want to have a game of Black Jack? Type 'y' or 'n'")
if starting == "y":
  starting_bool = True
elif starting == 'n':
  starting_bool = False
else:
  starting = input("You have entered an invalid word. Please type 'y' or 'n'.")
  if starting == "y":
    starting_bool = True
  elif starting == 'n':
    starting_bool = False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def giving_cards(who,num):
  card_number = 0
  for n in range(num):
    who.append(random.choice(cards))
    card_number += 1

def calculate_score(card_list):
  score = 0 
  for n in range(0,len(card_list)):
    if score <= 21:
      number = card_list[n] 
      score += int(number)   
    else:
      if int(card_list[n]) ==11:
        card_list[n] = 1
        number = card_list[n]
        score += int(number)
      else:
        number = card_list[n] 
        score += int(number)
  return score

while starting_bool == True:
  print(logo)
  player_card = []
  comp_card = []
  giving_cards(player_card,2)
  giving_cards(comp_card,2)
  player_score = calculate_score(player_card)
  comp_score = calculate_score(comp_card)
  print(f"Your cards {player_card}, current score: {player_score}")
  print(f"Computer's first card:{comp_card[0]}")
  # Looking for initial Black Jacks
  if comp_score == 21:
    print("Computer got Black Jack! You lose!")
    starting = input("Do you want to have another game of Black Jack? Type 'y' or 'n'")
    if starting == "y":
      clear()
      starting_bool = True
    elif starting == 'n':
      starting_bool = False
  if player_score == 21:
    print("You got Black Jack! You Won!")
    starting = input("Do you want to have another game of Black Jack? Type 'y' or 'n'")
    if starting == "y":
      clear()
      starting_bool = True
    elif starting == 'n':
      starting_bool = False
  
  #for computer
  while comp_score < 17:
    giving_cards(comp_card,1)
    comp_score = calculate_score(comp_card)

  

  player_continue = True
  while player_continue == True:
    cont_ques=input("Type 'y' to get another card, type 'n' to pass:")
    if cont_ques == "y":
      player_continue = True
      giving_cards(player_card,1)
      player_score = calculate_score(player_card)
      print(f"Your cards {player_card}, current score: {player_score}")
      print(f"Computer's first card:{comp_card[0]}")
    elif cont_ques == "n":
      player_continue = False
      print(f"Your final hand:{player_card}, final score: {player_score}")
      print(f"Computer's final hand:{comp_card}, final score: {comp_score}")
      if comp_score > player_score and comp_score <=21:
        print("Computer wins. You lose!")
      elif player_score > 21:
        print("You went over, you lose!")
      elif player_score == 21 :
        print("You won!")
      elif  player_score > comp_score  and player_score <=21:
        print("You won!")
      elif comp_score > 21 and player_score <= 21:
        print("You won!")
      elif comp_score == player_score:
        print("It's a tie")


      starting = input("Do you want to have another game of Black Jack? Type 'y' or 'n'")
      if starting == "y":
        clear()
        starting_bool = True
      elif starting == 'n':
        starting_bool = False

      



  




#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

