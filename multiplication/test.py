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
    for jk in range(10, 100):
        i = randrange(0, 10000)
        j = randrange(0, 10000)
        ij = i * j
        bin_i = [str(int(x)) for x in bin(i)[2:]]
        bin_j = [str(int(x)) for x in bin(j)[2:]]
        bin_ij = [str(int(x)) for x in bin(ij)[2:]]
        print(' '.join(bin_i) + " * " + ' '.join(bin_j) + "\n" + ' '.join(bin_ij), file=open("a", "w"))
        print(check_output(["java", "-jar", "Check.jar", "Check", "a", "code.txt", "code.txt"]))