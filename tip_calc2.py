#Program will;
    #prompt the user for total bill amount, the level of service (good, fair, or bad) and 
    #the amount of ways to split the bill
    #calculate the tip amount, total bill amount and the amount for each person to pay
    #tip amount should be based on level of service (good -> 20%, fair -> 15%, bad -> 10%)

bill_total_input = float(input("Total bill amount? "))
service_level_input = str(input("Level of service? (good, fair, or bad) "))
split_input = int(input("Split how many ways? "))


if service_level_input == "good": 
    tip = .20

elif service_level_input == "fair":
    tip = .15

elif (service_level_input == "bad"):
    tip = .10

tip_output = (bill_total_input * tip)
bill_total = (bill_total_input * tip) + bill_total_input
bill_split = (bill_total / split_input)

print("Tip amount: ","$"+format(tip_output, ",.2f"))
print("Total amount: ","$"+format(bill_total,",.2f"))
print("Amount per person: ","$"+format(bill_split,",.2f"))