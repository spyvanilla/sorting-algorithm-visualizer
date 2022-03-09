import sys
import random

import pygame
pygame.font.init()

font = pygame.font.SysFont('Arial',40)

width,height = 1200,800

white = (255,255,255)
green = (0,255,0)
color_list = [(127,127,127),(50,50,50),(0,0,0)]

window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Sorting Algorithm Visualizer')

option_length = (300,100)
detail_length = (320,120)

option1 = pygame.Rect((width-350,10),option_length)
option1_detail = pygame.Rect((width-360,0),detail_length)
option1_text = font.render("Sort",1,color_list[2])

option2 = pygame.Rect((width-750,10),option_length)
option2_detail = pygame.Rect((width-760,0),detail_length)
option2_text = font.render("Choose method",1,color_list[2])

option3 = pygame.Rect((width-1150,10),option_length)
option3_detail = pygame.Rect((width-1160,0),detail_length)
option3_text = font.render("Change list",1,color_list[2])

start_list = []

for i in range(80):
    start_list.append(random.randint(0,50))

def bubble_sort():
    end = len(start_list)

    while end > 1:
        traded = False
        index = 0
        
        while index < end-1:
            if start_list[index] > start_list[index+1]:
                traded = True
                temp = start_list[index]
                start_list[index] = start_list[index+1]
                start_list[index+1] = temp
            index += 1

        if not traded:
            break
        end -= 1

def draw():
    window.fill(white)

    rect_width = 800//len(start_list)
    
    for position,number in enumerate(start_list):
        number_column = pygame.Rect(200+rect_width*position,height-number*10,rect_width,number*10)

        if 50//2+10 < number:
            pygame.draw.rect(window,color_list[2],number_column)
        elif 50//2-10 <= number <= 50//2+10:
            pygame.draw.rect(window,color_list[1],number_column)
        else:
            pygame.draw.rect(window,color_list[0],number_column)

    pygame.draw.rect(window,color_list[1],option1_detail)
    pygame.draw.rect(window,color_list[0],option1)
    window.blit(option1_text,(width-233,40))

    pygame.draw.rect(window,color_list[1],option2_detail)
    pygame.draw.rect(window,color_list[0],option2)
    window.blit(option2_text,(width-723,40))

    pygame.draw.rect(window,color_list[1],option3_detail)
    pygame.draw.rect(window,color_list[0],option3)
    window.blit(option3_text,(width-1103,40))

    pygame.display.update()

def main():
    click = False
    clock = pygame.time.Clock()

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
                pass
            click = False
        draw()

if __name__ == '__main__':
    main()