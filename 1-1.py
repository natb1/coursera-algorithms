def test_that_it_multiplies_small_numbers():
    assert int(multiply('32', '64')) == 32 * 64

def test_that_it_multiplies_numbers_with_odd_digits():
    assert int(multiply('333', '666')) == 333 * 666

def test_that_it_multiplies_numbers_with_1_digit():
    assert int(multiply('2', '3')) == 2 * 3

def test_that_it_multiplies_different_n():
    assert int(multiply('12', '3')) == 12 * 3

def test_star():
    result = star(4, '672', 2, str(56*34), str(78*12), '2652')
    expected = 1234 * 5678
    assert int(result) == expected, '{} {}'.format(result, expected)

#def test_star_odd_n():
#    result = star(3, '672', 1, str(56*34), str(78*12), '2652')
#    expected = 123 * 567
#    assert int(result) == expected, '{} {}'.format(result, expected)

def test_string_addition_without_remainder():
    assert int(string_addition('111', '222')) == 111 + 222

def test_string_addition_with_remainder():
    assert int(string_addition('999', '999')) == 999 + 999

def test_string_addition_with_different_n():
    result = string_addition('9', '9999999')
    expected = 9 + 9999999
    assert int(result) == expected, '{} {}'.format(result, expected)

def test_big_numbers():
    x = '3141592653589793238462643383279502884197169399375105820974944592'
    y = '2718281828459045235360287471352662497757247093699959574966967627'
    result = multiply(x, y)
    expected = '8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184'
    assert result == expected

def multiply(x, y):
    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))
    xstr = str(x)
    ystr = str(y)
    xpartition = len(x)/2
    ypartition = len(y)/2
    a = x[:xpartition]
    b = x[xpartition:]
    c = y[:ypartition]
    d = y[ypartition:]
    ac = multiply(a, c)
    ad = multiply(a, d)
    bc = multiply(b, c)
    bd = multiply(b, d)
    return star(len(x), ac, len(x)/2, ad, bc, bd).lstrip('0')

def star(acdigit, ac, adbcdigit, ad, bc, bd):
    acpadded = ac + '0'*acdigit
    adbcpadded = string_addition(ad, bc) + '0'*adbcdigit
    return string_addition(string_addition(acpadded, adbcpadded), bd)

def string_addition(x, y):
    offset = abs(len(x) - len(y))
    if len(x) < len(y):
        x = '0'*offset + x
    elif len(y) < len(x):
        y = '0'*offset + y
    remainder = 0
    total = []
    for a, b in reversed(zip(x, y)):
        sum_ = str(int(a) + int(b) + remainder)
        total.insert(0, str(sum_[-1]))
        remainder = 1 if len(sum_) > 1 else 0
    total.insert(0, str(remainder))
    return ''.join(total)

test_string_addition_without_remainder()
test_string_addition_with_remainder()
test_string_addition_with_different_n()
test_star()
#test_star_odd_n()
test_that_it_multiplies_small_numbers()
test_that_it_multiplies_different_n()
#test_that_it_multiplies_numbers_with_odd_digits()
test_that_it_multiplies_numbers_with_1_digit()
test_big_numbers()
