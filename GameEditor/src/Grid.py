import pygame

class Grid():
    def __init__(self,zCorX,zCorY,eCorX,eCorY):
        self.zCorX = zCorX
        self.zCorY = zCorY
        self.eCorX = eCorX
        self.eCorY = eCorY
    def Render(self,win):
        rangeI = int((self.eCorX-self.zCorX)/50)+1
        for i in range(rangeI):
            pygame.draw.line(win,(0,0,0),(self.zCorX+(50*i),self.zCorY),(self.zCorX+(50*i),self.eCorY))
        rangeI2 = int((self.eCorY-self.zCorY)/50)+1
        for i in range(rangeI2):
            pygame.draw.line(win,(0,0,0),(self.zCorX,self.zCorY+(50*i)),(self.eCorX,self.zCorY+(50*i)))
    def Center(self):
        centerS = []
        rangeI2 = int((self.eCorY-self.zCorY)/50)+1
        rangeI = int((self.eCorX-self.zCorX)/50)+1
        for i in range(rangeI):
            for j in range(rangeI2):
                centerS.append(((i*50)+60,(j*50)+40))

        return centerS
    def CenterIt(self,pos,centers):
        screenW = pygame.display.Info().current_w
        screenH = pygame.display.Info().current_h
        for i in range(len(centers)):
            centerE = (centers[i][0]+50,centers[i][1]+50)
            if centers[i][0]+50 <= screenW-40:   
                if pos[0] >= centers[i][0] and pos[0]<=centerE[0]:
                    if pos[1]>+centers[i][1] and pos[1]<=centerE[1]:
                        return centers[i]
            if centers[i][0]+50 >= screenW-40:  
                return (centers[i][0]-50,centers[i][1])




        
        
        