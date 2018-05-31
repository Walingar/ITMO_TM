from subprocess import *
from random import randrange
from math import factorial
import sys

for i in range(0, 31):
    bin_i = [str(int(x)) for x in bin(i)[2:]]
    bin_fact = [str(int(x)) for x in bin(factorial(i))[2:]]
    print(' '.join(bin_i) + "\n" + ' '.join(bin_fact), file=open("a", "w"))
    print(check_output(["java", "-jar", "Check.jar", "Check", "a", "code.txt", "code.txt"]))
