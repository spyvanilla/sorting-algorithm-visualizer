import sys
import random

import pygame

import algorithms
import draw

width,height = 1200,800

white = (255,255,255)
color_list = [(127,127,127),(50,50,50),(0,0,0)]

window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Sorting Algorithm Visualizer')

detail_length = (320,120)
option1_detail = pygame.Rect((width-360,0),detail_length)
option2_detail = pygame.Rect((width-760,0),detail_length)
option3_detail = pygame.Rect((width-1160,0),detail_length)

def reset_list():
    start_list = []
    for i in range(120):
        start_list.append(random.randint(1,51))
    return start_list

def main():
    click = False
    clock = pygame.time.Clock()
    start_list = reset_list()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        
        mx,my = pygame.mouse.get_pos()

        if click == True:
            if option1_detail.collidepoint(mx,my):
                algorithms.bubble_sort(window,start_list)
            if option2_detail.collidepoint(mx,my):
                pass
            if option3_detail.collidepoint(mx,my):
                start_list = reset_list()

        click = False
        draw.draw(window,start_list)

if __name__ == '__main__':
    main()