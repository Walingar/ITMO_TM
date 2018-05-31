import sys
 
task_name = "infixlogic"
 
sys.stdout = open(task_name + ".out", "w")
 
print('''2
 
S 0 _ -> S _ > 0 >
S 1 _ -> S _ > 1 >
S a _ -> AND _ > _ <
S o _ -> S _ > o >
S ( _ -> S _ > ( >
S ) _ -> CLOSE _ ^ _ <
S _ _ -> ANSWER _ ^ _ <
 
AND 0 0 -> S _ > 0 >
AND 0 1 -> S _ > 0 >
AND 1 0 -> S _ > 0 >
AND 1 1 -> S _ > 1 >
AND ( 0 -> addAND ( ^ 0 >
AND ( 1 -> addAND ( ^ 1 >
 
addAND ( _ -> S _ > a >
 
CLOSE _ 0 -> CLOSE _ ^ _ <
CLOSE _ 1 -> CLOSE1 _ ^ _ <
CLOSE _ o -> CLOSE _ ^ _ <
CLOSE _ a -> AND 0 ^ _ <
CLOSE _ ( -> S _ > 0 >
 
CLOSE1 _ 0 -> CLOSE1 _ ^ _ <
CLOSE1 _ 1 -> CLOSE1 _ ^ _ <
CLOSE1 _ o -> CLOSE1 _ ^ _ <
CLOSE1 _ a -> AND 1 ^ _ <
CLOSE1 _ ( -> S _ > 1 >
 
ANSWER _ 0 -> ANSWER _ ^ _ <
ANSWER _ 1 -> AC 1 ^ _ ^
ANSWER _ o -> ANSWER _ ^ _ <
ANSWER _ _ -> AC 0 ^ _ ^''')
 
sys.stdout.close()