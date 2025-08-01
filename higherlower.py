import random
import os
data = [
    {
        "Name": "Cristiano Ronaldo",
        "Description": "footballer",
        "Country": "Portugal",
        "Followers": 630
    },
    {
        "Name": "Selena Gomez",
        "Description": "singer and actress",
        "Country": "USA",
        "Followers": 430
    },
    {
        "Name": "Virat Kohli",
        "Description": "cricketer",
        "Country": "India",
        "Followers": 270
    },
    {
        "Name": "Lionel Messi",
        "Description": "footballer",
        "Country": "Argentina",
        "Followers": 520
    },
    {
        "Name": "Kylie Jenner",
        "Description": "model and entrepreneur",
        "Country": "USA",
        "Followers": 410
    },
    {
        "Name": "Narendra Modi",
        "Description": "Prime Minister",
        "Country": "India",
        "Followers": 90
    },
    {
        "Name": "Taylor Swift",
        "Description": "singer-songwriter",
        "Country": "USA",
        "Followers": 270
    },
    {
        "Name": "Tom Holland",
        "Description": "actor",
        "Country": "UK",
        "Followers": 80
    },
    {
        "Name": "MrBeast",
        "Description": "YouTuber and philanthropist",
        "Country": "USA",
        "Followers": 210
    },
    {
        "Name": "BTS",
        "Description": "K-pop group",
        "Country": "South Korea",
        "Followers": 330
    },
    {
    "Name": "Dwayne Johnson",
    "Description": "actor and wrestler",
    "Country": "USA",
    "Followers": 395
},
{
    "Name": "Billie Eilish",
    "Description": "singer-songwriter",
    "Country": "USA",
    "Followers": 120
},
{
    "Name": "Zendaya",
    "Description": "actress and singer",
    "Country": "USA",
    "Followers": 190
},
{
    "Name": "Emma Watson",
    "Description": "actress and activist",
    "Country": "UK",
    "Followers": 75
},
{
    "Name": "Robert Downey Jr.",
    "Description": "actor",
    "Country": "USA",
    "Followers": 110
},
{
    "Name": "Kylian Mbappé",
    "Description": "footballer",
    "Country": "France",
    "Followers": 120
},
{
    "Name": "Anushka Sharma",
    "Description": "Actress",
    "Country": "India",
    "Followers": 70
},
{
    "Name": "PewDiePie",
    "Description": "YouTuber",
    "Country": "Sweden",
    "Followers": 25
}

]
contine_flag = True
score = 0
account_1 = random.choice(data)
while contine_flag:
   
   account_2 = random.choice(data)
   while account_1 == account_2:
      account_2 = random.choice(data)
   def check_answer(followers_count1, followers_count2 ):
      if followers_count1 > followers_count2:
         if guess == 1:
          
            return True
            
         else:
            
            return False
      else:
         if guess == 1:
            return False
         else:
            return True

   def detailsof_person(account):
      name = account["Name"]
      description = account["Description"]
      country = account["Country"]
      return f"{name} , a {description}, rom {country}"
   

   print(f"Compare 1 : {detailsof_person(account_1)}")
   print("VS")
   print(f"Compare 2 : {detailsof_person(account_2)}")
   guess = int(input("Whose has more followers (1 or 2) : "))
   followers_count1 = account_1["Followers"]
   followers_count2 = account_2["Followers"]

   is_correct = check_answer(followers_count1, followers_count2)
   if is_correct:
      score += 1
      if followers_count1 > followers_count2:
           account_1 = account_1
      else:
         account_1 = account_2
      print(f"You are right , Your score is {score}")
      os.system("clear")
      
      
   else:
      print(f"You lose. Your score is {score}")
      contine_flag = False
      




   









