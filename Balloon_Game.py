#Set volume to 10 on laptop

import pygame
from pygame.locals import *
pygame.init()
import time
import random
       
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Balloon Game")
balloon = pygame.image.load("balloon.png")
oof = pygame.image.load("pop.png")
popSound = pygame.mixer.music.load("oof.mp3")
pygame.mixer.music.set_volume(500)

stuff = []     
end = 0
new = 0
move = 0
press = " "
poof = 0
score = 0
wrong = 0
letters = []
wx = 0

back = pygame.image.load("rainbow.jpg")
lose = pygame.image.load("devil.jpg")
yay = pygame.image.load("angel.png")

plzwork = "Score: 0"
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   

def show_text(msg,x,y,color):     
      fontobj=pygame.font.SysFont("freeans",60)
      msgobj=fontobj.render(msg,False,color)
      screen.blit(msgobj,(x,y))

def stupidpython(msg,x,y,color):     
      fontobj=pygame.font.SysFont("freeans",30)
      msgobj=fontobj.render(msg,False,color)
      screen.blit(msgobj,(x,y))

def fail():    
      plzwork = " "
      screen.fill((0,0,0))

      while True:            
            screen.fill((0,0,0))
            screen.blit(lose,(0,0))
            wx = 0
            wy = 0
            
            for y in range(0,20,1):                  
                  for x in range(0,5,1):                        
                        stupidpython("YOU LOSE",wx,wy,(0,0,0))
                        time.sleep(0.5)
                        wx = wx + 110
                        pygame.display.update()
                  wy = wy + 25
                  wx = 0
                  pygame.display.update()
            break 

def win():
      
      while True:
            screen.fill((0,0,0))
            screen.blit(yay,(0,0))
            wx = 0
            wy = 250
            for y in range(0,10,1):
                  for x in range(0,5,1):
                        stupidpython("YOU WIN",wx,wy,(255,255,255))
                        time.sleep(0.5)
                        wx = wx + 100
                        pygame.display.update()
                  wy = wy + 25
                  wx = 0
                  pygame.display.update()
            break

class Balloon:
    def __init__(self):
        self.x = random.randint(0,450)
        self.y = 500
        
        if score<=5:
              self.up = 0.5
        if 5<score<=10:
              self.up = 1
        if 10<score<=15:
              self.up = 1.5
        if 15<score<=20:
              self.up = 2
        if 20<score<=25:
              self.up = 2.5
        if 25<score<=30:
              self.up = 2.6
        if 30<score<=35:
              self.up = 2.7
        if 35<score<=40:
              self.up = 2.8
        if 40<score<=45:
              self.up = 2.9
        if 45<score<=49:
              self.up = 3
        if score>=51:
              self.up = 1
              win()
              
        self.key = random.choice(alphabet)

    def draw(self):
        screen.blit(balloon,(self.x,500))
        show_text(self.key,self.x+27,self.y+30,(255,255,255))

    def move(self):
        if score == 50:
              win()
        else:
              self.y = self.y - self.up
              screen.blit(balloon,(self.x,self.y))
              show_text(self.key,self.x+27,self.y+30,(255,255,255))

while True:
    pygame.display.update()
    screen.blit(back,(0,0)) 

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()  
            exit()

        elif event.type==KEYDOWN:
                new = 1
                if event.key == K_a:
                    press="a"
                if event.key == K_b:
                    press="b"
                if event.key == K_c:
                    press="c"
                if event.key == K_d:
                    press="d"
                if event.key == K_e:
                    press="e"
                if event.key == K_f:
                    press="f"
                if event.key == K_g:
                    press="g"
                if event.key == K_h:
                    press="h"
                if event.key == K_i:
                    press="i"
                if event.key == K_j:
                    press="j"
                if event.key == K_k:
                    press="k"
                if event.key == K_l:
                    press="l"
                if event.key == K_m:
                    press="m"
                if event.key == K_n:
                    press="n"
                if event.key == K_o:
                    press="o"
                if event.key == K_p:
                    press="p"
                if event.key == K_q:
                    press="q"
                if event.key == K_r:
                    press="r"
                if event.key == K_s:
                    press="s"
                if event.key == K_t:
                    press="t"
                if event.key == K_u:
                    press="u"
                if event.key == K_v:
                    press="v"
                if event.key == K_w:
                    press="w"
                if event.key == K_x:
                    press="x"
                if event.key == K_y:
                    press="y"
                if event.key == K_z:
                    press="z"
                if event.key == K_SPACE:
                    press = "random letter"

                for i in range (0,len(stuff)):
                    if press == stuff[i].key:
                        blue = i
                        thing = stuff[i]
                        poof = 1
                        score = score + 1
                        plzwork = "Score: "+str(score)

                if press not in letters and press != "random letter":
                     score = score - 1
                     plzwork = "Score: "+str(score)    

    if new == 1:
        ball = Balloon()
        stuff.append(ball)
        letters.append(ball.key)
        ball.draw()
        new = 0
        move = 1

    if move == 1:
         for i in range (0,len(stuff)):
             stuff[i].move()
             if stuff[i].y + 50 <= 0:
                 screen.fill((0,0,0))
                 pygame.display.update()
                 fail()
                 score=0
                 end = 1
                 #run game over function

    if poof == 1:
          pygame.mixer.music.play(0)
          screen.blit(back,(0,0))
          stuff.pop(blue)
          letters.pop(blue)
          screen.blit(oof,(thing.x,thing.y))
          pygame.display.update()
          time.sleep(0.3)
          poof = 0

    if score == 51:
          screen.fill((255,255,255))
          win()
          break

    else:
          show_text(plzwork, 10 , 10, (0,0,0))

    if end == 1:
          screen.fill((0,0,0))
          fail()
          break

pygame.display.update()
