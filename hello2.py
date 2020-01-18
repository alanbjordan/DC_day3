#Prompts user for a name 
#Prints HELLO with user's name
#Capitalize user's name
#Tells user the number of letters in their name

name_request = input("What is your name? ")

nameCount = len(name_request)

print("HELLO, " + name_request.upper() + "!")
print ("YOUR NAME HAS", nameCount, "LETTERS IN IT! AWESOME!")