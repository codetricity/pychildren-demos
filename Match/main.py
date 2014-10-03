import pygame, sys, time, random
from pygame.locals import *

try:
    import android
except ImportError:
    android = None


class Square():
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color
        self.match = False
        self.viewable_trigger = False
        

class image_Square():
    def __init__(self, rect, fishes):
        self.rect = rect
        #self.color = color    
        #self.image = pygame.Surface((SQUARE_WIDTH, SQUARE_HEIGHT))
        #self.image.fill(color)
        self.image = fishes
        self.match = False
        self.viewable_trigger = False



def randomize_squares():
    block_list = []
    ## makes a list of the colors
    #colors_list = [WHITE, BLUE, RED, PURPLE, PINK, BLACK, SKY_BLUE, ORANGE]
    
    fishes_list = [brook_trout, brown_trout, carp, cooking, cutthroat_trout, duck, bass, tilapia]
    
    
    #total_colors = len(colors_list)
    total_fishes = len(fishes_list)
    
    #color_occurence_dict = {}
    
    fish_occurence_dict = {}
    
    #for color in colors_list:
    #    color_occurence_dict.update({color:0})
    
    for fish in fishes_list:
        fish_occurence_dict.update({fish:0})
    
    ## variable for defining the maximum number of occurences for the colors
    #max_color = 2
    
    max_fish = 2
    
    
        
    for y in range(0, GAME_SCREEN_HEIGHT, SQUARE_HEIGHT):
        for x in range(0, GAME_SCREEN_WIDTH, SQUARE_WIDTH):
            index_number = random.randrange(0, total_fishes)
            
            #color = colors_list[index_number]
            
            fishes = fishes_list[index_number]
            
            ## checks to see if the maximum number of occureneces has been passed
            if fish_occurence_dict[fishes] < max_fish:
                fish_occurence_dict[fishes] = fish_occurence_dict[fishes] + 1
                
            else:
                while fish_occurence_dict[fishes] >= max_fish:
                    index_number = random.randrange(0, total_fishes)
                    #color = colors_list[index_number]
                    
                    fishes = fishes_list[index_number]
                    
                    print("Generated NEW random color")
                fish_occurence_dict[fishes] = fish_occurence_dict[fishes] + 1
                
                
            
            rect = pygame.Rect(x, y, SQUARE_WIDTH, SQUARE_HEIGHT)
            
            square = image_Square(rect, fishes)
            
            block_list.append(square)
    return(block_list)
    



pygame.init()

GREEN = (0, 255, 0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (148, 2, 246)
PINK = (246, 2, 238)
SKY_BLUE = (2, 222, 246)
ORANGE = (255, 162, 0)

## Load the fish images
brook_trout = pygame.image.load("img/brook.jpg")
brown_trout = pygame.image.load("img/brown_trout.png")
carp = pygame.image.load("img/carp.jpg")
cooking = pygame.image.load("img/cooking.jpg")
cutthroat_trout = pygame.image.load("img/cutthroat.jpg")
bass = pygame.image.load("img/kong.jpg")
tilapia = pygame.image.load("img/tilapia.jpg")
duck = pygame.image.load("img/duck.JPG")

square_row = 4
square_height = 4

square_number = square_row * square_height

# SCREEN_WIDTH = 480
# SCREEN_HEIGHT = 320
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 480

GAME_SCREEN_HEIGHT = SCREEN_HEIGHT - 20
GAME_SCREEN_WIDTH = SCREEN_WIDTH

windowSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

SQUARE_WIDTH = GAME_SCREEN_WIDTH / square_row
SQUARE_HEIGHT = GAME_SCREEN_HEIGHT / square_height

## defining the squares borders
squares_list = randomize_squares()


            
count = 0




start_time = pygame.time.get_ticks()

clock = pygame.time.Clock()
FPS = 30

gameOn = True


if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

while True:
    if gameOn == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                            
            mouse_pos = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONDOWN:
                if count < 2:
                    count += 1
                else:
                        count = 0
                        
                for square in squares_list:
                    if square.rect.collidepoint(mouse_pos):
                        square.viewable_trigger = True
            
            
            
        #### Checks to see if the mouse clicks on any square and adds number to count
        #    for list_index in range(0, square_number):
        #        if event.type == MOUSEBUTTONUP and squares_list[list_index].rect.collidepoint(mouse_pos):
        #            squares_list[list_index].viewable_trigger = True
        #            # print("trigger {}".format(list_index))
        #            count = count + 1        
    
    ### if the trigger is activated draws blue square over green     
        if count == 1:
            #for list_index in range(0, square_number):
            #    if squares_list[list_index].viewable_trigger == True:
            #        ## randomizes the color of the squares
            #        color = squares_list[list_index].color
            #        pygame.draw.rect(windowSurface, color, squares_list[list_index].rect)
            #        print("color 1 = {}".format(color))
            #        ## saves the color of the square as first_selection
            #        first_selection = list_index
            for square in squares_list:
                if square.viewable_trigger == True:
                    #pygame.draw.rect(windowSurface, square.color, square.rect)
                    windowSurface.blit(square.image, square.rect)
                    first_selection = squares_list.index(square)
                
        elif count == 2:
           #for list_index in range(0, square_number):
           #     if squares_list[list_index].viewable_trigger == True:
           #         color2 = squares_list[list_index].color
           #         pygame.draw.rect(windowSurface, color2, squares_list[list_index].rect)
           #         
           #         if list_index != first_selection:
           #             second_selection = list_index
           
            for square in squares_list:
                if square.viewable_trigger == True:
                    #pygame.draw.rect(windowSurface, square.color, square.rect)
                    windowSurface.blit(square.image, square.rect)
                    
                    ## set up a temporary variable to avoid having the same square
                    current_index = squares_list.index(square)
                    if current_index != first_selection:
                        second_selection = current_index
                        
            
                        #color = squares_list[first_selection].color
                        #color2 = squares_list[second_selection].color
                        
                        fish = squares_list[first_selection].image
                        fish2 = squares_list[second_selection].image
                        
                        #if color == color2:
                        #    squares_list[first_selection].match = True
                        #    squares_list[second_selection].match = True
                            
                            
                        if fish == fish2:
                            squares_list[first_selection].match = True
                            squares_list[second_selection].match = True
                    
        
            #print(count)
    ### if count reaches 2 delay 2 sec then return count to zero    
        else:
            #pygame.time.wait(500)
            #windowSurface.fill(GREEN)
            for square in squares_list:
                if square.match == False:
                    pygame.draw.rect(windowSurface, GREEN, square.rect)
                
            for list_index in range(0, square_number):
                squares_list[list_index].viewable_trigger = False
            count = 0
    
        ## drawing statments for the grid
        for x in range(0, GAME_SCREEN_WIDTH, SQUARE_WIDTH):
            grid_1 = pygame.draw.line(windowSurface, BLACK, (x, 0), (x, GAME_SCREEN_HEIGHT), 3)
            for y in range(0, GAME_SCREEN_HEIGHT, SQUARE_HEIGHT):
                grid_2 = pygame.draw.line(windowSurface, BLACK, (0, y), (GAME_SCREEN_WIDTH, y), 3)
        
        
        
        ## setting up the fonts for the timer
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
         
        timerFont = pygame.font.Font("fonts/FreeSans.ttf", 20)
        timerText = timerFont.render("Time : " + str(elapsed_time) , True, RED)
        timerRect = pygame.Rect(10, 460, 60, 50)
        blank_rect = pygame.Rect(0, 460, 320, 50)
        
        
        ## Blitting the timer to the screen
        pygame.draw.rect(windowSurface, BLACK, blank_rect)
        windowSurface.blit(timerText, timerRect)
    
        ## detecting if the game is over
        viewable_squares = 0
        for square in squares_list:
            if square.match == True:
                viewable_squares += 1
            print(viewable_squares)
            if viewable_squares == 16:
                end_time = elapsed_time
                gameOn = False

        
    if gameOn == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        mouse_pos = pygame.mouse.get_pos()
        windowSurface.fill(BLACK)
        
        ## Setup end screen fonts
        timeFont = pygame.font.Font("fonts/FreeSans.ttf", 50)
        timeText = timeFont.render("Your time is  " , True, GREEN)
        timeRect = pygame.Rect(10, 25, 320, 160)
        
        timeText2 = timeFont.render(str(end_time) + " seconds", True, GREEN)
        timeRect2 = pygame.Rect(50, 75, 320, 100)
        
        play_again_text = timeFont.render("Play Again?", True, BLUE)
        play_again_rect = pygame.Rect(50, 160, 320, 160)
        
        yesFont = pygame.font.Font("fonts/FreeSans.ttf", 75)
        yesText = yesFont.render("YES", True, WHITE)
        yesRect = pygame.Rect(20, 260, 130, 100)
        
        noFont = pygame.font.Font("fonts/FreeSans.ttf", 75)
        noText = noFont.render("No...", True, ORANGE)
        noRect = pygame.Rect(160, 390, 130, 100)
        
        
        if noRect.collidepoint(mouse_pos):
            pygame.quit()
            sys.exit()
            
        if yesRect.collidepoint(mouse_pos):
            viewable_squares = 0
            count = 0
            fish_occurence_dict = {}
            start_time = pygame.time.get_ticks()
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
            print ("YES Button pressed")
            for square in squares_list:
                square.match = False
                square.viewable_trigger = False
            squares_list = randomize_squares()
            gameOn = True
            
        
        windowSurface.blit(timeText, timeRect)
        windowSurface.blit(timeText2, timeRect2)
        windowSurface.blit(play_again_text, play_again_rect)
        #pygame.draw.rect(windowSurface, WHITE, noRect)
        #pygame.draw.rect(windowSurface, PINK, yesRect)
        windowSurface.blit(noText, noRect)
        windowSurface.blit(yesText, yesRect)
    
    clock.tick(FPS)
    pygame.display.update()
    
    
                
            
    
        
        
            
    
    
