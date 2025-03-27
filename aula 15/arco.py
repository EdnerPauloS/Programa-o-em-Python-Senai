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
        pygame.draw.arc(tela,'red',(350,300,200,200),0,3.13,8)
        pygame.display.flip()#sequencia de quadros
        
        
        