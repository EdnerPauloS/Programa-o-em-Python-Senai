import pygame

pygame.init() # inicio o sistema(funcionamento do modulo) 
tela = pygame.display.set_mode((1000, 800))# cria a tela e seu tamanho
tela.fill((255,0,0)) #prencher o fundo de tela
pygame.display.flip()#sequencia de quadros

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            pygame.quit()
        tela.fill('black')
        pygame.draw.circle(tela, ('red'), (450,350), 50)
        pygame.draw.circle(tela, ('red'), (700,350), 50)
        pygame.draw.circle(tela, ('red'), (150,350), 50)
       
        pygame.display.flip()#sequencia de quadros
        
        
        