# This file is a collection of methods for testing base n addition TM works
from tm import TM
import random


def tm1_generate_string(chars, blank="B"):
    ret_str = ""
    for _ in range(5):
        ret_str += blank
    for _ in range(random.randint(10, 50)):
        ret_str += chars[random.randint(0, len(chars) - 1)]
    for _ in range(5):
        ret_str += blank
    return ret_str


def tm1_test():
    print("Remove b from ab string:")
    tm = TM("tm1.txt")
    for _ in range(20):
        string = tm1_generate_string("ab")
        print("input:  " + string)
        print("output: " + tm.run(string) + "\n")


def tm2_generate_string(chars, blank="B"):
    ret_str = ""
    for _ in range(5):
        ret_str += blank
    for _ in range(random.randint(5, 25)):
        ret_str += chars[random.randint(0, 1)]
    ret_str += chars[2]
    for _ in range(random.randint(5, 25)):
        ret_str += chars[random.randint(0, 1)]
    for _ in range(5):
        ret_str += blank
    return ret_str


def tm2_test():
    print("Binary addition:")
    tm2 = TM("binary_addition.txt")
    for _ in range(20):
        string = tm2_generate_string("01+")
        print("input:  " + string)
        print("output: " + tm2.run(string) + "\n")


def tm3_generate_string(n, blank="B"):
    ret_str = ""
    for _ in range(5):
        ret_str += blank
    for _ in range(580):
        ret_str += str(random.randint(0, n-1))
    ret_str += "+"
    for _ in range(580):
        ret_str += str(random.randint(0, n-1))
    for _ in range(5):
        ret_str += blank
    return ret_str


def tm3_test():
    n = 10
    print("Decimal addition:")
    tm3 = TM("decimal_addition.txt")
    for _ in range(20):
        string = tm3_generate_string(n)
        print("input:  " + string)
        print("output: " + tm3.run(string) + "\n")
