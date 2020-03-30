import pygame
from button import button

class ToolPanel():
    
    
    def __init__(self,color,x,y,width,h):
        self.color = color
        self.x = x
        self.y = y 
        self.h = h
        self.width = width
        
    def draw(self,win):
        pygame.draw.rect(win,(0,0,0,),(self.x-2,self.y-2,self.width+4,self.h+4),0)
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.h),0)
        Buttons= []
        for i in range(5):
            Buttons.append(button((0,0,0),self.x+5,self.y+5+(5*i)+(30*i),self.width-10,self.width-10,''))
        Buttons[0].draw(win,None,'Img/playButton.png')
        Buttons[1].draw(win,None,'Img/hamerButton.png')
        Buttons[2].draw(win,None,'Img/deletButton.png')
        Buttons[3].draw(win,None,'Img/downloadButton.png')
        Buttons[4].draw(win,None,'Img/openButton.png')
        return Buttons
   

                
       
         
                


        
       
