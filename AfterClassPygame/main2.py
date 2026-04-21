import pygame

pygame.init()
screen=pygame.display.set_mode((640,480))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(0,0,100,60))
    text=pygame.font.Font(None,36).render("After Class Project",True,
                                      pygame.Color("black"))

    pygame.display.flip()