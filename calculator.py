import os
def add(a , b):
   return a + b
def subtract(a , b):
   return a - b
def multiply(a , b):
   return a * b
def divide(a , b):
   return a / b

operation_dict ={
   "+" : add,
   "-" : subtract,
   "*" : multiply,
   "/" : divide
}
def calculator():
   number_flag = True
   number1 = float(input("Enter the first number : "))
   while number_flag:

      for symbol in operation_dict:
         print(symbol)
      op_symbol = input("Enter the operation : ")
      number2 = float(input("Enter the second number : "))
      calculator_opt = operation_dict[op_symbol]
      output = calculator_opt(number1 , number2)
      print(f"{number1} {op_symbol} {number2} = {output}")
      continueor_no = input("Enter 'y' if you want to continue or 'n' if you want to start over or 'x' to exit" ).lower()
      if continueor_no == 'y':
         number1 = output
      elif continueor_no == 'n':
         number_flag = False
         os.system("clear")
         calculator()
      else:
         number_flag = False
         print("Exiting.....")
         
calculator()



