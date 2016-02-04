# Pylons-lang
Python 3 based golf language.

Pretty basic stack based language. Mostly just doing this because I want to get a better feel for how stack based languages work.

All commands operate on the top two elements of the stack unless otherwise specified.

Variables and constants must be defined with capital letters.

Supports the following things:

1. Appending number to the stack `\d`.
1. Blocks `|\d+|`.
1. Basic arithmetic `+,-,/,*`.
1. For loops `{command,count}`. This works with an integer or a block for count.
1. Square root `s`. Sets the top of the stack equal to the square root of the previous top of stack. Ex. `4s == [2]`
1. Exponential multiplication `e`. 
1. Printing the stack `p`.
1. Printing the stack as a string `c`.
1. Swap the top of the stack `\`
1. Constants with `:name(value or block)`. Ex: `:A1`. Currently these all have to be declared at the start of the program.
1. Variables with `[name(value or block)]`. Ex: `[A12+] == [3]` or `[A|11|2+]A == [13]`