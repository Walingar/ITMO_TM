import sys
 
task_name = "reverse"
 
sys.stdout = open(task_name + ".out", "w")
 
print('''start: S
reject: RJ
accept: AC
blank: _
  
S 0 -> S 0 >
S 1 -> S 1 > 
S _ -> Back _ <
  
Back _ -> Answer _ >
Back 0 -> Add0 4 >
Back 1 -> Add1 5 >
Back 2 -> Back 2 <
Back 3 -> Back 3 <
Back 4 -> Back 4 <
Back 5 -> Back 5 <
  
Add0 0 -> Add0 0 >
Add0 1 -> Add0 1 >
Add0 2 -> Add0 2 >
Add0 3 -> Add0 3 >
Add0 4 -> Add0 4 >
Add0 5 -> Add0 5 >
Add0 _ -> Back 2 <
  
Add1 0 -> Add1 0 >
Add1 1 -> Add1 1 >
Add1 2 -> Add1 2 >
Add1 3 -> Add1 3 >
Add1 4 -> Add1 4 >
Add1 5 -> Add1 5 >
Add1 _ -> Back 3 <
 
Answer _ -> Just_back _ <
Answer 2 -> Answer 0 >
Answer 3 -> Answer 1 >
Answer 4 -> Answer _ >
Answer 5 -> Answer _ >
  
Just_back 0 -> Just_back 0 <
Just_back 1 -> Just_back 1 < 
Just_back _ -> AC _ >''')
 
sys.stdout.close()