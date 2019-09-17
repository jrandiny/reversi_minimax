from abc import ABC, abstractmethod


class BotBase(ABC):

    # init
    def init(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    # Player do some move
    # Return tuple of (x,y)
    @abstractmethod
    def doMove(self, board, turn):
        pass
