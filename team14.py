import random
import copy

inf = 1e6

class Player14(object):

    def __init__(self):
        self.inf = 1e10

    def move(self, current_board_game, board_stat, move_by_opponent, flag):
        if move_by_opponent == (-1, -1):
            return (4, 4)
        self.myMark = flag
        self.other = self.getOpp(self.myMark)
        possible_cells = self.getValidCells(current_board_game, board_stat, move_by_opponent)
        self.node_count = 0
        idx = possible_cells[0]
        best_val = -self.inf
        depth = 0
        while best_val != inf and self.node_count < 10000:
            depth += 1
            best_val = -self.inf
            for cell in possible_cells:
                bstat = board_stat[:]
                self.updateBoardStat(current_board_game, bstat, cell, flag)
                temp = self.alphaBetaPruning(current_board_game, bstat, depth, -self.inf, self.inf, True, cell)
                if temp > best_val:
                    best_val = temp
                    idx = cell
                current_board_game[cell[0]][cell[1]] = '-'
            my_move = idx
            return my_move

    def getOpp(self, flag):
        if flag == 'x':
            return 'o'
        return 'x'

    def getValidCells(self, current_board_game, board_stat, move_by_opponent):
        row, column = move_by_opponent[0] % 3, move_by_opponent[1] % 3
        valid_blocks = []
        if row == 0 and column == 0:
            valid_blocks = [0, 1, 3]
        elif row == 0 and column == 2:
            valid_blocks = [1, 2, 5]
        elif row == 2 and column == 0:
            valid_blocks = [3, 6, 7]
        elif row == 2 and column == 2:
            valid_blocks = [5, 7, 8]
        else:
            valid_blocks = [3 * row + column]
        valid_cells = []
        #must generate valid cells now
