# Ask user for their name remove space from str and capitalize
name = input("what is your name? ").strip().title()

first, last = name.split(" ")

# say hello to user
print(f"hello, {first}")
