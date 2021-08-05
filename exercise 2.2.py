# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight1 = int(weight)
height1 = float(height)

BMI = int(( weight1 ) // (height1 ** 2))
BMI1 = str(BMI)

print("Your BMI is " + BMI1)
