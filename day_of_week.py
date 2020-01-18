#Program;
    #prompts the user for a day number
    #converts a numeric string to a number
    #print the day of the week based on given number

day_input = int(input(' Day (0-6)? '))
day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(day_list[day_input])


