import threading
from abc import ABC, abstractmethod
from bot_base import BotBase
from enum import Enum
from queue import Queue


class UIMessageType(Enum):
    QUIT = 0
    BOARD = 1
    TURN = 2
    SCORE = 3
    FORFEIT = 4
    DOTURN = 5


class UICommandType(Enum):
    NOOP = -1
    QUIT = 0
    MOVE = 1


class UIPlayer(BotBase):
    def __init__(self, moveQueue, askForMove):
        self.askForMove = askForMove
        self.moveQueue: Queue = moveQueue

    def getName(self, moveQueue):
        return "Player"

    def doMove(self, board, turn):
        self.askForMove()
        move = self.moveQueue.get(block=True)
        return move


class UIBase(ABC):
    def __init__(self):
        self.inputQueue = Queue()
        self.outputQueue = Queue()
        self.moveQueue = Queue()
        self.uiThread = threading.Thread(target=self.threadWorker)
        self.uiThread.start()

    def giveNewBoard(self, board):
        self.inputQueue.put({"type": UIMessageType.BOARD, "data": board})
        self.inputQueue.join()

    def giveNewTurn(self, turn):
        self.inputQueue.put({"type": UIMessageType.TURN, "data": turn})
        self.inputQueue.join()

    def giveNewScore(self, score):
        self.inputQueue.put({"type": UIMessageType.SCORE, "data": score})
        self.inputQueue.join()

    def giveForfeitTurn(self):
        self.inputQueue.put({"type": UIMessageType.FORFEIT})

    def giveTurnSignal(self):
        self.inputQueue.put({"type": UIMessageType.DOTURN})

    def forceQuitUI(self):
        self.inputQueue.put({"type": UIMessageType.QUIT})
        self.uiThread.join()

    def getUICommand(self):
        if (not self.outputQueue.empty()):
            command = self.outputQueue.get()
            self.outputQueue.task_done()
            return command
        else:
            return {"type": UICommandType.NOOP}

    def getPlayer(self):
        return UIPlayer(self.moveQueue, self.giveTurnSignal)

    @abstractmethod
    def threadWorker(self):
        pass
