import pygame
import os
import sys
from pygame.locals import *
from basicgame import *

class MainMenuState(GameState):
    def __init__(self,game):
        super(MainMenuState,self).__init__(game)
        self.playGameState == None
        self.font = pygame.font.Font('MagicSchoolOne.ttf',40)
        self.index = 0 #currently selected item is stored in 'index'
        self.inputTick = 0
        self.menuItems = ['Start Game','Records','Mode','Quit']
    def setPlayState(self,state):
        self.playGameState = state
    def update(self, gameTime): #here should write work with keys to choose menu items
        keys = pygame.key.pet_pressed()
        if ((keys[K_w] or keys[K_s]) and self.inputTick == 0):
            self.inputTick = 250
            if keys[K_w]:
                self.index -= 1 #index controlls what is happening
                if (self.index<0):
                    self.index = len(self.menuItems) -1
            elif keys[K_s]:
                 self.index+=1
                 if self.index == len(self.menuItems):
                     self.index=0
        elif self.inputTick>0: #scrolling control
            self.inputTick -= gameTime
        if self.inputTick<0:
            self.inputTick=0
    def render(self,surface): #here senarios, when people click
        surface.blit(self.font.render('Quidditch',True,(0,255,255),(screen_width//2,screen_height//2+100)))
        count=0
        y=screen_height//2
        for item in self.menuItems:
            itemText = ' '
            if count == self.index:
                itemText = '>>'
            itemText += item
            surface.blit(self.font.render(itemText,True,(0,255,255),(screen_width//2,y)))
            y += 150
            count += 1
       
