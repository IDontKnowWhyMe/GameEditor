import pygame
import numpy as np


class CraftP():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cordinates = []
        self.string = ''
    def Render(self,win):
        pygame.draw.rect(win,(255,255,255),(self.x,self.y,self.width,self.height),0)
    def Add(self,pos):
        self.cordinates.append(pos)
    def Save(self):
       
        result = np.array(self.cordinates)
        res = result.flatten()
        with open('year.txt', 'w') as file:
            for xy in res:
                file.write("%i\n" % xy)
       
        file.close()
   

