import pygame
from Player import Player
from Orb import Orb
from Camera import Camera
import random

start_width = 50
start_height = 50
FPS = 60
Player_Start_x = 0
Player_Start_y = 0
Player_Texture = "body_red.png"



starting_orbs = 30



class MainGame:
    def __init__(self):

        pygame.display.set_caption("M21 slither.io")
        self.windDims = (1000, 1000)
        self.window = pygame.display.set_mode(self.windDims)
        self.winColor = (225, 225, 225)
        self.quit = False
        self.clock = pygame.time.Clock()
        self.camera = Camera(Player_Start_x,Player_Start_y, (start_width,start_height), self.windDims)

        self.player = Player(Player_Start_x,Player_Start_y,start_width,start_height,Player_Texture)
        self.orbs = []

    def init(self):
        textures = ["blue_orb.png","purple_orb.png","yellow_orb.png"]
        for i in range(starting_orbs):
            randX = random.randint(0, self.windDims[0])
            randY = random.randint(0,self.windDims[1])
            randR = random.randint(10,start_width)

            randTextures = random.choice(textures)

            new_orb = Orb(randX,randY,randR,randTextures)
            self.orbs.append(new_orb)

        self.play()

    def play(self):
        while self.quit == False:
            self.update()
            self.render()

    def update(self):
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

        self.player.update(self.windDims)

        for orb in self.orbs:
            if orb.update(self.player):
                self.orbs.remove(orb)

        self.camera.update(self.player.rect.x,self.player.rect.y)

    def render(self):
        self.window.fill(self.winColor)
        self.player .draw(self.window, self.camera)
        for orb in self.orbs:
            orb.draw(self.window, self.camera)
        pygame.display.update()
