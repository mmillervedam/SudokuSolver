"""
Test Suite for Sudoku.
"""
import poc_simpletest

# Global Test Cases
INVALID_PARTIAL1 = {(0,0):1, (0,1):1}
INVALID_PARTIAL2 = {(0,0):2, (2,1):2}
INVALID_PARTIAL3 = {(0,0):3, (5,0):3}
INVALID_PARTIAL4 = {(0,1):1, (0,3):2, (0,5):3, (0,8):4, (3,0):5,
                    (5,0):6, (8,0):7, (1,1):8, (2,2):9}

VALID_PARTIAL = {(0,0):1, (0,1):2, (0,2):3, (1,0):4, (1,1):5,
                 (1,2):6, (2,0):7, (2,1):8}

INVALID_FULL = {(0,0):1, (0,1):2, (0,2):3, (0,3):4, (0,4):5,
                (0,5):6, (0,6):7, (0,7):8, (0,8):9}
for row in range(1,9):
        for col in range(9):
            INVALID_FULL[(row, col)] = row

VALID_FULL = {(0,0):1, (0,1):2, (0,2):3, (0,3):4, (0,4):5, (0,5):6, (0,6):7, (0,7):8, (0,8):9,
              (1,0):4, (1,1):5, (1,2):6, (1,3):7, (1,4):8, (1,5):9, (1,6):1, (1,7):2, (1,8):3,
              (2,0):7, (2,1):8, (2,2):9, (2,3):1, (2,4):2, (2,5):3, (2,6):4, (2,7):5, (2,8):6,
              (3,0):2, (3,1):3, (3,2):4, (3,3):5, (3,4):6, (3,5):7, (3,6):8, (3,7):9, (3,8):1,
              (4,0):5, (4,1):6, (4,2):7, (4,3):8, (4,4):9, (4,5):1, (4,6):2, (4,7):3, (4,8):4,
              (5,0):8, (5,1):9, (5,2):1, (5,3):2, (5,4):3, (5,5):4, (5,6):5, (5,7):6, (5,8):7,
              (6,0):3, (6,1):4, (6,2):5, (6,3):6, (6,4):7, (6,5):8, (6,6):9, (6,7):1, (6,8):2,
              (7,0):6, (7,1):7, (7,2):8, (7,3):9, (7,4):1, (7,5):2, (7,6):3, (7,7):4, (7,8):5,
              (8,0):9, (8,1):1, (8,2):2, (8,3):3, (8,4):4, (8,5):5, (8,6):6, (8,7):7, (8,8):8}

GAME1 = {(0,2):7, (0,8):3, (1,2):8, (1,5):6, (1,7):4,
         (2,4):7, (2,7):5, (3,0):1, (3,4):4, (3,8):2,
         (4,1):8, (5,0):2, (5,3):8, (5,5):5, (5,8):7,
         (6,1):7, (6,4):5, (7,1):6, (7,3):3, (7,6):8,
         (7,7):9, (8,0):4, (8,6):5}

# The main event
def run_suite1(Sudoku, printout = False):
    """
    Testing code for Sudoku class set up functions.
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # Testing initializer, set_board and update functions
    suite.run_test(Sudoku().rows[0], [0,0,0,0,0,0,0,0,0], "Init Test #1:")
    suite.run_test(Sudoku().cols[0], [0,0,0,0,0,0,0,0,0], "Init Test #2:")
    suite.run_test(Sudoku().boxes[1], [0,0,0,0,0,0,0,0,0], "Init Test #3:")

    test1 = Sudoku(VALID_FULL)
    suite.run_test(test1.rows[0], [1,2,3,4,5,6,7,8,9], "Init Test #4:")
    suite.run_test(test1.cols[0], [1,4,7,2,5,8,3,6,9], "Init Test #5:")
    suite.run_test(test1.boxes[1], [4,5,6,7,8,9,1,2,3], "Init Test #6:")

    # Testing next_empty()

    # Testing is_valid()
    suite.run_test(Sudoku(INVALID_PARTIAL1).is_valid(), False, "is_valid() Test #1")
    suite.run_test(Sudoku(INVALID_PARTIAL2).is_valid(), False, "is_valid() Test #2")
    suite.run_test(Sudoku(INVALID_PARTIAL3).is_valid(), False, "is_valid() Test #3")
    suite.run_test(Sudoku(INVALID_PARTIAL4).is_valid(), False, "is_valid() Test #4")
    suite.run_test(Sudoku(VALID_PARTIAL).is_valid(), True, "is_valid() Test #5")
    suite.run_test(Sudoku(INVALID_FULL).is_valid(), False, "is_valid() Test #6")
    suite.run_test(Sudoku(VALID_FULL).is_valid(), True, "is_valid() Test #7")
    suite.run_test(Sudoku(GAME1).is_valid(), True, "is_valid() Test #8")

    # Testing is_full()
    suite.run_test(Sudoku(INVALID_PARTIAL4).is_full(), False, "is_full() Test #1")
    suite.run_test(Sudoku(VALID_PARTIAL).is_full(), False, "is_full() Test #2")
    suite.run_test(Sudoku(INVALID_FULL).is_full(), True, "is_full() Test #3")
    suite.run_test(Sudoku(VALID_FULL).is_full(), True, "is_full() Test #4")

    # Testing is_solved()
    suite.run_test(Sudoku(INVALID_PARTIAL4).is_solved(), False, "is_solved() Test #1")
    suite.run_test(Sudoku(VALID_PARTIAL).is_solved(), False, "is_solved() Test #2")
    suite.run_test(Sudoku(INVALID_FULL).is_solved(), False, "is_solved() Test #3")
    suite.run_test(Sudoku(VALID_FULL).is_solved(), True, "is_solved() Test #4")

    # Testing clone()and set_pos()
    test2 = Sudoku(VALID_PARTIAL)
    test3 = test2.clone()
    suite.run_test(test3.rows[1][1], 5, "clone() Test #1")
    suite.run_test(test2.cols, test3.cols, "clone() Test #2")
    test3.set_pos(1,1,2)
    suite.run_test(test3.rows[1][1], 2, "clone() Test #3")
    suite.run_test(test2.rows[1][1], 5, "clone() Test #4")

    # report test results
    suite.report_results()

    # optional console printout
    if printout:
        print ""
        print "==========================================="
        print "Testing __init__(including set_board and update fxns) "
        print "-------------------------------------------"
        print "UNSEEDED BOARD:"
        print Sudoku()
        print "SEEDED BOARD:"
        print test1
        print "First Row: ", test1.rows[0]
        print "First Col: ", test1.cols[0]
        print "Second Box: ", test1.boxes[1]
        print ""
        print "==========================================="
        print "Testing is_valid(), is_full() and is_solved() "
        print "-------------------------------------------"
        for setup in [INVALID_PARTIAL4, VALID_PARTIAL, INVALID_FULL, VALID_FULL]:
            board = Sudoku(setup)
            print "BOARD:"
            print board
            print "Valid Board? ", board.is_valid()
            print "Full Board? ", board.is_full()
            print "Solved Board? ", board.is_solved()
            print "-------------------------------------------"

def run_suite2(Sudoku, printout = False):
    """
    Testing code for helper functions in solving process.
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # Testing get_moves() and next_empty()
    test1 = Sudoku(VALID_PARTIAL)
    suite.run_test(test1.get_moves(2,2), [9], "get_moves() Test #1:")
    suite.run_test(test1.get_moves(3,0), [2,3,5,6,8,9], "get_moves() Test #2:")
    suite.run_test(test1.next_empty(), ((2,2),[9]), "next_empty() Test #1")

    test2 = Sudoku(INVALID_PARTIAL4)
    suite.run_test(test2.get_moves(0,0), [], "get_moves() Test #3:")
    suite.run_test(set(test2.get_moves(0,4)), set([5,6,7,8,9]), "get_moves() Test #4:")
    suite.run_test(test2.next_empty(), None, "next_empty() Test #2")

    # Testing trial()
    test3 = Sudoku(VALID_FULL)
    fifth_row =  list(test3.rows[5])
    test3.rows[5] = [0,0,0,0,0,0,0,0,0]
    #test3.update()
    suite.run_test(test3.is_full(), False, "trial() Test #1")
    trial3 = test3.trial()
    suite.run_test(trial3.is_full(), True, "trial() Test #2")
    suite.run_test(trial3.rows[5], fifth_row, "trial() Test #3")
    suite.run_test(trial3.is_solved(), True, "trial() Test #4")

    test4 = Sudoku(VALID_FULL)
    last_box =  list(test4.boxes[8])
    test4.rows[6] = [3,4,5,6,7,8,0,0,0]
    test4.rows[7] = [6,7,8,9,1,2,0,0,0]
    test4.rows[8] = [9,1,2,3,4,5,0,0,0]
    #test4.update()
    suite.run_test(test4.is_full(), False, "trial() Test #5")
    suite.run_test(test4.boxes[8], [0,0,0,0,0,0,0,0,0], "trial() Test #6")
    trial4 = test4.trial()
    suite.run_test(trial4.is_full() or not trial4.is_valid(), True, "trial() Test #7")
    suite.run_test(trial3.is_solved() or trial4.boxes[8].count(0) > 0, True, "trial() Test #8")

    test5 = Sudoku(VALID_FULL)
    last_box =  list(test5.boxes[8])
    test5.rows[6] = [0,0,0,0,0,0,0,0,0]
    test5.rows[7] = [0,0,0,0,0,0,0,0,0]
    test5.rows[8] = [0,0,0,0,0,0,0,0,0]
    #test5.update()
    trial5 = test5.trial()
    suite.run_test(trial5.is_full(), trial5.is_valid(), "trial() Test #9")
    suite.run_test(trial5.is_solved(), trial5.boxes[8].count(0) == 0, "trial() Test #10")

    test6 = Sudoku(INVALID_PARTIAL4)
    trial6 = test6.trial()
    suite.run_test(test6.boxes, trial6.boxes, "trial() Test #11")
    suite.run_test(trial6.next_empty(), None, "trial() Test #12")

    test7 = Sudoku(INVALID_PARTIAL4)
    test7.rows[0][1] = 0
    #test7.update()
    trial7 = test7.trial()
    suite.run_test(trial7.is_full(), trial7.is_valid(), "trial() Test #13")
    suite.run_test(trial7.is_solved(),trial7.boxes[8].count(0)== 0, "trial() Test #14")


    # report test results
    suite.report_results()

    # optional console printout
    if printout:
        print ""
        print "==========================================="
        print "Testing get_moves() and next_empty"
        print "-------------------------------------------"
        print "VALID PARTIAL BOARD:"
        print test1
        print "Moves for (2,2) ", test1.get_moves(2,2)
        print "Moves for (3,0): ", test1.get_moves(3,0)
        print ""
        print "==========================================="
        print "Testing trial()"
        print "-------------------------------------------"
        print "ORIGINAL BOARD:"
        print test3
        print "Trial Results: "
        print trial3
        print "Valid Board? ", trial3.is_valid()
        print "Full Board? ", trial3.is_full()
        print "Solved Board? ", trial3.is_solved()
        print "-------------------------------------------"
        print "ORIGINAL BOARD:"
        print test5
        print "Trial Results: "
        print trial5
        print "Valid Board? ", trial5.is_valid()
        print "Full Board? ", trial5.is_full()
        print "Solved Board? ", trial5.is_solved()
        print "-------------------------------------------"
        print "ORIGINAL BOARD:"
        print test7
        print "Trial Results: "
        print trial7
        print "Valid Board? ", trial7.is_valid()
        print "Full Board? ", trial7.is_full()
        print "Solved Board? ", trial7.is_solved()
        print "-------------------------------------------"

def run_suite3(Sudoku, printout = False):
    """
    Testing suite for solve function.
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # Testing get_moves() and next_empty()
    test1 = Sudoku(VALID_FULL)
    suite.run_test(test1.solve().is_solved(), True, "solve() Test #1:")

    test2 = Sudoku(VALID_FULL)
    test2.rows[6] = [3,4,5,6,7,8,0,0,0]
    test2.rows[7] = [6,7,8,9,1,2,0,0,0]
    test2.rows[8] = [9,1,2,3,4,5,0,0,0]
    #test2.update()
    trial2= test2.solve()
    suite.run_test(trial2.is_solved(), True, "solve() Test #2:")

    test3 = Sudoku(INVALID_PARTIAL4)
    test3.rows[0][1] = 0
    #test3.update()
    trial3 = test3.solve()
    suite.run_test(trial3.is_full(), trial3.is_valid(), "solve() Test #3")

    test4 = Sudoku(GAME1)
    suite.run_test(test4.is_solved(), False, "solve() Test #4")
    trial4 = test4.solve()
    suite.run_test(trial4.is_solved(), True, "solve() Test #5")

    # report test results
    suite.report_results()

    # optional console printout
    if printout:
        print ""
        print "==========================================="
        print "Testing solve()"
        print "-------------------------------------------"
        print "ORIGINAL BOARD:"
        print test2
        print "Solve Results: "
        print trial2
        print "Valid Board? ", trial2.is_valid()
        print "Full Board? ", trial2.is_full()
        print "Solved Board? ", trial2.is_solved()
        print ""
        print "-------------------------------------------"
        print "ORIGINAL BOARD:"
        print test3
        print "Solve Results: "
        print trial3
        print "Valid Board? ", trial3.is_valid()
        print "Full Board? ", trial3.is_full()
        print "Solved Board? ", trial3.is_solved()
        print "-------------------------------------------"
        print "ORIGINAL BOARD:"
        print test4
        print "Solve Results: "
        print trial4
        print "Valid Board? ", trial4.is_valid()
        print "Full Board? ", trial4.is_full()
        print "Solved Board? ", trial4.is_solved()
