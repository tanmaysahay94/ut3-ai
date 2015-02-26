import random

class Player14:

    def __init__(self):
        pass

    def move(self, current_board_game, board_stat, move_by_opponent, flag):
        # current_board_game is 2-D 9x9 with char 'o', 'x', '-'
        # board_stat is 1-D 9-size with char 'o', 'x', '-'
        # move by opponent is a tuple (p, q)
        # flag is a character which tells me whether I'm 'x' or 'o'
        for_corner = [0, 2, 3, 5, 6, 8]

        #list of permitted blocks based on old move
        blocks_allowed = []

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

        cells = get_empty_out_of(current_board_game, blocks_allowed, board_stat)
#       return cells[random.randrange(len(cells))]

def get_empty_out_of(gameb, blal, block_stat):
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
