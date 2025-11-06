import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)
    s = input("Input: ")
    print(figlet.renderText(s))

elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    fonts = figlet.getFonts()
    if sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
        s = input("Input: ")
        print(figlet.renderText(s))
    else:
        sys.exit("Invalid font name")

else:
    sys.exit("Invalid usage")
