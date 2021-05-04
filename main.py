# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lovers = name1 + name2
lovers =  lovers.lower()
# print(lovers)

totalTrue = str(lovers.count('t') + lovers.count('r') + lovers.count('u') + lovers.count('e'))
totalLove = str(lovers.count('l') + lovers.count('o') + lovers.count('v') + lovers.count('e'))

scoreLove = int(totalTrue + totalLove)
message = ''

if scoreLove < 10 or scoreLove > 90:
  message = f"Your score is {scoreLove}, you go together like coke and mentos."
elif scoreLove >= 40 and scoreLove <= 50:
  message = f"Your score is {scoreLove}, you are alright together."
else:
  message = f"Your score is {scoreLove}."

print(message)
