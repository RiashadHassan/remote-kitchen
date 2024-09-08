import random
import string


def generate_random_order_no():
    digits = random.randint(100000, 999999)
    letters = ""

    for i in range(4):
        char = random.choice(string.ascii_uppercase)
        letters += char

    return "#" + str(digits) + str(letters)
