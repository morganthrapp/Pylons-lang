from main import run
import sys

sys.argv = sys.argv[1:]

assert run('#25#2+7*') == [189]
assert run('26/') == [3]
assert run('48*') == [4 * 8]
assert run('1{1+,3}') == [4]
assert run('1{1+,#11#}') == [12]
assert run('12+;0') == [3, 3]
assert run('12+;04+') == [3, 7]
assert run('   12+34+56;#4#') == [3, 7, 5, 10, 5, 6]
assert run('4q') == [2]
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
assert run('2fA2+@A') == [4]
assert run('"A"') == [65]
assert run('"Hello, World!"c') == [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
assert run('2fA2.+@AA') == [2, 4, 6]
assert run('11fA..+@{A,9}') == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
assert run('1234s') == [10]
assert run('123l') == [3]
assert run('123x') == []
assert run('12,') == [1]
assert run('12t') == [2]
assert run('12b') == [1]
assert run('1d') == [1, 1]
assert run('11-z2') == [0]
assert run('1w1+,5g}') == [5]
assert run('3542`') == [2, 3, 4, 5]
assert run('123v') == [3, 2, 1]
assert run('012u') == [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
assert run('5m')
assert run('1111223o') == [4, 1, 2, 2, 1, 3]
assert run('1234j') == [1, 2, 3, 4]
assert run('3!') == [6]
assert run('1(234)-s') == [6]
assert run('(234)1-2hs') == [8]
assert run(':A()A1h') == [[1]]
assert run('(123)(12)+') == [[4, 5, 6]]
assert run('(123)(12)*') == [[3, 6, 9]]