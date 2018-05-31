from subprocess import *
from random import randrange
from math import factorial

import sys

sys.stdout = open("code.txt", "w")

def to_bin(i):
	return ''.join([str(int(x)) for x in bin(i)[2:]])

def print_it(i):
	global was
	print_i = "print" + i

	if (print_i in was):
		return
	else:
		was.add(print_i)

	print_less = "print" + i[1:]
	print_now = "1"
	if (i[0] == "0"):
		print_now = "0"

	if (i == "0" or i == "1"):
		print(print_i + " _ -> BACK " + print_now + " <")
		return

	print(print_i + " _ -> " + print_less + " " + print_now + " >")
	print_it(i[1:])

print(
'''1
''')

numbers = [to_bin(i) for i in range(6)]
fac = [to_bin(factorial(i)) for i in range(6)]

print("S 0 -> S0 _ >")
print("S 1 -> S1 _ >")
print("BACK 0 -> BACK 0 <")
print("BACK 1 -> BACK 1 <")
print("BACK _ -> AC _ >")
print()


was = set()

for i in range(len(numbers)):
	si = "S" + numbers[i]
	print(si + " 0 -> " + si + "0 _ >")
	print(si + " 1 -> " + si + "1 _ >")
	print(si + " _ -> print" + fac[i] + " _ >")
	print()

for i in fac:
	print_it(i)
	print()

sys.stdout.close()