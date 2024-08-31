import pygame
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Cores suaves
light_gray = (240, 240, 240)
highlight_green = (50, 205, 50)
light_green = (144, 238, 144)
light_orange = (255, 204, 153)
light_blue = (173, 216, 230)

# Configurações da raquete e da bola
paddle_width = 64
paddle_height = 128
ball_size = 15

# Carregar e redimensionar imagens
paddle_a_image = pygame.image.load('paddle_a.png')
paddle_b_image = pygame.image.load('paddle_b.png')

# Redimensionar imagens das raquetes para o tamanho especificado
paddle_a_image = pygame.transform.scale(paddle_a_image, (paddle_width, paddle_height))
paddle_b_image = pygame.transform.scale(paddle_b_image, (paddle_width, paddle_height))

# Criar máscaras para as raquetes
paddle_a_mask = pygame.mask.from_surface(paddle_a_image)
paddle_b_mask = pygame.mask.from_surface(paddle_b_image)

# Posições iniciais
paddle_a_pos = [30, screen_height // 2 - paddle_height // 2]
paddle_b_pos = [screen_width - 30 - paddle_width, screen_height // 2 - paddle_height // 2]
ball_pos = [screen_width // 2, screen_height // 2]
ball_speed = [5, 5]

# Velocidade das raquetes
paddle_speed = 10
bot_speed = 7

# Placar
score_a = 0
score_b = 0
font = pygame.font.Font(None, 74)

# Configurações de jogo
difficulty = "Medium"
game_time = 60  # Tempo padrão em segundos
clock = pygame.time.Clock()
menu_index = 0

# Opções do menu
menu_options = ["Start Game", "Difficulty", "Time", "Game Mode"]
game_mode = "Player vs Bot"

# Tela inicial com menu configurável
def show_start_screen():
    global menu_index
    screen.fill(light_gray)
    title_font = pygame.font.Font(None, 100)
    text_surface = title_font.render("Pong", True, light_blue)
    screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, screen_height // 4))

    start_font = pygame.font.Font(None, 50)
    option_colors = [highlight_green if i == menu_index else light_green for i in range(len(menu_options))]

    start_text = start_font.render("Start Game", True, option_colors[0])
    screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 2))

    difficulty_text = start_font.render(f"Difficulty: {difficulty}", True, option_colors[1])
    screen.blit(difficulty_text, (screen_width // 2 - difficulty_text.get_width() // 2, screen_height // 2 + 50))

    time_text = start_font.render(f"Time: {'Infinite' if game_time == 0 else f'{game_time} seconds'}", True, option_colors[2])
    screen.blit(time_text, (screen_width // 2 - time_text.get_width() // 2, screen_height // 2 + 100))

    mode_text = start_font.render(f"Game Mode: {game_mode}", True, option_colors[3])
    screen.blit(mode_text, (screen_width // 2 - mode_text.get_width() // 2, screen_height // 2 + 150))

    pygame.display.flip()

    navigate_menu()

# Navegação do menu usando WASD
def navigate_menu():
    global menu_index, difficulty, game_time, game_mode
    navigating = True
    while navigating:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:  # Sobe no menu
                    menu_index = (menu_index - 1) % len(menu_options)
                    show_start_screen()
                elif event.key == pygame.K_s:  # Desce no menu
                    menu_index = (menu_index + 1) % len(menu_options)
                    show_start_screen()
                elif event.key == pygame.K_a or event.key == pygame.K_d:  # Muda opções de dificuldade, tempo ou modo
                    if menu_index == 1:
                        change_difficulty()
                    elif menu_index == 2:
                        change_time()
                    elif menu_index == 3:
                        change_game_mode()
                    show_start_screen()
                elif event.key == pygame.K_RETURN:  # Seleciona a opção
                    if menu_index == 0:
                        navigating = False
                    elif menu_index == 1:
                        change_difficulty()
                    elif menu_index == 2:
                        change_time()
                    elif menu_index == 3:
                        change_game_mode()
                    show_start_screen()
                elif event.key == pygame.K_SPACE and menu_index == 0:  # Começar o jogo
                    navigating = False

# Alterar dificuldade
def change_difficulty():
    global difficulty, ball_speed, bot_speed
    if difficulty == "Easy":
        difficulty = "Medium"
        ball_speed = [5, 5]
        bot_speed = 7
    elif difficulty == "Medium":
        difficulty = "Hard"
        ball_speed = [7, 7]
        bot_speed = 10
    else:
        difficulty = "Easy"
        ball_speed = [3, 3]
        bot_speed = 5

# Alterar tempo de jogo
def change_time():
    global game_time
    if game_time == 60:
        game_time = 120
    elif game_time == 120:
        game_time = 0
    else:
        game_time = 60

# Alterar modo de jogo
def change_game_mode():
    global game_mode
    if game_mode == "Player vs Bot":
        game_mode = "Bot vs Bot"
    elif game_mode == "Bot vs Bot":
        game_mode = "Player vs Player"
    else:
        game_mode = "Player vs Bot"

# Desenho dos objetos
def draw_objects():
    screen.fill(light_gray)
    screen.blit(paddle_a_image, paddle_a_pos)
    screen.blit(paddle_b_image, paddle_b_pos)
    pygame.draw.ellipse(screen, light_orange, (*ball_pos, ball_size, ball_size))
    pygame.draw.aaline(screen, light_blue, (screen_width // 2, 0), (screen_width // 2, screen_height))

    score_text = font.render(str(score_a), True, light_blue)
    screen.blit(score_text, (screen_width // 4, 20))
    score_text = font.render(str(score_b), True, light_blue)
    screen.blit(score_text, (screen_width * 3 // 4, 20))

# Movimento da bola
def move_ball():
    global ball_speed, score_a, score_b
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Colisão com as bordas superior e inferior
    if ball_pos[1] <= 0 or ball_pos[1] >= screen_height - ball_size:
        ball_speed[1] *= -1

    # Colisão com as raquetes
    paddle_a_rect = pygame.Rect(paddle_a_pos[0], paddle_a_pos[1], paddle_width, paddle_height)
    paddle_b_rect = pygame.Rect(paddle_b_pos[0], paddle_b_pos[1], paddle_width, paddle_height)

    if paddle_a_rect.colliderect(pygame.Rect(ball_pos[0], ball_pos[1], ball_size, ball_size)):
        offset_x = int(ball_pos[0] - paddle_a_pos[0])
        offset_y = int(ball_pos[1] - paddle_a_pos[1])
        if (0 <= offset_x < paddle_width) and (0 <= offset_y < paddle_height) and paddle_a_mask.get_at((offset_x, offset_y)):
            ball_speed[0] *= -1

    if paddle_b_rect.colliderect(pygame.Rect(ball_pos[0], ball_pos[1], ball_size, ball_size)):
        offset_x = int(ball_pos[0] - paddle_b_pos[0])
        offset_y = int(ball_pos[1] - paddle_b_pos[1])
        if (0 <= offset_x < paddle_width) and (0 <= offset_y < paddle_height) and paddle_b_mask.get_at((offset_x, offset_y)):
            ball_speed[0] *= -1

    # Pontuação
    if ball_pos[0] < 0:
        score_b += 1
        reset_ball()
    elif ball_pos[0] > screen_width - ball_size:
        score_a += 1
        reset_ball()

# Resetar a bola para o centro
def reset_ball():
    global ball_pos, ball_speed
    ball_pos = [screen_width // 2, screen_height // 2]
    ball_speed[0] *= -1

# Movimento das raquetes
def move_paddles():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a_pos[1] > 0:
        paddle_a_pos[1] -= paddle_speed
    if keys[pygame.K_s] and paddle_a_pos[1] < screen_height - paddle_height:
        paddle_a_pos[1] += paddle_speed

# Movimento do bot
def move_bot():
    if paddle_b_pos[1] + paddle_height // 2 < ball_pos[1]:
        paddle_b_pos[1] += bot_speed
    elif paddle_b_pos[1] + paddle_height // 2 > ball_pos[1]:
        paddle_b_pos[1] -= bot_speed

# Controle do segundo jogador
def move_player_b():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_b_pos[1] > 0:
        paddle_b_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_b_pos[1] < screen_height - paddle_height:
        paddle_b_pos[1] += paddle_speed

# Loop principal do jogo
def game_loop():
    show_start_screen()
    start_ticks = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Controle das raquetes baseado no modo de jogo
        if game_mode == "Player vs Player":
            move_paddles()
            move_player_b()
        elif game_mode == "Player vs Bot":
            move_paddles()
            move_bot()
        else:  # Bot vs Bot
            move_bot()
            move_bot()

        move_ball()
        draw_objects()

        pygame.display.flip()
        clock.tick(60)

        # Verifica o tempo de jogo
        if game_time > 0:
            seconds = (pygame.time.get_ticks() - start_ticks) // 1000
            if seconds >= game_time:
                break

    # Fim do jogo
    show_end_screen()

# Tela de fim de jogo
def show_end_screen():
    screen.fill(light_gray)
    end_font = pygame.font.Font(None, 100)
    end_text = end_font.render("Game Over", True, light_blue)
    screen.blit(end_text, (screen_width // 2 - end_text.get_width() // 2, screen_height // 4))

    result_font = pygame.font.Font(None, 50)
    result_text = result_font.render(f"Final Score - Player: {score_a}, Bot: {score_b}", True, light_orange)
    screen.blit(result_text, (screen_width // 2 - result_text.get_width() // 2, screen_height // 2))

    restart_text = result_font.render("Press R to Restart or Q to Quit", True, light_orange)
    screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 100))

    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    reset_game()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Resetar o jogo
def reset_game():
    global score_a, score_b, paddle_a_pos, paddle_b_pos, ball_pos, ball_speed
    score_a = 0
    score_b = 0
    paddle_a_pos = [30, screen_height // 2 - paddle_height // 2]
    paddle_b_pos = [screen_width - 30 - paddle_width, screen_height // 2 - paddle_height // 2]
    ball_pos = [screen_width // 2, screen_height // 2]
    ball_speed = [5, 5]
    reset_ball()
    game_loop()

game_loop()
