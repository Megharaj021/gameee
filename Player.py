import pygame
from Common import Common
from Segment import Segment


class Player(Common):
    def __init__(self, x, y, w, h, filepath):
        super().__init__(x, y, w, h, filepath)

        self.speed = 10
        self.prevScore = 0
        self.score = 0
        self.segments = []

    def update(self, winDims):
        mousePos = pygame.mouse.get_pos()
        worldPos = (mousePos[0] - winDims[0] / 2 + self.rect.x, mousePos[1] - winDims[1] / 2 + self.rect.y)

        distVec = [worldPos[0] - self.rect.x, worldPos[1] - self.rect.y]
        length = (distVec[0] ** 2 + distVec[1] ** 2) ** (1 / 2)
        distVec = (distVec[0] / length, distVec[1] / length)

        self.rect.x += distVec[0] * self.speed
        self.rect.y += distVec[1] * self.speed

        if self.score - self.prevScore == 20:
            self.prevScore = self.score

        start_X = distVec[0] * -1 * self.rect.w + self.rect.x
        start_Y = distVec[1] * -1 * self.rect.h + self.rect.y
        new_Segment = Segment(start_X, start_Y, self.rect.w, self.rect.h,"body_red.png",self.speed)
        self.segments.append(new_Segment)

        for i in range(len(self.segments)):
            if i == 0:
                self.segments[i].update((self.rect.x, self.rect.y))

            else:
                self.segments[i].update((self.segments[i-1].rect.x, self.segments[i-1].rect.y))





    def draw(self, window, camera):
        window.blit(self.texture, camera.translate(self.rect.x, self.rect.y))

        for segment in self.segments:
            window.blit(segment.texture, camera.translate(segment.rect.x, segment.rect.y))

