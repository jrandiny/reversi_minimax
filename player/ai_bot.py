from player_base import PlayerBase
from utils import *


class AIBot(PlayerBase):
    def doMove(self, board, turn):
        # Prosedur untuk melakukan gerakan random pada giliran "giliran"
        # I.S. papan dan giliran terdefinisi
        # F.S. dilakukan gerakan random pada papan
        #move = getBestMove(board,turn)
        # x = move[0]
        # y = move[1]
        print(f"bot bergerak [{x+1},{y+1}]")
        return {"x": x, "y": y}

    def evaluateState(board):
        skor = countScore(board)
        posValue = hitungPositionValue(board)
        value = (skor[WHITE] - skor[BLACK]) * 100 + (posValue[WHITE] -
                                                     posValue[BLACK])
        return {value}

    def hitungPositionValue(board):
        valuePutih = 0
        valueHitam = 0

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == WHITE:
                    valuePutih += TABLE_VALUE[row][col]
                else:
                    valueHitam += TABLE_VALUE[row][col]
        return {WHITE: valuePutih, BLACK: valueHitam}

    def minimax(board, depth, alpha, beta, turn):
        if depth == 0:
            return evaluateState(board)

        availableMove = getAvailableMove(board, turn)

        if turn == WHITE:
            maxEval = -9999
            for move in availableMove:
                copy = copyBoard(board)
                makeMove(copy, turn, move['lokasi'], move['x'], move['y'])
                eval = minimax(copy, depth - 1, alpha, beta, nextTurn(turn))
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = 9999
            for move in availableMove:
                copy = copyBoard(board)
                makeMove(copy, turn, move['lokasi'], move['x'], move['y'])
                eval = minimax(board, depth - 1, alpha, beta, nextTurn(turn))
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval

    # def getBestMove(board, turn):
    #     score = minimax(board, 3, -9999, 9999, turn)

    #     return [X, Y]
