# Pylons-lang
Python based golf language.

Pretty basic stack based language. Mostly just doing this because I want to get a better feel for how stack based languages work.

All commands operate on the top two elements of the stack unless otherwise specified.

Supports the following things:

1. Appending number to the stack `\d`.
1. Blocks `|\d+|`.
1. Basic arithmatic `+,-,/,*`.
1. For loops `{command,count}`. This works with an integer or a block for count.
1. Square root `s`. Sets the top of the stack equal to the square root of the previous top of stack. Ex. `4s == [2]`
1. Exponential multiplication `e`. 
1. Printing the stack `p`.
1. Printing the stack as a string `c` or `C` for upper case printing. `c` doesn't change the case at all.
