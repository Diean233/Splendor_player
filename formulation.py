from enum import Enum
from typing import List

class Gem(Enum):
    WHITE = 0
    BLUE = 1
    GREEN = 2
    RED = 3
    BLACK = 4

class Card:
    def __init__(self, gems:List[int], score:int, color:Gem):
        self.gems = gems
        self.score = score
        self.color = color
    
    # calculate cost given gems player already has
    def cost(self, player_gems:List[int]) -> int:
        return sum(self.gems[i] - player_gems[i] if self.gems[i] > player_gems[i] else 0 for i in range(5))

class Noble:
    def __init__(self, gems:List[int]):
        self.gems = gems
    
    # decide if player can have the noble
    def satisfied(self, player_gems:List[int]) -> bool:
        return 5 == sum(self.gems[i] <= player_gems[i] for i in range(5))

class Board:
    def __init__(self, deck:List[Card], nobles:List[Noble], T:int=5):
        self.deck = deck
        self.nobles = nobles
        self.T = T

class Player:
    def __init__(self):
        self.gems = [0, 0, 0, 0, 0]
        self.cards = [0, 0, 0, 0, 0]
        self.score = 0
    
    # what the player can afford right now
    def purchasing_power(self) -> List[int]:
        return [x + y for x, y in zip(self.gems, self.cards)]
