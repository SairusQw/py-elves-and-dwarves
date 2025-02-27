def calculate_team_total_rating(total_rating: list):
    return sum(player.get_rating() for player in total_rating)


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
