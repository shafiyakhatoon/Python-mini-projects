size = input("Enter the type of pizza(small, medium, large) : ")
bill = 0
if(size == 's' or size == 'S'):
   bill = 100
elif(size == 'm' or size == 'M'):
   bill = 200
else:
   bill = 300
pep = input("Want pepporoni ((y or Y) if yes) : ")
if( pep == 'y' or pep == 'Y'):
   if(size == 's' or size == 'S'):
       bill += 30
   else:
      bill += 50
extra_cheese = input("Do you want extra cheese : ")
if(extra_cheese =='y' or extra_cheese =='Y'):
    bill += 20   
print(f"Total bill is : {bill}")      
