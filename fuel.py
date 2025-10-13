def main():
    while True:
        try:
            fraction = input("Fraction: ")
            X, Y = fraction.split("/")
            X = int(X)
            Y = int(Y)
            
            if Y == 0 or X > Y:
                continue

            percent = round((X/Y) * 100)
            break

        except (ValueError, ZeroDivisionError):
            continue
    
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

if __name__ == "__main__":
    main()



