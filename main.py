import sys
import random

import pygame

import options

width,height = 1200,800

window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Sorting Algorithm Visualizer')

white = (255,255,255)
color_list = [(127,127,127),(50,50,50),(0,0,0)]

detail_length = (320,120)
option1_detail = pygame.Rect((width-360,0),detail_length)
option2_detail = pygame.Rect((width-760,0),detail_length)
option3_detail = pygame.Rect((width-1160,0),detail_length)
option4_detail = pygame.Rect((width-760,0+detail_length[1]+40),detail_length)
back_detail = pygame.Rect((width//2-detail_length[0]//2,height-detail_length[1]-5),detail_length)

def reset_list(list_len):
    start_list = []
    for i in range(list_len):
        start_list.append(random.randint(1,51))
        algorithms = options.Algorithms(window,start_list)
    return start_list,algorithms

def change_length(keys_pressed):
    pass

def main():
    list_len = 1200
    screen = 1
    click = False
    clock = pygame.time.Clock()
    start_list,algorithms = reset_list(list_len)

    draw = options.Draw(window)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        
        mx,my = pygame.mouse.get_pos()

        if screen == 1:
            if click == True:
                if option1_detail.collidepoint(mx,my):
                    algorithms.bubble_sort()
                if option2_detail.collidepoint(mx,my):
                    screen = 2
                if option3_detail.collidepoint(mx,my):
                    start_list,algorithms = reset_list()
                if option4_detail.collidepoint(mx,my):
                    screen = 3

            click = False
            draw.draw(start_list)

        if screen == 2:
            if click == True:
                if back_detail.collidepoint(mx,my):
                    screen = 1

        if screen == 3:
            if click == True:
                if back_detail.collidepoint(mx,my):
                    screen = 1

            click = False

            keys_pressed = pygame.key.get_pressed()

            draw.change_length()

if __name__ == '__main__':
    main()