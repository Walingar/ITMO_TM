from subprocess import *
from random import randrange
import sys

def baseb(n, b):
    e = n // b
    q = n % b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return baseb(e, b) + str(q)

for ik in range(10, 100):
    i = randrange(50000, 100000)
    bin_i = [str(int(x)) for x in bin(i)[2:]]

    print(' '.join([x for x in baseb(i, 3)]) + "\n" + ' '.join(bin_i), file=open("a", "w"))
    print(check_output(["java", "-jar", "Check.jar", "Check", "a", "code.txt", "code.txt"]))