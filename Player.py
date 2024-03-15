from typing import List

from formulation import Card, Board, Gem, Noble
class Player:
    def __init__(self):
        self.gems = [0, 0, 0, 0, 0]
        self.cards = [0, 0, 0, 0, 0]
        self.score = 0
        self.nobles = []

    def purchasing_power(self) -> List[int]:
        """Calculate what the player can afford."""
        return [self.gems[i] + self.cards[i] for i in range(5)]

    def can_purchase_card(self, card: Card) -> bool:
        """Check if the player can afford a card."""
        total_resources = self.purchasing_power()
        return all(card_cost <= total_resources[i] for i, card_cost in enumerate(card.gems))

    def purchase_card(self, card: Card):
        """Purchase a card, adjusting player's resources."""
        for i in range(5):
            gem_cost = max(0, card.gems[i] - self.cards[i])
            self.gems[i] -= gem_cost
        self.cards[card.color.value] += 1
        self.score += card.score

    def select_gems_to_take(self, board: Board) -> List[int]:
        """Determine which gems to take, prioritizing diversity."""
        gems_taken = [0, 0, 0, 0, 0]
        types_taken = 0
        for i in range(5):
            if board.T[i] > 0 and types_taken < 3:
                board.T[i] -= 1
                self.gems[i] += 1
                gems_taken[i] = 1
                types_taken += 1
        return gems_taken
