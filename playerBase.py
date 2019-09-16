from abc import ABC, abstractmethod
from typing import Tuple


class playerBase(ABC):

    # init
    def init(self) -> None:
        pass

    # Player do some move
    # Return tuple of (x,y)
    @abstractmethod()
    def doMove(self) -> Tuple[int, int]:
        pass

    # Give board to player
    def setBoard(self) -> None:
        pass
