from hightowers4 import hightowers
from render import render


# TEST 1
def run_test1():
    print('TEST 1:')
    start = (0, 0)
    end = (0, 1)
    obstacles = []
    width = 3
    height = 3
    print('expected:', [((0, 0), (0, 1))])
    print('actual:  ', hightowers(start, end, obstacles, width, height))
    render('test1', obstacles, width, height, hightowers(start, end, obstacles, width, height))


# TEST 2
def run_test2():
    print('TEST 2:')
    start = (1, 3)
    end = (3, 1)
    obstacles = [((0, 0), (0, 4)), ((0, 4), (4, 4)),
                 ((4, 4), (4, 0)), ((4, 0), (0, 0))]
    width = 4
    height = 4
    print('expected:', [((1, 3), (3, 3)), ((3, 3), (3, 1))])
    print('actual:  ', hightowers(start, end, obstacles, width, height))


# TEST 3
def run_test3():
    print('TEST 3:')
    start = (0, 4)
    end = (3, 3)
    obstacles = [((1, 0), (1, 4)), ((1, 4), (4, 4)), ((4, 4), (4, 1))]
    width = 5
    height = 5
    print('expected:', [((0, 4), (0, 5)), ((0, 5), (5, 5)), ((5, 5), (5, 0)), ((5, 0), (3, 0)), ((3, 0), (3, 3))])
    print('actual:  ', hightowers(start, end, obstacles, width, height))


# TEST 4
def run_test4():
    print('TEST 4:')
    start = (1, 5)
    end = (4, 4)
    obstacles = [((2, 0), (2, 5)), ((2, 5), (5, 5)), ((5, 5), (5, 2)), ((0, 1), (2, 1)),
                 ((0, 1), (0, 7)), ((0, 7), (7, 7)), ((7, 7), (7, 0)), ((7, 0), (2, 0))]
    width = 7
    height = 7
    print('expected:', [((1, 5), (1, 6)), ((1, 6), (6, 6)), ((6, 6), (6, 1)), ((6, 1), (4, 1)), ((4, 1), (4, 4))])
    print('actual:  ', hightowers(start, end, obstacles, width, height))


# TEST 5
def run_test5():
    print('TEST 5:')
    start = (1, 1)
    end = (3, 2)
    obstacles = [((2, 1), (2, 3)), ((2, 3), (4, 3)), ((4, 3), (4, 1)), ((4, 1), (2, 1)), ((
        0, 0), (0, 4)), ((0, 4), (5, 4)), ((5, 4), (5, 0)), ((5, 0), (0, 0))]
    width = 6
    height = 5
    print('expected:', None)
    print('actual:  ', hightowers(start, end, obstacles, width, height))



# TEST 6
def run_test6():
    print('TEST 6:')
    start = (0, 5)
    end = (4, 5)
    obstacles = [((1, 5), (1, 9)), ((3, 8), (3, 0))]
    width = 5
    height = 10
    print('expected:', [((0, 5), (0, 4)), ((0, 4), (2, 4)), ((2, 4), (2, 9)), ((2, 9), (4, 9)), ((4, 9), (4, 5))])
    print('actual:  ', hightowers(start, end, obstacles, width, height))


# TEST 7
def run_test7():
    print('TEST 7:')
    start = (0, 0)
    end = (12, 12)
    obstacles = [((1, 0), (2, 0)), ((2, 0), (2, 4)), ((0, 6), (4, 6)), ((6, 0), (6, 9)), ((
        1, 11), (8, 11)), ((8, 5), (12, 5)), ((9, 8), (11, 8)), ((11, 8), (11, 12))]
    width = 12
    height = 12
    print('expected:', [((0, 0), (0, 5)), ((0, 5), (5, 5)), ((5, 5), (5, 10)), ((5, 10), (7, 10)), ((7, 10), (7, 6)), ((7, 6), (12, 6)), ((12, 6), (12, 12))])
    print('actual:  ', hightowers(start, end, obstacles, width, height))


# TEST 8
def run_test8():
    print('TEST 8:')
    start = (1, 1)
    end = (7, 7)
    obstacles = [((0, 0), (0, 8)), ((0, 8), (8, 8)), ((8, 8), (8, 0)), ((8, 0), (0, 0)), ((
        2, 0), (2, 5)), ((2, 5), (4, 5)), ((2, 8), (2, 7)), ((2, 7), (4, 7)), ((4, 2), (6, 2)), ((6, 2), (6, 8))]
    width = 9
    height = 9
    print('expected:', [((1, 1), (1, 6)), ((1, 6), (5, 6)), ((5, 6), (5, 4)), ((5, 4), (3, 4)), ((3, 4), (3, 1)), ((3, 1), (7, 1)), ((7, 1), (7, 7))])
    print('actual:  ', hightowers(start, end, obstacles, width, height))


run_test1()  # pass
# run_test2()  # pass
# run_test3()  # pass, need post editing
# run_test4()  # pass, need post editing
# run_test5()  # pass
# run_test6()  # pass
# run_test7()  # pass, need post editing
# run_test8()  # pass, need post editing