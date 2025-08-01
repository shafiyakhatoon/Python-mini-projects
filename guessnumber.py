import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def difficulty_level(level):
   if level == 'easy':
      return EASY_LEVEL_ATTEMPTS
   else:
       return HARD_LEVEL_ATTEMPTS
def check_answer(guess_number,answer,attempts):
   if guess_number < answer:
      print("Number is too low")
      return attempts-1
   elif guess_number > answer:
      print("Number is too high")
      return attempts-1
   else:
      print(f"You guessed corect, answer is {answer} ")



def guess_the_number() :
   print("Welcome to Guess the number Game")
   print("Let me think of a number between 1 to 50")
   answer = random.randint(1,50)
   level = input("Enter level of difficulty.. choose easy or hard : ").lower()
   attempts = difficulty_level(level)
   guess_number = 0

   while guess_number != answer :
      print(f"You have {attempts} attempts left : ")
      guess_number = int(input("Guess a number : "))
      attempts = check_answer(guess_number,answer,attempts)
      if attempts == 0:
         print("You are out of your guesses.. You lose")
         return
      elif guess_number != answer:
         print("Guess again")
guess_the_number()