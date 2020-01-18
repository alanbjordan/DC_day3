#Program will;
    #prompt the user for a number in degrees Celsius
    #convert the value to degrees in Fahrenheit
    #display converted temperature

celsius_input = int(input("Temperature in C?: "))

fahrenheit_output = (celsius_input * 1.8) + 32

print(fahrenheit_output,"F")