from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class PokopiaArchipelagoOptions:
    include_cooking: PokopiaIncludeCooking
    include_minigames: PokopiaIncludeMiniGames
    include_daily_challenges: PokopiaIncludeDailies
    include_crafting: PokopiaIncludeCrafting

    

class PokopiaGame(Game):
    name = "Pokopia"
    platform = KeymastersKeepGamePlatforms.SW2

    is_adult_only_or_unrated = False

    options_cls = PokopiaArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        game_objective_templates.extend([
        GameObjectiveTemplate(
            label="Gather GATHER_COUNT GATHER",
            data={
                "GATHER_COUNT": (self.gather_count, 1),
                "GATHER": (self.gather_list, 1),
            },
            is_time_consuming=False,
            is_difficult=False,
            weight=3,
        ),
        GameObjectiveTemplate(
            label="Harvest HARVEST_COUNT HARVEST",
            data={
                "HARVEST_COUNT": (self.gather_count, 1),
                "HARVEST": (self.harvest_list, 1),
            },
            is_time_consuming=False,
            is_difficult=False,
            weight=2,
        ),
        ])
        if self.include_daily_challenges:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Complete DAILIES_COUNT daily challenges",
                    data={
                        "DAILIES_COUNT": (self.dailies_count, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ]),
        if self.include_minigames:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Play a round of MINIGAME (minigame)",
                    data={
                        "MINIGAME":(self.minigames_list, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
            ]),
        if self.include_cooking:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Cook COOKING_COUNT MEALS meals",
                    data={
                        "COOKING_COUNT": (self.cooking_count, 1),
                        "MEALS": (self.cooking_list, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            ]),
        if self.include_crafting:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Craft CRAFTING_COUNT CRAFT_RESOURCE",
                    data={
                        "CRAFTING_COUNT": (self.crafting_count, 1),
                        "CRAFT_RESOURCE": (self.craft_resource_list, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                    ),
            ]),
        return game_objective_templates

    @property
    def include_daily_challenges(self) -> bool:
        return self.archipelago_options.include_daily_challenges.value
    
    @property
    def include_crafting(self) -> bool:
        return self.archipelago_options.include_crafting.value
    
    @property
    def include_cooking(self) -> bool:
        return self.archipelago_options.include_cooking.value
    
    @property
    def include_minigames(self) -> bool:
        return self.archipelago_options.include_minigames.value

    @staticmethod
    def gather_list() -> List[str]:
        return [
        "twine",
        "sturdy sticks",
        "vines",
        "stones",
        "veggies(any)",
        "seaweed",
        "leaves",
        "ores(any)",
        "iron ore",
        "copper ore",
        "gold ore",
        "small logs",
        "stardust",
        "seashells",
        "sea glass fragments",
        "nonburnable garbage",
        "wastepaper",
        "cave mushrooms",
    ]

    @staticmethod
    def craft_resource_list() -> List[str]:
        return [
        "iron ingot",
        "copper ingot",
        "lumber",
        "pokemetal",
    ]

    @staticmethod
    def minigames_list() -> List[str]:
        return[
            "Hide-and-Seek",
            "Jump Rope",
            "Look That Way",
            "Quiz",
        ]
    
    @staticmethod
    def harvest_list() -> List[str]:
        return[
            "beans",
            "potatoes",
            "wheat",
            "tomatoes",
            "chesto berry",
            "leppa berry",
            "pecha berry",
            "lum berry",
        ]
    
    @staticmethod
    def cooking_list() -> List[str]:
        return[
            "Simple Salad",
            "Leppa Salad",
            "Seaweed Salad",
            "Shredded Salad",
            "Crushed-Berry Salad",
            "Crouton Salad",
            "Simple Soup",
            "Mushroom Soup",
            "Electrifying Soup",
            "Healthy Soup",
            "Flavorful Soup",
            "Simple Bread",
            "Leppa Bread",
            "Recycled Bread",
            "Fluffy Bread",
            "Bread Bowl",
            "Simple Hamburger Steak",
            "Mushroom Hamburger Steak",
            "Tomato Hamburger Steak",
            "Potato Hamburger Steak",
            "Bitter Hamburger Steak",
            "Vibrant Hamburger Steak",
        ]
    
    @staticmethod
    def dailies_count() -> range:
        return range(1,4)
    
    @staticmethod
    def cooking_count() -> range:
        return range(1,10,1)
    
    @staticmethod
    def gather_count() -> range:
        return range(1,25,5)
    
    @staticmethod
    def crafting_count() -> range:
        return range(1,50,5)
    
class PokopiaIncludeCooking(Toggle):
    """
    Include cooking dishes as potential challenges?
    """

    display_name = "Include Cooking"

class PokopiaIncludeMiniGames(Toggle):
    """
    Include minigames such as "Hide-and-Seek" "Look That Way" "Quizzes" "Jump Rope" as potential challenges?
    """

    display_name = "Include MiniGames"

class PokopiaIncludeCrafting(Toggle):
    """
    Include crafting items such as Furniture, Ingots, Blocks, Lumber etc
    """

    display_name = "Include Crafting"

class PokopiaIncludeDailies(Toggle):
    """
    Include completeing Daily Challenges to the pool
    """

    display_name = "Include Daily Challenges"
