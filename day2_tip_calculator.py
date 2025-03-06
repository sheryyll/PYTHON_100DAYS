# The below code calculates the tip
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
bill_with_tip = bill *tip_percent
total = (bill + bill_with_tip) / people
print(total)
