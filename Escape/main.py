import pygame, sys, random
from pygame.locals import *

try:
    import android
except ImportError:
    android = None

pygame.init()

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/pavement.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = 320
    def update(self):
        self.rect.left -= 8
    
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = 320 - 26
        self.rect.left = 1080
    def update(self):
        self.rect.left -= 8
        
class Bug(pygame.sprite.Sprite):
    def __init__(self, name_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = 600
        self.rect.top = 200
    def update(self):
        self.rect.left = self.rect.left - 6
    
        
def load_pavement(pavement):
    pavement.empty()
    for x in range(0, 544, 32):
        ground = Ground()
        ground.rect.left = x
        pavement.add(ground)
    return(pavement)
    
    

windowSurface = pygame.display.set_mode((480, 320), 0, 32)

## Variables
background_img = pygame.image.load("img/ruins3.jpg").convert_alpha()
small_surface = pygame.Surface((480, 320))
bg_x = 0
background_width = background_img.get_width()


jump_rect = pygame.Rect(400, 280, 120, 120)
jump_number = 0

jump_arrow = pygame.image.load("img/jump_arrow2.png").convert_alpha()
jump_arrow_rect = jump_arrow.get_rect(top = 75, right = 465)

level = 0

RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (80, 211, 238)
PINK = (238, 80, 206)
MOSS_GREEN = (34, 227, 98)


## Load the images for the animals
animal_rect = pygame.Rect(50, 50, 175, 130)

barnacle = pygame.image.load("img/barnacle2.png").convert_alpha()
slug = pygame.image.load("img/Slug.png").convert_alpha()
sloth = pygame.image.load("img/Sloth.png").convert_alpha()
turtle = pygame.image.load("img/turtle.png").convert_alpha()
hippo = pygame.image.load("img/Hippo.png").convert_alpha()
kaiyote = pygame.image.load("img/Kaiyote.png").convert_alpha()


## rectangles for end screen
explanation_font = pygame.font.Font("animeace2_reg.ttf", 8)
rank_font = pygame.font.Font("animeace2_reg.ttf", 12)

barnacle_text = explanation_font.render("Barnacle = 200m or less", True, PINK).convert_alpha()
barnacle_rect = barnacle_text.get_rect(left = 260, top = 215)
slug_text = explanation_font.render("Slug = 400m or less", True, PINK).convert_alpha()
slug_rect = slug_text.get_rect(left = 260, top = 230)
sloth_text = explanation_font.render("Sloth = 600m or less", True, PINK).convert_alpha()
sloth_rect = sloth_text.get_rect(left = 260, top = 245)
turtle_text = explanation_font.render("Turtle = 800m or less", True, PINK).convert_alpha()
turtle_rect = turtle_text.get_rect(left = 260, top = 260)
hippo_text = explanation_font.render("Hippo = 1000m or less", True, PINK).convert_alpha()
hippo_rect = hippo_text.get_rect(left = 260, top = 275)
kaiyote_text = explanation_font.render("Kaiyote = 1000m or more", True, PINK).convert_alpha()
kaiyote_rect = kaiyote_text.get_rect(left = 260, top = 290)

rank = "blank"

## Variables for distance to run
run_font = pygame.font.Font("animeace2_reg.ttf", 24)
check_font = pygame.font.Font("animeace2_reg.ttf", 48)



##initialize fonts for start screen
baseFont = pygame.font.Font("basefont.ttf", 72)
startText = baseFont.render("START", True, GREEN).convert_alpha()
startRect = startText.get_rect(left = 130, top = 110)


## rectangles for the Start scree
start_text1 = rank_font.render("You are the last remaining survivor of an ancient clan:" , True, SKY_BLUE).convert_alpha()
start_rect1 = start_text1.get_rect(left = 10, top = 10)
start_text2 = rank_font.render("The Kaiyote's. Many are trying to extinguish you, wiping" , True, SKY_BLUE)
start_rect2 = start_text1.get_rect(left = 10, top = 30)
start_text3 = rank_font.render("out the clan. The descendants of Kaiyote are known for " , True, SKY_BLUE)
start_rect3 = start_text1.get_rect(left = 10, top = 50)
start_text4 = rank_font.render("their running ability. Now, your strength will be put to " , True, SKY_BLUE)
start_rect4 = start_text1.get_rect(left = 10, top = 70)
start_text5 = rank_font.render("the test." , True, SKY_BLUE)
start_rect5 = start_text1.get_rect(left = 10, top = 90)
start_text6 = rank_font.render("Escape your enemies and survive to see another day." , True, SKY_BLUE)
start_rect6 = start_text1.get_rect(left = 10, top = 110)

direction_text1 = run_font.render("Directions:", True, MOSS_GREEN)
direction_rect1 = direction_text1.get_rect(left = 10, top = 205)
direction_text2 = rank_font.render("1) Tap yellow up arrow to jump once", True, MOSS_GREEN)
direction_rect2 = direction_text1.get_rect(left = 10, top = 235)
direction_text3 = rank_font.render("2) Tap arrow twice to double jump", True, MOSS_GREEN)
direction_rect3 = direction_text1.get_rect(left = 10, top = 255)
direction_text4 = rank_font.render("Warning: After completing a double jump, your character", True, MOSS_GREEN)
direction_rect4 = direction_text1.get_rect(left = 10, top = 275)
direction_text5 = rank_font.render("will be rendered helpless until he touches ground.", True, MOSS_GREEN)
direction_rect5 = direction_text1.get_rect(left = 10, top = 295)



## create rectangles/text for end screen
gameOver_text = baseFont.render("GAME OVER", True, RED).convert_alpha()
gameOver_rect = gameOver_text.get_rect(left = 5, top = 10)

playAgain_text = baseFont.render("Play Again?", True, GREEN).convert_alpha()
playAgain_rect = playAgain_text.get_rect(left = 5, top = 80)

bloodyFont = pygame.font.Font("BLOODY.ttf", 78)
astonishFont = pygame.font.Font("ASTONISH.TTF", 78)

yes_text = astonishFont.render("YES", True, GREEN).convert_alpha()
yes_rect = yes_text.get_rect(left = 30, top = 200)

no_text = bloodyFont.render("NO", True, RED).convert_alpha()
no_rect = no_text.get_rect(left = 160, top = 200)


## create font for the win screen
win_text = baseFont.render("YOU WON!", True, PINK).convert_alpha()
win_rect = win_text.get_rect(left = 75, top = 80)


## Player
player_list = []

player_sheet = pygame.image.load("img/walksheet.png").convert_alpha()
sheet_width = player_sheet.get_width()
sheet_height = player_sheet.get_height()
player_width = sheet_width / 6
player_height = sheet_height / 5

## runs the animation for the runner
for y in range(0, sheet_height, player_height):
    for x in range(0, sheet_width, player_width):
    
        player = pygame.Surface((player_width, player_height))
        player.blit(player_sheet, (0, 0), (x, y, player_width, player_height))
        color_key = player.get_at((0, 0))
        player.set_colorkey(color_key)
        small_player = pygame.transform.scale(player, (int(player_width / 2.5), int(player_height / 2.5)))
        
        player_list.append(small_player)

player_position = 0

pavement = pygame.sprite.Group()
ground_counter = 32
pavement = load_pavement(pavement)

## instantiate the obstacle
obstacle_group = pygame.sprite.Group()
log = Obstacle("img/log.png")
cactus = Obstacle("img/cactus.png")
pillar = Obstacle("img/pillar.png")
obstacle_group.add(log)
obstacle_group.add(cactus)
spawn_delay = 15

## instantiate the bug
bug_group = pygame.sprite.Group()
bug_counter = 200

##jump direction
jump = "stop"
player_rect = pygame.Rect(150, 185, small_player.get_width(), small_player.get_height())

## Game Clock
Clock = pygame.time.Clock()
FPS = 40

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)


while True:
    # event handler
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if level == 0:
                if startRect.collidepoint(mouse_pos):
                    level = 1 
            elif level == 1:
                if jump_arrow_rect.collidepoint(mouse_pos):
                    if jump_number <= 1:
                        jump = "up"
                        jump_number +=1
                        #print ("Jumper Number %d" % jump_number)
                        
            if level == 100:
                jump = "stop"
                jump_number = 0
                player_rect.top = 185
                if yes_rect.collidepoint(mouse_pos):
                    level = 1
                    obstacle_group.empty()
                    bug_group.empty()
                    bg_x = 0
                    
                if no_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
            
                    
            if level == 1000:
                pass
                    
    # end event handler        
    
    ## Check for the end of game
    if bg_x >= background_width - 480:
    #print(bg_x)
    #if bg_x >= 200:
        level = 1000
    
    if level == 1:
        small_surface.blit(background_img, (0,0), (bg_x, 0, 480, 320))
        bg_x = bg_x + 1
        windowSurface.blit(small_surface, (0, 0))
        
        ## Draws the animals onto the sceen
        if bg_x <= 200 and bg_x >= 0:
            windowSurface.blit(barnacle, animal_rect)
        if bg_x <= 400 and bg_x >= 201:
            windowSurface.blit(slug, animal_rect)
        if bg_x <= 600 and bg_x >= 401:
            windowSurface.blit(sloth, animal_rect)
        if bg_x <= 800 and bg_x >= 601:
            windowSurface.blit(turtle, animal_rect)
        if bg_x <= 1000 and bg_x >= 801:
            windowSurface.blit(hippo, animal_rect)
        if bg_x >= 1001:
            windowSurface.blit(kaiyote, animal_rect)
        
        
        ## Jumping statement for player
    
        if jump_number == 1:
            if player_rect.top <= 60:
                jump = "down"
        elif jump_number == 2:
            if player_rect.top <= 5:
                jump = "down"
        
        
        if player_rect.top >= 185 and jump == "down":
            jump = "stop"
            jump_number = 0
            
        
        if jump == "up" and jump_number <= 2:
            player_rect.top = player_rect.top - 8
        
        if jump == "down":
            player_rect.top = player_rect.top + 8
     
    
        
        
        if ground_counter > 0:
            pavement.update()
            ground_counter -= 8
        else:
            pavement = load_pavement(pavement)
            ground_counter = 32
        
        for obstacle in obstacle_group:
            if obstacle.rect.right < 0:
                obstacle_group.remove(obstacle)
        
        pavement.draw(windowSurface)
        
        ## collision detection for player/obstacle
        for obstacle in obstacle_group:
            innerPlayer_rect = player_rect.inflate(-30, -10)
            inner_obstacle_rect = obstacle.rect.inflate(-10, -10)
            if inner_obstacle_rect.colliderect(innerPlayer_rect):
                #print("COLLIDE")
                #print(innerPlayer_rect, inner_obstacle_rect)
                windowSurface.fill((255, 0, 0))
                level = 100
        
        ## collistion detection for player/obstacle
        for bug in bug_group:
            innerPlayer_rect = player_rect.inflate(-50, -20)
            inner_bug_rect = bug.rect.inflate(-10, -10)
            if inner_bug_rect.colliderect(innerPlayer_rect):
                windowSurface.fill((0, 255, 0))
                level = 100
        
        ## spawn delay for obstacles
        if spawn_delay > 0:
            spawn_delay = spawn_delay - 1
        else:
            plant = random.randrange(1, 5)
            if plant == 1:        
                obstacle_group.add(Obstacle("img/log.png"))
            if plant == 2:
                obstacle_group.add(Obstacle("img/cactus.png"))
            if plant == 3:
                obstacle_group.add(Obstacle("img/pillar.png"))
            if plant == 4:
                bug_group.add(Bug("img/wasp.png"))
            spawn_delay = random.randrange(50, 100, 5)
        
        
        
        ## blit the obstacles onto the screen
        obstacle_group.update()
        obstacle_group.draw(windowSurface)
        
        ## blit the wasp onto the screen
        bug_group.update()
        
      ## removing the wasp after it goes off the screen
        for bug in bug_group:
            if bug.rect.right <= 0:
                bug_group.remove(bug)
        bug_group.draw(windowSurface)
        
        windowSurface.blit(jump_arrow, jump_arrow_rect)
        
        ## blit the meters to go onto the screen
        distance_end = background_width - 480 - bg_x
        check_text = check_font.render("Youre HALFWAY ", True, GREEN).convert_alpha()
        check_rect = check_text.get_rect(left = 15, top = 50)
        check_text2 = check_font.render("THERE!!", True, GREEN).convert_alpha()
        check_rect2 = check_text2.get_rect(left = 100, top = 100)
        if bg_x > distance_end / 2 + 100 and bg_x < distance_end / 2 + 200:
            windowSurface.blit(check_text, check_rect)
            windowSurface.blit(check_text2, check_rect2)            
        
        run_text = run_font.render("The finish is %i " % distance_end, True, BLUE).convert_alpha()
        run_rect = run_text.get_rect(left = 15, top = 15)
        run_text2 = run_font.render("meters away", True, BLUE).convert_alpha()
        run_rect2 = run_text2.get_rect(left = 290, top = 15)
        
        windowSurface.blit(run_text, run_rect)
        windowSurface.blit(run_text2, run_rect2)
        
        
        ## blit the player
        if player_position < len(player_list):
            player_position = player_position + 1
        else:
            player_position = 0
        windowSurface.blit(player_list[player_position - 1], player_rect)
    
    
    
    if level == 0:
        windowSurface.fill(RED)
        ## Blit the start text onto the screen
        windowSurface.blit(start_text1, start_rect1)
        windowSurface.blit(start_text2, start_rect2)
        windowSurface.blit(start_text3, start_rect3)
        windowSurface.blit(start_text4, start_rect4)
        windowSurface.blit(start_text5, start_rect5)
        windowSurface.blit(start_text6, start_rect6)
        
        windowSurface.blit(direction_text1, direction_rect1)
        windowSurface.blit(direction_text2, direction_rect2)
        windowSurface.blit(direction_text3, direction_rect3)
        windowSurface.blit(direction_text4, direction_rect4)
        windowSurface.blit(direction_text5, direction_rect5)
        #pygame.draw.rect(windowSurface, YELLOW, startRect)
        windowSurface.blit(startText, startRect)
        
    if level == 100:
        windowSurface.fill(BLUE)
        windowSurface.blit(gameOver_text, gameOver_rect)
        windowSurface.blit(playAgain_text, playAgain_rect)
        
        windowSurface.blit(yes_text, yes_rect)
        windowSurface.blit(no_text, no_rect)
        
        distance_font = pygame.font.Font("animeace2_reg.ttf", 16)
        distance_text = distance_font.render("You ran %i meters" % bg_x  , True, GREEN).convert_alpha()
        distance_rect = distance_text.get_rect(left = 260, top = 180)
        windowSurface.blit(distance_text, distance_rect)
        
        if bg_x <= 200 and bg_x >= 0:
            rank = "barnacle"
        if bg_x <= 400 and bg_x >= 201:
            rank = "slug"
        if bg_x <= 600 and bg_x >= 401:
            rank = "sloth"
        if bg_x <= 800 and bg_x >= 601:
            rank = "turtle"
        if bg_x <= 1000 and bg_x >= 801:
            rank = "hippo"
        if bg_x >= 1001:
            rank = "kaiyote"
            
            
            
        rank_text = rank_font.render("Your rank is %s " % rank, True, PINK)
        rank_rect = rank_text.get_rect(left = 260, top = 200)
        windowSurface.blit(rank_text, rank_rect)
        windowSurface.blit(barnacle_text, barnacle_rect)
        windowSurface.blit(slug_text, slug_rect)
        windowSurface.blit(sloth_text, sloth_rect)
        windowSurface.blit(turtle_text, turtle_rect)
        windowSurface.blit(hippo_text, hippo_rect)
        windowSurface.blit(kaiyote_text, kaiyote_rect)
        print(rank)
        #if rank == "barnacle":
        #    print("barnacle")
        #if rank == "slug":
        #    print("slug")
        #if rank == "sloth":
        #    print("sloth")
        #if rank == "turtle":
        #    print("turtle")
        #if rank == "hippo":
        #    print("hippo")
        #if rank == "kaiyote":
        #    print("kaiyote")
            
            
        
    
    if level == 1000:
        windowSurface.fill(SKY_BLUE)
        windowSurface.blit(win_text, win_rect)
        rank_text = run_font.render("You are a KaiYote", True, PINK)
        rank_rect = rank_text.get_rect(left = 10, top = 200)
        windowSurface.blit(rank_text, rank_rect)
    
    Clock.tick(FPS)
    pygame.display.update()