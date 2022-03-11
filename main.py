import sys
import random
import time
from xmlrpc.server import list_public_methods

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

bubble_sort_detail = pygame.Rect((width-360,0),detail_length)
insertion_sort_detail = pygame.Rect((width-760,0),detail_length)
shell_sort_detail = pygame.Rect((width-1160,0),detail_length)

back_detail = pygame.Rect((width//2-detail_length[0]//2,height-detail_length[1]-5),detail_length)

number_keys = {
    pygame.K_0:0,
    pygame.K_1:1,
    pygame.K_2:2,
    pygame.K_3:3,
    pygame.K_4:4,
    pygame.K_5:5,
    pygame.K_6:6,
    pygame.K_7:7,
    pygame.K_8:8,
    pygame.K_9:9
}

def reset_list(list_len):
    start_list = []

    for i in range(list_len):
        start_list.append(random.randint(1,51))
        algorithms = options.Algorithms(window,start_list)
    return start_list,algorithms

def change_length(keys_pressed,list_len,change_len,exceeded_error):
    if len(change_len) < 4:

        for key,value in number_keys.items():
            if keys_pressed[key]:
                change_len.append(value)
                time.sleep(0.2)

    if keys_pressed[pygame.K_BACKSPACE]:
        if len(change_len) > 0:
            del change_len[len(change_len)-1]

            if exceeded_error is not None:
                return list_len,change_len,None

            time.sleep(0.2)
    if keys_pressed[pygame.K_RETURN]:
        if int("".join(str(value) for value in change_len)) > 1200:
            time.sleep(0.5)
            return list_len,change_len,True
        time.sleep(0.5)
        return int("".join(str(value) for value in change_len)),[],exceeded_error
    return list_len,change_len,exceeded_error

def main():
    sort_method = 1
    exceeded_error = None
    change_len = []
    list_len = 200
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

                    if sort_method == 1:
                        algorithms.bubble_sort()
                    if sort_method == 2:
                        algorithms.insertion_sort()
                    if sort_method == 3:
                        algorithms.shell_sort()

                if option2_detail.collidepoint(mx,my):
                    screen = 2
                if option3_detail.collidepoint(mx,my):
                    start_list,algorithms = reset_list(list_len)
                if option4_detail.collidepoint(mx,my):
                    screen = 3

            click = False
            draw.draw(start_list)

        if screen == 2:
            if click == True:
                if bubble_sort_detail.collidepoint(mx,my):
                    sort_method = 1
                if insertion_sort_detail.collidepoint(mx,my):
                    sort_method = 2
                if shell_sort_detail.collidepoint(mx,my):
                    sort_method = 3
                if back_detail.collidepoint(mx,my):
                    screen = 1

            click = False
            draw.change_sort_method()

        if screen == 3:
            if click == True:
                if back_detail.collidepoint(mx,my):
                    start_list,algorithms = reset_list(list_len)
                    screen = 1

            click = False

            keys_pressed = pygame.key.get_pressed()
            list_len,change_len,exceeded_error = change_length(keys_pressed,list_len,change_len,exceeded_error)

            draw.change_length(change_len,exceeded_error)

if __name__ == '__main__':
    main()