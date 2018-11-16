
#1 Init pygame
import pygame

#2 Create a screen with a size
    # - in order to use pygame we have to run the init method. This gets pygame ready to do something... goes and fetches the module. like turning on a car. don't car how the car is wired or works
pygame.init()
# - the screen size MUST be a tuple
screen_size = (512, 480)

    # we need to tell pygame to set the screen up and store it so pygame can use it. 
pygame_screen = pygame.display.set_mode(screen_size)

    #set the title of the window.
pygame.display.set_caption("Chasing the Goblin")

#===========VARIABLES FOR OUR GAME=====================
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
#3 Create the game loop (while 1)
    # -  create a boolean for whether the game should run or not.
game_on = True
while game_on:
    #- we are inside the main game loop, it will keep running as long as the condition is true.

#4 Add a quit event (requires sys)
    # - pygame comes with an event loop, just like js.
    for event in pygame.event.get(): #event is a variable that we made up. It could johndoe or whatever...
        # we need to give pygame a way out or python will freak out because it's inside an infinite loop.
        if(event.type == pygame.QUIT):  
            game_on = False


#5 Screen.fill (pass bg_color)
    # - we want to draw on the screen; we are using a built in function called "blit" which stands for BLOCK IMAGE TRANSFER
        # blit is a function and takes 2 arguements
        # 1. WHAT DO YOU WANT TO DRAW?
        # 2. WHERE DO YOU WANT TO DRAW AT?
        pygame_screen.blit(background_image,[0,0])
#6 Flip the screen and start over
        pygame.display.flip()