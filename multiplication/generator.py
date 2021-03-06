import sys
 
task_name = "multiplication"
 
sys.stdout = open(task_name + ".out", "w")
 
print('''start: S
accept: AC
reject: RJ
blank: _
 
S 0 -> Save0' 2 >
S 1 -> Save1' 3 >
S * -> RefreshA * <
Save0' 0 -> Save0' 0 >
Save0' 1 -> Save0' 1 >
Save0' * -> Save0' * >
Save0' w -> Save0 w >
Save0' _ -> Save0 w >
Save0 0 -> Save0 0 >
Save0 1 -> Save0 1 >
Save0 _ -> BackToAppend 0 <
Save1' 0 -> Save1' 0 >
Save1' 1 -> Save1' 1 >
Save1' * -> Save1' * >
Save1' w -> Save1 w >
Save1' _ -> Save1 w >
Save1 0 -> Save1 0 >
Save1 1 -> Save1 1 >
Save1 _ -> BackToAppend 1 <
BackToAppend 0 -> BackToAppend 0 <
BackToAppend 1 -> BackToAppend 1 <
BackToAppend w -> BackToAppend w <
BackToAppend * -> BackToAppend * <
BackToAppend 2 -> S 2 >
BackToAppend 3 -> S 3 >
RefreshA 2 -> RefreshA 0 <
RefreshA 3 -> RefreshA 1 <
RefreshA _ -> Counting' _ >
Counting' 0 -> Counting' 0 >
Counting' 1 -> Counting' 1 >
Counting' * -> Counting' * >
Counting' w -> BM1 w <
BM1 0 -> BM1 0 <
BM1 1 -> BP1 0 >
BM1 * -> ZEROCLEAR * >
ZEROCLEAR 0 -> ZEROCLEAR 0 >
ZEROCLEAR 1 -> ZEROCLEAR 1 >
ZEROCLEAR w -> ZEROCLEAR w >
ZEROCLEAR _ -> ZERO _ <
ZERO 0 -> ZERO _ <
ZERO 1 -> ZERO _ <
ZERO w -> ZERO _ <
ZERO * -> ZERO _ <
ZERO _ -> AC 0 ^
BP1 0 -> BP1 1 >
BP1 w -> BMinus1 w <
 
 
 
 
Counting 0 -> Counting 0 >
Counting 1 -> Counting 1 >
Counting * -> toEndB * >
 
toEndB 0 -> toEndB 0 >
toEndB 1 -> toEndB 1 >
toEndB w -> BMinus1 w <
 
BMinus1 0 -> BMinus1 0 <
BMinus1 1 -> BPlus1 0 >
BMinus1 * -> DeleteAll' * >
  
BPlus1 0 -> BPlus1 1 >
BPlus1 w -> Adding w >
 
Adding 0 -> Adding 0 >
Adding 1 -> Adding 1 >
Adding 2 -> AddingFound 2 <
Adding 3 -> AddingFound 3 <
Adding _ -> AddingFound _ <
 
AddingFound 0 -> Add0' 2 <
AddingFound 1 -> Add1' 3 <
AddingFound w -> RefreshingC w >
 
RefreshingC 2 -> RefreshingC 0 >
RefreshingC 3 -> RefreshingC 1 >
RefreshingC _ -> RefreshingAll _ <
 
RefreshingAll 0 -> RefreshingAll 0 <
RefreshingAll 1 -> RefreshingAll 1 <
RefreshingAll 2 -> RefreshingAll 0 <
RefreshingAll 3 -> RefreshingAll 1 <
RefreshingAll w -> RefreshingAll w <
RefreshingAll * -> RefreshingAll * <
RefreshingAll _ -> Counting _ >
 
BackToB 0 -> BackToB 0 <
BackToB 1 -> BackToB 1 <
BackToB w -> BackToB w <
BackToB * -> toEndB * >
 
Add0' 0 -> Add0' 0 <
Add0' 1 -> Add0' 1 <
Add0' w -> Add0' w <
Add0' * -> Add0 * <
 
Add0 0 -> BackToC 2 >
Add0 1 -> BackToC 3 >
Add0 2 -> Add0 2 <
Add0 3 -> Add0 3 <
Add0 _ -> BackToC 2 >
 
Add1' 0 -> Add1' 0 <
Add1' 1 -> Add1' 1 <
Add1' w -> Add1' w <
Add1' * -> Add1 * <
 
Add1 0 -> BackToC 3 >
Add1 1 -> Add1Simple 2 <
Add1 2 -> Add1 2 <
Add1 3 -> Add1 3 <
Add1 _ -> BackToC 3 >
 
Add1Simple 0 -> BackToC 1 >
Add1Simple 1 -> Add1Simple 0 <
Add1Simple _ -> BackToC 1 >
 
BackToC * -> BackToC' * >
BackToC 0 -> BackToC 0 >
BackToC 1 -> BackToC 1 >
BackToC 2 -> BackToC 2 >
BackToC 3 -> BackToC 3 >
 
BackToC' 0 -> BackToC' 0 >
BackToC' 1 -> BackToC' 1 >
BackToC' w -> BackToC' w >
BackToC' 2 -> AddingFound 2 <
BackToC' 3 -> AddingFound 3 <
 
DeleteAll' 0 -> DeleteAll' 0 >
DeleteAll' w -> DeleteAll' w >
DeleteAll' 1 -> DeleteAll' 1 >
DeleteAll' _ -> DeleteAll _ <
 
DeleteAll 0 -> DeleteAll _ <
DeleteAll w -> DeleteAll _ <
DeleteAll 1 -> DeleteAll _ <
DeleteAll * -> TOSTARTA _ <
 
TOSTARTA 0 -> TOSTARTA 0 <
TOSTARTA 1 -> TOSTARTA 1 <
TOSTARTA _ -> AC _ >
 
 
DEBUG 0 -> DEBUG 0 <
DEBUG 1 -> DEBUG 1 <
DEBUG 2 -> DEBUG 2 <
DEBUG 3 -> DEBUG 3 <
DEBUG w -> DEBUG w <
DEBUG * -> DEBUG * <
DEBUG _ -> AC _ >''')
 
sys.stdout.close()