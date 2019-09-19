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

import pygame, sys
from pygame import *
import time

def move(x1,y1):         #just make the same kind of function but 4 decreasing
    global x
    global y
    global t
    global v
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
            y1=y1+5                       #original
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
            
        screen.blit(mouse_c, (x1,y1))
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
        
        if x1>t:                              #1
             x1=x1-6
        if y1>v:
             y1=y1-6
        if x1==t and y1>v:
            y1=y1-6
        if y1==v and x1>t:
            x1=x1-6
            
        screen.blit(frame, (x1,y1))
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
        screen.blit(frame2, (x1,y1))
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
            
        screen.blit(frame3, (x1,y1))
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
            
        screen.blit(frame4, (x1,y1))
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
            
        screen.blit(frame5, (x1,y1))
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
            
        screen.blit(frame6, (x1,y1))
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
            
        screen.blit(frame7, (x1,y1))
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
            
        screen.blit(frame8, (x1,y1))
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
            
        screen.blit(frame9, (x1,y1))
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
            
        screen.blit(frame10, (x1,y1))
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
            
        screen.blit(frame11, (x1,y1))
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
            
        screen.blit(frame12, (x1,y1))
        time.sleep(0.07)


        pygame.display.update()
        if x1==t and y1==v:
            map1(int(x1),int(y1))
            break






def moveleft(x1,y1):
    global x
    global y
    global t
    global v
    global frame
    global background
    global mouse_c
    global frame2
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
            y1=y1+5                       #original
        if x1==t and y1<v:
            y1=y1+5
        if y1==v and x1<t:        
            x1=x1+5
            
        #screen.blit(mouse_c, (x1,y1))
        #time.sleep(0.07)


        pygame.display.update()
        if x1==t and y1==v:
            map1(int(x1),int(y1))
            break
    
        

def map1(x1,y1):                          #make left vers of this
    pygame.init()   
    global screen
    screen=pygame.display.set_mode((900,900))

    pygame.display.set_caption("game")

    pygame.mouse.get_focused()

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
    
    
    global background
    background=pygame.image.load(fif).convert()
    global mouse_c    
    mouse_c=pygame.image.load(fra).convert_alpha()

    

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                global t
                global v
                t,v=pygame.mouse.get_pos()
                print (t)
                print (v)
                print("")
                if (x1,y1)==(t,v):
                    map1(x1,y1)
                    break
                if (x1,y1)<(t,v):
                    move(x1,y1)
                    break
                if (x1,y1)>(t,v):
                    pass
                    #moveleft(x1,y1)
                    #break

        screen.blit(background, (0,0))
        
        screen.blit(mouse_c, (x1,y1))
        
        
        pygame.display.update()


def leftvers(x1,y1):                          
    pygame.init()   
    global screen
    screen=pygame.display.set_mode((900,900))

    pygame.display.set_caption("game")

    pygame.mouse.get_focused()

    global background
    background=pygame.image.load(fif).convert()
    #global mouse_c    
    #mouse_c=pygame.image.load(fra).convert_alpha()

    #add left vers frames

    

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                global t
                global v
                t,v=pygame.mouse.get_pos()
                print (t)
                print (v)
                print("")
                if (x1,y1)==(t,v):
                    map1(x1,y1)
                    break
                if (x1,y1)<(t,v):
                    move(x1,y1)
                    break
                if (x1,y1)>(t,v):
                    pass
                    #moveleft(x1,y1)
                    #break

        screen.blit(background, (0,0))
        
        #screen.blit(mouse_c, (x1,y1))
        
        
        pygame.display.update()

map1(100,100)
