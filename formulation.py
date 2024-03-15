from enum import Enum
from typing import List
import random

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

c = Card([2, 2, 0, 0, 0], 0, Gem.GREEN)
n = Noble([3, 3, 3, 0, 0])
b = Board([c], [n])

# standard cards from the game
# https://docs.google.com/spreadsheets/d/15ghp8rJ_vdVgxZIVJGawAYQXRMZSVHJYpZRfQUplAhE/htmlview
CARDS = [Card([1, 1, 1, 1, 0], 0, Gem.BLACK),
         Card([1, 2, 1, 1, 0], 0, Gem.BLACK),
         Card([2, 2, 0, 1, 0], 0, Gem.BLACK),
         Card([0, 0, 1, 3, 1], 0, Gem.BLACK),
         Card([0, 0, 2, 1, 0], 0, Gem.BLACK),
         Card([2, 0, 2, 0, 0], 0, Gem.BLACK),
         Card([0, 0, 3, 0, 0], 0, Gem.BLACK),
         Card([0, 4, 0, 0, 0], 1, Gem.BLACK),

         Card([1, 0, 1, 1, 1], 0, Gem.BLUE),
         Card([1, 0, 1, 2, 1], 0, Gem.BLUE),
         Card([1, 0, 2, 2, 0], 0, Gem.BLUE),
         Card([0, 1, 3, 1, 0], 0, Gem.BLUE),
         Card([1, 0, 0, 0, 2], 0, Gem.BLUE),
         Card([0, 0, 2, 0, 2], 0, Gem.BLUE),
         Card([0, 0, 0, 0, 3], 0, Gem.BLUE),
         Card([0, 0, 0, 4, 0], 1, Gem.BLUE),

         Card([0, 1, 1, 1, 1], 0, Gem.WHITE),
         Card([0, 1, 2, 1, 1], 0, Gem.WHITE),
         Card([0, 2, 2, 0, 1], 0, Gem.WHITE),
         Card([3, 1, 0, 0, 1], 0, Gem.WHITE),
         Card([0, 0, 0, 2, 1], 0, Gem.WHITE),
         Card([0, 2, 0, 0, 2], 0, Gem.WHITE),
         Card([0, 3, 0, 0, 0], 0, Gem.WHITE),
         Card([0, 0, 4, 0, 0], 1, Gem.WHITE),
         
         Card([1, 1, 0, 1, 1], 0, Gem.GREEN),
         Card([1, 1, 0, 1, 2], 0, Gem.GREEN),
         Card([0, 1, 0, 2, 2], 0, Gem.GREEN),
         Card([1, 3, 1, 0, 0], 0, Gem.GREEN),
         Card([2, 1, 0, 0, 0], 0, Gem.GREEN),
         Card([0, 2, 0, 2, 0], 0, Gem.GREEN),
         Card([0, 0, 0, 3, 0], 0, Gem.GREEN),
         Card([0, 0, 0, 0, 4], 1, Gem.GREEN),
         
         Card([1, 1, 1, 0, 1], 0, Gem.RED),
         Card([2, 1, 1, 0, 1], 0, Gem.RED),
         Card([2, 0, 1, 0, 2], 0, Gem.RED),
         Card([1, 0, 0, 1, 3], 0, Gem.RED),
         Card([0, 2, 1, 0, 0], 0, Gem.RED),
         Card([2, 0, 0, 2, 0], 0, Gem.RED),
         Card([3, 0, 0, 0, 0], 0, Gem.RED),
         Card([4, 0, 0, 0, 0], 1, Gem.RED),
         
         Card([3, 2, 2, 0, 0], 1, Gem.BLACK),
         Card([3, 0, 3, 0, 2], 1, Gem.BLACK),
         Card([0, 1, 4, 2, 0], 2, Gem.BLACK),
         Card([0, 0, 5, 3, 0], 2, Gem.BLACK),
         Card([5, 0, 0, 0, 0], 2, Gem.BLACK),
         Card([0, 0, 0, 0, 6], 3, Gem.BLACK),
         
         Card([0, 2, 2, 3, 0], 1, Gem.BLUE),
         Card([0, 2, 3, 0, 3], 1, Gem.BLUE),
         Card([5, 3, 0, 0, 0], 2, Gem.BLUE),
         Card([2, 0, 0, 1, 4], 2, Gem.BLUE),
         Card([0, 5, 0, 0, 0], 2, Gem.BLUE),
         Card([0, 6, 0, 0, 0], 3, Gem.BLUE),

         Card([0, 0, 3, 2, 2], 1, Gem.WHITE),
         Card([2, 3, 0, 3, 0], 1, Gem.WHITE),
         Card([0, 0, 1, 4, 2], 2, Gem.WHITE),
         Card([0, 0, 0, 5, 3], 2, Gem.WHITE),
         Card([0, 0, 0, 5, 0], 2, Gem.WHITE),
         Card([6, 0, 0, 0, 0], 3, Gem.WHITE),

         Card([3, 0, 2, 3, 0], 1, Gem.GREEN),
         Card([2, 3, 0, 0, 2], 1, Gem.GREEN),
         Card([4, 2, 0, 0, 1], 2, Gem.GREEN),
         Card([0, 5, 3, 0, 0], 2, Gem.GREEN),
         Card([0, 0, 5, 0, 0], 2, Gem.GREEN),
         Card([0, 0, 6, 0, 0], 3, Gem.GREEN),

         Card([2, 0, 0, 2, 3], 1, Gem.RED),
         Card([0, 3, 0, 2, 3], 1, Gem.RED),
         Card([1, 4, 2, 0, 0], 2, Gem.RED),
         Card([3, 0, 0, 0, 5], 2, Gem.RED),
         Card([0, 0, 0, 0, 5], 2, Gem.RED),
         Card([0, 0, 0, 6, 0], 3, Gem.RED),
         
         Card([3, 3, 5, 3, 0], 3, Gem.BLACK),
         Card([0, 0, 0, 7, 0], 4, Gem.BLACK),
         Card([0, 0, 3, 6, 3], 4, Gem.BLACK),
         Card([0, 0, 0, 7, 3], 5, Gem.BLACK),

         Card([3, 0, 3, 3, 5], 3, Gem.BLUE),
         Card([7, 0, 0, 0, 0], 4, Gem.BLUE),
         Card([6, 3, 0, 0, 3], 4, Gem.BLUE),
         Card([7, 3, 0, 0, 0], 5, Gem.BLUE),

         Card([0, 3, 3, 5, 3], 3, Gem.WHITE),
         Card([0, 0, 0, 0, 7], 4, Gem.WHITE),
         Card([3, 0, 0, 3, 6], 4, Gem.WHITE),
         Card([3, 0, 0, 0, 7], 5, Gem.WHITE),

         Card([5, 3, 0, 3, 3], 3, Gem.GREEN),
         Card([0, 7, 0, 0, 0], 4, Gem.GREEN),
         Card([3, 6, 3, 0, 0], 4, Gem.GREEN),
         Card([0, 7, 3, 0, 0], 5, Gem.GREEN),

         Card([3, 5, 3, 0, 3], 3, Gem.RED),
         Card([0, 0, 7, 0, 0], 4, Gem.RED),
         Card([0, 3, 6, 3, 0], 4, Gem.RED),
         Card([0, 0, 7, 3, 0], 5, Gem.RED),]

NOBLES = [(0, 0, 0, 4, 4),
          (3, 0, 3, 0, 3),
          (0, 4, 4, 0, 0),
          (4, 0, 4, 0, 0),
          (0, 4, 0, 4, 0),
          (0, 3, 0, 3, 3),
          (0, 3, 3, 3, 0),
          (4, 4, 0, 0, 0),
          (3, 3, 3, 0, 0),
          (3, 0, 0, 3, 3),]

b = Board(CARDS, NOBLES)
