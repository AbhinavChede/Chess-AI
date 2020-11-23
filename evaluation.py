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
        danger = False
        for y in range(0,8):
            for x in range(0,8):
                king_state = board([x][y])
        def getColor([x][y]):
            return color[x][y]
        if getColor([x+1],[y]) or getColor[x-1][y] or getColor[x][y+1] or getColor[x][y-1] == self.color :
            return danger = False
        if getColor([x+1],[y]) or getColor[x-1][y] or getColor[x][y+1] or getColor[x][y-1] != self.color :
            if x < 6 :
                return danger = False
            elif x==8 or x==7
                 return danger = True
            elif x > 3
                return danger = True
        
        moves = ([x + 1, y + 2], [x + 2, y + 1], [x + 2, y - 1], [x + 1, y - 2],[x - 1, y + 2], [x - 2, y + 1], [x - 1, y - 2], [x - 2, y - 1])
        for m in moves:
            if  x >= 0 and x <= 7 
                if king_state == getColor(m)
                    return danger = True
                elif king_state !=getColor(m)
                    return danger = False
            if y >= 0 and y <= 7:
                if king_state == getColor(m)
                    return danger = True
                elif king_state !=getColor(m)
                    return danger = False


    def pawnStructure(board, color):
        danger = False
        pawn_state = baord([x,y])
        def getColor([x][y]):
            return color[x][y]
        if getColor([x+1],[y]) or getColor[x-1][y] or getColor[x][y+1] or getColor[x][y-1] != getColor([x][y]) :
            return danger = False

        moves = ([x + 1, y + 2], [x + 2, y + 1], [x + 2, y - 1], [x + 1, y - 2],[x - 1, y + 2], [x - 2, y + 1], [x - 1, y - 2], [x - 2, y - 1])
            if board[moves[0]][moves[1]] != None:
                return danger = False
            board[pawn_state[0]][pawn_state[1]] = None
                return danger = True
            if True:
                self.pawn_state = False
                    return danger = False

            if pawn_state[0] < 0 or pawn_state[1] < 0:
                return danger = False
            opponent = board([x+1],[y]) or board[x-1][y] or board[x][y+1] or board[x][y-1]
            if opponent == None:
                return danger = False
            elif opponent.getColor() == self.color:
                return danger = False
            elif opponent.getColor() != self.color:
                return danger = True
            else:
                return danger = True
        moves = []
        if self.color == 'White':
            new_pawn_state = (pawn_state[0] - 2, pawn_state[1])
            if super(pawnStructure).in_bounds(board, new_pawn_state):
                moves.append(new_pawn_state)
           

        else:
            new_pawn_state = (pawn_state[0] + 2, pawn_state[1])
            if super(pawnStructure).in_bounds(board, new_pawn_state):
                moves.append(new_pawn_state)
            new_pawn_state = (pawn_state[0] + 1, pawn_state[1])
            if super(pawnStructure).in_bounds(board, new_pawn_state):
                moves.append(new_pawn_state)

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