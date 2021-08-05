# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# age to int from str
age1 = int(age)

# years to live in your life
y = 90

# years left in your life
year_left = y - age1

# Months left in your life
months_in_1_Year = 12
months_in_year_Left_Year = year_left * months_in_1_Year

# weeks left in your life
weeks_in_1_Year = 52
weeks_in_year_Left_Year = year_left * weeks_in_1_Year

# days left in your life
days_in_1_Year = 365
days_in_year_Left_Year = year_left * days_in_1_Year

message = f"You have {days_in_year_Left_Year} days, {weeks_in_year_Left_Year} weeks and {months_in_year_Left_Year} months left."

print(message)
