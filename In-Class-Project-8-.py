'''
created by: Mahmoud B.

Here is what the program needs to do:
1.Return all elements with an even index
2.Return the first and last elements of any list
3.Replace every third value in a list with None
4.Return the second largest element of a list
5.Move all even elements to the front of the list
6.Return True if the list has adjacent duplicate elements7.
Shift all elements by one to the right by one and move the
last element into first position8.
then each function is followed by its function test
'''
N = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_N = []


def evenIndex(N):
    evens = []
    for i in range(0, len(N)):
        if i % 2 == 0:
            evens.append(N[i])
    return evens


def test_evenIndex():
    assert evenIndex(N) == [0, 2, 4, 6, 8]


def first_last(N):
    return N[0], N[-1]


def test_first_last():
    assert first_last(N) == (0, 9)


def thirdValueNone(N):
    new_N = N
    for i in range(0, len(new_N)):
        if not (i % 3):
            new_N[i] = None
    return new_N


def test_thirdValueNone():
    assert thirdValueNone(N) == ([None, 1, 2, None, 4, 5, None, 7, 8, None])


def secondLargest(N):
    second_max = (sorted(set(N))[-2])
    return second_max


def test_secondLargest():
    assert secondLargest([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8


def evenElementInFront(N):
    for i in range(0, len(N)):
        if i % 2 == 0:
            N.insert(0, N.pop(i))
    return N


def test_evenElementInFront():
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert evenElementInFront(A) == ([8, 6, 4, 2, 0, 1, 3, 5, 7, 9])


def adjacentExist(N):
    for i in range(0, len(N) - 1):
        if N[i] == N[i + 1]:
            return True
    return False


def test_adjacentExist():
    assert adjacentExist(([0, 1, 2, 2, 3, 4, 5])) == True


def shiftByOneRight(N):
    N.insert(0, N.pop(-1))
    return N


def test_shiftByOneRight():
    B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert shiftByOneRight(B) == [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
