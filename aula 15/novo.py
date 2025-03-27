import pygame

pygame.init() # inicio o sistema(funcionamento do modulo) 
tela = pygame.display.set_mode((500,500))# cria a tela e seu tamanho

quadrado = pygame.Rect(250,250,50,50)
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:# movimentando atravaez de evento 
        
            if event.key == pygame.K_RIGHT:#pressionando teclas
                quadrado.move_ip([10,0])
            
            if event.key == pygame.K_LEFT:
                quadrado.move_ip([-10,0])
            
            if event.key == pygame.K_DOWN:
                quadrado.move_ip([0,10])
            
            if event.key == pygame.K_UP:
                quadrado.move_ip([0,-10])
        
        if event.type == pygame.KEYDOWN:# movimentando atravaez de evento 
        
            if event.key == pygame.K_d:#pressionando teclas
                quadrado.move_ip([10,0])
            
            if event.key == pygame.K_a:
                quadrado.move_ip([-10,0])
            
            if event.key == pygame.K_s:
                quadrado.move_ip([0,10])
            
            if event.key == pygame.K_w:
                quadrado.move_ip([0,-10])
                        
    tela.fill('red')
    pygame.draw.rect(tela,('white'),quadrado)
    pygame.display.update()
        
        