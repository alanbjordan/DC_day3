#Program will;
    #prompt the user for a day of the week
    #print "Go to work" if the day is Monday - Friday
    #print "Sleep in" if the day is Saturday or Sunday


day_input = int(input("What is the day of the week? Enter 0-6: "))
day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

day_output = day_list[day_input]

if day_output == ("Saturday") or day_output == ("Sunday"):
    print("Sleep in")
else:
    print("Go to work")



