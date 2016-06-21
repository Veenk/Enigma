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
coords = {'G': (201, 241), 'K': (311, 241), 'Q': (43, 214), 'E': (115, 214), 'N': (252, 270),
          'T': (190, 214), 'W': (79, 214), 'P': (31, 270), 'D': (127, 241), 'H': (238, 241),
          'J': (274, 241), 'F': (164, 241), 'U': (233, 214), 'I': (300, 214), 'O': (337, 214),
          'L': (326, 270), 'Y': (68, 270), 'S': (90, 241), 'A': (53, 241), 'R': (147, 214),
          'Z': (226, 214), 'B': (216, 270), 'M': (289, 270), 'C': (142, 270), 'V': (179, 270),
          'X': (105, 270)}
print(coords)
f = open('cypher.txt', 'w')
f1 = open('message.txt', 'w') 
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
        self.R = R
        self.M = M
        self.L = L
        text_display('0', 329, 163)
        text_display('0', 369, 163)
        text_display('0', 409, 163)
        while not Exit:
            f = open('cypher.txt', 'a')
            f1 = open('message.txt', 'a') 
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                print(mouse)
                if event.type == pygame.QUIT:           ## проверка на нажатие "крестика"
                    pygame.quit()
                    quit()
                    
                if event.type == pygame.KEYDOWN:   ## нажатие клавиш машины
                    
                    self.R += 1
                    if self.R == 22:
                        self.M += 1
                        if self.M == 5:
                             self.L += 1
                             if self.L == 26:
                                self.L = 0
                        elif self.M == 26:
                            self.M = 0
                    elif self.R == 26:
                        self.R = 0
                        
                    if event.key == pygame.K_q:
                        self.letter = 'Q'
                    if event.key == pygame.K_w:
                        self.letter = 'W'
                    if event.key == pygame.K_e:
                        self.letter = 'E'
                    if event.key == pygame.K_r:
                        self.letter = 'R'
                    if event.key == pygame.K_t:
                        self.letter = 'T'
                    if event.key == pygame.K_y:
                        self.letter = 'Y'
                    if event.key == pygame.K_u:
                        self.letter = 'U'
                    if event.key == pygame.K_i:
                        self.letter = 'I'
                    if event.key == pygame.K_o:
                        self.letter = 'O'
                    if event.key == pygame.K_p:
                        self.letter = 'P'
                    if event.key == pygame.K_a:
                        self.letter = 'A'
                    if event.key == pygame.K_s:
                        self.letter = 'S'
                    if event.key == pygame.K_d:
                        self.letter = 'D'
                    if event.key == pygame.K_f:
                        self.letter = 'F'
                    if event.key == pygame.K_g:
                        self.letter = 'G'
                    if event.key == pygame.K_h:
                        self.letter = 'H'
                    if event.key == pygame.K_j:
                        self.letter = 'J'
                    if event.key == pygame.K_k:
                        self.letter = 'K'
                    if event.key == pygame.K_l:
                        self.letter = 'L'
                    if event.key == pygame.K_z:
                        self.letter = 'Z'
                    if event.key == pygame.K_x:
                        self.letter = 'X'
                    if event.key == pygame.K_c:
                        self.letter = 'C'
                    if event.key == pygame.K_v:
                        self.letter = 'V'
                    if event.key == pygame.K_b:
                        self.letter = 'B'
                    if event.key == pygame.K_n:
                        self.letter = 'N'
                    if event.key == pygame.K_m:
                        self.letter = 'M'
                           
                if 320+16 > mouse[0] > 320 and 130+14 > mouse[1] > 130:       ## даем возможность изменить стартовое                                                            
                    if click[0] == 1 and self.L < 25:                              
                        self.L += 1
                elif 360+16 > mouse[0] > 360 and 130+14 > mouse[1] > 130:
                    if click[0] == 1 and self.M < 25:
                        self.M += 1
                elif 400+16 > mouse[0] > 400 and 130+14 > mouse[1] > 130:
                    if click[0] == 1 and self.R < 25:
                        self.R += 1
                if 320+16 > mouse[0] > 320 and 180+14 > mouse[1] > 180:                                                                  
                    if click[0] == 1 and self.L > 0:                              
                        self.L -= 1
                elif 360+16 > mouse[0] > 360 and 180+14 > mouse[1] > 180:
                    if click[0] == 1 and self.M > 0:
                        self.M -= 1
                elif 400+16 > mouse[0] > 400 and 180+14 > mouse[1] > 180:
                    if click[0] == 1 and self.R > 0:
                        self.R -= 1                                             ## значение роторов(левого-L, среднего-M, правого-R

            self.window.blit(self.surface, ((800-390)/2, (600-538)/2))
            self.surface.blit(self.ngm, (0,0))
            Machine(self.R,self.M,self.L)
            for a in range(1):
                if type(self.letter) == str:
                    f1.write(self.letter)
                    f1.close()
                    Machine.compute(self, self.letter)
                    surface.blit(glow, coords[self.letter])
                    f.write(self.letter)
                    f.close()
                    self.letter = 1
            text_display(str(self.L), 329, 163)
            text_display(str(self.M), 369, 163)
            text_display(str(self.R), 409, 163)
            pygame.display.update()
            clock.tick(20)
            
              
Visual(glow, ngm, window, surface, main, main2)
pygame.quit()
quit()




