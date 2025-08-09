print("welcome to tip calculator")
bill=float(input("how much the bill amount ? $"))
tip=int(input("how much the tip is ?10,20,or 30"))
people=int(input("how many people are gonna split the bill?"))
total_bill=tip/100*bill+bill
amount_per_person=total_bill/people
print(f"the amount need to be paid by each one is ${amount_per_person}")
