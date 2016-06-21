import pygame
from text import text_object, text_display
from enigma1 import Machine


pygame.init()

ngm = pygame.image.load('machine.png')
glow = pygame.image.load('glow.png')
main = pygame.image.load('enlogo.png')
main2 = pygame.image.load('enlogo_change.png')
resolution = (800,600)
window = pygame.display.set_mode(resolution)
surface = pygame.Surface((390, 538))
pygame.display.set_caption('ENIGMA')

clock = pygame.time.Clock()

class Visual:
    def __init__(self, glow, ngm, window, surface, main, main2, intro = True):
        self.ngm = ngm
        self.glow = glow
        self.window = window
        self.main = main
        self.main2 = main2
        self.surface = surface
        self.intro = intro
        while self.intro:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if 224+346 > mouse[0] > 224 and 222+166 > mouse[1] > 222: ## границы логотипа энигмы на стартововом экране
                    self.window.blit(self.main2, ((800-375)/2,(600-360)/2))
                    if click[0] == 1:
                        Visual.game_loop(self)
                else:
                    self.window.blit(self.main, ((800-375)/2,(600-360)/2))
            pygame.display.update()
            clock.tick(15)
        
    def game_loop(self, R=0, M=0, L=0, Exit = False, letter = 2):
        self.letter = letter
        print(self.letter)
        self.R = R
        self.M = M
        self.L = L
        text_display('0', 329, 163)
        text_display('0', 369, 163)
        text_display('0', 409, 163)
        while not Exit:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                
                if event.type == pygame.QUIT:           ## проверка на нажатие "крестика"
                    pygame.quit()
                    quit()
                    
                if event.type == pygame.KEYDOWN:   ## нажатие клавиш машины

                    if event.key == pygame.K_q:
                        self.letter = 'Q'
                        surface.blit(glow, (55-12,226-12))
                        pygame.display.update()
                           
                if 320+16 > mouse[0] > 320 and 130+14 > mouse[1] > 130:       ## даем возможность изменить стартовое                                                            
                    if click[0] == 1 and self.L < 25:                              
                        self.L += 1
                elif 360+16 > mouse[0] > 360 and 130+14 > mouse[1] > 130:
                    if click[0] == 1 and self.M < 25:
                        self.M += 1
                elif 400+16 > mouse[0] > 400 and 130+14 > mouse[1] > 130:
                    if click[0] == 1 and self.R < 25:
                        self.R += 1                                                ## значение роторов(левого-L, среднего-M, правого-R

                
##                print(mouse)
            
            self.window.blit(self.surface, ((800-390)/2, (600-538)/2))
            self.surface.blit(self.ngm, (0,0))
            Machine(self.R,self.M,self.L)
            if type(self.letter) == str:
                Machine.imput(self, self.letter)
            text_display(str(self.L), 329, 163)
            text_display(str(self.M), 369, 163)
            text_display(str(self.R), 409, 163)
            pygame.display.update()
            clock.tick(20)
            
              
Visual(glow, ngm, window, surface, main, main2)
pygame.quit()
quit()




