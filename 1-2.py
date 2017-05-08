def count_inversions(x):
    if len(x) == 1:
        return 0, x
    left = x[:len(x)/2]
    right = x[len(x)/2:]
    c_left, left = count_inversions(left)
    c_right, right = count_inversions(right)
    c_merge, x_sorted = merge(left, right)
    c = c_left + c_right + c_merge
    return c, x_sorted

def merge(left, right):
    merged = []
    c = 0
    i = 0
    j = 0
    while True:
        if i == len(left):
            for j in range(j, len(right)):
                merged.append(right[j])
            break
        elif j == len(right):
            for i in range(i, len(left)):
                merged.append(left[i])
            break
        l = left[i]
        r = right[j]
        if l <= r:
            merged.append(l)
            i += 1
        else:
            merged.append(r)
            j += 1
            c += len(left) - i
    return c, merged

def test_one_inversion_even():
    c, a = count_inversions([1, 3, 2, 4])
    assert c == 1

def test_one_inversion_equal():
    c, a = count_inversions([1, 3, 1, 4])
    assert c == 1

def test_total_inversion():
    c, a = count_inversions([3, 4, 1, 2])
    assert c == 4

def quiz():
    numbers = []
    with open('1-2-input.txt') as fd:
        for line in fd:
            numbers.append(int(line.strip()))
    c, a = count_inversions(numbers)
    print(c)

test_one_inversion_even()
test_one_inversion_equal()
test_total_inversion()
quiz()
