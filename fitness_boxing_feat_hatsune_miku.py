from __future__ import annotations


from typing import List

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class FitnessBoxingHatsuneMikuArchipelagoOptions:
    #miku_boxing_difficulties: MikuBoxingDifficulties
    pass

class FitnessBoxingHatsuneMikuGame(Game):
    name = "Fitness Boxing feat. HATSUNE MIKU"
    platforms = KeymastersKeepGamePlatforms.SW

    is_adult_only_or_unreated = False

    options_cls = FitnessBoxingHatsuneMikuArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
        GameObjectiveTemplate(
            label="Play SONG on DIFFICULTY difficulty",
            data={
                "SONG": (self.miku_exercise_list, 1),
                "DIFFICULTY": (self.difficulties_list, 1),
            }
            is_time_consuming=False,
            is_difficult=False,
            weight=3,
        ),
        GameObjectiveTemplate(
            label="Play any song on DIFFICULTY difficulty",
            data={
                "DIFFICULTY": (self.difficulties_list, 1),
            }
            is_time_consuming=False,
            is_diffuclt=False,
            weight=1,
        ),
    ]

    @staticmethod
    def miku_exercise_list() -> List[str]:
        return [
        "I Will Make You Miku Miku(Miku Miku ni Shiteageru)",
        "Melt",
        "THE END OF HATSUNE MIKU",
        "Fire Flower",
        "Po Pi Po",
        "Double Lariat",
        "Romeo & Cinderella",
        "Just Be Friends",
        "melancholic",
        "World's End Dancehall",
        "8HIT",
        "Tell Your World",
        "Ai Dee",
        "Lost One's Weeping",
        "Burikinodansu",
        "Alien Alien",
        "Teo",
        "Hated By Life",
        "BRING IT ON",
        "Shoujo Rei",
        "Bitter Choco Decoration",
        "Telecaster b boy (long ver.)",
        "The Vampire",
        "God-ish",
        "Rise up",
        "Medic: A Doll",
        "OVER LIT",
        "Lovesong ni Shukuhaiwo!",
        "Champion Road to True Love",
        "Let's Mikusercise!!",
        "watashi no audiro",
    ]

    @staticmethod
    def difficulties_list() -> List[str]:
        return [
        "Lightweight",
        "Middlweight",
        "Heavyweight",
    ]

