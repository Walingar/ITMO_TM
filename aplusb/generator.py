import sys
 
sys.stdout = open("aplusb.out", "w")
 
print('''start: S
reject: RJ
accept: AC
blank: _
 
S 0 -> S 0 >
S 1 -> S 1 >
S 2 -> S 2 >
S 3 -> S 3 >
S + -> S + > 
S _ -> B _ <
 
B 0 -> B0 _ <
B 1 -> B1 _ <
B + -> complete _ <
 
complete _ -> AC _ >
complete 2 -> complete 0 <
complete 0 -> complete 0 <
complete 3 -> complete 1 <
complete 1 -> complete 1 <
complete + -> AC + ^
 
B0 0 -> B0 0 <
B0 1 -> B0 1 <
B0 + -> simple_add_0 + <
 
B1 0 -> B1 0 <
B1 1 -> B1 1 <
B1 + -> simple_add_1 + <
 
simple_add_1 0 -> S 3 >
simple_add_1 1 -> add_1 2 <
simple_add_1 2 -> simple_add_1 2 <
simple_add_1 3 -> simple_add_1 3 <
simple_add_1 _ -> S 3 >
 
simple_add_0 0 -> S 2 >
simple_add_0 1 -> S 3 >
simple_add_0 2 -> simple_add_0 2 <
simple_add_0 3 -> simple_add_0 3 <
simple_add_0 _ -> S 2 >
 
add_1 0 -> S 1 >
add_1 1 -> add_1 0 <
add_1 _ -> S 1 >''')
 
sys.stdout.close()