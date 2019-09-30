# Tugas Besar Intelegensi Buatan #1
# Tanggal   : Kamis, 12 Sept 2019
# Deskripsi : back engine reversi
# Support   : Python reversi engine module, command base
# Interface : gtk

import random
import importlib
from constant import *
from utils import *
import time
import sys
import argparse
from ui.console.console import ConsoleUI
from ui.gui.main import QTUI
from ui.dummy.dummy import DummyUI
from ui_base import UICommandType
from bot.random_bot import RandomBot


def game(players, board, ui):
    turn = BLACK
    play = True

    while play:
        ui.giveNewBoard(board)
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

    parser.add_argument("--white",
                        type=str,
                        nargs="?",
                        default="random_bot/RandomBot",
                        help="Specify White AI")

    parser.add_argument("--black",
                        type=str,
                        nargs="?",
                        default="random_bot/RandomBot",
                        help="Specify Black AI")

    parser.add_argument("--gui",
                        action='store_const',
                        const=True,
                        help="Using GUI?")

    args = parser.parse_args()

    benchmarkMode = args.loopCount > 1

    players = {}

    if (benchmarkMode):
        ui = DummyUI()
    else:
        if (args.gui):
            ui = QTUI()
        else:
            ui = ConsoleUI()

    if (benchmarkMode):
        aiWhiteName = args.white.split("/")
        aiWhiteModule = importlib.import_module("bot." + aiWhiteName[0])
        aiWhiteClass = getattr(aiWhiteModule, aiWhiteName[1])
        players[WHITE] = aiWhiteClass()

        aiBlackName = args.black.split("/")
        aiBlackModule = importlib.import_module("bot." + aiBlackName[0])
        aiBlackClass = getattr(aiBlackModule, aiBlackName[1])
        players[BLACK] = aiBlackClass()
    else:
        players[WHITE] = RandomBot()
        players[BLACK] = ui.getPlayer()

    blackWin = 0
    whiteWin = 0

    startTime = time.time()

    for x in range(args.loopCount):
        board = newBoard(DIM)
        resetBoard(board)

        if (benchmarkMode):
            print("Game {}/{}".format(x + 1, args.loopCount))

        game(players, board, ui)

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
        ui.forceQuitUI()
    else:
        ui.forceQuitUI()
        print("")
        print("Mode benchmark selesai")
        print("----------------------")
        print("Waktu : {:.2f} detik".format(time.time() - startTime))
        print("")
        print("Hitam ({}) : {}".format(players[BLACK].getName(), blackWin))
        print("Putih ({}) : {}".format(players[WHITE].getName(), whiteWin))