import inflect

p= inflect.engine()
i = []

while True:
    try:
        j = input("Name: ")
        i.append(j)
    except EOFError:
        print()
        break

farewell = p.join(i)

print(f"Adieu, adieu, to {farewell}")
