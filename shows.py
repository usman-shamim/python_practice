SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    " Jimmy Neutron",
    "the Proud family "
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print(", ".join(cleaned_shows))

main()