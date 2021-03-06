import pygame

pygame.font.init()

font = pygame.font.SysFont('Arial',40)

width,height = 1200,800

white = (255,255,255)
red = (255,0,0)
color_list = [(127,127,127),(50,50,50),(0,0,0)]

option_length = (300,100)
detail_length = (320,120)

#Options of the first screen
option1 = pygame.Rect((width-350,10),option_length)
option1_detail = pygame.Rect((width-360,0),detail_length)
option1_text = font.render("Sort",1,color_list[2])

option2 = pygame.Rect((width-750,10),option_length)
option2_detail = pygame.Rect((width-760,0),detail_length)
option2_text = font.render("Choose method",1,color_list[2])

option3 = pygame.Rect((width-1150,10),option_length)
option3_detail = pygame.Rect((width-1160,0),detail_length)
option3_text = font.render("Reset list",1,color_list[2])

option4 = pygame.Rect((width-750,10+option_length[1]+60),option_length)
option4_detail = pygame.Rect((width-760,0+detail_length[1]+40),detail_length)
option4_text = font.render("Change length",1,color_list[2])

back_option = pygame.Rect((width//2-option_length[0]//2,height-(option_length[1]+30//2)),option_length)
back_detail = pygame.Rect((width//2-detail_length[0]//2,height-detail_length[1]-5),detail_length)
back_text = font.render("Back",1,color_list[2])

#Options of the sort method selection screen
bubble_sort_option = pygame.Rect((width-350,10),option_length)
bubble_sort_detail = pygame.Rect((width-360,0),detail_length)
bubble_sort_text = font.render("Bubble sort",1,color_list[2])

insertion_sort_option = pygame.Rect((width-750,10),option_length)
insertion_sort_detail = pygame.Rect((width-760,0),detail_length)
insertion_sort_text = font.render("Insertion sort",1,color_list[2])

shell_sort_option = pygame.Rect((width-1150,10),option_length)
shell_sort_detail = pygame.Rect((width-1160,0),detail_length)
shell_sort_text = font.render("Shell sort",1,color_list[2])

quick_sort_option = pygame.Rect((width-350,210),option_length)
quick_sort_detail = pygame.Rect((width-360,200),detail_length)
quick_sort_text = font.render("Quick sort",1,color_list[2])

pigeonhole_sort_option = pygame.Rect((width-750,210),option_length)
pigeonhole_sort_detail = pygame.Rect((width-760,200),detail_length)
pigeonhole_sort_text = font.render("Pigeohole sort",1,color_list[2])

cycle_sort_option = pygame.Rect((width-1150,210),option_length)
cycle_sort_detail = pygame.Rect((width-1160,200),detail_length)
cycle_sort_text = font.render("Cycle sort",1,color_list[2])

#Options of the length change screen
change_len = pygame.Rect((width//2-option_length[0]//2,height//2-option_length[1]//2+100),option_length)
change_len_detail = pygame.Rect((width//2-detail_length[0]//2,height//2-detail_length[1]//2+100),detail_length)
change_len_text = font.render("Enter the value of your list:",1,color_list[2])
exceeded_error_message = font.render("The maximum list length in 1200",1,red)

class Draw:
    
    def __init__(self,window):
        self.window = window

    def draw(self,start_list):
        self.window.fill(white)

        rect_width = 1200//len(start_list)
        
        for position,number in enumerate(start_list):
            number_column = pygame.Rect(0+rect_width*position,height-number*10,rect_width,number*10)

            if 50//2+10 < number:
                pygame.draw.rect(self.window,color_list[2],number_column)
            elif 50//2-10 <= number <= 50//2+10:
                pygame.draw.rect(self.window,color_list[1],number_column)
            else:
                pygame.draw.rect(self.window,color_list[0],number_column)

        pygame.draw.rect(self.window,color_list[1],option1_detail)
        pygame.draw.rect(self.window,color_list[0],option1)
        self.window.blit(option1_text,(option1.x+150-option1_text.get_width()//2,option1.y+50-option1_text.get_height()//2))

        pygame.draw.rect(self.window,color_list[1],option2_detail)
        pygame.draw.rect(self.window,color_list[0],option2)
        self.window.blit(option2_text,(option2.x+150-option2_text.get_width()//2,option2.y+50-option2_text.get_height()//2))

        pygame.draw.rect(self.window,color_list[1],option3_detail)
        pygame.draw.rect(self.window,color_list[0],option3)
        self.window.blit(option3_text,(option3.x+150-option3_text.get_width()//2,option3.y+50-option3_text.get_height()//2))

        pygame.draw.rect(self.window,color_list[1],option4_detail)
        pygame.draw.rect(self.window,color_list[0],option4)
        self.window.blit(option4_text,(option4.x+150-option4_text.get_width()//2,option4.y+50-option4_text.get_height()//2))

        pygame.display.update()

    def change_sort_method(self):
        self.window.fill(white)

        pygame.draw.rect(self.window,color_list[1],bubble_sort_detail)
        pygame.draw.rect(self.window,color_list[0],bubble_sort_option)
        self.window.blit(bubble_sort_text,(bubble_sort_option.x+150-bubble_sort_text.get_width()//2,bubble_sort_option.y+50-bubble_sort_text.get_height()//2))

        pygame.draw.rect(self.window,color_list[1],insertion_sort_detail)
        pygame.draw.rect(self.window,color_list[0],insertion_sort_option)
        self.window.blit(insertion_sort_text,(insertion_sort_option.x+150-insertion_sort_text.get_width()//2,insertion_sort_option.y+50-insertion_sort_text.get_height()//2))

        pygame.draw.rect(self.window,color_list[1],shell_sort_detail)
        pygame.draw.rect(self.window,color_list[0],shell_sort_option)
        self.window.blit(shell_sort_text,(shell_sort_option.x+150-shell_sort_text.get_width()//2,shell_sort_option.y+50-shell_sort_text.get_height()//2))

        pygame.draw.rect(self.window,color_list[1],quick_sort_detail)
        pygame.draw.rect(self.window,color_list[0],quick_sort_option)
        self.window.blit(quick_sort_text,(quick_sort_option.x+150-quick_sort_text.get_width()//2,quick_sort_option.y+50-quick_sort_text.get_height()//2))

        pygame.draw.rect(self.window,color_list[1],pigeonhole_sort_detail)
        pygame.draw.rect(self.window,color_list[0],pigeonhole_sort_option)
        self.window.blit(pigeonhole_sort_text,(pigeonhole_sort_option.x+150-pigeonhole_sort_text.get_width()//2,pigeonhole_sort_option.y+50-pigeonhole_sort_text.get_height()//2))

        pygame.draw.rect(self.window,color_list[1],cycle_sort_detail)
        pygame.draw.rect(self.window,color_list[0],cycle_sort_option)
        self.window.blit(cycle_sort_text,(cycle_sort_option.x+150-cycle_sort_text.get_width()//2,cycle_sort_option.y+50-cycle_sort_text.get_height()//2))

        pygame.draw.rect(self.window,color_list[1],back_detail)
        pygame.draw.rect(self.window,color_list[0],back_option)
        self.window.blit(back_text,(back_option.x+150-back_text.get_width()//2,back_option.y+50-back_text.get_height()//2))

        pygame.display.update()

    def change_length(self,input_values,exceeded_error):
        self.window.fill(white)

        if type(input_values) == list:
            input_values = font.render("".join(str(value) for value in input_values),1,color_list[2])
        else:
            input_values = font.render(str(input_values),1,color_list[2])

        pygame.draw.rect(self.window,color_list[2],change_len_detail)
        pygame.draw.rect(self.window,white,change_len)
        self.window.blit(change_len_text,(width//2-change_len_text.get_width()//2,height//2-change_len_text.get_height()//2))
        self.window.blit(input_values,(change_len.x+150-input_values.get_width()//2,change_len.y+50-input_values.get_height()//2))

        if exceeded_error is not None:
            self.window.blit(exceeded_error_message,(width//2-exceeded_error_message.get_width()//2,height//2-exceeded_error_message.get_height()//2-100))

        pygame.draw.rect(self.window,color_list[1],back_detail)
        pygame.draw.rect(self.window,color_list[0],back_option)
        self.window.blit(back_text,(back_option.x+150-back_text.get_width()//2,back_option.y+50-back_text.get_height()//2))

        pygame.display.update()