import os
def get_highbidder(bidder_winner):
   high_bid = 0
   winner = " "
   for bidder in bidder_winner:
      price = bidder_winner[bidder]
      if price > high_bid:
         high_bid = price
         winner = bidder
   print(f"The winner is {winner} with a bid price of {high_bid}")


bidder_info = {}
more_bidder = False
while not more_bidder:  
   name = input("Enter the player's name : ")
   amount = int(input("Enter the bid amount of the player : "))
   bidder_info[name] = amount
   choice = input("Are there any another player's (yes/no) : ").lower()
   if choice == "no":
      more_bidder = True
      get_highbidder(bidder_info)
   elif choice == "yes":
      os.system("clear")