from bot_base import BotBase
from utils import *
import random

LEVEL_DEPTH = [5, 3, 2]


class AIBot(BotBase):
    def getName(self):
        return "Minimax bot"

    def doMove(self, board, turn):
        # Prosedur untuk melakukan gerakan random pada giliran "giliran"
        # I.S. papan dan giliran terdefinisi
        # F.S. dilakukan gerakan random pada papan
        availableMove = getAvailableMove(board, turn)
        if len(availableMove) == 1:
            move = availableMove[0]
        else:
            move = self.minimax(board, LEVEL_DEPTH[self.config["level"] - 1],
                                -9999, 9999, turn)[1]
        x = move[0]
        y = move[1]
        return {"x": x, "y": y}

    def evaluateState(self, board):
        skor = countScore(board)
        posValue = self.hitungPositionValue(board)
        value = (skor[WHITE] - skor[BLACK]) * SKOR_FACTOR
        value += (posValue[WHITE] - posValue[BLACK])
        return value

    def hitungPositionValue(self, board):
        valuePutih = 0
        valueHitam = 0

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == WHITE:
                    valuePutih += TABLE_VALUE[row][col]
                else:
                    valueHitam += TABLE_VALUE[row][col]
        return {WHITE: valuePutih, BLACK: valueHitam}

    def minimax(self, board, depth, alpha, beta, turn):
        availableMove = getAvailableMove(board, turn)

        if depth == 0 or len(availableMove) == 0:
            return [self.evaluateState(board), INVALID_MOVE]
        elif turn == WHITE:
            maxEval = -9999
            for move in availableMove:
                copy = copyBoard(board)
                makeMove(copy, turn, move[0], move[1])

                value = self.minimax(copy, depth - 1, alpha, beta,
                                     nextTurn(turn))[0]
                if value > maxEval:
                    maxEval = value
                    gerakan = move
                elif value == maxEval:
                    if (random.randint(1, 10) % 2 == 0):
                        gerakan = move

                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return [maxEval, gerakan]
        else:
            minEval = 9999

            for move in availableMove:
                copy = copyBoard(board)
                makeMove(copy, turn, move[0], move[1])

                value = self.minimax(board, depth - 1, alpha, beta,
                                     nextTurn(turn))[0]
                if value < minEval:
                    minEval = value
                    gerakan = move
                elif value == minEval:
                    if (random.randint(1, 10) % 2 == 0):
                        gerakan = move

                beta = min(beta, value)
                if beta <= alpha:
                    break
            return [minEval, gerakan]
