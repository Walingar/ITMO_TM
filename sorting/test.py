from subprocess import *
from random import randrange
import sys

for test in range(100):
    l = []
    sortedL = []
    for k in range(20):
        i = randrange(1024)
        sortedL.append(i)
        l.append(''.join([str(int(x)) for x in bin(i)[2:]]))
    sortedL = map(lambda i: ''.join([str(int(x)) for x in bin(i)[2:]]), sorted(sortedL))
    print('|'.join(l) + "\n" + '|'.join(sortedL), file=open("a", "w"))
    print(check_output(["java", "-jar", "check.jar", "Check", "a", "sorting.out", "sorting.out"]))
