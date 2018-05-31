import sys
 
task_name = "tandem"
 
sys.stdout = open(task_name + ".out", "w")
 
print('''start: S
accept: AC
reject: RJ
blank: _
 
S 0 -> Simple_forward 2 >
S 1 -> Simple_forward 3 >
S 2 -> Check 2 <
S 3 -> Check 3 <
 
Simple_forward 0 -> Simple_forward 0 >
Simple_forward 1 -> Simple_forward 1 >
Simple_forward 2 -> Back 2 <
Simple_forward 3 -> Back 3 <
Simple_forward _ -> Back _ <
 
Back 0 -> Simple_back 2 <
Back 1 -> Simple_back 3 <
Back 2 -> RJ _ ^
Back 3 -> RJ _ ^
 
Simple_back 0 -> Simple_back 0 <
Simple_back 1 -> Simple_back 1 <
Simple_back 2 -> S 2 >
Simple_back 3 -> S 3 >
Simple_back _ -> S _ >
 
Check 0 -> Check 0 <
Check 1 -> Check 1 <
Check 2 -> Check0 0 > 
Check 3 -> Check1 1 >
Check _ -> AC _ ^
 
Check0 _ -> Check0Back _ <
Check0 0 -> Check0 0 >
Check0 1 -> Check0 1 >
Check0 2 -> Check0 2 >
Check0 3 -> Check0 3 >
 
Check0Back 2 -> CheckBack _ <
Check0Back 3 -> RJ _ ^
 
Check1 _ -> Check1Back _ <
Check1 0 -> Check1 0 >
Check1 1 -> Check1 1 >
Check1 2 -> Check1 2 >
Check1 3 -> Check1 3 >
 
Check1Back 2 -> RJ _ ^
Check1Back 3 -> CheckBack _ <
 
CheckBack 0 -> Check 0 <
CheckBack 1 -> Check 1 <
CheckBack 2 -> CheckBack 2 <
CheckBack 3 -> CheckBack 3 <''')
 
sys.stdout.close()