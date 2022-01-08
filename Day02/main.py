print("Welcome to the Tip Calculator!\n")

# Receiving the bill value
bill = float(input("What was the total bill? $"))

# Choosing the tip percentage
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Number of people to split the bill
split = int(input("How many people to split the bill? "))

# Calculator
bill_with_tip = tip / 100 * bill + bill

bill_per_person = round(bill_with_tip / split, 2)

# print the final result
print(f"Each person should pay ${bill_per_person}.\n")