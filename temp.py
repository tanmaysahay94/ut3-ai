#!/usr/bin/python
import random

class Player14:
    def __init__(self):
        pass

    def get_empty_out_of(self, gameb, blal, block_stat):
        cells = []
        for idb in blal:
            id1 = idb / 3
            id2 = idb % 3
            for i in range(id1 * 3, id1 * 3 + 3):
                for j in range(id2 * 3, id2 * 3 + 3):
                    if gameb[i][j] == '-':
                        cells.append((i, j))
        if cells == []:
            for i in range(9):
                for j in range(9):
                    no = i / 3 * 3
                    no += j / 3
                    if gameb[i][j] == '-' and block_stat[no] == '-':
                        cells.append((i, j))
        return cells

    def allowed_moves(self, current_board_game, board_stat, move_by_opponent, flag):
        if move_by_opponent[0] == -1 and move_by_opponent[1] == -1:
            return [(4, 4)]
        for_corner = [0, 2, 3, 5, 6, 8]
        # list of permitted blocks based on old move
        blocks_allowed = []
        mod = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        (x, y) = move_by_opponent
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
        crrnt_brd_gm = current_board_game[:]
        brd_stt = board_stat[:]
        mv_by_ppnnt = move_by_opponent[:]
        node = (crrnt_brd_gm, brd_stt, mv_by_ppnnt)
        ret = self.alphaBetaPruning(node, 4, -inf, inf, True, flag)
        my_move = ret[1]
        print my_move[0], my_move[1]
#        moves = self.allowed_moves(crrnt_brd_gm, brd_stt, mv_by_ppnnt, flag)
#        return random.choice(moves)
        return my_move

    def getOpp(self, flg):
        if flg == 'o':
            return 'x'
        return 'o'

    def getChildren(self, node, flag):
        # returns a list of children where type(child) == node
        generatedChildren = []
        child_board, child_bstat, child_opp_move = node
        possible_moves = self.allowed_moves(child_board, child_bstat, child_opp_move, flag)
        for move in possible_moves:
            x, y = move
            tmp_board, tmp_bstat, tmp_opp_move = node
            tmp_board[x][y] = flag
 #           tmp_bstat = self.getbstat(tmp_bstat, tmp_board, move, flag)
            tmp_opp_move = move
            generatedChildren.append((tmp_board, tmp_bstat, tmp_opp_move))
        return generatedChildren

    def getbstat(self, board_stat, board, move, flag):
        ret_board_stat = board_stat
        x, y = move
        p, q = x/3, y/3
        cell = 3 * p + q
        if ret_board_stat[cell] != '-':
            return ret_board_stat
        else:
            base_x = 3 * p
            base_y = 3 * q
            f = flag
            if ((board[base_x][base_y] == f and board[base_x][base_y+1] == f and board[base_x][base_y+2] == f) or \
                    (board[base_x+1][base_y] == f and board[base_x+1][base_y+1] == f and board[base_x+1][base_y+2] == f) or \
                    (board[base_x+2][base_y] == f and board[base_x+2][base_y+1] == f and board[base_x+2][base_y+2] == f) or \
                    (board[base_x][base_y] == f and board[base_x+1][base_y] == f and board[base_x+2][base_y] == f) or \
                    (board[base_x][base_y+1] == f and board[base_x+1][base_y+1] == f and board[base_x+2][base_y+1] == f) or \
                    (board[base_x][base_y+2] == f and board[base_x+1][base_y+2] == f and board[base_x+2][base_y+2] == f) or \
                    (board[base_x][base_y] == f and board[base_x+1][base_y+1] == f and board[base_x+2][base_y+2] == f) or \
                    (board[base_x+2][base_y] == f and board[base_x+1][base_y+1] == f and board[base_x][base_y+2] == f)):
                ret_board_stat[cell] = f
            return ret_board_stat

    def isTerminal(self, node):
        game_board = node[0][:]
        bs = node[1][:]
        block_stat = bs[:]
        if bs[0] == bs[1] and bs[1] == bs[2] and bs[1] != '-' and bs[1] \
            != 'd' or bs[3] != 'd' and bs[3] != '-' and bs[3] == bs[4] \
            and bs[4] == bs[5] or bs[6] != 'd' and bs[6] != '-' \
            and bs[6] == bs[7] and bs[7] == bs[8]:
            return (True, 'W')
        elif bs[0] != 'd' and bs[0] == bs[3] and bs[3] == bs[6] \
            and bs[0] != '-' or bs[1] != 'd' and bs[1] == bs[4] \
            and bs[4] == bs[7] and bs[4] != '-' or bs[2] != 'd' \
            and bs[2] == bs[5] and bs[5] == bs[8] and bs[5] != '-':
    # # Col win
            return (True, 'W')
        elif bs[0] == bs[4] and bs[4] == bs[8] and bs[0] != '-' \
            and bs[0] != 'd' or bs[2] == bs[4] and bs[4] == bs[6] \
            and bs[2] != '-' and bs[2] != 'd':
    # # Diag win
            return (True, 'W')
        else:
            smfl = 0
            for i in range(9):
                for j in range(9):
                    if game_board[i][j] == '-' and block_stat[i / 3 * 3 + j / 3] == '-':
                        smfl = 1
                        break
            if smfl == 1:
                        # Game is still on!
                return (False, 'Continue')
            else:
                        # Changed scoring mechanism
                        # 1. If there is a tie, player with more boxes won, wins.
                        # 2. If no of boxes won is the same, player with more corner move, wins.
                point1 = 0
                point2 = 0
                for i in block_stat:
                    if i == 'x':
                        point1 += 1
                    elif i == 'o':
                        point2 += 1
                if point1 > point2:
                    return (True, 'P1')
                elif point2 > point1:
                    return (True, 'P2')
                else:
                    point1 = 0
                    point2 = 0
                    for i in range(len(game_board)):
                        for j in range(len(game_board[i])):
                            if i % 3 != 1 and j % 3 != 1:
                                if game_board[i][j] == 'x':
                                    point1 += 1
                                elif game_board[i][j] == 'o':
                                    point2 += 1
                    if point1 > point2:
                        return (True, 'P1')
                    elif point2 > point1:
                        return (True, 'P2')
                    else:
                        return (True, 'D')

    def heuristic(self, node):
        return random.choice([0, 1])

    def alphaBetaPruning(self, node, depth, alpha, beta, maximizingPlayer, flg):
        # returns a tuple (a, b) where a is the heuristic value and b is the move, which itself is a tuple
        if depth == 0 or self.isTerminal(node)[0]:
            return (self.heuristic(node), node[2])
        if maximizingPlayer:
            v = -inf
            children = self.getChildren(node, flg)
            for child in children:
                print child[2][0], child[2][1]
                tmp = self.alphaBetaPruning(child, depth - 1, alpha, beta, False, self.getOpp(flg))
                if tmp[0] > v:
                    v = tmp[0]
                if alpha < v:
                    alpha = v
                    move_to_return = tmp[1]
                if beta <= alpha:
                    break
            return (v, move_to_return)
        else:
            v = inf
            children = self.getChildren(node, self.getOpp(flg))
            for child in children:
                print child[2][0], child[2][1]
                tmp = self.alphaBetaPruning(child, depth - 1, alpha, beta, True, flg)
                if tmp[0] < v:
                    v = tmp[0]
                if beta > v:
                    beta = v
                    move_to_return = tmp[1]
                if beta <= alpha:
                    break
            return (v, move_to_return)
