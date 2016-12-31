import pygame
import time
import random

pygame.init()
breadth = 800
length = 600

gameDisplay = pygame.display.set_mode((breadth,length))


pygame.display.set_caption("flappy bird")
crashtree=pygame.mixer.Sound("crashtree.wav")
pygame.mixer.music.load("bird.wav")
bird=pygame.image.load("bird.png")
backgrd=pygame.image.load("landscape.png")
white = (255,255,255)
black = (0,0,0)


red = (200,0,0)
bright_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (0,255,0)
bright_green = (0,200,0)
light_blue=(0,0,200)

clock = pygame.time.Clock()
def back(x,y):
    gameDisplay.blit(backgrd,(x,y))
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def button(msg,x,y,b,l,ic,ac,action=None):
            mouse = pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()

            #print(mouse)

            if x+b > mouse[0] > x and y+l > mouse[1] > y:
                pygame.draw.rect(gameDisplay, ac,(x,y,b,l))
                if click[0]==1 and action!=None:
                    if action=="play":
                        game_loop()
                    #if action==unpause:
                        #unpause()
                    if action=="quit":
                        pygame.quit()
                        quit()
            else:
                pygame.draw.rect(gameDisplay, ic,(x,y,b,l))

            smalltext=pygame.font.SysFont("calibri",20)
            TextSurf,TextRect=text_objects(msg,smalltext)
            TextRect.center=((x+b/2),(y+l/2))
            gameDisplay.blit(TextSurf, TextRect)
    

def game_intro():

        intro = True

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            gameDisplay.fill(white)
            back(0,0)
            largeText = pygame.font.SysFont('calibri',80)
            TextSurf, TextRect = text_objects("Flappy Bird", largeText)
            TextRect.center = ((breadth/2),(length/2))
            gameDisplay.blit(TextSurf, TextRect)


            mouse = pygame.mouse.get_pos()
            

            #print(mouse)

            
            button("start",150,450,100,50,green,bright_green,"play")
            button("quit",550,450,100,50,red,bright_red,"quit")
            
            pygame.display.update()
            clock.tick(15)

def thing_gone(cal):
    font=pygame.font.SysFont("calibri",40)
    text=font.render("score:"+str(cal),True,black)
    gameDisplay.blit(text,(0,0))
    

def crash():
        
        

       
        intro = True

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            #gameDisplay.fill(white)
            pygame.mixer.Sound.play(crashtree)
            pygame.mixer.music.stop()
            largeText = pygame.font.SysFont('calibri',100)
            TextSurf, TextRect = text_objects("you crashed", largeText)
            TextRect.center = (400,300)
            gameDisplay.blit(TextSurf, TextRect)


            mouse = pygame.mouse.get_pos()
            

            #print(mouse)

            
            button("play again",150,450,100,50,green,bright_green,"play")
            button("quit",550,450,100,50,red,bright_red,"quit")
            
            pygame.display.update()
            clock.tick(15)
def pillar1(x,y):
    pygame.draw.rect(gameDisplay,green,(x,0,60,y))
    pygame.draw.rect(gameDisplay,green,(x+300,0,60,y+60))
def pillar2(pillar2x,pillar2y,y):
       pygame.draw.rect(gameDisplay,green,(pillar2x,y,60,pillar2y))
       pygame.draw.rect(gameDisplay,green,(pillar2x+600,y-60,60,pillar2y))
       pygame.draw.rect(gameDisplay,green,(pillar2x+400,y-80,60,pillar2y))
       
def game_loop():
    landx=0
    landy=0
    breadth=800
    length=600
    birdx=100
    birdy=350
    dodged=0
    yin=0
    y=600-random.randint(0.1*length,0.4*length)
    pygame.mixer.music.play(-1)
    breadth = 800
    length = 600
    pillar2x=820
    pillar2y=600-random.randint(0.1*length,0.4*length)
    pillar1x=820
    pillar1y=random.randint(0.1*length,0.3*length)
    
    end = False

    while not end:
        for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        yin=-4
                    if event.key==pygame.K_DOWN:
                        yin=4
                if event.type==pygame.KEYUP:
                    #yin+=4
                    yin=5
                    
        pillar1x-=7
        pillar2x-=7
        gameDisplay.fill(white)
        back(landx,landy)
        pillar1(pillar1x,pillar1y)
        pillar2(pillar2x,pillar2y,y)
            
        thing_gone(dodged)   
        birdy+=yin
        gameDisplay.blit(bird,(birdx,birdy))
        
      
        if pillar1x+360<0:
             pillar1x=820
             pillar1y=random.randrange(0.1*length,0.45*length)
             dodged+=2
        if pillar2x+660<0:
             pillar2x=820
             pillar2y=600-random.randrange(0.1*length,0.3*length)
        if birdy>540:
            crash()
        
        if pillar1y>birdy>0 or pillar1y>birdy+50>0 :
            if pillar1x+60>birdx>pillar1x or pillar1x + 60>birdx+50>pillar1x:
                   crah()
        if pillar1y+55>birdy>0 or pillar1y+55>birdy+50>0 :
            if pillar1x+420>birdx>pillar1x+360 or pillar1x + 420>birdx+50>pillar1x+360:
                    crash()
        if pillar2y>birdy>y or pillar2y>birdy+60>y :
            if pillar2x+60>birdx>pillar2x or pillar2x + 60>birdx+60>pillar2x:
                    crash()
        if pillar2y>birdy>y-60 or pillar2y>birdy+60>y-60 :
           if pillar2x+720>birdx>pillar2x+660 or pillar2x + 720>birdx+60>pillar2x+660:
                    crash()
        if pillar2y>birdy>y-80 or pillar2y>birdy+60>y-80 :
           if pillar2x+520>birdx>pillar2x+460 or pillar2x + 520>birdx+60>pillar2x+460:
                    crash()
        
        pygame.display.update()
        clock.tick(60)
game_intro()      
game_loop()
pygame.quit()
quit()

