import sys
 
task_name = "convertto2"
 
sys.stdout = open(task_name + ".out", "w")
 
print('''start: S
accept: AC
reject: RJ
blank: _
 
S 0 -> S 0 <
S 1 -> S 1 <
S 2 -> S 2 <
S _ -> Append0 w <
 
Append0 _ -> toB 0 >
 
toB 0 -> toB 0 >
toB 1 -> toB 1 >
toB w -> toEndB w >
 
toEndB 0 -> toEndB 0 >
toEndB 1 -> toEndB 1 >
toEndB 2 -> toEndB 2 >
toEndB _ -> Bminus1 _ <
 
Bminus1 0 -> Bminus1 0 <
Bminus1 1 -> Bplus 0 >
Bminus1 2 -> Bplus 1 >
Bminus1 w -> toEndBClear w >
 
Bplus 0 -> Bplus 2 >
Bplus _ -> toA _ <
 
toA 0 -> toA 0 <
toA 1 -> toA 1 <
toA 2 -> toA 2 <
toA w -> Aplus1 w <
 
Aplus1 0 -> toB 1 >
Aplus1 1 -> Aplus1 0 <
Aplus1 _ -> toB 1 >
 
toEndBClear 0 -> toEndBClear 0 >
toEndBClear _ -> clearB _ <
 
clearB 0 -> clearB _ <
clearB w -> toFinish _ <
 
toFinish 0 -> toFinish 0 <
toFinish 1 -> toFinish 1 <
toFinish _ -> AC _ >
''')
 
sys.stdout.close()