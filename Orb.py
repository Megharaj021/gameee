import pygame

from Common import Common
SCORE_INCREMENT = 5


class Orb(Common):
    def __init__(self, x, y, r, filepath):
        super().__init__( x, y, r, r, filepath)

    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.score += SCORE_INCREMENT
            return True
        return False
