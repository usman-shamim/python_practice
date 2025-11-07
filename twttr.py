def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(s):
    vowels = "aeiouAEIOU"
    result = ""
    for c in s:
        if c not in vowels:
            result += c
    return result


if __name__ == "__main__":
    main()
