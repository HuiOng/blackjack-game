############### Blackjack Project #####################
from replit import clear
from art import logo
import random

starting = input("Do you want to have a game of Black Jack? Type 'y' or 'n':")
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
      if len(card_list)>=3:
        if int(card_list[n]) ==11:
         card_list[n] = 1
         number = card_list[n]
         score += int(number)
        else:
          number = card_list[n]
          score += int(number)
      else:
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
    elif starting == "n":
      starting_bool = False
      player_continue = False
      print("End of game")
  if player_score == 21:
    print("You got Black Jack! You Won!")
    starting = input("Do you want to have another game of Black Jack? Type 'y' or 'n'")
    if starting == "y":
      clear()
      starting_bool = True
    elif starting == "n":
      starting_bool = False
      player_continue = False
      print("End of game")
  if player_score == 22 :
    print("You got Double Aces! Amazing! You Won!")
    starting = input("Do you want to have another game of Black Jack? Type 'y' or 'n'")
    if starting == "y":
      clear()
      starting_bool = True
    elif starting == "n":
      starting_bool = False
      player_continue = False
      print("End of game")
  if comp_score == 22 :
    print("Computer got Double Aces! You Lose!")
    starting = input("Do you want to have another game of Black Jack? Type 'y' or 'n'")
    if starting == "y":
      clear()
      starting_bool = True
    elif starting == "n":
      starting_bool = False
      player_continue = False
      print("End of game")
  

  
  #for computer
  while comp_score < 17 :
    giving_cards(comp_card,1)
    comp_score =calculate_score(comp_card)
      
      
    

  

  player_continue = True
  while player_continue == True:
    cont_ques=input("Type 'y' to get another card, type 'n' to pass:")
    if cont_ques == "y":
      player_continue = True
      giving_cards(player_card,1)
      player_score = calculate_score(player_card)
      print(f"Your cards {player_card}, current score: {player_score}")
      print(f"Computer's first card: {comp_card[0]}")
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
      if player_score <=21 and len(player_card)==5 :
        print("You got 5 cards Charlie(五龙)! You Won!")
      if comp_score <=21 and len(comp_card)==5 :
        print("Computer got 5 cards Charlie(五龙)! You Lose!")
    

      starting = input("Do you want to have another game of Black Jack? Type 'y' or 'n'")
      if starting == "y":
        clear()
        starting_bool = True
      elif starting == "n":
        starting_bool = False
        player_continue = False
        print("End of game")

      
