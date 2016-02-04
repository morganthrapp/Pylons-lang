# Pylons-lang
Python 3 based golf language.

Pretty basic stack based language. Mostly just doing this because I want to get a better feel for how stack based languages work.

All commands operate as follows `stack[-1] op stack[-2]` unless otherwise specified.

Variables and constants must be defined with capital letters.

Implicitly prints the stack at the end of the instruction set.

Supports the following things:

1. Appending number to the stack `\d`.
1. Blocks `#\d+#`.
1. Basic arithmetic `+-/*%`.
1. Bitwise operators `<>|&^~`. Left shift, right shift, or, and, xor, twos compliment. Twos compliment only affects the top of the stack. 
1. For loops `{command,count}`. This works with an integer or a block for count.
1. Square root `s`. Sets the top of the stack equal to the square root of the previous top of stack. Ex. `4s == [2]`
1. Exponential multiplication `e`. 
1. Printing the stack `p`.
1. Printing the stack as a string `c`.
1. Swap the top of the stack `\`
1. Constants with `:name(value or block)`. Ex: `:A1`. Currently these all have to be declared at the start of the program.
1. Variables with `[name(value or block)]`. Ex: `[A12+] == [3]` or `[A#11#2+]A == [13]`. Variables can only be an integer, not complex types for now.
1. Taking command line input with `i`.
1. Set the stack pointer to a specific location `;(value or block)`. Zero indexed.