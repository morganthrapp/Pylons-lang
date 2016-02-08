# Pylons-lang
Python 3 based golf language.

Pretty basic stack based language. Mostly just doing this because I want to get a better feel for how stack based languages work.

All commands operate as follows `stack[-1] op stack[-2]` unless otherwise specified.

Variables and constants must be defined with capital letters.

Any place you can use an integer literal, you can use a command, variable, or function.

Implicitly prints the stack at the end of the instruction set.

# How to run.

    `py -3 main.py program.p *args`
    

# Some examples.

    "Hello, World!"c  # Hello world.
    0{d1+,i}c         # Print the ascii table (0,sys.argv[0]]
    i:At,{n,A}j@      # [Look and Say](https://oeis.org/A005150)
    11fA..+@{A,i}     # First sys.argv[0] Fibonacci numbers
    

# Bonus quine, all credit to [kms7047](https://github.com/kms70847)
    
    #272905715458918625954929791277018732980372648151923925534616453307621588598692438414443279763003025372409097795417741330602167388103514682342382282390274176094981540184583036198531713253138700693955928801808034338692982310398308250577863556014805403336841267395172018000805496670641969318196854690330530651#[S],#35#[L0][TS]w[LL1+][T#10#T/],0Tg}[C1L-]{#10#C#10#eS/%#48#+[C1C-],L}#35#[L0][TS]w[LL1+][T8T>],0Tg}[C0]{#256#C8*S>%[C1C+],L}c


# Supports the following operations:

## Basic Operations ##

| Command | Result                                                                                                     |
|---------|------------------------------------------------------------------------------------------------------------|
| \d+     | Push the number to the stack.                                                                              |
| #\d+#   | Push the number between the # marks to the stack.                                                          |
| +-/*%   | Basic arithmetic operations.                                                                               |
| <>|&^~  | Left shift, right shift, or, and, xor, twos compliment. Twos compliment only affects the top of the stack. |


## Variables ##

| Command                  | Result                                                                            |
|--------------------------|-----------------------------------------------------------------------------------|
| :name(value)             | Creates a constant.                                                               |
| [name(value or command)] | Create a variable. If no value is given, takes the value of the top of the stack. |


## Loops ##

| Command                | Result                                                 |
|------------------------|--------------------------------------------------------|
| {command,count}        | For loop. Repeats command count times.                 |
| w(command),(condition} | While loop, repeat command while condition is truthy.  |


## Stack Commands ##

| Command | Result                                                                                                   |
|---------|----------------------------------------------------------------------------------------------------------|
| q       | Sets the top of the stack equal to the square root of the previous top of stack.                         |
| e       | Set the top of the stack equal to stack[-2] ** stack[-1]                                                 |
| p       | Print the stack.                                                                                         |
| m       | Return the primality of the top of the stack.                                                            |
| c       | Print the stack as a string. Exits after printing.                                                       |
| \       | Swap the top two elements of the stack.                                                                  |
| i       | Take command line arguments and put them on the stack.                                                   |
| s       | Sum the stack and return it.                                                                             |
| l       | Return the length of the stack.                                                                          |
| x       | Clear the stack.                                                                                         |
| ,       | Pop the top of the stack and discard it.                                                                 |
| t       | Get the top of the stack.                                                                                |
| b       | Get the bottom of the stack.                                                                             |
| d       | Duplicate the top of the stack.                                                                          |
| g       | Check if stack[-1] > stack[-2]                                                                           |
| `       | Sort the stack.                                                                                          |
| v       | Reverse the stack.                                                                                       |
| !       | Returns the factorial of the top of the stack.                                                           |
| o       | Count the items in the stack. Sets the stack equal to [count, element...] for each element in the stack. |
| j       | Join and print the stack. Exits after printing.                                                          |
| @       | Quit without printing the stack.                                                                         |
| r       | Push a random int to the top of the stack.                                                               |
| a       | Get the first stack[-1] digits of pi. If the stack is empty, returns the first 100.                      |
| h       | Push the top of the stack to the list in stack[-2].                                                      |
| _       | Check if the top of the stack is in the stack excluding the top.                                         |


## Complex Commands ##

| Command        | Result                                                                                        |
|----------------|-----------------------------------------------------------------------------------------------|
| ;(value)       | Set the stack pointer equal to value.                                                         |
| f(name)(body)@ | Create a function. Uses . for args that get replaced with the top of the stack left to right. |
| (values)       | Create a list. Any operation done on a list is done matrix wise. Ex. `1(234)-s == [6]`.       |
| ?(condition)   | If statement. If stack[-1] == condition, skip the next instruction.                           |
