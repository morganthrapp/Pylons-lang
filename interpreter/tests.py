from main import run, tokenize

assert run('|25|2+7*') == [189]
assert run('48*') == [4 * 8]
assert run('1{1+,3}') == [4]
assert run('1{1+,|11|}') == [12]
assert run('|72||101|c') == [72, 101]
assert run('12+;0') == [3, 3]
assert run('12+;04+') == [3, 7]
assert run('   12+34+56;|4|') == [3, 7, 5, 10, 5, 6]
assert run('4s') == [2]
assert run('22e') == [4]
assert run('12\\') == [2, 1]
assert run(':A1A2+') == [3]
assert run('[A12+]A2A+') == [3, 5]
assert run('[A|11|2+]A') == [13]
assert run('23p') == [2, 3]  # Should also print [2, 3]
assert run('2i+') == [4]  # This takes input of 2 and returns 4