from math import sqrt
import sys

def is_prime(num):
    if num == 1 or num == 2:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(sqrt(num)) + 1, 6):
        if num % i == 0:
            return False

    for i in range(7, int(sqrt(num)) + 1, 6):
        if num % i == 0:
            return False

    return True


for num in sys.argv:
    try:
        num = int(num)
    except:
        continue

    if is_prime(num) == True:
        print(f'{num} is a prime number')

