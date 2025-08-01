import random
user_choice = int(input("Enter your choice(0 for rock, 1 for paper, 2 for scissor) : "))
com_choice = random.randint(0,2)
if(user_choice <= 2):
  print(f"Computer's choice is : {com_choice}")
  if(user_choice == com_choice):
   print("Its a draw")
  elif(user_choice == 2 and com_choice == 0):
   print("You lose")
  elif(user_choice == 0 and com_choice == 2):
   print("You win")
  elif(user_choice > com_choice):
   print("You win")
  elif(user_choice < com_choice):
   print("You lose")  
else:
   print("You have entered incorrect choice, so you lose *_* ")
