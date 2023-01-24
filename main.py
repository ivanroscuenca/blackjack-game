############### Blackjack Project #####################

import random
from art import logo
from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def calculate_score(cards):
  if sum(cards)==21 and len(cards) ==2:
    return 0
  if 11 in cards and sum(cards) >21:
    #cards.insert(0,1)
    #cards.remove(11)
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score,computer_score):
  if user_score==computer_score:
    return "That's a draw"
  elif computer_score==0 or user_score >21:
    return "Computer Wins"
  elif user_score==0 or computer_score>21:
    return "User wins"
  elif user_score>computer_score:
    return "User wins"
  else:
    return "Computer wins"

def play():
  print(logo)
  
  user_cards =[]
  computer_cards=[]
  is_game_over=False

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score= calculate_score(computer_cards)
    print(f"The cards of user are: {user_cards}, current score is : {user_score}")
    print(f"The first card of computer is: {computer_cards[0]}")
    
    if user_score == 0 or computer_score==0 or user_score>21:
      is_game_over=True
    else:
     user_should_deal= input("Do you want to draw another card. If yes, then write 'y' if not, then write 'n': ")
     if user_should_deal=='y':
      user_cards.append(deal_card())
     else:
       is_game_over=True
    
  while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score= calculate_score(computer_cards)
  
  print(f"Your final hand : {user_cards}, final score: {user_score}")
  print(f"computer hand : {computer_cards}, final score: {computer_score}")
  print(compare(user_score,computer_score))
    
while input("Do tou wanna play blackjack : 'y' for yes and 'n' for no: ")=='y':
  clear()
  play()

print("Thank you to enter in this program")
    
  
  
               

