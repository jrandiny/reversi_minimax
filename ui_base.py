from abc import ABC, abstractmethod
from queue import Queue
import threading
from enum import Enum


class UIMessageType(Enum):
    QUIT = 0
    BOARD = 1
    TURN = 2
    SCORE = 3


class UICommandType(Enum):
    NOOP = -1
    QUIT = 0


class UIBase(ABC):
    def __init__(self):
        self.inputQueue = Queue()
        self.outputQueue = Queue()
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

    def forceQuitUI(self):
        self.inputQueue.put({"type": UIMessageType.QUIT})

    def getUICommand(self):
        if (not self.outputQueue.empty()):
            command = self.outputQueue.get()
            self.outputQueue.task_done()
            return command
        else:
            return {"type": UICommandType.NOOP}

    @abstractmethod
    def threadWorker(self):
        pass
