numbers = input("Enter the numbers(seperated by space) : ")
numbers_list = numbers.split( )
count = 0
for i in numbers_list:
   count = count+1
for i in range(count):
   numbers_list[i] = int(numbers_list[i])
print(numbers_list)
max = numbers_list[0]
for i in numbers_list:
   if i > max:
      max = i
print(max)
