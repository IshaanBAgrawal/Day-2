print("Welcome tp the tip calculator.")

total_bill = input("What was the total bill? $")
float_total_bill = float(total_bill)

tip = input('What percentage tip would you like to give? 10, 12 or 15? ')
tip_integer = int(tip) / 100

total_amount = float_total_bill + (float_total_bill * tip_integer)

people = input("How many people to split the bill? ")
people1 = int(people)

money_paid_by_each_person = total_amount / people1
money_paid_by_each_person_rounded = round(money_paid_by_each_person, 2)

print(f"Each person should pay ${money_paid_by_each_person_rounded}.")

print()
print()
