name = input("What's your name?")
print ("Hello", name)
age = input("How old are you?")
print (name, "you were born in", 2025 - int(age))
#another way to format print is via f-strings
print (f"{name}, you were born in {2025 - int(age)}")