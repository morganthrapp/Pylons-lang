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
1. Print the stack with `p`.
1. Check the primality of the top of the stack `m`.
1. Printing the stack as a string `c`.
1. Swap the top of the stack `\`
1. Constants with `:name(value or block)`. Ex: `:A1`. Currently these all have to be declared at the start of the program.
1. Variables with `[name(value or block)]`. Ex: `[A12+] == [3]` or `[A#11#2+]A == [13]`. Variables can only be an integer, not complex types for now.
1. Taking command line input with `i`.
1. Set the stack pointer to a specific location `;(value or block)`. Zero indexed.
1. Functions with `f(name)(body)@`. Uses `.` for args that get replaced with the top of the stack left to right. Not super stable right now. Ex. `2fA2+@ == [4]` 
1. Sum the stack with `s`. Sets the stack equal to the sum of the stack.
1. Append the length of the stack with `l`. Sets the stack equal to the length of the stack before this command.
1. Clear the stack with `x`.
1. Pop and discard the top of the stack with `,`.
1. Get the top/bottom of the stack with `t` and `b` respectively. Sets the stack/variable to the top/bottom of the stack.
1. Duplicate the top of the stack with `d`.
1. Check if `_stack[-1] > _stack[-2]` with `g`. This overwrites the stack, so it should only be used for a variable or a while loop.
1. While loop with `w(command),(condition}`. Ex. `1w1+,5g} == [5]`
1. Sort the stack with <code>`</code>.
1. Reverse the stack with `v`.
1. Get all possible permutations of the stack with `m`. This returns a list of tuples, so caution should be used. It's also not very efficient.
1. Factorial of the top of the stack with `!`. 
1. Count the items in the stack with `o`. Sets the stack equal to `[element, count...]` for each element in the stack.
1. Join and print the stack with `j`.
1. Create a list with `({values})`. Any operation done on a list is done matrix wise. Ex. `1(234)-s == [6]`.
 