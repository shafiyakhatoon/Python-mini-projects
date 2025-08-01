import random
#choice = int(input("Choose heads or tail(0 - tail, 1 - head) : "))
side = random.randint(0, 1)
if(side == 1):
   print("Head")
else:
   print("Tail")