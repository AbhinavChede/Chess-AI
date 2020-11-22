import chess
import random

class Evaluation:
    def pieceDifference(self, board, color):
        score = 0
        for (piece, value) in [(chess.PAWN, 0.004448), (chess.BISHOP, 0.01468), (chess.KING, 0.88968),\
                            (chess.QUEEN, 0.040036), (chess.KNIGHT, 0.014235), (chess.ROOK, 0.022242)]:
            score += (len(board.pieces(piece, color)) - len(board.pieces(piece, not color))) * value
        return score

    def kingProtection(self, board, color):
        ourKing = board.king(color)
        enemyKing = board.king(not color)
        pass

    def pawnStructure(self, board, color):
        pass

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