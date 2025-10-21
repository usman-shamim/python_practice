groceries = {}

while True:
    try:
        item = input("").strip().upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
    except EOFError:
        print()
        break

for item in sorted(groceries.keys()):
    print(groceries[item], item)

