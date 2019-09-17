from player_base import PlayerBase


class RandomBot(PlayerBase):
    def doMove(self):
        return (1, 3)
