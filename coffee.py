profit = 0
Menu = {
   "latte" : {
      "ingredients" : {
         "water" : 200,
         "milk" : 150,
         "coffee" : 24
      }, 
      "cost" : 150
   } ,
   "espresso" : {
      "ingredients" : {
         "water" : 150,
         "milk" : 100,
         "coffee" : 20
      } ,
      "cost" : 200
   } ,
   "cappuccino" : {
      "ingredients" : {
         "water" : 220,
         "milk" : 130,
         "coffee" : 26
      },
      "cost" : 210
   } ,
}
resources = {
   "water" : 1000,
   "milk" : 500,
   "coffee" : 450
}
is_on = True
def make_coffee(coffee_name,coffee_ingredient):
   for item in coffee_ingredient:
      resources[item] -= coffee_ingredient[item]
   print(f"Here is your {coffee_name}... Enjoy")

def process_coins():
   print("Please enter coins \n")
   total = 0
   coins_five = int(input("How many 5Rs coins💰: "))
   coins_ten = int(input("How many 10Rs coins💰 : "))
   coins_twenty = int(input("How many 20Rs coins💰 : "))
   total = coins_five * 5 + coins_ten * 10 + coins_twenty * 20
   return total
def is_payment_successful(money , coffee_cost):
   if money >= coffee_cost:
      global profit
      profit += coffee_cost
      change = money - coffee_cost
      print(f"Here is your Rs{change} 🪙 in change.")
      return True
   else:
      print("Sorry that's not enough money. Money refunded.")
      return False
   
def check_resources(order_ingredients):
   for item in order_ingredients:
      if order_ingredients[item] > resources[item]:
         print(f"Sorry there is not enough {item}")
         return False
   return True

while is_on:
   choice = input("What would you like to have? (Latte/Cappuccino/Espresso) : ").lower()
   if choice == 'off':
      is_on = False
   if choice == "report":
      print("🧾" )
      print(f"Water = {resources['water']}ml")
      print(f"Milk = {resources['milk']}ml")
      print(f"Coffee = {resources['coffee']}ml")
      print(f"Money = Rs{profit}")
      
   
   elif choice in Menu:
     coffee_type = Menu[choice]
     print(coffee_type)
     if check_resources(coffee_type['ingredients']):
         payment = process_coins()
         if is_payment_successful(payment , coffee_type["cost"]):
            make_coffee(choice , coffee_type['ingredients'] )
   else:
         print("Invalid choice....")