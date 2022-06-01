from abc import ABC

from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self,
                 nickname: str,
                 favourite_dish
                 ):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        return (f"{self.nickname} is eating"
                f" {self._favourite_dish}")
