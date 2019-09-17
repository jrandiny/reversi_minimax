from player_base import PlayerBase
from utils import *
import random


class RandomBot(PlayerBase):
    def doMove(self, board, turn):
        # Prosedur untuk melakukan gerakan random pada giliran "giliran"
        # I.S. papan dan giliran terdefinisi
        # F.S. dilakukan gerakan random pada papan
        gerakan = gerakanTersedia(board, turn)
        random.shuffle(gerakan)
        terpilih = gerakan[0]
        x = terpilih[0]
        y = terpilih[1]
        lokasi = cekGerakanValid(board, turn, x, y)
        print(f"bot bergerak [{x+1},{y+1}]")
        return {"x": x, "y": y, "lokasi": lokasi}
