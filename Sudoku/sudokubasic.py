from string import whitespace
import pygame
import requests
from sys import exit

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
color = (0, 0, 255)
grid_copy=[[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
background_color = (251, 247, 245)
def insert(screen,position):
    i,j=position[1],position[0]
    myfont= pygame.font.SysFont('comic sans ms', 35)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
            if event.type==pygame.KEYDOWN:
                if(grid_copy[i-1][j-1] != 0): 
                    return
                if(event.key == 48):
                    grid[i-1][j-1] = event.key-48
                    pygame.draw.rect(screen,background_color,(position[0]*50+10,position[1]*50+10,50-20,50-20))      
                    pygame.display.update()
                    return
                if(0 < event.key-48 < 10):
                    pygame.draw.rect(screen,background_color,(position[0]*50+10,position[1]*50+10,50-20,50-20))    
                    value=myfont.render(str(event.key-48),True,(0,0,0))
                    screen.blit(value,(position[0]*50+15,position[1]*50))
                    grid[i-1][j-1]=event.key-48
                    pygame.display.update()
                    return
                return     
def main():
    pygame.init()
    
    screen = pygame.display.set_mode((550, 550))
    pygame.display.set_caption("SUDOKU")
    screen.fill(background_color)
    myfont = pygame.font.SysFont('comic sans ms', 35)

    for i in range(0, 10):
        if(i % 3 == 0):
            pygame.draw.line(screen, (0, 0, 0), (50+50*i, 50), (50+50*i, 500), 4)
            pygame.draw.line(screen, (0, 0, 0), (50, 50+50*i), (500, 50+50*i), 4)
        pygame.draw.line(screen, (0, 0, 0), (50+50*i, 50), (50+50*i, 500), 1)
        pygame.draw.line(screen, (0, 0, 0), (50, 50+50*i), (500, 50+50*i), 1)
    pygame.display.flip()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, color)
                screen.blit(value, ((j+1)*50+15, (i+1)*50))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                insert(screen,(pos[0]//50,pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        
main()   