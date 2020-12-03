import chess
import random

class Evaluation:
    """
        This class calculates useful information to use in th evaluation function.
    """
        
    # Calculates the piece difference of both sides with weights that calculated, assigned, and adjusted to fit in a 0 to 1 scale.
    def pieceDifference(self, board, color):
        self.poseval = {"P":[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5, 0.5, -0.5, 1.0, 0.0, 0.0, -1.0, -0.5, 0.5, 0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5, 1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
            "N":[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0, -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0, -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0, -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0, -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0, -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0, -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0, -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0], 
            "B":[-2, -1, -1, -1, -1, -1, -1, -2, -1, 0.5, 0, 0, 0, 0, 0.5, -1,  -1, 1, 1, 1, 1, 1, 1, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1, -1, 0, 0.5, 1, 1, 0.5, 0, -1, -1, 0, 0, 0, 0, 0, 0, -1, -2, -1, -1, -1, -1, -1, -1, -2],
            "R":[0, 0, 0, 0.5, 0.5, 0, 0, 0, -.5, 0, 0, 0, 0, 0, 0, -.5,-.5, 0, 0, 0, 0, 0, 0, -.5,-.5, 0, 0, 0, 0, 0, 0, -.5,-.5, 0, 0, 0, 0, 0, 0, -.5,-.5, 0, 0, 0, 0, 0, 0, -.5, .5, 1, 1, 1, 1, 1, 1, .5, 0, 0, 0, 0, 0, 0, 0, 0 ],
            "Q":[-2, -1, -1, -.5, -.5, -1, -1, -2, -1, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1, -1, .5, .5, .5, .5, .5, 0.0, -1, 0, 0, 0.5, .5, .5, .5, 0.0, -.5, -.5, 0, .5, .5, .5, .5, 0, -.5, -1, 0, .5, .5, .5, .5, 0, -1, -1, 0, 0, 0, 0, 0, 0, -1, -2, -1, -1, -.5, -.5, -1, -1, -2],
            "K":[2, 3, 1, 0, 0, 1, 3, 2, 2, 2, 0, 0, 0, 0, 2, 2, -1, -2, -2, -2, -2, -2, -2, -1,-2, -3, -3, -4, -4, -3, -3, -2, -3, -4, -4, -5, -5, -4, -4, -3,-3, -4, -4, -5, -5, -4, -4, -3,-3, -4, -4, -5, -5, -4, -4, -3,-3, -4, -4, -5, -5, -4, -4, -3]}
        score = 0
        for (piece, value) in [(chess.PAWN, 0.004448), (chess.BISHOP, 0.01468), (chess.KING, 0.88968),\
                            (chess.QUEEN, 0.040036), (chess.KNIGHT, 0.014235), (chess.ROOK, 0.022242)]:
            score += (len(board.pieces(piece, color)) - len(board.pieces(piece, not color))) * value
        return score

    # Calculates the difference in pawn islands of both sides to figure out who has better pawn structure
    def pawnStructure(self, board, color):
        ourPawns = list(board.pieces(chess.PAWN, color))
        enemyPawns = list(board.pieces(chess.PAWN, not color))
        ourPawnIslands = 1
        enemyPawnIslands = 1
        if len(ourPawns) > 0:
            firstSquare = ourPawns[0]
            for square in ourPawns:
                if chess.square_distance(firstSquare, square) > 1:
                    ourPawnIslands += 1
                firstSquare = square
        if len(enemyPawns) > 0:
            firstSquare = enemyPawns[0]
            for square in enemyPawns:
                if chess.square_distance(firstSquare, square) > 1:
                    enemyPawnIslands += 1
                firstSquare = square
        return enemyPawnIslands - ourPawnIslands
        
    # Calculates the difference between piece development of each piece at its respective square of both sides with weights that calculated, assigned, and adjusted to fit in a 0 to 1 scale.
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
            if board.color_at(square) == color and color:
                ourDevelopment += developmentTables[6 - board.piece_type_at(square)][7 - int((square - square % 8)/8)][square % 8]
            elif board.color_at(square) and board.color_at(square) != color and not color:
                enemyDevelopment += developmentTables[6 - board.piece_type_at(square)][int((square - square % 8)/8)][square % 8]
        return ourDevelopment - enemyDevelopment

    # Calculates a integer of the difference of center control of both sides
    def centerControl(self, board, color):
        oppositeControl = 0
        ownControl = 0
        center = [(chess.D5, chess.BB_D5), (chess.E5, chess.BB_E5), (chess.D4, chess.BB_D4), (chess.E4, chess.BB_E4)]
        for num, square in center:
            ownControl += len(list(board.attackers(color, num)))
            oppositeControl += len(list(board.attackers(not color, num)))
        return ownControl - oppositeControl

    def incrEval(self, oldBoard, newBoard, move, prevEval, color):
        incr = 0
        mateval = [0,10,30,30,50,90,900]
        if (newBoard.is_game_over()):
            if (newBoard.is_variant_draw()):
                return 0
            if (newBoard.turn == color):
                return -float("inf")
            else:
                return float("inf")
        fromPiece = oldBoard.piece_at(move.from_square)
        toPiece = oldBoard.piece_at(move.to_square)
        if fromPiece.color == color:
            if toPiece: #enemy piece was taken, add mateval
                incr += mateval[toPiece.piece_type]
            #subtract previous piece poseval and add new poseval
            incr -= self.poseval[fromPiece.symbol().upper()][move.from_square]
            incr += self.poseval[fromPiece.symbol().upper()][move.to_square]
            if move.promotion: # a friendly promotion happened
                incr += mateval[move.promotion]
        else:
            if toPiece: #friendly piece taken, subtract mateval and poseval
                incr -= mateval[toPiece.piece_type]
                incr -= self.poseval[toPiece.symbol().upper()][move.to_square]            
            if move.promotion: # an enemy promotion happened
                incr -= mateval[move.promotion]
        return prevEval+incr        

    # Adds up all features to calculate a final evaluation
    def finalEvaluation(self, board, color): # oldBoard, newBoard, prevEval, move):
        weights = [1.00, 1.00, 0.05, 0.05]
        result = weights[0] * self.pieceDifference(board, color) + weights[1] * self.pieceDevelopment(board, color) + \
                 weights[2] * self.centerControl(board, color) + weights[3] * self.pawnStructure(board, color)
        return result # + self.incrEval(oldBoard, newBoard, move, prevEval, color)

