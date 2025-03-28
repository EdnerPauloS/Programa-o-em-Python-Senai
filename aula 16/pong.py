import pygame

# Inicializa o Pygame
pygame.init()

# Definindo a janela do jogo
janela = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Ping Pong')

# Definindo as cores
PRETO = (255, 255, 255)
BRANCO = (0, 0, 0)

# Posições iniciais das raquetes e bola
raquete1_x, raquete1_y = 50, 225
raquete2_x, raquete2_y = 450, 225
bola_x, bola_y = 250, 250

# Velocidades de movimento
velocidade_raquete = 0.5
velocidade_bola_x, velocidade_bola_y = 0.2,0.1

# Tamanhos das raquetes e bola
raquete_largura, raquete_altura = 20, 100
bola_largura, bola_altura = 20, 20

# Placar inicial
placar1 = 0
placar2 = 0

# Fonte para o placar
font = pygame.font.SysFont(None, 55)

# Função para desenhar elementos
def desenhar():
    # Limpa a tela
    janela.fill(BRANCO)

    # Desenha as raquetes
    pygame.draw.rect(janela, PRETO, (raquete1_x, raquete1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(janela, PRETO, (raquete2_x, raquete2_y, raquete_largura, raquete_altura))

    # Desenha a bola
    pygame.draw.ellipse(janela, PRETO, (bola_x, bola_y, bola_largura, bola_altura))

    # Desenha o placar
    placar = font.render(f"{placar1} - {placar2}", True, PRETO)
    janela.blit(placar, (200, 20))

# Loop principal do jogo
LOOP = True
while LOOP:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            LOOP = False

    # Movimentação das raquetes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < 500 - raquete_altura:
        raquete1_y += velocidade_raquete
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500 - raquete_altura:
        raquete2_y += velocidade_raquete

    # Movimentação da bola
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    # Colisão com as bordas superiores e inferiores
    if bola_y <= 0 or bola_y >= 500 - bola_altura:
        velocidade_bola_y = -velocidade_bola_y

    # Colisão com as raquetes
    if (raquete1_x < bola_x < raquete1_x + raquete_largura) and (raquete1_y < bola_y < raquete1_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
    if (raquete2_x < bola_x < raquete2_x + raquete_largura) and (raquete2_y < bola_y < raquete2_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x

    # Placar e reinício da bola
    if bola_x <= 0:  # Jogador 2 marca ponto
        placar2 += 1
        bola_x, bola_y = 250, 250  # Reinicia a bola
        velocidade_bola_x = -velocidade_bola_x  # Inverte a direção da bola
    if bola_x >= 500 - bola_largura:  # Jogador 1 marca ponto
        placar1 += 1
        bola_x, bola_y = 250, 250  # Reinicia a bola
        velocidade_bola_x = -velocidade_bola_x  # Inverte a direção da bola

    # Desenha os elementos na tela
    desenhar()

    # Atualiza a tela
    pygame.display.update()

# Finaliza o Pygame
pygame.quit()
