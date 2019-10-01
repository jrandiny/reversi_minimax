from bot_base import BotBase
from utils import *
import random


class RandomBot(BotBase):
    def getName(self):
        return "Random bot"

    def doMove(self, board, turn):
        # Prosedur untuk melakukan gerakan random pada giliran "giliran"
        # I.S. papan dan giliran terdefinisi
        # F.S. dilakukan gerakan random pada papan
        move = getAvailableMove(board, turn)
        random.shuffle(move)
        terpilih = move[0]
        x = terpilih[0]
        y = terpilih[1]
        return {"x": x, "y": y}
