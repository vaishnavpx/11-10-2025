import pygame
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT=500,500

display_surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Adding image and background image")

background_color = (58, 58, 58)  # Blue

character_image=pygame.transform.scale(
    pygame.image.load("Character.png").convert_alpha(),(300,300))

character_rect=character_image.get_rect(center=(SCREEN_WIDTH//2,
                                                SCREEN_HEIGHT//2-30))

text=pygame.font.Font(None,36).render("My First Game Screen.",True,
                                      pygame.Color("black"))

text_rect=text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+110))
def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        display_surface.blit(character_image,character_rect)
        display_surface.blit(text,text_rect)

        pygame.display.flip()
        clock.tick(30)

    display_surface.fill(background_color)
    pygame.display.flip()

    pygame.quit()

if __name__=="__main__":
    game_loop()