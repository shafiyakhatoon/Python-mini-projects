start = int(input("Enter the number to start : "))
end = int(input("Enter the number to end : "))
till = range(start,end+1)
for number in till:
   if  number % 5 == 0 and number % 3 == 0:
      print("FizzBuzz")
   elif number % 5 == 0:
      print("Buzz")
   elif number % 3 == 0:
      print("Fizz")
   else:
      print(number)

      