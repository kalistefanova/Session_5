# virtual bartender
drinks = ["vodka", "whiskey", "gin", "tequila", "rum", "rakia", "sake"]
print("Welcome to the Virtual pub!")
name = input("I am your virtual bartender, how do I call you?")
try:
    age = input(f"How old are you, {name}?")
    age = int(age)
    if age >= 21:
        legal = True
    if age <= 16:
        legal = False
    else:
        country = input(f"Based on your age, I need to ask where are you from")
        legal = False
        if age >= 21:
            legal = True
        elif age >= 18 and country != "USA":
            legal = True
        elif age >= 16 and country == "Luxembourg":
            legal = True
        #else:
            #legal = False - another way of writing that part
        if age > 120 and age < 5:
            print ("Please do not lie to the virtual bartender")
        elif legal:
            print ("You're allowed to drink")
            print(f"Here is a {choice (drinks)} for you")
        else:
            print (f"Dear {name}, unfortunately I am not allowed to serve you")
except ValueError:
    print ("Please give a valid age")

