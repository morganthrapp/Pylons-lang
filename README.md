# Pylons-lang
Python 3 based golf language.

Pretty basic stack based language. Mostly just doing this because I want to get a better feel for how stack based languages work.

All commands operate as follows `stack[-1] op stack[-2]` unless otherwise specified.

Variables and constants must be defined with capital letters.

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
* Constants with `:name(value or block)`. Ex: `:A1`. Currently these all have to be declared at the start of the program.
* Variables with `[name(value or block)]`. Ex: `[A12+] == [3]` or `[A#11#2+]A == [13]`. Variables can only be an integer, not complex types for now. If you declare a variable without a value, it will automatically take the value of the top of the stack.


## Loops ##
* For loops `{command,count}`. This works with an integer or a block for count.
* While loop with `w(command),(condition}`. Ex. `1w1+,5g} == [5]`


## Stack Commands ##
* Square root `s`. Sets the top of the stack equal to the square root of the previous top of stack. Ex. `4s == [2]`
* Exponential multiplication `e`. 
* Print the stack with `p`.
* Check the primality of the top of the stack `m`.
* Printing the stack as a string `c`. Exits after printing.
* Swap the top of the stack `\`
* Taking command line input with `i`.
* Sum the stack with `s`. Sets the stack equal to the sum of the stack.
* Append the length of the stack with `l`. Sets the stack equal to the length of the stack before this command.
* Clear the stack with `x`.
* Pop and discard the top of the stack with `,`.
* Get the top/bottom of the stack with `t` and `b` respectively. Sets the stack/variable to the top/bottom of the stack.
* Duplicate the top of the stack with `d`.
* Check if `_stack[-1] > _stack[-2]` with `g`. This overwrites the stack, so it should only be used for a variable or a while loop.
* Sort the stack with <code>`</code>.
* Reverse the stack with `v`.
* Get all possible permutations of the stack with `m`. This returns a list of tuples, so caution should be used. It's also not very efficient.
* Factorial of the top of the stack with `!`. 
* Count the items in the stack with `o`. Sets the stack equal to `[count, element...]` for each element in the stack.
* Join and print the stack with `j`. Exits after printing.
* Quit without printing the stack with `@`
* Append a random int to the top of the stack with `r`. If there is more than one value on the stack, it does `randint(_stack[-2], _stack[-1])`. If there's only one value on the stack it does `randint(0, _stack[-1])`. If the stack is empty it does `randint(0, sys.maxsize)`.
 

## Complex Commands ##
* Set the stack pointer to a specific location `;(value or block)`. Zero indexed.
* Functions with `f(name)(body)@`. Uses `.` for args that get replaced with the top of the stack left to right. Not super stable right now. Ex. `2fA2+@ == [4]` 
* Create a list with `({values})`. Any operation done on a list is done matrix wise. Ex. `1(234)-s == [6]`.
* Push the top of the stack to a list with `h`. Ex, `:A()A1h == [List(1)]` 
* Get the first `stack[-1]` digits of pi. If the stack is empty, returns the first 100.
* If statements with `?{condition}`. If `_stack[-1] == condition`, jump past the next instruction 
