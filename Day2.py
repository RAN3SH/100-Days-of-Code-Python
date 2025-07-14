print("Welcome to the tip caluclator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10 12 15 "))
bill_with_tip = (bill) + (bill * (tip/100))
people = int(input("How many people to split the bill? "))
each_person_bill = bill_with_tip / people
print(f"Each person should pay: ${each_person_bill}")
