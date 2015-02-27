import random

inf = 1e20

class Player14:

    def __init__(self):
        pass
    
    def get_empty_out_of(self, gameb, blal, block_stat):
        cells = []
        for idb in blal:
            id1 = idb/3
            id2 = idb%3
            for i in range(id1 * 3, id1 * 3 + 3):
                for j in range(id2 * 3, id2 * 3 + 3):
                    if gameb[i][j] == '-':
                        cells.append((i, j))
        if cells == []:
            for i in range(9):
                for j in range(9):
                    no = (i/3) * 3
                    no += (j/3)
                    if gameb[i][j] == '-' and block_stat[no] == '-':
                        cells.append((i, j))
        return cells


    def allowed_moves(self, current_board_game, board_stat, move_by_opponent, flag):
        if move_by_opponent[0] == -1 and move_by_opponent[1] == -1:
            return [(4, 4)]
        for_corner = [0, 2, 3, 5, 6, 8]
        #list of permitted blocks based on old move
        blocks_allowed = []
        mod = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        x, y = move_by_opponent
        if x in for_corner and y in for_corner:
            if x % 3 == 0 and y % 3 == 0:
                blocks_allowed = [0, 1, 3]
            elif x % 3 == 0 and y % 3 == 2:
                blocks_allowed = [1, 2, 5]
            elif x % 3 == 2 and y % 3 == 0:
                blocks_allowed = [3, 6, 7]
            elif x % 3 == 2 and y % 3 == 2:
                blocks_allowed = [5, 7, 8]
        else:
            if x % 3 == 0 and y % 3 == 1:
                blocks_allowed = [1]
            elif x % 3 == 1 and y % 3 == 0:
                blocks_allowed = [3]
            elif x % 3 == 2 and y % 3 == 1:
                blocks_allowed = [7]
            elif x % 3 == 1 and y % 3 == 2:
                blocks_allowed = [5]
            elif x % 3 == 1 and y % 3 == 1:
                blocks_allowed = [4]
        for i in reversed(blocks_allowed):
            if board_stat[i] != '-':
                blocks_allowed.remove(i)
        cells = self.get_empty_out_of(current_board_game, blocks_allowed, board_stat)
        return cells

    def move(self, current_board_game, board_stat, move_by_opponent, flag):
        # current_board_game is 2-D 9x9 with char 'o', 'x', '-'
        # board_stat is 1-D 9-size with char 'o', 'x', '-'
        # move by opponent is a tuple (p, q)
        # flag is a character which tells me whether I'm 'x' or 'o'
        node = (current_game_board, board_stat, move_by_opponent, flag)
        ret = self.alphaBetaPruning(node, 4, -inf, inf, True, flag)
        my_move = ret[1]
        return my_move

    def getOpp(self, flg):
        if flg == 'o':
            return 'x'
        return 'o'

    def getChildren(self, node, flag):
        # returns a list of tuples (a, b) where a is the state of the game and b is a tuple, i.e., the move we are making
        generatedChildren = []
        return generatedChildren

    def isTerminal(self, node):
        pass

    def heuristic(self, node):
        pass

    def alphaBetaPruning(self, node, depth, alpha, beta, maximizingPlayer, flg):
        # returns a tuple (a, b) where a is the heuristic value and b is the move, which itself is a tuple
        if depth == 0 or self.isTerminal(node):
            return self.heuristic(node), node[2]
        if maximizingPlayer:
            v = -inf
            children = self.getChildren(node, flg)
            for child, move in children:
                tmp = self.alphaBetaPruning(child, depth - 1, alpha, beta, False, self.getOpp(flg))
                if tmp[0] > v:
                    v = tmp[0]
                if alpha < v:
                    alpha = v
                    move_to_return = tmp[1]
                if beta <= alpha:
                    break
            return v, move_to_return
        else:
            v = inf
            children = self.getChildren(node, self.getOpp(flg))
            for child in children:
                tmp = self.alphaBetaPruning(child, depth - 1, alpha, beta, True, flg)
                if tmp[0] < v:
                    v = tmp[0]
                if beta > v:
                    beta = v
                    move_to_return = tmp[1]
                if beta <= alpha:
                    break
            return v, move_to_return
