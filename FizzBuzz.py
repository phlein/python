#asks the user to enter an integer
#and tests if the entered integer is divisible by 5, 3 or both (and prints Buzz, Fizz or Fizzbuzz, respectively)
#also let's the user know if zero was entered.
try:
    number = int(input("Please enter an integer: "))
    

    if number == 0:
        print("You entered zero.")
    elif number%5 == 0 and number%3 == 0:
        print("FizzBuzz")
    elif number%5 == 0:
        print("Buzz")
    elif number%3 == 0:
        print("Fizz")
    else:
        print("You entered: ")
        print(number)
#prints an error message if the user entered a non-integer
except:
    ValueError: print("Error. User did not enter an integer.")