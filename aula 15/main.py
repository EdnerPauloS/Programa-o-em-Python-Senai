import pygame

pygame.init() # inicio o sistema(funcionamento do modulo) 
tela = pygame.display.set_mode((1000, 1000))# cria a tela e seu tamanho
tela.fill((255,0,0)) #prencher o fundo de tela
pygame.display.flip()#sequencia de quadros

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            pygame.quit()
        tela.fill('black')
        pygame.draw.rect(tela,'red',(450,600,200,200))
        pygame.draw.arc(tela,'white',(350,300,200,200),0,3.13,8)
        pygame.draw.line(tela,'yellow', (200,500), (200, 800), 5)
        pygame.draw.ellipse(tela, ('blue'), (450,150,200,100))
        pygame.draw.circle(tela, ('green'), (150,350), 50)
        pygame.draw.aaline(tela,'silver', (400,250), (400, 400),10)
        
        pygame.display.flip()#sequencia de quadros
        
        
        