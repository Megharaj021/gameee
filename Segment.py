import pygame
from Common import Common


class Segment(Common):
    def __init__(self, x, y, w, h, filepath, speed):
        super().__init__(x, y, w, h, filepath)
        self.speed = speed

    def update(self, targetPos):
        direction = [targetPos[0] - self.rect.x, targetPos[1] - self.rect.y]

        length = (direction[0] ** 2 + direction[1] ** 2) ** (1 / 2)
        if length < self.rect.w:
            return

        direction[0] /= length
        direction[1] /= length

        self.rect.x += direction[0] * self.speed
        self.rect.y += direction[1] * self.speed
