from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self,
                 nickname: str,
                 skill_level: int,
                 favourite_dish: str
                 ):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self):
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the "
                f"{self._skill_level} level"
                )

    def get_rating(self):
        return self._skill_level
