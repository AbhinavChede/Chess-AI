import chess
import random

def pieceDifference(board, color):
    score = 0
    for (piece, value) in [(chess.PAWN, 0.004448), (chess.BISHOP, 0.01468), (chess.KING, 0.88968),\
                           (chess.QUEEN, 0.040036), (chess.KNIGHT, 0.14235), (chess.ROOK, 0.022242)]:
        score += (len(board.pieces(piece, color)) - len(board.pieces(piece, not color))) * value
    return score

def kingProtection(board, color):
    pass

def pawnStructure(board, color):
    pass

def pieceDevelopment(board, color):
    pass

def centerControl(board, color):
    pass

def pieceAttacking(board, color):
    pass