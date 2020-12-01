import random
import chess
import chess.syzygy
from multiprocessing import Process, current_process, Pool
import time
from evaluation import Evaluation

class Player:
    def __init__(self, board, color, time):
        self.color = color
        pass
        
    def move(self, board, time): 
<<<<<<< HEAD
        return self.minimax(board, 6, -1 * float('inf'), float('inf'), self.color)[0]
=======
        return self.minimax(board, 2, -1 * float('inf'), float('inf'), self.color)[0]
>>>>>>> 08b55fbf51465aca023168c65c70fc91a47fa473

    # Searches through the game tree to find an optimal move
    def minimax(self, board, depth, alpha, beta, maximizing_player):
        eval = Evaluation()
        legalMoves = list(board.legal_moves)
        best_move = None
        if len(legalMoves) > 0:
            best_move = random.choice(legalMoves)
        if maximizing_player and len(legalMoves) > 0 and depth > 0:
            max_eval = -1 * float('inf')
            for legalMove in legalMoves:
                board.push(legalMove)
                # current_eval = self.minimax(board, depth - 1, alpha, beta, not self.color)[1]
                current_eval = self.quiescence(board, self.color, alpha, beta)
                board.pop()
                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move = legalMove
                alpha = max(alpha, current_eval)
                if beta <= alpha:
                    break
            return best_move, max_eval
        elif not maximizing_player and len(legalMoves) > 0 and depth > 0:
            min_eval = float('inf')
            for legalMove in legalMoves:
                board.push(legalMove)
                # current_eval = self.minimax(board, depth - 1, alpha, beta, self.color)[1]
                current_eval = self.quiescence(board, not self.color, alpha, beta)
                board.pop()
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move = legalMove
                beta = min(beta, current_eval)
                if beta <= alpha:
                    break
            return best_move, min_eval
        if depth == 0 or len(legalMoves) == 0:
            return None, eval.finalEvaluation(board, self.color)

    def quiescence(self, board, color, alpha, beta):
        eval = Evaluation()
        e = eval.finalEvaluation(board, color)
        if e > beta:
            return beta
        if alpha < e:
            alpha = e
        legalMoves = board.legal_moves
        score = 0
        for legalMove in legalMoves:
            numPieces = eval.pieceDifference(board, color)
            board.push(legalMove)
            newNumPieces = eval.pieceDifference(board, color)
            if numPieces > newNumPieces + 0.01 or numPieces < newNumPieces - 0.01:
                score = -1 * self.quiescence(board, color, alpha, beta)
            board.pop()
            if score >= beta:
                return beta
            if score >= alpha:
                alpha = score
        return alpha
            


                    
