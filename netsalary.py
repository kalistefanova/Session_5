print("Welcome to the Net Salary Calculator")
try:
    gross = input("What's your gross salary?")
    gross = int(gross)
    if gross < 1000:
        tax_rate = 10
    elif gross < 2000:
        tax_rate = 12
    elif gross < 4000:
        tax_rate = 14
    else:
        tax_rate = 18

    tax = (tax_rate / 100) * gross

    try:
        kids = input("How many kids do you have?")
        kids = int(kids)
        if gross < 2000:
            tax_cut = (1/100) * gross
        else:
            tax_cut = (0.5/100) * gross

        tax -= kids * tax_cut

        tax = max(0, tax)

        net_salary = gross - tax
        print(f"Your net salary is, {net_salary}!")

    except ValueError:
            print("It seems like your input for the number of kids is invalid. Please enter a valid number.")

except ValueError:
    print("It seems like your input for gross salary is invalid. Please enter a valid number.")

print("Thank you for using the Net Salary Calculator. Hope that helped!")
