import pygame
walkRight = [pygame.image.load('Img/R1.png'), pygame.image.load('Img/R2.png'), pygame.image.load('Img/R3.png'), pygame.image.load('Img/R4.png'), pygame.image.load('Img/R5.png'), pygame.image.load('Img/R6.png'), pygame.image.load('Img/R7.png'), pygame.image.load('Img/R8.png'), pygame.image.load('Img/R9.png')]
walkLeft = [pygame.image.load('Img/L1.png'), pygame.image.load('Img/L2.png'), pygame.image.load('Img/L3.png'), pygame.image.load('Img/L4.png'), pygame.image.load('Img/L5.png'), pygame.image.load('Img/L6.png'), pygame.image.load('Img/L7.png'), pygame.image.load('Img/L8.png'), pygame.image.load('Img/L9.png')]

char = pygame.image.load('Img/standing.png')
class player():
    def __init__(self,x,y,width,height):
        self.velocity = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.falling = True
        self.onGround = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
    
    def jump(self):
        if(self.onGround == False):
            return
        self.velocity = 8
        self.onGround = False
     
   
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))

    def detectCollisions(self,x1,y1,w1,h1,x2,y2,w2,h2):
    
        if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
            
            return True

        elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
           
            return True

        elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
         
            return True

        elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
            
            return True

        else:
            
            return False
 
    def update(self,gravity,blockList):
        if(self.velocity<0):
            self.falling = True
        collision = False;
        blockX,blockY = 0,0
        for block in blockList:
            collision = self.detectCollisions(self.x,self.y,self.width,self.height,block.x,block.y,block.width,block.height)

            if collision == True:
                blockX = block.x
                blockY = block.y
                break
        if(collision == True):
            if(self.falling == True):
                self.falling = False
                self.velocity =0
                self.onGround = True
                
        if(collision == False):
            if(self.falling == False):
                self.falling = True
                self.onGround = False

        if(self.onGround == False):
            self.velocity+=gravity
        self.y-=self.velocity
