from Player import Player
from formulation import Card, Board, Gem, Noble
import random

# total amount of noble cards
noble_amount = 10
# total amount of gem cards
card_amount = 90

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
         Card([0, 0, 7, 3, 0], 5, Gem.RED), ]

NOBLES = [(0, 0, 0, 4, 4),
          (3, 0, 3, 0, 3),
          (0, 4, 4, 0, 0),
          (4, 0, 4, 0, 0),
          (0, 4, 0, 4, 0),
          (0, 3, 0, 3, 3),
          (0, 3, 3, 3, 0),
          (4, 4, 0, 0, 0),
          (3, 3, 3, 0, 0),
          (3, 0, 0, 3, 3), ]


# def play(n:int=card_amount, m:int=3, p:int=15, T:int=5):
#     # initialization
#     cards = CARDS
#     if n < card_amount:
#         cards = random.sample(CARDS, n)
#     
#     nobles = random.sample(NOBLES, m)
#     
#     p = Player()
#     b = Board(cards, nobles, T)
# 
#     # play with greedy algo
#     return greedy_play(p, b, p)
#     pass

def greedy_action(player: Player, board: Board):
    affordable_cards = [card for card in board.deck if player.can_purchase_card(card)]
    if affordable_cards:
        # Prioritize cards by score and then by minimal cost
        best_card = max(affordable_cards, key=lambda card: (card.score, -sum(card.gems)))
        player.purchase_card(best_card)
        board.deck.remove(best_card)
        print(f"Purchased card with score {best_card.score} and cost {best_card.gems}.")
    else:
        # If no affordable card, take gems
        gems_taken = player.select_gems_to_take(board)
        print(f"Took gems: {gems_taken}")


def play(n: int = card_amount, m: int = noble_amount, p: int = 15, T: int = 5):

    cards = random.sample(CARDS, n)

    nobles = random.sample(NOBLES, m)

    player = Player()
    board = Board(cards, nobles, T)  #

    turn = 0
    while player.score < p and turn < 100:
        greedy_action(player, board)
        turn += 1

    return player.score >= p, turn


n_cards = 90
n_nobles = 10
target_points = 15
initial_tokens = 4

game_won, turns_taken = play(n=n_cards, m=n_nobles, p=target_points, T=initial_tokens)

if game_won:
    print(f"玩家赢得了游戏，在{turns_taken}回合内达到了{target_points}分！")
else:
    print(f"玩家未能在{turns_taken}回合内赢得游戏。")
