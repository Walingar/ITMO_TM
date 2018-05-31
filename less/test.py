from subprocess import *
from random import randrange
import sys

for ik in range(10, 100):
    for jk in range(10, 100):
        i = randrange(100000000, 10000000000)
        j = randrange(100000000, 10000000000)
        bin_i = [str(int(x)) for x in bin(i)[2:]]
        bin_j = [str(int(x)) for x in bin(j)[2:]]
        print(' '.join(bin_i) + " < " + ' '.join(bin_j) + "\n" + str(i < j), file=open("a", "w"))
        print(check_output(["java", "-jar", "Check.jar", "Check", "a", "code.txt", "code.txt"]))
