import pygame

class Ground():
    def __init__(self,pos,imgSrc):
        self.imgSrc =imgSrc
        self.pos = pos
        self.width = 50
        self.height = 50
        self.x = self.pos[0]
        self.y = self.pos[1]
      
        
    def draw(self,win):
        
        Img = pygame.image.load(self.imgSrc)
        win.blit(Img,self.pos)
    
  


            
