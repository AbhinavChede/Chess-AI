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
        return self.minimax(board, 1, -1 * float('inf'), float('inf'), self.color)[0]

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
                current_eval = self.minimax(board, depth - 1, alpha, beta, not self.color)[1]
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
                current_eval = self.minimax(board, depth - 1, alpha, beta, self.color)[1]
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

                    
