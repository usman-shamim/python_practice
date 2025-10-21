months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
while True:
    date = input("Date: ").strip()

    if "/" in date:
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except ValueError:
            pass

    elif "," in date:
        try:
            parts = date.replace(",", "").split()
            month_str = parts[0]
            day = int(parts[1])
            year = int(parts[2])
            month= months.index(month_str)+1
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except(ValueError, IndexError):
            pass


    print("Invalid Date formate, try again.")
