import pygame, sys

class PreGame: 

    def __init__(self):
        pygame.init()
        
        
        self.start_surface = pygame.Surface((480, 320))
        self.RED = (255, 0, 0)
        self.BLACK = (0,0,0)
        self.GREEN = (0, 255, 0)
        self.LIGHT_BLUE = (95, 255, 251)
        self.YELLOW = (255, 248, 95)
        self.BLUE = (95, 106, 255)
        self.LIGHT_GREEN = (181, 249, 133)
        self.WHITE = (255, 255, 255)
        
        self.next_rect = pygame.Rect(200, 250, 90, 50)
        self.next_rect_2 = pygame.Rect(350, 250, 90, 50)
        self.game_rect = pygame.Rect(200, 150, 95, 50)

######## the girl and the monster, stage C
        self.c_stage_Font = pygame.font.Font("fonts/ASTONISH.TTF", 80)
        self.girl = pygame.image.load("img/girl.png")
        self.girl_rect = pygame.Rect(300, 250, 50, 50)
        self.girl_instruction_rect = pygame.Rect(10, 230, 200, 50)
        self.girl_info_font = self.c_stage_Font.render("Save the Girl", True, self.WHITE)
        
        self.monster = pygame.image.load("img/monster.png")
        self.monster_rect = pygame.Rect(350, 90, 31, 32)
        self.monster_instruction_rect = pygame.Rect(10, 1, 200, 50)
        self.monster_instruction_rect_2 = pygame.Rect(80, 60, 200, 50)
        self.monster_info_font = self.c_stage_Font.render("Defeat 8 Waves of", True, self.YELLOW)
        self.monster_info_font_2 = self.c_stage_Font.render("Zombies", True, self.YELLOW)
        
    
### rectangles for text at beginning
        self.move_instruction_rect = pygame.Rect(10, 10, 100, 50)
        self.move_instruction_rect2 = pygame.Rect(50, 40, 100, 50)
        self.move_instruction_rect3 = pygame.Rect(10, 70, 100, 50)
        self.move_instruction_rect4 = pygame.Rect(80, 100, 100, 50)
        self.move_instruction_rect5 = pygame.Rect(10, 150, 100, 50)
        self.move_instruction_rect6 = pygame.Rect(10, 180, 100, 50)
        self.move_instruction_rect7 = pygame.Rect(10, 210, 100, 50)
       
##############
        self.fire_instruction_rect = pygame.Rect(10, 10, 100, 50)
        self.fire_instruction_rect2 = pygame.Rect(50, 40, 100, 50)
        self.fire_instruction_rect3 = pygame.Rect(10, 70, 100, 50)
        self.fire_instruction_rect4 = pygame.Rect(80, 100, 100, 50)
        self.fire_instruction_rect5 = pygame.Rect(10, 150, 100, 50)
        self.fire_instruction_rect6 = pygame.Rect(10, 180, 100, 50)
        self.fire_instruction_rect7 = pygame.Rect(10, 210, 100, 50)
        
        ## font setup
        self.info_Font = pygame.font.Font("fonts/animeace2_reg.ttf", 20)
        
        self.next_Font = pygame.font.Font("fonts/BLOODY.ttf", 40)
        self.next_image = self.next_Font.render("Next", True, self.BLACK)
        self.game_image = self.next_Font.render("Start", True, self.BLACK)
    
#### text for move / fire
        self.move_info_1 = self.info_Font.render("The yellow buttons on the left ", True, self.GREEN)
        self.move_info_2 = self.info_Font.render("moves character", True, self.GREEN)
        self.move_info_3 = self.info_Font.render("The clear yellow button stops ", True, self.YELLOW)
        self.move_info_4 = self.info_Font.render("your hero", True, self.YELLOW)
        self.move_info_5 = self.info_Font.render("Obstacles stop you from moving", True, self.LIGHT_BLUE)
        self.move_info_6 = self.info_Font.render("Tap the arrows repeately to", True, self.LIGHT_BLUE)
        self.move_info_7 = self.info_Font.render("force your way through them", True, self.LIGHT_BLUE)
        
############
        self.fire_info_1 = self.info_Font.render("The red buttons on the right ", True, self.RED)
        self.fire_info_2 = self.info_Font.render("shoot the bulllets", True, self.RED)
        self.fire_info_3 = self.info_Font.render("It takes many shots to kill the ", True, self.LIGHT_GREEN)
        self.fire_info_4 = self.info_Font.render("zummy or the zombie crab", True, self.LIGHT_GREEN )
        self.fire_info_5 = self.info_Font.render("The counter at the top of the ", True, self.BLUE)
        self.fire_info_6 = self.info_Font.render("screen shows your bullets", True, self.BLUE)
        self.fire_info_7 = self.info_Font.render("do NOT run out!", True, self.BLUE)
        
        self.start_level = "A"
    
    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        self.start_surface.fill(self.BLACK)
        if self.start_level == "A":        
            pygame.draw.rect(self.start_surface, self.GREEN, self.next_rect)
            #self.start_surface.blit(self.next_image, self.next_rect)
            self.start_surface.blit(self.next_image, self.next_rect)
            self.start_surface.blit(self.move_info_1, self.move_instruction_rect)
            self.start_surface.blit(self.move_info_2, self.move_instruction_rect2)
            self.start_surface.blit(self.move_info_3, self.move_instruction_rect3)
            self.start_surface.blit(self.move_info_4, self.move_instruction_rect4)
            self.start_surface.blit(self.move_info_5, self.move_instruction_rect5)
            self.start_surface.blit(self.move_info_6, self.move_instruction_rect6)
            self.start_surface.blit(self.move_info_7, self.move_instruction_rect7)
            
    
        elif self.start_level == "B":
            pygame.draw.rect(self.start_surface, self.LIGHT_GREEN, self.next_rect_2)
            self.start_surface.blit(self.next_image, self.next_rect_2)
            
            self.start_surface.blit(self.fire_info_1, self.fire_instruction_rect)
            self.start_surface.blit(self.fire_info_2, self.fire_instruction_rect2)
            self.start_surface.blit(self.fire_info_3, self.fire_instruction_rect3)
            self.start_surface.blit(self.fire_info_4, self.fire_instruction_rect4)
            self.start_surface.blit(self.fire_info_5, self.fire_instruction_rect5)
            self.start_surface.blit(self.fire_info_6, self.fire_instruction_rect6)
            self.start_surface.blit(self.fire_info_7, self.fire_instruction_rect7)
            
        elif self.start_level == "C":
            pygame.draw.rect(self.start_surface, self.RED, self.game_rect)
            self.start_surface.blit(self.game_image, self.game_rect)
            self.start_surface.blit(self.girl, self.girl_rect)
            pygame.draw.rect(self.start_surface, self.WHITE, self.monster_rect)
            self.start_surface.blit(self.monster, self.monster_rect)
            
            self.start_surface.blit(self.girl_info_font, self.girl_instruction_rect)
            self.start_surface.blit(self.monster_info_font, self.monster_instruction_rect)
            self.start_surface.blit(self.monster_info_font_2, self.monster_instruction_rect_2)
        
        return(self.start_surface)
    
    
    def checkLevel(self):
        level = 0
        
        mouse_pos = pygame.mouse.get_pos()
                
        if self.start_level == "C" and self.game_rect.collidepoint(mouse_pos):
            level = 1
        elif self.next_rect.collidepoint(mouse_pos) and self.start_level == "A":
            print("go to next screen.  Now at {}, {}".format(self.start_level, level))
            self.start_level = "B"
            level = 0
        elif self.next_rect_2.collidepoint(mouse_pos) and self.start_level == "B":
            self.start_level = "C"
            level = 0
            
        return(level)
        