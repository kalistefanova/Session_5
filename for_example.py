sum = 0
for x in range (1, 101):
    sum = sum + x
print (sum)

#let's print the multiplication table until 10
for i in range (1, 11):
    for j in range (1, 11):
        print(f"{1} x {j} = {i*j}")
    print()
