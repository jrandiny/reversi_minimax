# Tugas Besar Intelegensi Buatan #1
# Tanggal   : Kamis, 12 Sept 2019
# Deskripsi : back engine reversi
# Support   : Python reversi engine module, command base
# Interface : gtk

import random
from constant import *
from utils import *
import time
import sys
import argparse
from bot.random_bot import RandomBot
from bot.human_player import HumanPlayer
from bot.ai_bot import AIBot
from bot.bot2 import Bot2
from ui.console.console import ConsoleUI
from ui.gui.main import QTUI
from ui_base import UICommandType


def game(players, board):
    turn = BLACK
    # hint = False
    play = True

    # players = {}
    # players[WHITE] = RandomBot()
    # players[WHITE] = AIBot()
    # players[WHITE] = Bot2()
    # # players[WHITE] = HumanPlayer()
    # # players[BLACK] = HumanPlayer()
    # players[BLACK] = RandomBot()
    # players[BLACK] = AIBot()
    # players[BLACK] = Bot2()
    # ui = QTUI()
    ui = ConsoleUI()

    while play:
        # print()
        # ui.giveNewBoard(board)
        # time.sleep(1)
        command = ui.getUICommand()

        if (command["type"] == UICommandType.QUIT):
            play = False
        elif (command["type"] == UICommandType.MOVE):
            print(command["data"])
        else:
            # ui.giveNewTurn(turn)
            # score = countScore(board)
            # ui.giveNewScore(score)

            # Cek apakah bisa jalan
            if (len(getAvailableMove(board, turn)) == 0):
                turn = nextTurn(turn)
                # ui.giveForfeitTurn()
            else:
                inputValid = False

                while not inputValid:
                    masukan = players[turn].doMove(board, turn)

                    if makeMove(board, turn, masukan["x"], masukan["y"]):
                        inputValid = True
                        turn = nextTurn(turn)

            play = not isFinish(board, turn)

    # print("\nPermainan berkahir")
    # score = countScore(board)
    # ui.giveNewBoard(board)
    # ui.giveNewScore(score)
    # ui.forceQuitUI()
    # pemenang = getWinner(score[BLACK], score[WHITE])
    # if pemenang == "draw":
    #     print("Hasilnya draw")
    # else:
    #     print("Pemenangnya adalah " + pemenang)
    # print("Terimakasih telah bermain")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reversi game")
    parser.add_argument("--benchmark",
                        dest="loopCount",
                        type=int,
                        nargs="?",
                        metavar="N",
                        const=50,
                        default=1,
                        help="Run in benchmark mode N times (default: 50)")

    args = parser.parse_args()

    players = {}

    players[WHITE] = Bot2()
    players[BLACK] = AIBot()

    blackWin = 0
    whiteWin = 0

    startTime = time.time()

    benchmarkMode = args.loopCount > 1

    for x in range(args.loopCount):
        if (benchmarkMode):
            print("Game {}/{}".format(x + 1, args.loopCount))

        board = newBoard(DIM)
        resetBoard(board)
        game(players, board)

        score = countScore(board)
        winner = getWinner(score[BLACK], score[WHITE])
        if winner == BLACK:
            blackWin += 1
        elif winner == WHITE:
            whiteWin += 1
        else:
            blackWin += 1
            whiteWin += 1

    if (not benchmarkMode):
        print("Permainan selesai")
    else:
        print("")
        print("Mode benchmark selesai")
        print("----------------------")
        print("Waktu : {:.2f} detik".format(time.time() - startTime))
        print("")
        print("Hitam ({}) : {}".format(players[BLACK].getName(), blackWin))
        print("Putih ({}) : {}".format(players[WHITE].getName(), whiteWin))