import pygame,sys
pygame.init()
# create a screen:
screen = pygame.display.set_mode((500,500))
done = False



# (red,green,blue)
c = (0,150,255)

# never ending loop now:
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for x in range(0,300,100):
        
        pygame.draw.line(screen,c,(1,x),(600,x), 2)
        pygame.draw.line(screen,c,(x,1),(x,600), 2)
        pygame.display.update()