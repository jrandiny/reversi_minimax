from abc import ABC, abstractmethod


class PlayerBase(ABC):

    # init
    def init(self):
        pass

    # Player do some move
    # Return tuple of (x,y)
    @abstractmethod
    def doMove(self, board, turn):
        pass
