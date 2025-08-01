import math
number = int(input("Enter a number : "))

def prime(number):
   is_prime = True
   if number == 1:
      is_prime = False
   for i in range(2 , (number//2) + 1):
      if number % i == 0:
         is_prime = False
   if is_prime:
      print("It is a prime number")
   else:
      print("It is not a prime number")
prime(number)
