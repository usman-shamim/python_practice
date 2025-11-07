x = input("what is x? ")
y = input("what is y? ")

# here i am using round for 2 digits
z = round(float(x) + float(y), 2)

# this is just for add coma after 3 digits
print(f"{z:,}")

# another way
i = int(input("what is i? "))
j = int(input("what is j? "))

# same thing as above
print(f"{i + j:.2f}")
