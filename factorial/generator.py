from subprocess import *
from random import randrange
from math import factorial

import sys

sys.stdout = open("factorial.out", "w")

def to_bin(i):
	return ''.join([str(int(x)) for x in bin(i)[2:]])



print(
'''start: S
accept: AC
reject: RJ
blank: _

''')

numbers = [to_bin(i) for i in range(31)]
fac = [to_bin(factorial(i)) for i in range(31)]

print("S 0 -> prepare 0 <")
print("S 1 -> prepare 1 <")
print("prepare _ -> prepare' w <")
print("prepare' _ -> toS 0 >")
print("toS w -> getNumber w >")
print("getNumber 0 -> S0 0 >")
print("getNumber 1 -> S1 1 >")


was = set()

for i in range(len(numbers)):
	si = "S" + numbers[i]
	print(si + " 0 -> " + si + "0 0 >")
	print(si + " 1 -> " + si + "1 1 >")
	print(si + " _ -> print" + fac[i] + " _ <")
	print()

for i in fac[1:]:
	print_i = "print" + i
	print_ix0 = print_i + "x0"
	print_ix1 = print_i + "x1"
	print_iback = print_i + "back"
	print_iget = print_i + "get"
	max_counter = len(i) - 1

	# clear to 0w_
	print(print_i + " 0 -> " + print_i + " _ <")
	print(print_i + " 1 -> " + print_i + " _ <")
	print()

	# print first
	print(print_i + " w -> " + print_ix1 + " w >")
	print()

	# HOWTO print 0
	print(print_ix0 + " 0 -> " + print_ix0 + " 0 >")
	print(print_ix0 + " 1 -> " + print_ix0 + " 1 >")
	print(print_ix0 + " w -> " + print_ix0 + " w >")
	print(print_ix0 + " _ -> " + print_iback + " 0 <")
	print()

	# HOWTO print 1
	print(print_ix1 + " 0 -> " + print_ix1 + " 0 >")
	print(print_ix1 + " 1 -> " + print_ix1 + " 1 >")
	print(print_ix1 + " w -> " + print_ix1 + " w >")
	print(print_ix1 + " _ -> " + print_iback + " 1 <")
	print()

	# HOWTO back
	print(print_iback + " 0 -> " + print_iback + " 0 <")
	print(print_iback + " 1 -> " + print_iback + " 1 <")
	print(print_iback + " w -> " + print_iget + " w <")
	print()

	# get 0/1 from counter
	for counter in range(max_counter):
		if (i[counter + 1] == '0'):
			print(print_iget + " " + str(counter) + " -> " + print_ix0 + " " + str(counter + 1) + " >")
		else:
			print(print_iget + " " + str(counter) + " -> " + print_ix1 + " " + str(counter + 1) + " >")
		print()
	
	# when all written
	print(print_iget + " " + str(max_counter) + " -> END _ >")
	print()

print("END w -> AC _ >")



# print(len(was))

sys.stdout.close()