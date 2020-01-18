#Program will; 
    #request missing information from user (name and favorite school subject)
    #fill in the missing information based on user's input
    #title case user's name


print("Please fill in the blanks below: ")

print("___(name)___'s favorite subject in school is ___(subject)___.")

user_name = input("What is your name? ").title()

fav_subject = input("What is your favorite subject in school? ")

print(user_name+"'s favorite subject in school is" , fav_subject+".")

