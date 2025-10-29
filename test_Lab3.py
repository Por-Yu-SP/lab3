import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_10_plus():
    result=0
    input_arr = [10,21,44,12,313,3232,4343,567,344,252,242,234,234,45,36,5345,234,1]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert(result==1)


def test_0():
    result = 0
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)

def test_int():
    result = 0
    input_arr = ["abc",123,121,12,2342,12.55]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 2)