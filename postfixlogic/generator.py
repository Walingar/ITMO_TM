import sys
 
task_name = "postfixlogic"
 
sys.stdout = open(task_name + ".out", "w")
 
print('''2
 
S 0 _ -> S _ > 0 >
S 1 _ -> S _ > 1 >
S a _ -> AND _ ^ _ <
S o _ -> OR _ ^ _ <
S _ _ -> GET _ ^ _ <
 
AND _ 1 -> AND1 _ ^ _ <
AND _ 0 -> AND0 _ ^ _ <
 
AND0 _ 0 -> S _ > 0 >
AND0 _ 1 -> S _ > 0 >
AND1 _ 0 -> S _ > 0 >
AND1 _ 1 -> S _ > 1 >
 
OR _ 1 -> OR1 _ ^ _ <
OR _ 0 -> OR0 _ ^ _ <
 
OR0 _ 0 -> S _ > 0 >
OR0 _ 1 -> S _ > 1 >
OR1 _ 0 -> S _ > 1 >
OR1 _ 1 -> S _ > 1 >
 
GET _ 1 -> AC 1 ^ _ ^
GET _ 0 -> AC 0 ^ _ ^''')
 
sys.stdout.close()