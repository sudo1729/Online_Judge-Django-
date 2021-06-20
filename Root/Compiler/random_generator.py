import string
import random

def getrandom():
    res = ''.join(random.choices(string.ascii_letters + string.digits, k = 5))
    return res