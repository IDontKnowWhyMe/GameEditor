
import pygame
from button import button
from ToolPanel import ToolPanel
from CraftingPlane import CraftP
from Block import *
from Grid import Grid
from BallPlayer import BPlayer





pygame.init()
monitpor_size = [pygame.display.Info().current_w,pygame.display.Info().current_h]
screenW = pygame.display.Info().current_w
screenH = pygame.display.Info().current_h
win = pygame.display.set_mode(monitpor_size,pygame.FULLSCREEN)
pygame.display.set_caption("")
run = True
redButton = button((255,0,0),pygame.display.Info().current_w-32,2,30,30,'X')
toolPanel = ToolPanel((169,169,169),10,40,40,screenH-70)
ToolButtons = toolPanel.draw(win)
craft = CraftP(60,40,screenW-100,screenH-70)
ground = []
addBlocks= False
KEY_REPEAT_SETTING = (200,70)
grid = Grid(60,40,screenW-40,screenH-30)
player= BPlayer(200,300,30,30)
gravity = -0.5

pygame.key.set_repeat(*KEY_REPEAT_SETTING)
playing = False
clock = pygame.time.Clock()






def renderWindow():
    win.fill((192,192,192))        
    redButton.draw(win,(0,0,0))
    toolPanel.draw(win)
    craft.Render(win)
    
    
    for block in ground:
        block.draw(win)
        
        
    
    if(playing == False):
        grid.Render(win)
   
    player.render(win)  
    pygame.display.update()
   



while run:
    
    clock.tick(30)
    
    for event in pygame.event.get():
        
        pos = pygame.mouse.get_pos()
        pX,pY = pos
  
  
        if event.type == pygame.MOUSEBUTTONDOWN:
           
            if(ToolButtons[0].isOver(pos)):
                addBlocks= False
                if playing == False:
                    playing = True
                else:
                    playing = False
            if(ToolButtons[1].isOver(pos)):
                addBlocks= True
            if(ToolButtons[2].isOver(pos)):
                ground.clear()
                craft.cordinates.clear()
            if(ToolButtons[3].isOver(pos)):
                craft.Save()
            
        
        
          
                
                    
            if(redButton.isOver(pos)):                               
                run = False
            if(addBlocks==True):
                if(pX>60and pX< screenW-40):
                    if(pY>40 and pY < screenH-30):
                        print(grid.CenterIt(pos,grid.Center()))
                        ground.append(Ground(grid.CenterIt(pos,grid.Center()),'Img/GroundBlock2.png'))
                        craft.Add(grid.CenterIt(pos,grid.Center()))
       

            
        if event.type == pygame.MOUSEMOTION:
            if(redButton.isOver(pos)):
                redButton.color = (139,0,0)
            else:
                redButton.color = (255,0,0)
  
    keys = pygame.key.get_pressed()
    if(playing == True):
        player.update()
        if keys[pygame.K_LEFT] and player.x > craft.x:
            player.x -= player.vel 

        if keys[pygame.K_RIGHT] and player.x < craft.x + craft.width - player.width:
            player.x += player.vel 

        if keys[pygame.K_UP] and player.y > craft.y :
            player.y -= player.vel 

        if keys[pygame.K_DOWN] and player.y < craft.y + craft.height - player.height:
            player.y += player.vel 
            
        for block in ground:
            player.collision(block.x,block.y,50,50)
    
    
    
    
   
    
  
          
    renderWindow()  
    

pygame.quit()
