import random

J=11
Q=12
K=13
A=14
cards=[2,3,4,5,6,7,8,9,10,J,Q,K,A]
deck=cards*4
random.shuffle(deck)

def game():
  
  user_card = random.choice(deck)
  cpu_card = random.choice(deck)
  
  # deck.remove(user_card)
  # deck.remove(cpu_card)
  
  user_hand = []
  cpu_hand = []
  
  if user_card > cpu_card:
    user_hand.insert(0, user_card)
    user_hand.insert(0, cpu_card)
    print("You won this round!")
    print(len(user_hand))
  elif user_card < cpu_card:
    user_hand.insert(0, user_card)
    user_hand.insert(0, cpu_card)
    print("The cpu won this round!")
    print(len(cpu_hand))
  if user_card == cpu_card:
    cpu_tie = random.choice(cards)
    user_tie = random.choice(cards)
    deck.remove(cpu_tie)
    deck.remove(user_tie)
    
    print("Cards are equal... WAR!!!!!")
    if user_tie > cpu_tie:
      for i in range(1,4):
        user_hand.insert(0, cpu_tie)
        user_hand.insert(0, user_tie)
        print("You won this war!")
        print(len(user_hand))
        
    elif user_tie < cpu_tie:
      for i in range(1,4):
        cpu_hand.insert(0, cpu_tie)
        cpu_hand.insert(0, user_tie)
        print("The cpu won this war!")
        print(len(user_hand))
        
  else:
    print("Doesn't work")
        
  if len(user_hand) > len(cpu_hand):
    print("Your'e winning!")
    
  elif len(user_hand) < len(cpu_hand):
    print("The cpu is winning!")
    
def main ():
  cont = True
  while cont == True:
    game()
    
    user_ans = input("Would you like to play the next hand?: ")
    if user_ans == ('yes', "Yes", "Y", "y"):
      cont = True
    elif user_ans == ("no", "No", "n", "N"):
      cont = False
    else:
      print("Error")
      
    if len(deck) > 0:
      cont = True
    else:
      cont = False
    
main()