# Tugas Besar Intelegensi Buatan #1
# Tanggal   : Kamis, 12 Sept 2019
# Deskripsi : back engine reversi
# Support   : Python reversi engine module, command base
# Interface : gtk

import random
from constant import *
from utils import *
import time
from player.random_bot import RandomBot
from player.human_player import HumanPlayer
from player.ai_bot import AIBot
from player.bot2 import Bot2
from ui.console.console import ConsoleUI
from ui.gui.main import QTUI
from ui_base import UICommandType

# def game(players, board):
if __name__ == "__main__":
    board = newBoard(DIM)
    resetBoard(board)
    turn = BLACK
    hint = False
    play = True

    players = {}
    players[WHITE] = RandomBot()
    # players[WHITE] = AIBot()
    # players[WHITE] = Bot2()
    # # players[WHITE] = HumanPlayer()
    # # players[BLACK] = HumanPlayer()
    players[BLACK] = RandomBot()
    # # players[BLACK] = RandomBot()
    # players[BLACK] = Bot2()
    ui = ConsoleUI()
    # ui = ConsoleUI()

    while play:
        print()
        ui.giveNewBoard(board)
        time.sleep(1)
        command = ui.getUICommand()

        if (command["type"] == UICommandType.QUIT):
            play = False
        elif (command["type"] == UICommandType.MOVE):
            print(command["data"])
        else:
            ui.giveNewTurn(turn)
            score = countScore(board)
            ui.giveNewScore(score)

            # Cek apakah bisa jalan
            if (len(getAvailableMove(board, turn)) == 0):
                turn = nextTurn(turn)
                ui.giveForfeitTurn()
            else:
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

# if __name__ == "__main__":
#     # main program

#     for x in range(10):
#         players = {}
#         players[WHITE] = RandomBot()
#         # players[WHITE] = AIBot()
#         # players[WHITE] = HumanPlayer()
#         # players[BLACK] = HumanPlayer()
#         players[BLACK] = AIBot()
#         # players[BLACK] = RandomBot()
#         board = newBoard(DIM)
#         resetBoard(board)
#         game(players, board)
#         import time
#         # time.sleep(1)
#         score = countScore(board)
#         pemenang = getWinner(score[BLACK], score[WHITE])
#         if pemenang == BLACK:
#             for x, y in players[BLACK].moveList:
#                 TABLE_VALUE[y][x] += 1
#         else:
#             for x, y in players[BLACK].moveList:
#                 TABLE_VALUE[y][x] -= 1
#     print(TABLE_VALUE)