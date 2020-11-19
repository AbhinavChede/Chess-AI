import random
import chess
import chess.syzygy

class Player:
    def __init__(self, board, color, time):
        self.color = color
        self.time = time
        self.king_pieceSquare = [[-0.03, -0.04, -0.04, -0.05, -0.05, -0.04, -0.04, -0.03], 
                                 [-0.03, -0.04, -0.04, -0.05, -0.05, -0.04, -0.04, -0.03], 
                                 [-0.03, -0.04, -0.04, -0.05, -0.05, -0.04, -0.04, -0.03], 
                                 [-0.03, -0.04, -0.04, -0.05, -0.05, -0.04, -0.04, -0.03], 
                                 [-0.02, -0.03, -0.03, -0.04, -0.04, -0.03, -0.03, -0.02], 
                                 [-0.01, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.01], 
                                 [0.02, 0.02, 0.00, 0.00, 0.00, 0.00, 0.02, 0.02], 
                                 [0.02, 0.03, 0.01, 0.00, 0.00, 0.01, 0.03, 0.02]]

        self.queen_piceSquare = [[-0.02, -0.01, -0.01, -0.005, -0.005, -0.01, -0.01, -0.02], 
                                 [-0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.01], 
                                 [-0.01, 0.00, 0.005, 0.005, 0.005, 0.005, 0.00, -0.01], 
                                 [-0.005, 0.00, 0.005, 0.005, 0.005, 0.005, 0.00, -0.005], 
                                 [0.00, 0.00, 0.005, 0.005, 0.005, 0.005, 0.00, -0.005], 
                                 [-0.01, 0.005, 0.005, 0.005, 0.005, 0.005, 0.00, -0.01], 
                                 [-0.01, 0.00, 0.005, 0.00, 0.00, 0.00, 0.00, -0.01], 
                                 [-0.02, -0.01, -0.01, -0.005, -0.005, -0.01, -0.01, -0.02]]

        self.rook_pieceSqaure = [[-0.02, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.02], 
                                 [-0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.01], 
                                 [-0.01, 0.00, 0.005, 0.01, 0.01, 0.005, 0.00, -0.01], 
                                 [-0.01, 0.005, 0.005, 0.01, 0.01, 0.005, 0.005, -0.01], 
                                 [-0.01, 0.00, 0.01, 0.01, 0.01, 0.01, 0.00, -0.01], 
                                 [-0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, -0.01], 
                                 [-0.01, 0.005, 0.00, 0.00, 0.00, 0.00, 0.005, -0.01], 
                                 [-0.02, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.02]]

        self.bishop_pieceSquare = [[-0.02, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.02], 
                                   [-0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -0.01], 
                                   [-0.01, 0.00, 0.005, 0.01, 0.01, 0.005, 0.00, -0.01], 
                                   [-0.01, 0.005, 0.005, 0.01, 0.01, 0.005, 0.005, -0.01], 
                                   [-0.01, 0.00, 0.01, 0.01, 0.01, 0.01, 0.00, -0.01], 
                                   [-0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, -0.01], 
                                   [-0.01, 0.005, 0.00, 0.00, 0.00, 0.00, 0.005, -0.01], 
                                   [-0.02, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.02]]

        self.knight_pieceSquare = [[-0.05, -0.04, -0.03, -0.03, -0.03, -0.03, -0.04, -0.05], 
                                   [-0.04, -0.02, 0.00, 0.00, 0.00, 0.00, -0.02, -0.04], 
                                   [-0.03, 0.00, 0.01, 0.015, 0.015, 0.01, 0.00, -0.03], 
                                   [-0.03, 0.005, 0.015, 0.02, 0.02, 0.015, 0.005, -0.03], 
                                   [-0.03, 0.00, 0.015, 0.02, 0.02, 0.015, 0.00, -0.03], 
                                   [-0.03, 0.005, -0.01, 0.015, 0.015, -0.01, 0.005, -0.03], 
                                   [-0.04, -0.02, 0.00, 0.005, 0.005, 0.00, -0.02, -0.04], 
                                   [-0.05, -0.04, -0.03, -0.03, -0.03, -0.03, -0.04, -0.05]]

        self.pawn_pieceSquare =  [[0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], 
                                  [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05], 
                                  [0.01, 0.01, 0.02, 0.03, 0.03, 0.02, 0.01, 0.01], 
                                  [0.005, 0.005, 0.01, 0.025, 0.025, 0.01, 0.005, 0.005], 
                                  [0.00, -0.01, -0.02, -0.01, -0.01, -0.02, -0.01, 0.00], 
                                  [0.005, -0.005, -0.01, 0.00, 0.00, -0.01, -0.005, 0.005], 
                                  [0.005, 0.01, 0.01, -0.02, -0.02, 0.01, 0.01, 0.005], 
                                  [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]]
        self.piecetable = [self.pawn_pieceSquare, self.knight_pieceSquare, self.bishop_pieceSquare, self.rook_pieceSqaure, self.queen_piceSquare, self.king_pieceSquare]
        self.endGame = False
        pass
        
    def move(self, board, time): 
        # scores = []
        # legalMoves = list(board.legal_moves)
        # for move in legalMoves:
        #     scores.append(self.evalFunction(board,  move))
        # return legalMoves[scores.index(max(scores))]
        # print(self.minimax(board, 1, -1 * float('inf'), float('inf'), self.color)[0])
        if not self.endGame:
            print(self.minimax(board, 4, -1 * float('inf'), float('inf'), self.color)[0])
            return self.minimax(board, 4, -1 * float('inf'), float('inf'), self.color)[0]
        # else:
        #     return self.boardEndGame(board)

    def evalFunction(self, board):
        pieceCount = 0
        pieceSum = 0
        score = 0
        new_board = board.copy()
        for (piece, value) in [(chess.PAWN, 0.004448), (chess.BISHOP, 0.01468), (chess.KING, 0.88968), (chess.QUEEN, 0.040036), (chess.KNIGHT, 0.14235), (chess.ROOK, 0.022242)]:
            score += (len(new_board.pieces(piece, self.color)) - len(new_board.pieces(piece, not self.color))) * value
        for i in range(64):
            if new_board.piece_at:
                pieceCount += 1
            if new_board.piece_type_at(i):
                if new_board.color_at(i) == self.color and self.color:
                    pieceSum += self.piecetable[new_board.piece_type_at(i) - 1][7 - int((i - i%8)/8)][i % 8]
                elif new_board.color_at(i) == self.color and not self.color:
                    pieceSum -= self.piecetable[new_board.piece_type_at(i) - 1][int((i - i%8)/8)][i % 8]
        # if new_board.is_checkmate():
        #     score += 1000000
        # if pieceCount <= 7:
        #     self.endGame = True
        return score + pieceSum

    # def boardEndGame(self, board):
    #     score = -1 * float('inf')
    #     bestMove = None
    #     with chess.syzygy.open_tablebase("data/syzygy/regular") as tablebase:
    #         for move in list(board.legal_moves):
    #             board.push(move)
    #             board_score = tablebase.probe_dtz(board)
    #             if board_score > score:
    #                 score = board_score
    #                 bestMove = move
    #     return bestMove

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        children = list(board.legal_moves)
        best_move = None
        if len(children) > 0:
            best_move = random.choice(children)
        if maximizing_player and (not depth > 0 or not board.is_game_over):
            max_eval = -1 * float('inf')
            for child in children:
                board.push(child)
                current_eval = self.minimax(board, depth - 1, alpha, beta, not self.color)[1]
                board.pop()
                if current_eval >= max_eval:
                    max_eval = current_eval
                    best_move = child
                alpha = max(alpha, current_eval)
                if beta <= alpha:
                    break
            return best_move, max_eval
        elif not maximizing_player and (not depth > 0 or not board.is_game_over):
            min_eval = float('inf')
            for child in children:
                board.push(child)
                current_eval = self.minimax(board, depth - 1, alpha, beta, self.color)[1]
                board.pop()
                if current_eval <= min_eval:
                    min_eval = current_eval
                    best_move = child
                beta = min(beta, current_eval)
                if beta <= alpha:
                    break
            return best_move, min_eval
        if board.is_game_over:
            return None, self.evalFunction(board)
        if depth <= 0:
            return random.choice(children), self.evalFunction(board)
