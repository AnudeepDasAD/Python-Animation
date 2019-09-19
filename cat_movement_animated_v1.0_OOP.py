fif="forest.jpg"
fra="frame1.png"
fra2="frame2.png"
fra3="frame3.png"
fra4="frame4.png"
fra5="frame5.png"
fra6="frame6.png"
fra7="frame7.png"
fra8="frame8.png"
fra9="frame9.png"
fra10="frame10.png"
fra11="frame11.png"
fra12="frame12.png"
fra13="frame13.png"

lef1="left1.png"
lef2="left2.png"
lef3="left3.png"
lef4="left4.png"
lef5="left5.png"
lef6="left6.png"
lef7="left7.png"
lef8="left8.png"
lef9="left9.png"
lef10="left10.png"
lef11="left11.png"
lef12="left12.png"
lef13="left13.png"


import pygame, sys
from pygame import *
import time


class Sprite:
    def __init__(self,image,x,y,t):
        self.x=x
        self.y=y
        self.image=image
        if t==1:
            x-=image.get_width()/4*3
            y-=image.get_height()/4*3
        if t==2:
            x-=image.get_width()/4
            y-=image.get_height()/4*3

        screen.blit(image, (x,y))
        return


def map1(x1,y1):                          #make left vers of this
    pygame.init()   
    global screen
    screen=pygame.display.set_mode((900,900))

    pygame.display.set_caption("game")

    pygame.mouse.get_focused()
    
    
    global background
    background=pygame.image.load(fif).convert()
    global mouse_c    
    mouse_c=pygame.image.load(fra).convert_alpha()

    #main=Sprite(mouse_c,x1,y1)
    

    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                right(x1,y1)

        screen.blit(background, (0,0))

        global main
        main=Sprite(mouse_c,x1,y1,1) 

        
        #screen.blit(mouse_c, (x1,y1))


        
        pygame.display.update()


def right(x1,y1):
    global frame
    frame=pygame.image.load(fra2).convert_alpha()
    global frame2
    frame2=pygame.image.load(fra3).convert_alpha()
    global frame3
    frame3=pygame.image.load(fra4).convert_alpha()
    global frame4
    frame4=pygame.image.load(fra5).convert_alpha()
    global frame5
    frame5=pygame.image.load(fra6).convert_alpha()
    global frame6
    frame6=pygame.image.load(fra7).convert_alpha()
    global frame7
    frame7=pygame.image.load(fra8).convert_alpha()
    global frame8
    frame8=pygame.image.load(fra9).convert_alpha()
    global frame9
    frame9=pygame.image.load(fra10).convert_alpha()
    global frame10
    frame10=pygame.image.load(fra11).convert_alpha()
    global frame11
    frame11=pygame.image.load(fra12).convert_alpha()
    global frame12
    frame12=pygame.image.load(fra13).convert_alpha()

    global left1    
    left1=pygame.image.load(lef1).convert_alpha()
    global left2
    left2=pygame.image.load(lef2).convert_alpha()
    global left3
    left3=pygame.image.load(lef3).convert_alpha()
    global left4
    left4=pygame.image.load(lef4).convert_alpha()
    global left5
    left5=pygame.image.load(lef5).convert_alpha()
    global left6
    left6=pygame.image.load(lef6).convert_alpha()
    global left7
    left7=pygame.image.load(lef7).convert_alpha()
    global left8
    left8=pygame.image.load(lef8).convert_alpha()
    global left9
    left9=pygame.image.load(lef9).convert_alpha()
    global left10
    left10=pygame.image.load(lef10).convert_alpha()
    global left11
    left11=pygame.image.load(lef11).convert_alpha()
    global left12
    left12=pygame.image.load(lef12).convert_alpha()
    global left13
    left13=pygame.image.load(lef13).convert_alpha()
    
    global t
    global v
    t,v=pygame.mouse.get_pos()
    print (t)
    print (v)
    print("")
    if (x1,y1)==(t,v):
        map1(x1,y1)       
    if (x1,y1)<(t,v):
        move(x1,y1)       
    if (x1,y1)>(t,v):
        moveleft(x1,y1)  #edit, make in2 function
        
    

def move(x1,y1):         #just make the same kind of function but 4 decreasing
    global x
    global y
    global t                   
    global v
    global main
    global frame
    global background
    global mouse_c
    global frame2
    while (x1,y1)!=(t,v):
        global screen
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:
            x1=x1+5
        
        if x1>t:                              #1
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram=Sprite(frame,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                   
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:
            x1=x1+5                        #2

        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
        fram2=Sprite(frame2,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:               #3
            x1=x1+5
        
        if x1>t:
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram3=Sprite(frame3,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:                   #4
            x1=x1+5
        
        if x1>t:
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram4=Sprite(frame4,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:                #5
            x1=x1+5
        
        if x1>t:
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram5=Sprite(frame5,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:          #6
            x1=x1+5
        
        if x1>t:
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram6=Sprite(frame6,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:
            x1=x1+5
        
        if x1>t:
             x1=x1-6                         #7
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram7=Sprite(frame7,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5                       #8
        if y1==v and x1<t:
            x1=x1+5
        
        if x1>t:
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram8=Sprite(frame8,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5                       #9
        if y1==v and x1<t:
            x1=x1+5
        
        if x1>t:
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram9=Sprite(frame9,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5                          #10
        if y1==v and x1<t:
            x1=x1+5
        
        if x1>t:
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram10=Sprite(frame10,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:
            x1=x1+5                       #11
        
        if x1>t:
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram11=Sprite(frame11,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:                              
            x1=x1+5
        if y1<v:
            y1=y1+5
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:
            x1=x1+5                       #12
        
        if x1>t:
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        fram12=Sprite(frame12,x1,y1,1)
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       #original, new area 
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6

        main=Sprite(mouse_c,x1,y1,1)   
        #screen.blit(mouse_c, (x1,y1))
        time.sleep(0.07)


        pygame.display.update()
        if x1==t and y1==v:
            map1(int(x1),int(y1))
            break
    
        

def leftvers(x1,y1):                          
    pygame.init()   
    global screen
    screen=pygame.display.set_mode((900,900))

    pygame.display.set_caption("game")

    pygame.mouse.get_focused()

    global background
    background=pygame.image.load(fif).convert()
    global left1    
    left1=pygame.image.load(lef1).convert_alpha()
    

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                right(x1,y1)

        screen.blit(background, (0,0))
        
        global main2
        main2=Sprite(left1,x1,y1,2)
        
        
        pygame.display.update()




def moveleft(x1,y1):
    global x
    global y
    global t
    global v
    global left1
    global background
    global mouse_c
    global main
    while (x1,y1)!=(t,v):
        global screen
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le2=Sprite(left2,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le3=Sprite(left3,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le4=Sprite(left4,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le5=Sprite(left5,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le6=Sprite(left6,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le7=Sprite(left7,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le8=Sprite(left8,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le9=Sprite(left9,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le10=Sprite(left10,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le11=Sprite(left11,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le12=Sprite(left12,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        le13=Sprite(left13,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        screen.blit(background, (0,0))
        if x1>t:
            x1=x1-6
        if y1>v:
            y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        if x1<t:
            x1=x1+5
        if y1<v:
            y1=y1+5                       
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        main2=Sprite(left1,x1,y1,2)        
        time.sleep(0.07)


        pygame.display.update()
        if x1==t and y1==v:
            leftvers(int(x1),int(y1))
            break

map1(100,100)
