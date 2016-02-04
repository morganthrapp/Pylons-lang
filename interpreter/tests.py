from main import run

assert run('#25#2+7*') == [189]
assert run('48*') == [4 * 8]
assert run('1{1+,3}') == [4]
assert run('1{1+,#11#}') == [12]
assert run('#72##101#c') == [72, 101]
assert run('12+;0') == [3, 3]
assert run('12+;04+') == [3, 7]
assert run('   12+34+56;#4#') == [3, 7, 5, 10, 5, 6]
assert run('4s') == [2]
assert run('22e') == [4]
assert run('12\\') == [2, 1]
assert run(':A1A2+') == [3]
assert run('[A12+]A2A+') == [3, 5]
assert run('[A#11#2+]A') == [13]
assert run('23p') == [2, 3]  # Should also print [2, 3]
assert run('2i+') == [2, 2, 72, 101, 108, 108, 111, 32, 87, 111, 114, 208]  # This takes input of 2, "Hello World"
assert run('34%') == [1]
assert run('32&') == [2]
assert run('82^') == [10]
assert run('53|') == [7]
assert run('1~') == [-2]
assert run('23<') == [12]
assert run('28>') == [2]
assert run('#72##101##108##108##111##44##32##87##111##114##108##100##33#c') == [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
assert run('2fA2+@A') == [4]
assert run('"A"') == [65]
assert run('"Hello, World!"c') == [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]