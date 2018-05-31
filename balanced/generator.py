import sys
 
task_name = "balanced"
 
sys.stdout = open(task_name + ".out", "w")
 
print('''start: S
reject: RJ
accept: AC
blank: _
 
S ( -> S ( >
S ) -> S ) >
S 0 -> S 0 >
S _ -> find_open_back _ <
 
find_open_back ) -> find_open_back ) <
find_open_back 0 -> find_open_back 0 <
find_open_back ( -> find_close 0 >
find_open_back _ -> check_close _ >
 
check_close 0 -> check_close 0 >
check_close _ -> AC _ ^
check_close ) -> RJ _ ^
 
find_close 0 -> find_close 0 >
find_close _ -> RJ _ ^
find_close ) -> find_open_back 0 <''')
 
sys.stdout.close()