import random
names = input("Enter the customer's names separated by commas: ")
lucky = names.split(",")
lenght=len(lucky)
print(f"Customers are : {lucky}")
random_name = random.randint(1,lenght-1)
print(f"{lucky[random_name]} pays the bill")
