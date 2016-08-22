######### import modules #########

import pygame
from random import randint
import time

pygame.init()


######### Initializing variables #########

elements= ["fire", "water", "earth", "air", "light"]
player_health = 260
enemy_health= 260
white= (255,255,255)
black = (0,0,0)
red= (220,0,0)
green= (0,220,0)

screen= pygame.display.set_mode((600,400))
pygame.display.set_caption('Alchemy Wars')

######### Load images #########

bg1= pygame.image.load('bg1.bmp')
f1= pygame.image.load('f1.bmp')


fire_orb_dim= pygame.image.load('fire.png')
fire_orb_dim.set_alpha(128)
water_orb_dim= pygame.image.load('water.png')
water_orb_dim.set_alpha(128)
earth_orb_dim= pygame.image.load('earth.png')
earth_orb_dim.set_alpha(128)
air_orb_dim= pygame.image.load('air.png')
air_orb_dim.set_alpha(128)
light_orb_dim= pygame.image.load('light.png')
light_orb_dim.set_alpha(128)

fire_orb= pygame.image.load('fire.png')
water_orb= pygame.image.load('water.png')
earth_orb= pygame.image.load('earth.png')
air_orb= pygame.image.load('air.png')
light_orb= pygame.image.load('light.png')


mud= pygame.image.load('mud.png')
heal= pygame.image.load('heal.png')
plasma= pygame.image.load('plasma.png')
thunder= pygame.image.load('thunder.png')
smoke= pygame.image.load('smoke.png')
ice= pygame.image.load('ice.jpg')
explosion= pygame.image.load('explosion.png')
sand= pygame.image.load('sand.jpg')
lava= pygame.image.load('lava.jpg')
steam= pygame.image.load('steam.png')
mist= pygame.image.load('mist.png')

bar= pygame.image.load('bar.png')
bar.set_alpha(128)

logo= pygame.image.load('logo.png')

######### Load sounds #########
pygame.mixer.music.load("battle.wav")
click_sound= pygame.mixer.Sound("click.wav")
fire_sound= pygame.mixer.Sound("fire.wav")      
water_sound= pygame.mixer.Sound("water.wav")      
earth_sound= pygame.mixer.Sound("earth.wav")      
air_sound= pygame.mixer.Sound("air.wav")      
light_sound= pygame.mixer.Sound("light.wav")      



######### Defining functions #########

def bg(background, floor):
    screen.blit(background, (0,0))
    screen.blit(floor, (0,330))
    screen.blit(logo, (400, 300))
    pygame.display.update()

def water(x,y):
    screen.blit(water_orb, (x, y))

def earth(x,y):
    screen.blit(earth_orb, (x, y))

def air(x,y):
    screen.blit(air_orb, (x, y))

def light(x,y):
    screen.blit(light_orb, (x, y))


def button(x,y,w,h,ic,ac, action = None):
    
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        screen.blit(ac, (x, y))
        if click[0] == 1 and action != None:
            pygame.mixer.Sound.play(click_sound)
            if action == "fire":
                msg_display('Player used fire')
                pygame.mixer.Sound.play(fire_sound)
                launch(fire_orb, 0, 150)
                print('FIRE')
                player_choice= "fire"
                enemy_choice = elements[randint(0,4)]
                enemy_launch(enemy_choice,600,150)
                reply(player_choice,enemy_choice)
            elif action == "water":
                msg_display('Player used water')
                pygame.mixer.Sound.play(water_sound)
                launch(water_orb, 0, 150)
                print("WATER")
                player_choice= "water"
                enemy_choice = elements[randint(0,4)]
                enemy_launch(enemy_choice,600,150)
                reply(player_choice,enemy_choice)
            elif action == "earth":
                msg_display('Player used earth')
                pygame.mixer.Sound.play(earth_sound)
                launch(earth_orb, 0, 150)
                print("EARTH")
                player_choice= "earth"
                enemy_choice = elements[randint(0,4)]
                enemy_launch(enemy_choice,600,150)
                reply(player_choice,enemy_choice)
            elif action == "air":
                msg_display('Player used air')
                pygame.mixer.Sound.play(air_sound)
                launch(air_orb, 0, 150)
                print("AIR")
                player_choice= "air"
                enemy_choice = elements[randint(0,4)]
                enemy_launch(enemy_choice,600,150)
                reply(player_choice,enemy_choice)
            elif action == "light":
                msg_display('Player used light')
                pygame.mixer.Sound.play(light_sound)
                launch(light_orb, 0, 150)
                print("LIGHT")
                player_choice= "light"
                enemy_choice = elements[randint(0,4)]
                enemy_launch(enemy_choice,600,150)
                reply(player_choice,enemy_choice)
           
    else:
        screen.blit(ic,(x, y))

######### function to define launch of Player's elements #########
        
def launch(name, x, y):   
    for x in range(600):
        
        screen.fill(white)
        screen.blit(logo, (400, 300))
        bg(bg1, f1)
        screen.blit(name, (x,y))
        x= x+0.8
        
        pygame.display.update()
######### function to define launch of Enem's elements #########
        
def enemy_launch(enemy_choice, x, y):
    
    msg_display("Enemy used " + str(enemy_choice))
    while x> -50:
        screen.fill(white)
        screen.blit(logo, (400, 300))
        bg(bg1, f1)
        if enemy_choice == "fire":
            
            pygame.mixer.Sound.play(fire_sound)
            screen.blit(fire_orb, (x,y))
        elif enemy_choice== "water":
            
            pygame.mixer.Sound.play(water_sound)
            screen.blit(water_orb, (x,y))
        elif enemy_choice== "earth":
            
            pygame.mixer.Sound.play(earth_sound)
            screen.blit(earth_orb, (x,y))
        elif enemy_choice== "air":
            
            pygame.mixer.Sound.play(air_sound)
            screen.blit(air_orb, (x,y))
        elif enemy_choice== "light":
            
            pygame.mixer.Sound.play(light_sound)
            screen.blit(light_orb, (x,y))

        x= x-2
        pygame.display.update() 
        
######### function to display messages on screen #########
        
def msg_display_res(text):
    if text == 'You WIN':
        screen.fill(green)
    elif text == 'You LOSE':
        screen.fill(red)
        
    largeText= pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect= text_objects_res(text, largeText)
    TextRect.center= ((600/2), (400/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    

def text_objects_res(text, font):
    textSurface= font.render(text, True, white)
    return textSurface, textSurface.get_rect()
    
def msg_points(text):
    screen.fill(white)
    screen.blit(logo, (400, 300))
    largeText= pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect= text_objects(text, largeText)
    TextRect.center= ((600/2), (400/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    
def msg_display(text):
    largeText= pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect= text_objects(text, largeText)
    TextRect.center= ((600/2), (400/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)

def text_objects(text, font):
    textSurface= font.render(text, True, black)
    return textSurface, textSurface.get_rect()

######### function that displays results of the outcome #########

def res(pic):
    x= 0
    while x <30:
        screen.fill(white)
        screen.blit(logo, (400, 300))
        screen.blit(pic, (0,0))
    
        pygame.display.update()
        x= x+1


######### function defining the logic of the game #########
        
def reply(player_choice, enemy_choice):
    global player_health
    global enemy_health
    
    print("Player used ",player_choice)
    print("Enemy used ",enemy_choice)
    
    if player_choice == "fire":
        if enemy_choice == "fire":
            print "No effect!"
            msg_display("NO EFFECT!")
            
        elif enemy_choice == "water":
            msg_display("It turned to STEAM ")
            res(steam)
            msg_points("Player lost 20 points")
            print "Player lose!"
            player_health= player_health-20
            
        elif enemy_choice == "earth":
            msg_display("It turned to LAVA")
            res(lava)
            msg_points("Enemy lost 40 points")
            print "Player Wins!"
            enemy_health= enemy_health-40
            
        elif enemy_choice == "air":
            msg_display("It turned to EXPLOSION")
            res(explosion)
            msg_points("Enemy lost 30 points")
            print "Player wins!"
            enemy_health= enemy_health -30
            
        elif enemy_choice == "light":
            msg_display("It turned to PLASMA")
            res(plasma)
            msg_points("Player lost 50 points")
            print "Player lose!"
            player_health = player_health-50
    
    if player_choice == "water":
        if enemy_choice == "water":
            msg_display("NO EFFECT!")
            print "No effect!"
        elif enemy_choice == "earth":
            msg_display("It turned to MUD")
            res(mud)
            msg_points("Player lost 20 points")
            print "Player lose!"
            player_health= player_health-10
            
        elif enemy_choice == "fire":
            print "Player Wins!"
            msg_display("It turned to STEAM")
            res(steam)
            msg_points("Enemy lost 10 points")
            enemy_health= enemy_health-10
            
        elif enemy_choice == "light":
            print "Player wins!"
            msg_display("It turned to HEAL")
            res(heal)
            msg_points("Player gain 30 points")
            player_health= player_health +30
            if player_health > 260:
                player_health = 260
            
        elif enemy_choice == "air":
            print "Player lose!"
            msg_display("It turned to ICE")
            res(ice)
            msg_points("Player lost 20 points")
            player_health = player_health-20


    if player_choice == "earth":
        if enemy_choice == "earth":
            print "No effect!"
            msg_display("NO EFFECT")
            
        elif enemy_choice == "fire":
            print "Player lose!"
            msg_display("It turned to LAVA")
            res(lava)
            msg_points("Player lost 40 points")
            
            player_health= player_health-40
            
        elif enemy_choice == "water":
            print "Player Wins!"
            msg_display("It turned to MUD")
            res(mud)
            msg_points("ENEMY lost 20 points")
            
            enemy_health= enemy_health-20
            
        elif enemy_choice == "air":
            print "Player wins!"
            msg_display("It turned to SAND")
            res(sand)
            msg_points("Enemy lost 10 points")
            
            enemy_health= enemy_health -10
            
        elif enemy_choice == "light":
            print "Player lose!"
            msg_display("EARTH absorbed LIGHT")
            msg_points("NO EFFECT")
            
            
    if player_choice == "air":
        if enemy_choice == "air":
            print "No effect!"
            msg_display("NO EFFECT")
            
        elif enemy_choice == "fire":
            print "Player lose!"
            msg_display("It turned to EXPLOSION")
            res(explosion)
            msg_points("Player lost 30 points")
            
            player_health= player_health-30
            
        elif enemy_choice == "water":
            print "Player Wins!"
            msg_display("It turned to MIST")
            res(mist)
            msg_points("Enemy lost 10 points")
            
            enemy_health= enemy_health-10
            
        elif enemy_choice == "light":
            print "Player wins!"
            msg_display("It turned to THUNDER")
            res(thunder)
            msg_points("Enemy lost 40 points")
            enemy_health= enemy_health -40
            
        elif enemy_choice == "earth":
            print "Player lose!"
            msg_display("It turned to SAND")
            res(sand)
            msg_points("Player lost 10 points")
            
            player_health = player_health-10

    if player_choice == "light":
        if enemy_choice == "light":
            print "No effect!"
            msg_display("NO EFFECT")
            
        elif enemy_choice == "water":
            print "Player lose!"
            msg_display("It turned to HEAL")
            res(heal)
            msg_points("Enemy gain 30 points")
            
            enemy_health= enemy_health + 30
            if enemy_health > 260:
                enemy_health = 260
        elif enemy_choice == "earth":
            print "Player Wins!"
            msg_display("EARTH absorbed LIGHT")
            msg_points("NO EFFECT")
            
        elif enemy_choice == "fire":
            print "Player wins!"
            msg_display("It turned to PLASMA")
            res(plasma)
            msg_points("Enemy lost 50 points")
            enemy_health= enemy_health -50
            
        elif enemy_choice == "air":
            print "Player lose!"
            msg_display("It turned to THUNDER")
            res(thunder)
            msg_points("Player lost 40 points")
            player_health = player_health-40

    
    return player_health, enemy_health
    
######### function to define the health of players #########

def health_bar(player_health, enemy_health):
    if player_health >50:
        player_health_color= green
    else:
        player_health_color= red

    if enemy_health > 50:
        enemy_health_color= green
    else:
        enemy_health_color= red

    

    if player_health <0 or player_health == 0:
        msg_display_res("You LOSE")
        gameExit = True
    elif enemy_health < 0 or enemy_health == 0:
        msg_display_res("You WIN")
        gameExit = True

    pygame.draw.rect(screen, player_health_color, (20,17, player_health,10))
    pygame.draw.rect(screen, enemy_health_color, (320,17, enemy_health,10))




computer = elements[randint(0,4)]

pygame.mixer.music.play(-1)
gameExit= False




######### MAIN GAME LOOP #########

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            
      
    screen.fill(white)
    
    
    screen.blit(bar, (10,10))
    screen.blit(bar, (310,10))
    health_bar(player_health, enemy_health)
    #x= x+0.7
    #earth(x,y)

    button(30, 320, 50, 50, fire_orb_dim, fire_orb, "fire")
    button(100, 320, 50, 50, water_orb_dim, water_orb, "water")
    button(170, 320, 50, 50, earth_orb_dim, earth_orb, "earth")
    button(240, 320, 50, 50, air_orb_dim, air_orb, "air")
    button(310, 320, 50, 50, light_orb_dim, light_orb, "light")

        
    
    screen.blit(logo, (400, 300))

    
    pygame.display.update()
    



pygame.quit()
quit()




