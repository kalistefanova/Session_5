name = input("What's your name?")
print ("Hello", name)
age = input("How old are you?")
try:
    #another way to format print is via f-strings
    print (f"{name}, you were born in {2025 - int(age)}")
    #division = int(age)/ 0
except ValueError:
    print("Age must be a valid number.")
    print(f"The value that you typed was {age}")
except ZeroDivisionError:
    print("You can't divide by zero.")
except: #all the other types of exceptions!
    print("No idea what else can go wrong, but just in case.")
else: #in case no exception happen
    print("Thanks for being a good sport and not trying to crush the app!")
finally: #this runs in the end no matter what
print("Thank you for playing!")