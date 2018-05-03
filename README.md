# Norma’s Machine in Python

Python program that simulates a Norma's Machine with 4 recorders.

## What's Norma's Machine?

NORMA (Number TheOretic Register MAchine) is a machine that has as memory an infinite set of registers instructions on each recorder:

* Increment of one;
* Decrement of one;
* Test whether the stored value is zero.

## How it's works?

Just with 2 steps:
First, it's necessary enter with the option. After, the user have to insert the Recorders values.

### Input option

The input option can be:

```
[1] Execute the Sum
[2] Execute the Multiplication
[3] Execute the Factorial
[0] Exit program
```

### Input data

The input file is a Python file (.py) that already is in the project in 'dist' directory. The project already has the three files that
contains instructions of the monolithic programs: sum, multiplication and factorial, that will be executed by the algorithm.

The program has 4 registers: A, B, C and D. The user must start their values at the program entry.

### Output data

The output of the program is a quintuple that shows the values of the registers after undergoing some kind of instruction, and the next line. Example:

#### Input:

```
Enter recorders values:
A: 2
B: 0
C: 3
D: 0
```

#### First line output:

```
Start of program
-> (A->2, B->0, C->3, D->0) [First Instruction]
```

#### Where, the output in the next lines will be:

```
((A value, B value, C value, D value), next_line)
```

## Actual example of operation

### Input file (sum.py):

```
__sum = (
    (1, 'ZER', 'B', 5, 2),
    (2, 'ADD', 'A', 3, 3),
    (3, 'ADD', 'C', 4, 4),
    (4, 'SUB', 'B', 1, 1),
    (5, 'ZER', 'C', 9, 6),
    (6, 'ADD', 'B', 7, 7),
    (7, 'SUB', 'C', 5, 5)
)
```

### Input values from, for example, the sum:

```
Enter recorders values:
A: 0
B: 2
C: 0
D: 0
```

### Line to line output:

```
Start of program
-> (0, 2, 0, 0) [First Instruction -> ZER]
((A->0, B->2, C->0, D->0), 2) > [ADD]
((A->1, B->2, C->0, D->0), 2) > [ADD]
((A->1, B->2, C->1, D->1), 3) > [SUB]
((A->1, B->1, C->1, D->1), 1) > [ZER]
((A->1, B->1, C->1, D->1), 2) > [ADD]
((A->2, B->1, C->1, D->1), 2) > [ADD]
((A->2, B->1, C->2, D->2), 3) > [SUB]
((A->2, B->0, C->2, D->2), 1) > [ZER]
((A->2, B->0, C->2, D->2), 5) > [ZER]
((A->2, B->0, C->2, D->2), 6) > [ADD]
((A->2, B->1, C->2, D->2), 6) > [SUB]
((A->2, B->1, C->1, D->1), 5) > [ZER]
((A->2, B->1, C->1, D->1), 6) > [ADD]
((A->2, B->2, C->1, D->1), 6) > [SUB]
((A->2, B->2, C->0, D->0), 5) > [ZER]
```

### Final result of the program:

```
End of monolithic program. Recorders have this values now:
A:  2
B:  2
C:  0
D:  0
```
