from settings import *
import pygame

class App:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIN_WID,WIN_HI))

    def main(self):
        pygame.init()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
            self.screen.fill("black")
            self.clock.tick(60)


myApp = App()
myApp.main()
