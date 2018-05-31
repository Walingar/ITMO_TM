import sys

sys.stdout = open("sorting.out", "w")


# first: input
# second: counter
# third: copy
# fourth: answer
# Я НЕ ОТВЕЧАЮ ЗА ТО, ЧТО ТУТ ПРОИСХОДИТ, КАЖДАЯ СТРОЧКА КОДА -- КОСТЫЛЬ (нет(4 ленты МТ :((((((( ))

def print_jump(state, f, state_to, to):
    print(state + " " + ' '.join(f) + " -> " + state_to + " " + ' '.join(to))


def print_adding_1():
    for i in ["0", "1"]:
        i_stay = i + " ^"
        # to end of counter
        print_jump("ADD", [i, "0", "_", "_"], "ADD", [i_stay, "0 >", "_ ^", "_ ^"])
        print_jump("ADD", [i, "1", "_", "_"], "ADD", [i_stay, "1 >", "_ ^", "_ ^"])
        print_jump("ADD", [i, "_", "_", "_"], "ADDING", [i_stay, "_ <", "_ ^", "_ ^"])

        # add 1 to counter
        print_jump("ADDING", [i, "0", "_", "_"], "2BEGIN", [i_stay, "1 ^", "_ ^", "_ ^"])
        print_jump("ADDING", [i, "1", "_", "_"], "ADDING", [i_stay, "0 <", "_ ^", "_ ^"])
        print_jump("ADDING", [i, "_", "_", "_"], "copy", [i_stay, "1 ^", "_ ^", "_ ^"])

        # to start of counter
        print_jump("2BEGIN", [i, "0", "_", "_"], "2BEGIN", [i_stay, "0 <", "_ ^", "_ ^"])
        print_jump("2BEGIN", [i, "1", "_", "_"], "2BEGIN", [i_stay, "1 <", "_ ^", "_ ^"])
        print_jump("2BEGIN", [i, "_", "_", "_"], "copy", [i_stay, "_ >", "_ ^", "_ ^"])
    for i in ["2", "3"]:
        i_stay = i + " ^"
        # to end of counter
        print_jump("ADD", [i, "0", "_", "_"], "ADD", [i_stay, "0 >", "_ ^", "_ ^"])
        print_jump("ADD", [i, "1", "_", "_"], "ADD", [i_stay, "1 >", "_ ^", "_ ^"])
        print_jump("ADD", [i, "_", "_", "_"], "ADDING", [i_stay, "_ <", "_ ^", "_ ^"])

        # add 1 to counter
        print_jump("ADDING", [i, "0", "_", "_"], "2BEGIN", [i_stay, "1 ^", "_ ^", "_ ^"])
        print_jump("ADDING", [i, "1", "_", "_"], "ADDING", [i_stay, "0 <", "_ ^", "_ ^"])
        print_jump("ADDING", [i, "_", "_", "_"], "copy", [i_stay, "1 ^", "_ ^", "_ ^"])
    for i in ["2", "3", "|"]:
        print_jump("2BEGIN", [i, "0", "_", "_"], "2BEGIN", [i + " >", "0 ^", "_ ^", "_ ^"])
        print_jump("2BEGIN", [i, "1", "_", "_"], "2BEGIN", [i + " >", "1 ^", "_ ^", "_ ^"])

    print_jump("2BEGIN", ["_", "0", "_", "_"], "2BEGIN", ["_ ^", "0 >", "_ ^", "_ ^"])
    print_jump("2BEGIN", ["_", "1", "_", "_"], "2BEGIN", ["_ ^", "1 >", "_ ^", "_ ^"])
    print_jump("2BEGIN", ["_", "_", "_", "_"], "toStartFirst", ["_ <", "_ ^", "_ ^", "_ ^"])
    print()
    print()


def print_copying():
    for counter in ["0", "1"]:
        counter_stay = counter + " ^"
        # copy number from input to copy line
        print_jump("copy", ["0", counter, "_", "_"], "copy'", ["0 >", counter_stay, "0 >", "_ ^"])
        print_jump("copy", ["1", counter, "_", "_"], "copy'", ["1 >", counter_stay, "1 >", "_ ^"])
        print_jump("copy'", ["0", counter, "_", "_"], "copy'", ["0 >", counter_stay, "0 >", "_ ^"])
        print_jump("copy'", ["1", counter, "_", "_"], "copy'", ["1 >", counter_stay, "1 >", "_ ^"])
        print_jump("copy", ["2", counter, "_", "_"], "copy", ["2 >", counter_stay, "_ >", "_ ^"])
        print_jump("copy", ["3", counter, "_", "_"], "copy", ["3 >", counter_stay, "_ >", "_ ^"])
        print_jump("copy", ["|", counter, "_", "_"], "copy", ["| >", counter_stay, "_ ^", "_ ^"])
        print_jump("copy'", ["|", counter, "_", "_"], "copied", ["| ^", counter_stay, "_ <", "_ ^"])
        print_jump("copy", ["_", counter, "_", "_"], "toStartFirst", ["_ >", counter_stay, "_ ^", "_ ^"])
        print_jump("copy'", ["_", counter, "_", "_"], "copied", ["_ ^", counter_stay, "_ <", "_ ^"])

        # to start of copy line after copying
        print_jump("copied", ["_", counter, "0", "_"], "copied", ["_ ^", counter_stay, "0 <", "_ ^"])
        print_jump("copied", ["_", counter, "1", "_"], "copied", ["_ ^", counter_stay, "1 <", "_ ^"])
        print_jump("copied", ["_", counter, "_", "_"], "checking", ["_ ^", counter_stay, "_ >", "_ ^"])
        print_jump("copied", ["|", counter, "0", "_"], "copied", ["| ^", counter_stay, "0 <", "_ ^"])
        print_jump("copied", ["|", counter, "1", "_"], "copied", ["| ^", counter_stay, "1 <", "_ ^"])
        print_jump("copied", ["|", counter, "_", "_"], "checking", ["| ^", counter_stay, "_ >", "_ ^"])
    print()
    print()


def print_checking():
    for inp in ["|", "_"]:
        inp_stay = inp + " ^"
        print_jump("checking", [inp, "0", "0", "_"], "checking", [inp_stay, "0 >", "0 >", "_ ^"])
        print_jump("checking", [inp, "1", "1", "_"], "checking", [inp_stay, "1 >", "1 >", "_ ^"])
        print_jump("checking", [inp, "_", "_", "_"], "here", [inp_stay, "_ <", "_ <", "_ ^"])

        print_jump("checking", [inp, "0", "1", "_"], "!here", [inp_stay, "0 ^", "0 ^", "_ ^"])
        print_jump("checking", [inp, "1", "0", "_"], "!here", [inp_stay, "1 ^", "0 ^", "_ ^"])
        print_jump("checking", [inp, "_", "0", "_"], "!here", [inp_stay, "_ ^", "0 ^", "_ ^"])
        print_jump("checking", [inp, "_", "1", "_"], "!here", [inp_stay, "_ ^", "1 ^", "_ ^"])
        print_jump("checking", [inp, "0", "_", "_"], "!here", [inp_stay, "0 ^", "0 ^", "_ ^"])
        print_jump("checking", [inp, "1", "_", "_"], "!here", [inp_stay, "1 ^", "0 ^", "_ ^"])
    print()
    print()


def print_not_here():
    # clear copy line
    for inp in ["|", "_"]:
        inp_stay = inp + " ^"
        print_jump("!here", [inp, "0", "1", "_"], "!here", [inp_stay, "0 >", "_ >", "_ ^"])
        print_jump("!here", [inp, "0", "0", "_"], "!here", [inp_stay, "0 >", "_ >", "_ ^"])
        print_jump("!here", [inp, "1", "1", "_"], "!here", [inp_stay, "1 >", "_ >", "_ ^"])
        print_jump("!here", [inp, "1", "0", "_"], "!here", [inp_stay, "1 >", "_ >", "_ ^"])
        print_jump("!here", [inp, "_", "1", "_"], "!here", [inp_stay, "_ ^", "_ >", "_ ^"])
        print_jump("!here", [inp, "_", "0", "_"], "!here", [inp_stay, "_ ^", "_ >", "_ ^"])
        if inp == "|":
            print_jump("!here", [inp, "_", "_", "_"], "2BEGIN", ["| >", "_ <", "_ >", "_ ^"])
        elif inp == "_":
            print_jump("!here", [inp, "_", "_", "_"], "toStartFirst", ["_ <", "_ ^", "_ >", "_ ^"])


def print_here():
    # copy to answer:
    for inp in ["_", "|"]:
        inp_stay = inp + " ^"
        print_jump("here", [inp, "0", "0", "_"], "here", [inp_stay, "0 <", "0 <", "_ ^"])
        print_jump("here", [inp, "1", "1", "_"], "here", [inp_stay, "1 <", "1 <", "_ ^"])
        print_jump("here", [inp, "_", "_", "_"], "copyCounterToAnswer", [inp_stay, "_ >", "_ >", "_ ^"])

        print_jump("copyCounterToAnswer", [inp, "0", "0", "_"], "copyCounterToAnswer", [inp_stay, "0 >", "0 >", "0 >"])
        print_jump("copyCounterToAnswer", [inp, "1", "1", "_"], "copyCounterToAnswer", [inp_stay, "1 >", "1 >", "1 >"])
        print_jump("copyCounterToAnswer", [inp, "_", "_", "_"], "replacingInputLine", [inp + " <", "_ ^", "_ >", "| >"])

    # replace 0 -> 2 and 1 -> 3 in input line
    print_jump("replacingInputLine", ["0", "_", "_", "_"], "replacingInputLine", ["2 <", "_ ^", "_ ^", "_ ^"])
    print_jump("replacingInputLine", ["1", "_", "_", "_"], "replacingInputLine", ["3 <", "_ ^", "_ ^", "_ ^"])
    print_jump("replacingInputLine", ["|", "_", "_", "_"], "2BEGIN", ["| >", "_ <", "_ ^", "_ ^"])
    print_jump("replacingInputLine", ["_", "_", "_", "_"], "2BEGIN", ["_ >", "_ <", "_ ^", "_ ^"])


# use toStartFirst when copied or !here
def print_to_start_1():
    print_jump("toStartFirst", ["0", "_", "_", "_"], "toStartFirst", ["0 <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartFirst", ["1", "_", "_", "_"], "toStartFirst", ["1 <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartFirst", ["2", "_", "_", "_"], "toStartFirst", ["2 <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartFirst", ["3", "_", "_", "_"], "toStartFirst", ["3 <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartFirst", ["|", "_", "_", "_"], "toStartFirst", ["| <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartFirst", ["_", "_", "_", "_"], "checkingFirst", ["_ >", "_ ^", "_ ^", "_ ^"])


def print_checking_first():
    print_jump("checkingFirst", ["0", "_", "_", "_"], "toStartChecking", ["0 <", "_ ^", "_ ^", "_ ^"])
    print_jump("checkingFirst", ["1", "_", "_", "_"], "toStartChecking", ["1 <", "_ ^", "_ ^", "_ ^"])
    print_jump("checkingFirst", ["2", "_", "_", "_"], "checkingFirst", ["2 >", "_ ^", "_ ^", "_ ^"])
    print_jump("checkingFirst", ["3", "_", "_", "_"], "checkingFirst", ["3 >", "_ ^", "_ ^", "_ ^"])
    print_jump("checkingFirst", ["|", "_", "_", "_"], "checkingFirst", ["| >", "_ ^", "_ ^", "_ ^"])
    print_jump("checkingFirst", ["_", "_", "_", "_"], "FINISH'", ["_ ^", "_ ^", "_ ^", "_ <"])


def print_finish():
    print_jump("FINISH'", ["_", "_", "_", "|"], "FINISH", ["_ <", "_ ^", "_ ^", "_ <"])

    for i in ["0", "1", "2", "3", "|", "_"]:
        print_jump("FINISH", [i, "_", "_", "0"], "FINISH", ["0 <", "_ ^", "_ ^", "_ <"])
        print_jump("FINISH", [i, "_", "_", "1"], "FINISH", ["1 <", "_ ^", "_ ^", "_ <"])
        print_jump("FINISH", [i, "_", "_", "|"], "FINISH", ["| <", "_ ^", "_ ^", "_ <"])
        print_jump("FINISH", [i, "_", "_", "_"], "AC", ["_ >", "_ ^", "_ ^", "_ <"])


def print_to_start_checking():
    print_jump("toStartChecking", ["0", "_", "_", "_"], "toStartChecking", ["0 <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartChecking", ["1", "_", "_", "_"], "toStartChecking", ["1 <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartChecking", ["2", "_", "_", "_"], "toStartChecking", ["2 <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartChecking", ["3", "_", "_", "_"], "toStartChecking", ["3 <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartChecking", ["|", "_", "_", "_"], "toStartChecking", ["| <", "_ ^", "_ ^", "_ ^"])
    print_jump("toStartChecking", ["_", "_", "_", "_"], "ADDING", ["_ >", "_ <", "_ ^", "_ ^"])


# rows count
print(4)
print()
print('''S 0 _ _ _ -> copy 0 ^ 0 ^ _ > _ >
S 1 _ _ _ -> copy 1 ^ 0 ^ _ > _ >''')

print_adding_1()
print_copying()
print_checking()
print_not_here()
print_here()
print_to_start_1()
print_checking_first()
print_finish()
print_to_start_checking()

sys.stdout.close()
