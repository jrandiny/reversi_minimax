# Tugas Besar Intelegensi Buatan #1
# Tanggal   : Kamis, 12 Sept 2019
# Deskripsi : back engine reversi
# Support   : Python reversi engine module, command base
# Interface : gtk

import random
from constant import *
from utils import *
from player.random_bot import RandomBot
from player.human_player import HumanPlayer
from ui.console.console import ConsoleUI
from ui_base import UICommandType

if __name__ == "__main__":
    # main program
    board = newBoard(DIM)
    resetBoard(board)
    turn = BLACK
    hint = False
    play = True

    players = {}
    players[WHITE] = RandomBot()
    players[BLACK] = HumanPlayer()

    ui = ConsoleUI()

    while play:
        print()

        ui.giveNewBoard(board)

        command = ui.getUICommand()

        if (command["type"] == UICommandType.QUIT):
            play = False
        else:
            ui.giveNewTurn(turn)
            score = countScore(board)
            ui.giveNewScore(score)

            inputValid = False

            while not inputValid:
                masukan = players[turn].doMove(board, turn)

                if makeMove(board, turn, masukan["x"], masukan["y"]):
                    inputValid = True
                    turn = nextTurn(turn)

            play = not isFinish(board, turn)

    print("\nPermainan berkahir")
    score = countScore(board)
    ui.giveNewBoard(board)
    ui.giveNewScore(score)
    ui.forceQuitUI()
    pemenang = getWinner(score[BLACK], score[WHITE])
    if pemenang == "draw":
        print("Hasilnya draw")
    else:
        print("Pemenangnya adalah " + pemenang)
    print("Terimakasih telah bermain")
