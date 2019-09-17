from bot_base import BotBase
from utils import *
import random


class Bot2(BotBase):
    def getName(self):
        return "Bot 2"

    def doMove(self, board, turn):
        # Given a board and the computer's tile, determine where to
        # move and return that move as a [x, y] list.
        possibleMoves = getAvailableMove(board, turn)

        # randomize the order of the possible moves
        random.shuffle(possibleMoves)

        # always go for a corner if available.
        # for x, y in possibleMoves:
        #     if self.isOnCorner(x, y):
        #         return {"x": x, "y": y}

        # Go through all the possible moves and remember the best scoring move
        bestScore = -1
        for x, y in possibleMoves:
            if self.isOnCorner(x, y):
                return {"x": x, "y": y}
            dupeBoard = copyBoard(board)
            makeMove(dupeBoard, turn, x, y)
            score = countScore(dupeBoard)[turn]
            if score > bestScore:
                bestMove = [x, y]
                bestScore = score
        return {"x": bestMove[0], "y": bestMove[1]}

    def isOnCorner(self, x, y):
        # Returns True if the position is in one of the four corners.
        return (x == 0 and y == 0) or (x == 7 and y == 0) or (
            x == 0 and y == 7) or (x == 7 and y == 7)
