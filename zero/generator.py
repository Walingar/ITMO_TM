import sys
 
sys.stdout = open("zero.out", "w")
 
print('''start: s
accept: ac
reject: rj
blank: _
s _ -> ac _ ^
s 0 -> n _ >
n 0 -> s _ >
n _ -> rj _ >''')
 
sys.stdout.close()