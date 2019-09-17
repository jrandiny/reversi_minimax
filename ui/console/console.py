from ui_base import UIBase, UIMessageType
from math import log10
from constant import *


class ConsoleUI(UIBase):
    def printScore(self, score):
        # Prosedur untuk mencetak skor sekarang ke layar
        # I.S. skor terdefinisi
        # F.S. skor tercetak ke layar sesuai kondisi papan
        print(
            f"Skor sekarang {BLACK}: {score[BLACK]}, {WHITE}: {score[WHITE]}")

    def printBoard(self, papan):
        # Prosedur untuk menampilkan kondisi papan ke layar
        # I.S. papan terdefinisi sebagai matriks persegi
        # F.S. papan tercetak di layar

        dim = len(papan)
        ORD = int(log10(dim)) + 1  # ordo dari dimensi papan
        SPACE = " " * ORD  # jumlah spasi
        GARISH = " " + SPACE + (("+--" + "-" * ORD) *
                                (dim)) + "+"  # garis horizontal
        GARISV = " " + SPACE + (("|  " + " " * ORD) *
                                (dim)) + "|"  # garis vertikal
        offset = int(1 + (ORD / 2))  # offset karakter dari border
        tail = (2 + ORD) - (offset + 1)  # jumlah spasi di belakang karakter

        # cetak koordinat X
        print("   ", end=SPACE)
        for i in range(dim):
            ordoI = int(log10(i + 1))
            print(f"{i+1}  " + " " * (ORD - ordoI), end="")

        # cetak Isi
        print("\n" + GARISH)
        for y in range(dim):
            print(GARISV)
            ordoY = int(log10(y + 1))
            # cetak koordinat Y
            print(y + 1, end=" " * (ORD - ordoY))
            # cetak isi papan
            for x in papan[y]:
                print("|" + " " * offset + x, end=" " * tail)
            print("|")
            print(GARISV)
            print(GARISH)

    def threadWorker(self):
        while True:
            io = self.inputQueue.get()

            if (io["type"] == UIMessageType.BOARD):
                self.printBoard(io["data"])
            elif (io["type"] == UIMessageType.SCORE):
                self.printScore(io["data"])
            elif (io["type"] == UIMessageType.TURN):
                turn = io["data"]
                print(f"Sekarang giliran {turn}")
            elif (io["type"] == UIMessageType.FORFEIT):
                print("Tidak ada langkah mungkin, skip")
            elif (io["type"] == UIMessageType.QUIT):
                break

            self.inputQueue.task_done()
