import pygame
import os
import sys
from pygame.locals import *
from ball import *
from mode import *
from mapp import *

class QuaffleModel(BallModel):
    def __init__(self, pos_x, pos_y, speed):
     super(QuaffleModel,self).__init__(pos_x, pos_y, speed)
     self.pos = pygame.math.Vector2(pos_x,pos_y)
     self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
     self.speed = pygame.math.Vector2(speed,speed)
     #self.mass = Mode().mode not right


class QuaffleController():
    def __init__(self,ball:QuaffleModel):
        self.ball = ball

    def fly(self,time):#time from Chaserpower
        for i in range(1,time):
            self.ball.pos.x=self.ball.pos.x+self.ball.speed.x*i
            self.ball.pos.y=self.ball.pos.y+self.ball.speed.y*i - (self.ball.g*(i**2))//2
            if self.ball.pos.y <=0:
                self.ball.pos.y = screen_height-100
                self.ball.pos.x = screen_width//2
            elif self.ball.pos.x <=0 and self.ball.pos.x>=1080:
                self.ball.pos.x = screen_width//2
                self.ball.pos.y = screen_height-100
            #add stop if interaction with hunter
    def got_caught(a):#add hunter
        #call funtion from collision controller
