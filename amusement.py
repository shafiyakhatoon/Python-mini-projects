height = int(input("Enter ht in feet : "))
bill = 0
if(height >= 3):
   print("You can ride.")
   age = int(input("Enter age : "))
   if(age > 18):
      bill = 500
   elif(age < 12):
      bill = 150
   else:
      bill = 250
   want_pics = input("Want to take photos : ")
   if(want_pics == 'y' or want_pics =='Y'):
         bill = bill + 50
   print(f"Bill is : {bill} " )
else:
   print("Cant ride")
         