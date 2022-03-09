import sys
import random

import pygame
pygame.font.init()

font = pygame.font.SysFont('Arial',40)

white = (255,255,255)

window = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Sorting Algorithm Visualizer')

def draw():
    window.fill(white)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        draw()

if __name__ == '__main__':
    main()