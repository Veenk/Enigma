import pygame

pygame.init()

resolution = (800,600)
window = pygame.display.set_mode(resolution)

def text_object(text, font):
    textsurf = font.render(text, True, (0,0,0))
    return textsurf, textsurf.get_rect()

def text_display(text, width, height):
    font_size = pygame.font.Font('freesansbold.ttf', 16)
    textsurf, textrect = text_object(text, font_size)
    textrect.center = (width, height)
    window.blit(textsurf, textrect)
    
