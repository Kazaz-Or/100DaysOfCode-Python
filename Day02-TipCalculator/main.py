#100 DaysOfCode - Days 2 - Day02-TipCalculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give in %?"))
number_of_people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / number_of_people

final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount}$")

