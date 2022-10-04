# Simple card drawing software
# 2022-09-27
# Jackson Blackman

import random
from PIL import Image
from time import sleep

suit = ["Spade", "Clubs", "Hearts", "Diamonds"]

number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cardsdrawn = []


def carddrawer():
    x = 0
    while x != userchoice:
        rsuit = random.choice(suit)
        rnumber = random.choice(number)
        carddrawn = rnumber + "_of_" + rsuit
        if carddrawn not in cardsdrawn:
            imagetoopen = "C:\\Users\\jblac\\Desktop\\pythonProject\\2022_Grade_12\\Card game\\Images\\" + carddrawn + ".png"
            im = Image.open(imagetoopen + "")
            im.show()
            cardsdrawn.append(carddrawn)
            x = x + 1


userchoice = int(input('Choose an amount of cards to draw \n:'))
carddrawer()
print(cardsdrawn)
sleep(100)
