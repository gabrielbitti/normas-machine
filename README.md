# Norma’s Machine in Python

Python program that simulates a Norma's Machine with 4 recorders.

## What's Norma's Machine?

NORMA (Number TheOretic Register MAchine) is a machine that has as memory an infinite set of registers instructions on each recorder:

* Increment of one;
* Decrement of one;
* Test whether the stored value is zero.

## How it's works?

### Input data

The input file is a text file (.txt) that is in the project in bin/monolithic_program.txt. The project already has a standard file that
contains 3 instructions of a monolithic program and will be executed by the algorithm.

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
-> (2, 0, 3, 0)
```

#### Where:

```
((A value, B value, C value, D value), next_line)
```

## Actual example of operation

### Input file:

```
1: ADD C 2
2: SUB A 3
3: ZER A 4 1
```

### Input values:

```
Enter recorders values:
A: 2
B: 0
C: 3
D: 0
```

### Line to line output:

#### Line 1

```
Start of program
-> (2, 0, 3, 0)
```

#### Line 2

```
((2, 0, 4, 0), 2)

```

#### Line 3

```
((1, 0, 4, 0), 3)

```

#### Line 4

```
((1, 0, 4, 0), 1)

```

#### Line 5

```
((1, 0, 5, 0), 2)

```

#### Line 6

```
((0, 0, 5, 0), 3)
```

#### Line 7

```
((0, 0, 5, 0), 4)
```

### Final result of the program:

```
End of monolithic program. Recorders have this values now:
A:  0
B:  0
C:  5
D:  0
```
