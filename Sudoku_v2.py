"""
Sudoku Class Module.
"""

from StackClass import Stack # for Python2
import sudoku_testsuite as testsuite # for Python2
from collections import deque

# Create Sudoku board class
class Sudoku():
    "Class to keep track of a sudoku board object."
    def __init__(self, setup = None):
        """
        Initialize sudoku board.
        Option to pass in initial state as list of rows.
        """
        self.rows = [[0]*9 for dummy_idx in range(9)]
        #self.cols = [[0]*9 for dummy_idx in range(9)]
        #self.boxes = [[0]*9 for dummy_idx in range(9)]
        if setup:
            self.set_board(setup)
            #self.update()

    def __str__(self):
        board = ""
        counter = 0
        for row in self.rows:
            counter += 1
            board += str(row[:3]) + "  "
            board += str(row[3:6])+ "  "
            board += str(row[6:9])+ "\n"
            if counter%3 == 0 and counter < 8:
                board += "\n"
        return board

    @property
    def cols(self):
    #def update_cols(self):
        """ Function to get list of columns."""
        cols = [[],[],[],[],[],[],[],[],[]]
        for row in self.rows:
            for idx in range(9):
                cols[idx].append(row[idx])
        return cols

    @property
    def boxes(self):
    #def update_boxes(self):
        """ Function to get list of boxes."""
        boxes = [[],[],[],[],[],[],[],[],[]]
        for row in range(9):
            r = row//3
            for col in range(9):
                c = col //3
                idx = 3 * r + c
                boxes[idx].append(self.rows[row][col])
        return boxes

    ##################################################
    # Functions for maintaining the board state.

    def set_pos(self, row, col, num):
        """ Sets the given number in that row and column."""
        self.rows[row][col] = num
        #self.update()

    def is_valid(self):
        """
        Check that no row, column or box has duplicates.
        Also returns false if any empty tile has no possible moves.
        """
        for group in self.rows + self.cols + self.boxes:
            if len(set(group)) == 9:
                continue
            elif len(set(group)) != len(group)- group.count(0) + 1:
                #print "Invalid row/col/box: ", group           # for debugging
                return False
        if not self.is_full():
            if not self.next_empty():
                return False
        return True

    def is_full(self):
        "Determines if the board is full."
        count = 0
        for row in self.rows:
            count += row.count(0)
        return count == 0

    def is_solved(self):
        "Determines if the board is solved."
        return self.is_valid() and self.is_full()

    def clone(self):
        setup = {}
        for row in range(9):
            for col in range(9):
                setup[(row,col)] = self.rows[row][col]
        new_board = Sudoku(setup)
        return new_board

    #######################################################
    # Helper functions to facilitate testing
    #
    # def update(self):
    #     """ Function to update columns and rows after changing a tile."""
    #     self.cols = self.update_cols()
    #     self.boxes = self.update_boxes()
    #
    def set_board(self, setup_dict):
        """
        Takes a setup dictionary of coordinates and
        values and loads them on to the given board.
        Assertion error if tile is already full.
        """
        for coord in setup_dict:
            assert self.rows[coord[0]][coord[1]] == 0 , "Tile " +str(coord) +" already full."
            self.rows[coord[0]][coord[1]] = setup_dict[coord]
    #     self.update()

    #######################################################
    # Helper functions for solution process

    def get_moves(self, row, col):
        """
        Function to generate a list of valid entries for that cell.
        """
        box = 3 * (row // 3) + col//3
        bad_num = set(self.rows[row]+self.cols[col]+self.boxes[box])
        #print "Checking cell:", row, col                        # for debugging
        #print "Row contains:", set(self.rows[row])              # for debugging
        #print "Col contins:", set(self.cols[col])               # for debugging
        #print "Box ", box, " contains: ", set(self.boxes[box])  # for debugging
        #print "bad num: ", bad_num                              # for debugging
        options = set([1,2,3,4,5,6,7,8,9])
        return list(options.difference(bad_num))

    def next_empty(self):
        """
        Returns the coordinates and options for an empty cell with
        the least number of possible moves.
        """
        assert (not self.is_full()), "Full board, no possible moves."

        cell = None
        moves = [0,0,0,0,0,0,0,0,0,0,0]
        for row in range(9):
            for col in range(9):
                new = self.get_moves(row,col)
                if self.rows[row][col] != 0:
                    pass
                elif len(new)== 0:
                    return None
                elif len(new)== 1:
                    return (row, col), new
                elif len(new) < len(moves):
                    cell = (row, col)
                    moves = new
        return cell , moves

    def trial(self, stored_game_states = Stack()):
        """
        Recursive function to solve a Sudoku board.
        Stored game states are a stack in the form:
            board, cell tried, remaining options
        """
        trial = self.clone()
        #print "ORIGINAL BOARD: "                        # for debugging
        #print trial                                     # for debugging
        while trial.is_valid() and not trial.is_full():
            #print "Next Move: ", trial.next_empty()     # for debugging
            cell, moves = trial.next_empty()
            trial.set_pos(cell[0], cell[1], moves.pop(0))
            if len(moves) > 0:
                stored_game_states.push((trial.clone(), cell, moves))
                #print ">>>> ARCHIVED: board, ", cell, moves # for debugging
        #print ""                                        # for debugging
        #print "RETURNED BOARD:"                         # for debugging
        #print trial                                     # for debugging
        #print ">>> Board Valid ? ", trial.is_valid()    # for debugging
        #print ">>> Board Full? ", trial.is_full()       # for debugging
        return trial


    ##################################################################
    # Main Solution functions (DEPTH FIRST SEARCH???)

    def solve(self):
        """
        Function to solve a sudoku puzzle using DFS (I think).
        Function modifies and returns a completed puzzle.
        """
        storage = Stack()
        attempt = self.trial(storage)
        #count = 0                           # for debugging
        while not attempt.is_solved():
            #count += 1                      # for debugging
            #print "Attempt #", count, ": ",len(storage)," item(s) in storage"
            if len(storage) == 0:
                print "This sudoku puzzle is not solvable."
                return self
            else:
                (board, cell, moves) = storage.pop()
                board.set_pos(cell[0], cell[1], moves[0])
                if len(moves) > 1:
                    storage.push((board.clone(), cell, moves[1:]))
                attempt = board.trial(storage)
        print "Solution found."
        self = attempt
        return self


# Calls to test suite
testsuite.run_suite1(Sudoku, printout = False)
testsuite.run_suite2(Sudoku, printout = False)
testsuite.run_suite3(Sudoku, printout = False)
