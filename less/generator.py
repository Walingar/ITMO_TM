import sys
 
task_name = "less"
 
sys.stdout = open(task_name + ".out", "w")
 
print('''start: S
accept: AC
reject: RJ
blank: _
 
S 0 -> S 0 >
S 1 -> S 1 >
S 2 -> S 2 >
S 3 -> S 3 >
S < -> toEndA < <
 
toEndA 0 -> toB0 2 >
toEndA 1 -> toB1 3 >
toEndA 2 -> toEndA 2 <
toEndA 3 -> toEndA 3 <
toEndA _ -> CheckB' _ >
 
toB0 2 -> toB0 2 >
toB0 3 -> toB0 3 >
toB0 < -> toEndB0 < >
 
toEndB0 0 -> toEndB0 0 >
toEndB0 1 -> toEndB0 1 >
toEndB0 2 -> Bminus0 2 <
toEndB0 3 -> Bminus0 3 <
toEndB0 _ -> Bminus0 _ <
 
Bminus0 0 -> toA 2 <
Bminus0 1 -> toA 3 <
Bminus0 < -> RJ _ ^
 
toB1 2 -> toB1 2 >
toB1 3 -> toB1 3 >
toB1 < -> toEndB1 < >
 
toEndB1 0 -> toEndB1 0 >
toEndB1 1 -> toEndB1 1 >
toEndB1 2 -> Bminus1 2 <
toEndB1 3 -> Bminus1 3 <
toEndB1 _ -> Bminus1 _ <
 
Bminus1 0 -> Bminus1' 3 <
Bminus1 1 -> toA 2 <
Bminus1 < -> RJ _ ^
 
Bminus1' 0 -> Bminus1' 1 <
Bminus1' 1 -> toA 0 <
Bminus1' < -> RJ _ ^
 
CheckB' 2 -> CheckB' 2 >
CheckB' 3 -> CheckB' 3 >
CheckB' < -> CheckB < >
 
CheckB 0 -> CheckB 0 >
CheckB 1 -> AC _ ^
CheckB 2 -> CheckB 2 >
CheckB 3 -> AC _ ^
CheckB _ -> RJ _ ^
 
toA 0 -> toA 0 <
toA 1 -> toA 1 <
toA < -> toEndA < <
''')
 
sys.stdout.close()