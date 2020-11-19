import random
import chess
import chess.syzygy
from multiprocessing import Process, current_process, Pool
import time

class Player:
    def __init__(self, board, color, time):
        self.monteCarloSum = 0
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
        if not self.endGame:
            x = self.minimax(board, 1, -1 * float('inf'), float('inf'), self.color)[0]
            print(x)
            return x
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

    def runSimulation(self, board):
        new_board = board.copy()
        children = list(new_board.legal_moves)
        while len(children) > 0:
            new_board.push(random.choice(list(new_board.legal_moves)))
            children = list(new_board.legal_moves)
        return self.evalFunction(new_board)

    def runSimulationsWithMultiThreading(self, board, n):
        simulationSum = 0
        board_list = []
        # results = []
        for num in range(n):
            board_list.append(board)
        p = Pool()
        results = p.map(self.runSimulation, board_list)
        p.close()
        p.join()
        # for result in results:
        #     simulationSum += result
        # return simulationSum/n
        print(results)

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        # print(maximizing_player)
        # print(board.is_game_over)
        # print(self.runSimulation(board))
        children = list(board.legal_moves)
        best_move = None
        if len(children) > 0:
            best_move = random.choice(children)
        # print("Hola")
        if maximizing_player and len(children) > 0 and depth > 0:
            # print("hello1")
            max_eval = -1 * float('inf')
            for child in children:
                # print(child)
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
        elif not maximizing_player and len(children) > 0 and depth > 0:
            # print("Hello2")
            min_eval = float('inf')
            for child in children:
                # print(child)
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
        if len(children) == 0:
            # print("gameOver")
            return None, self.evalFunction(board)
        if depth == 0:
            # print("depth")
            new_board = board.copy()
            return None, self.runSimulation(new_board)
    
