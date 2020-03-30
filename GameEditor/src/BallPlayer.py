import pygame

class BPlayer():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width= width
        self.height = height
        self.color = (255,0,0)
        self.IsGround = False
        self.gravity = -0.5
        self.velocity = 5
        self.vel = 5
        
    def render(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),0)

    def collision(self,x1,y1,w1,h1):
        if self.x >= x1-self.width and self.x < x1+w1 and self.y + self.height == y1:
            self.y -= self.vel
            self.IsGround = True
        if self.y >= y1-self.height and self.y < y1+h1 and self.x + self.width == x1:
            self.x -= self.vel
            
        if self.y >= y1-self.height and self.y < y1+h1 and self.x  == x1 + w1:
            self.x += self.vel
            
        if self.x >= x1-self.width and self.x < x1+w1 and self.y == y1+ h1:
            self.y += self.vel
            
        
      
      
       
    def update(self):
        self.y -= self.velocity*self.gravity
        print(self.velocity)
    def update(self):
        self.y -= self.velocity*self.gravity

        
