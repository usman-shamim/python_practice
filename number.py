while True:
    try:
        x = int(input("what's x?"))
    except ValueError:
        print("X is not an integer")
    else:
        break

print(f"x is {x}")
