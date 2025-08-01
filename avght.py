user_val = input("Enter the heights of persons sepearted by commas(in cm) : ")
height = user_val.split(",")
sum = 0
count = 0
for i in height:
   count = count+1
for i in range(count):
  height[i] = int(height[i])
print(height)
for i in height:
   sum = sum + i
avg_ht = int(sum/count)
print(f"The average height is : {avg_ht}")