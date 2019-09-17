from player_base import PlayerBase
from utils import *


class HumanPlayer(PlayerBase):
    def doMove(self, board, turn):
        # Prosedur yang mengatur input pada saat giliran "giliran"
        # I.S. papan dan giliran terdefinisi
        # F.S. mengembalikan input hint/ quit/
        #       titik disk yang diterima yang valid untuk gerakan dan titik seberangnya
        valid = False
        while not valid:
            masukan = input("masukan: ").lower()
            titik = masukan.split()
            if len(titik) == 2:
                if titik[0].isdigit() and titik[1].isdigit():
                    # kedua input adalah integer
                    x = int(titik[0]) - 1
                    y = int(titik[1]) - 1
                    lokasi = cekGerakanValid(board, turn, x, y)
                    if lokasi != False:
                        # titik yang valid
                        valid = True
                    else:
                        print("titik tidak valid")
                else:
                    print("masukan koordinat angka")
            else:
                print("input tidak valid")
        return {"x": x, "y": y, "lokasi": lokasi}
