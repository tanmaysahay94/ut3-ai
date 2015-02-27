#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

inf = 1e20


class Player14:

    def __init__(self):
        pass

    def get_empty_out_of(
        self,
        gameb,
        blal,
        block_stat,
        ):

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

    def allowed_moves(
        self,
        current_board_game,
        board_stat,
        move_by_opponent,
        flag,
        ):

        if move_by_opponent[0] == -1 and move_by_opponent[1] == -1:
            return [(4, 4)]
        for_corner = [
            0,
            2,
            3,
            5,
            6,
            8,
            ]

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
        cells = self.get_empty_out_of(current_board_game,
                blocks_allowed, board_stat)
        return cells

    def move(
        self,
        current_board_game,
        board_stat,
        move_by_opponent,
        flag,
        ):

        # current_board_game is 2-D 9x9 with char 'o', 'x', '-'
        # board_stat is 1-D 9-size with char 'o', 'x', '-'
        # move by opponent is a tuple (p, q)
        # flag is a character which tells me whether I'm 'x' or 'o'

        node = (current_game_board, board_stat, move_by_opponent, flag)
        ret = self.alphaBetaPruning(
            node,
            4,
            -inf,
            inf,
            True,
            flag,
            )
        my_move = ret[1]
        return my_move

    def getOpp(self, flg):
        if flg == 'o':
            return 'x'
        return 'o'

    def getChildren(self, node, flag):

        # returns a list of tuples (a, b) where a is the state of the game and b is a tuple, i.e., the move we are making

        generatedChildren = []
        allowedMoves = allowed_moves(node)
        for (i, j) in allowedMoves:
            tempNode = node
            update_lists(tempNode)
            generateChildren.append(tempNode)
        return generatedChildren

    def update_lists(
        game_board,
        block_stat,
        move_ret,
        fl,
        ):

    # move_ret has the move to be made, so we modify the game_board, and then check if we need to modify block_stat

        game_board[move_ret[0]][move_ret[1]] = fl

        block_no = move_ret[0] / 3 * 3 + move_ret[1] / 3
        id1 = block_no / 3
        id2 = block_no % 3
        mg = 0
        mflg = 0
        if block_stat[block_no] == '-':
            if game_board[id1 * 3][id2 * 3] == game_board[id1 * 3
                    + 1][id2 * 3 + 1] and game_board[id1 * 3 + 1][id2
                    * 3 + 1] == game_board[id1 * 3 + 2][id2 * 3 + 2] \
                and game_board[id1 * 3 + 1][id2 * 3 + 1] != '-':
                mflg = 1
            if game_board[id1 * 3 + 2][id2 * 3] == game_board[id1 * 3
                    + 1][id2 * 3 + 1] and game_board[id1 * 3 + 1][id2
                    * 3 + 1] == game_board[id1 * 3][id2 * 3 + 2] \
                and game_board[id1 * 3 + 1][id2 * 3 + 1] != '-':
                mflg = 1

            if mflg != 1:
                for i in range(id2 * 3, id2 * 3 + 3):
                    if game_board[id1 * 3][i] == game_board[id1 * 3
                            + 1][i] and game_board[id1 * 3 + 1][i] \
                        == game_board[id1 * 3 + 2][i] \
                        and game_board[id1 * 3][i] != '-':
                        mflg = 1
                        break

                # ## row-wise

            if mflg != 1:
                for i in range(id1 * 3, id1 * 3 + 3):
                    if game_board[i][id2 * 3] == game_board[i][id2 * 3
                            + 1] and game_board[i][id2 * 3 + 1] \
                        == game_board[i][id2 * 3 + 2] \
                        and game_board[i][id2 * 3] != '-':
                        mflg = 1
                        break

        if mflg == 1:
            block_stat[block_no] = fl

        # check for draw on the block.

        id1 = block_no / 3
        id2 = block_no % 3
        cells = []
        for i in range(id1 * 3, id1 * 3 + 3):
            for j in range(id2 * 3, id2 * 3 + 3):
                if game_board[i][j] == '-':
                    cells.append((i, j))

        if cells == [] and mflg != 1:
            block_stat[block_no] = 'd'  # Draw

        return

    def isTerminal(self, node):
        game_board = node[0]
        bs = node[1]
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
                    if game_board[i][j] == '-' and block_stat[i / 3 * 3
                            + j / 3] == '-':
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
        pass

    def alphaBetaPruning(
        self,
        node,
        depth,
        alpha,
        beta,
        maximizingPlayer,
        flg,
        ):

        # returns a tuple (a, b) where a is the heuristic value and b is the move, which itself is a tuple

        if depth == 0 or self.isTerminal(node)[0]:
            return (self.heuristic(node), node[2])
        if maximizingPlayer:
            v = -inf
            children = self.getChildren(node, flg)
            for (child, move) in children:
                tmp = self.alphaBetaPruning(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    False,
                    self.getOpp(flg),
                    )
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
                tmp = self.alphaBetaPruning(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    True,
                    flg,
                    )
                if tmp[0] < v:
                    v = tmp[0]
                if beta > v:
                    beta = v
                    move_to_return = tmp[1]
                if beta <= alpha:
                    break
            return (v, move_to_return)



			
