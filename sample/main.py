#!/usr/local/bin/python
#encoding: utf-8

from recorder import Recorder
from dist import sum, multiplication, factorial


print("\n<<< Norma's Machine >>>")

def main():
    print("\n[1] > Execute the Sum")
    print("[2] > Execute the Multiplication")
    print("[3] > Execute the Factorial")
    print("[0] > Exit program")
    while True:
        option = input("\nEnter your option: ")
        if option == '0':
            print("End of program!")
            exit()
        elif option == '1':
            print("\nEnter the values of the Recorders A and B: ")
            temp = int(input("A: "))
            A = Recorder(temp)
            temp = int(input("B: "))
            B = Recorder(temp)
            C = D = Recorder(0)
            program = sum.get()
            break
        elif option == '2':
            print("\nEnter the values of the Recorders A and B: ")
            temp = int(input("A: "))
            A = Recorder(temp)
            temp = int(input("B: "))
            B = Recorder(temp)
            C = D = Recorder(0)
            program = multiplication.get()
            break
        elif option == '3':
            print("\nEnter the value of Recorder A, where it will be the result of the factorial: ")
            temp = int(input("A: "))
            A = Recorder(temp)
            B = C = D = Recorder(0)
            program = factorial.get()
            break
        else:
            print("(!) This option does not exist. type again!")
    instructions = []
    for linha in program:
        instructions += [[linha[0], linha[1], linha[2], linha[3], linha[4]]]
    i = 0
    print("\nStart of program\n-> (A->{}, B->{}, C->{}, D->{}) [First Instruction -> {}]".format(A.value, B.value, C.value, D.value, instructions[i][1]))
    while i < len(instructions):
        try:
            if instructions[i][1] == 'ADD':
                if instructions[i][2] == 'A':
                    A.add()
                elif instructions[i][2] == 'B':
                    B.add()
                elif instructions[i][2] == 'C':
                    C.add()
                else:
                    D.add()
                i = instructions[i][3]
                i -= 1
                print("((A->{}, B->{}, C->{}, D->{}), {}) > [{}]".format(A.value, B.value, C.value, D.value, i, instructions[i][1]))
            elif instructions[i][1] == 'SUB':
                if instructions[i][2] == 'A':
                    A.sub()
                elif instructions[i][2] == 'B':
                    B.sub()
                elif instructions[i][2] == 'C':
                    C.sub()
                else:
                    D.sub()
                i = instructions[i][3]
                i -= 1
                print("((A->{}, B->{}, C->{}, D->{}), {}) > [{}]".format(A.value, B.value, C.value, D.value, i + 1, instructions[i][1]))
            elif instructions[i][1] == 'ZER':
                if instructions[i][2] == 'A':
                    i = instructions[i][3] if (A.zer()) == 1 else instructions[i][4]
                elif instructions[i][2] == 'B':
                    i = instructions[i][3] if (B.zer()) == 1 else instructions[i][4]
                elif instructions[i][2] == 'C':
                    i = instructions[i][3] if (C.zer()) == 1 else instructions[i][4]
                else:
                    i = instructions[i][3] if (D.zer()) == 1 else instructions[i][4]
                i -= 1
                print("((A->{}, B->{}, C->{}, D->{}), {}) > [{}]".format(A.value, B.value, C.value, D.value, i + 1, instructions[i][1]))
        except IndexError:
            print("\nEnd of program. The recorders now have these values: ")
            print("A: ", A.value)
            print("B: ", B.value)
            print("C: ", C.value)
            print("D: ", D.value)

if __name__ == '__main__':
    main()
    while True:
        option = input("Do you want to run the program again? [Y/N] ")
        if option == 'N' or option == 'n':
            print("\nProgram closed!")
            break
        elif option == 'Y' or option == 'y':
            main()
        else:
            print("Incorrect option!")
