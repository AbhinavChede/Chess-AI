import chess
import random

class Evaluation:
    def pieceDifference(self, board, color):
        score = 0
        for (piece, value) in [(chess.PAWN, 0.004448), (chess.BISHOP, 0.01468), (chess.KING, 0.88968),\
                            (chess.QUEEN, 0.040036), (chess.KNIGHT, 0.014235), (chess.ROOK, 0.022242)]:
            score += (len(board.pieces(piece, color)) - len(board.pieces(piece, not color))) * value
        return score

    def kingProtection(board, color):
        def isFree(x, y):
            return board[y][x] == ' '

        def getColor(x, y):
            if board[y][x] == ' ':
                return ' '
            elif board[y][x].isupper():
                return 'w'
            elif board[y][x].islower():
                return 'b'

        def isThreatened(board,color, lx, ly):
            if color == 'w':
                if lx < 7 and ly > 0 and board[ly - 1][lx + 1] == 'p':
                    return True
                elif lx > 0 and ly > 0 and board[ly - 1][lx - 1] == 'p':
                    return True
            else:
                if lx < 7 and ly < 7 and board[ly + 1][lx + 1] == 'P':
                    return True
                elif lx > 0 and ly < 7 and board[ly + 1][lx - 1] == 'P':
                    return True
            m = [(lx + 1, ly + 2), (lx + 2, ly + 1), (lx + 2, ly - 1), (lx + 1, ly - 2),
                    (lx - 1, ly + 2), (lx - 2, ly + 1), (lx - 1, ly - 2), (lx - 2, ly - 1)]
            for p in m:
                if p[0] >= 0 and p[0] <= 7 and p[1] >= 0 and p[1] <= 7:
                    if board[p[1]][p[0]] == "n" and color == 'w':
                        return True
                    elif board[p[1]][p[0]] == "N" and color == 'b':
                        return True
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1),
                    (1, 1), (-1, 1), (1, -1), (-1, -1)]
            for d in dirs:
                x = lx
                y = ly
                dx, dy = d
                steps = 0
                while True:
                    steps += 1
                    x += dx
                    y += dy
                    if x < 0 or x > 7 or y < 0 or y > 7:
                        break
                    if isFree(x, y):
                        continue
                    elif getColor(x, y) == color:
                        break
                    else:
                        p = board[y][x].upper()
                        if p == 'K' and steps == 1:
                            return True
                        elif p == 'Q':
                            return True
                        elif p == 'R' and abs(dx) != abs(dy):
                            return True
                        elif p == 'B' and abs(dx) == abs(dy):
                            return True
                        break
            return False
        def getKingLocation(board, color):
            for y in range(0,8):
                for x in range(0,8):
                    if board[y][x] == "K" and color == 'w':
                        return (x,y)
                    if board[y][x] == "k" and color == 'b':
                        return (x,y)

        kx, ky = getKingLocation(board, color)
        return isThreatened(board, color, kx, ky)

    def pawnStructure(board, color):
        my_pos = ()
        was_enemy = False

        def get_my_pos():
            return my_pos

        def get_color():
            return color

        def make_move(board, move):
            if board[move[0]][move[1]] != None:
                was_enemy = False
            board[my_pos[0]][my_pos[1]] = None

        def in_bounds(self, board, new_pos):

            if was_enemy:
                self.was_enemy = False
                return False

            # make sure 'new_pos' in inside the board
            if new_pos[0] < 0 or new_pos[1] < 0:
                return False
            try:
                item = board[new_pos[0]][new_pos[1]]
                # item can only be an enemy
                if item == None:
                    return True
                elif item.get_color() == self.get_color():
                    return False
                elif item.get_color() != self.get_color:
                    self.was_enemy = True
                    return True
                else:
                    return True
            except:
                return False
        is_first_move = True
        moves = []
        my_pos = super(pawnStructure).get_my_pos()
        if color == 'White':
            if is_first_move:
                is_first_move = False
                new_pos = (my_pos[0] - 2, my_pos[1])
                if super(pawnStructure).in_bounds(board, new_pos):
                    moves.append(new_pos)
            new_pos = (my_pos[0] - 1, my_pos[1])
            if super(pawnStructure).in_bounds(board, new_pos):
                moves.append(new_pos)

        else:
            if is_first_move:
                is_first_move = False
                new_pos = (my_pos[0] + 2, my_pos[1])
                if super(pawnStructure).in_bounds(board, new_pos):
                    moves.append(new_pos)
            new_pos = (my_pos[0] + 1, my_pos[1])
            if super(pawnStructure).in_bounds(board, new_pos):
                moves.append(new_pos)

        return moves


    def pieceDevelopment(self, board, color):
        king_developmentTable = [[-0.03, -0.04, -0.04, -0.05, -0.05, -0.04, -0.04, -0.03], 
                                 [-0.03, -0.04, -0.04, -0.05, -0.05, -0.04, -0.04, -0.03], 
                                 [-0.03, -0.04, -0.04, -0.05, -0.05, -0.04, -0.04, -0.03], 
                                 [-0.03, -0.04, -0.04, -0.05, -0.05, -0.04, -0.04, -0.03], 
                                 [-0.02, -0.03, -0.03, -0.04, -0.04, -0.03, -0.03, -0.02], 
                                 [-0.01, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.01], 
                                 [0.02, 0.02, 0.00, 0.00, 0.00, 0.00, 0.02, 0.02], 
                                 [0.02, 0.03, 0.01, 0.00, 0.00, 0.01, 0.03, 0.02]]

        queen_developmentTable = [[-0.02, -0.01, -0.01, -0.005, -0.005, -0.01, -0.01, -0.02], 
                                 [-0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.01], 
                                 [-0.01, 0.00, 0.005, 0.01, 0.01, 0.005, 0.00, -0.01], 
                                 [-0.005, 0.00, 0.01, 0.015, 0.015, 0.01, 0.00, -0.005], 
                                 [-0.005, 0.00, 0.01, 0.015, 0.015, 0.01, 0.00, -0.005], 
                                 [-0.01, 0.00, 0.005, 0.01, 0.01, 0.005, 0.00, -0.01], 
                                 [-0.01, 0.00, 0.000, 0.00, 0.00, 0.00, 0.00, -0.01], 
                                 [-0.02, -0.01, -0.01, -0.005, -0.005, -0.01, -0.01, -0.02]]

        rook_developmentTable = [[-0.02, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.02], 
                                 [-0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.01], 
                                 [-0.01, 0.005, 0.01, 0.01, 0.01, 0.01, 0.005, -0.01], 
                                 [-0.01, 0.01, 0.01, 0.015, 0.015, 0.01, 0.01, -0.01], 
                                 [-0.01, 0.01, 0.01, 0.015, 0.015, 0.01, 0.01, -0.01], 
                                 [-0.01, 0.005, 0.01, 0.01, 0.01, 0.01, 0.005, -0.01], 
                                 [-0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.01], 
                                 [-0.02, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.02]]

        bishop_developmentTable = [[-0.02, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.02], 
                                   [-0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.01], 
                                   [-0.01, 0.00, 0.005, 0.01, 0.01, 0.005, 0.00, -0.01], 
                                   [-0.01, 0.005, 0.005, 0.015, 0.015, 0.005, 0.005, -0.01], 
                                   [-0.01, 0.00, 0.01, 0.015, 0.015, 0.01, 0.00, -0.01], 
                                   [-0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, -0.01], 
                                   [-0.01, 0.005, 0.00, 0.00, 0.00, 0.00, 0.005, -0.01], 
                                   [-0.02, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.02]]

        knight_developmentTable = [[-0.05, -0.04, -0.03, -0.03, -0.03, -0.03, -0.04, -0.05], 
                                   [-0.04, -0.02, 0.00, 0.00, 0.00, 0.00, -0.02, -0.04], 
                                   [-0.03, 0.00, 0.01, 0.015, 0.015, 0.01, 0.00, -0.03], 
                                   [-0.03, 0.005, 0.015, 0.02, 0.02, 0.015, 0.005, -0.03], 
                                   [-0.03, 0.00, 0.015, 0.02, 0.02, 0.015, 0.00, -0.03], 
                                   [-0.03, 0.005, -0.01, 0.015, 0.015, -0.01, 0.005, -0.03], 
                                   [-0.04, -0.02, 0.00, 0.005, 0.005, 0.00, -0.02, -0.04], 
                                   [-0.05, -0.04, -0.03, -0.03, -0.03, -0.03, -0.04, -0.05]]

        pawn_developmentTable =  [[0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
                                  [0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015], 
                                  [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01], 
                                  [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01], 
                                  [0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005], 
                                  [0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005], 
                                  [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
                                  [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]]

        developmentTables = [king_developmentTable, queen_developmentTable, rook_developmentTable, \
                             bishop_developmentTable, knight_developmentTable, pawn_developmentTable]
        ourDevelopment = 0
        enemyDevelopment = 0
        for square in range(64):
            if board.color_at(square) == color:
                ourDevelopment += developmentTables[6 - board.piece_type_at(square)][7 - int((square - square % 8)/8)][square % 8]
            elif board.color_at(square) and board.color_at(square) != color:
                enemyDevelopment += developmentTables[6 - board.piece_type_at(square)][int((square - square % 8)/8)][square % 8]
        return ourDevelopment - enemyDevelopment

    def centerControl(self, board, color):
        oppositeControl = 0
        ownControl = 0
        center = [(chess.D5, chess.BB_D5), (chess.E5, chess.BB_E5), (chess.D4, chess.BB_D4), (chess.E4, chess.BB_E4)]
        for num, square in center:
            ownControl += len(list(board.attackers(color, num)))
            oppositeControl += len(list(board.attackers(not color, num)))
        return ownControl - oppositeControl