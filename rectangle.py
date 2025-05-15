import pygame

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рисование прямоугольников")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Переменные состояния
drawing = False
start_pos = None
end_pos = None
filled = False

# Основной цикл программы
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Начало рисования
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = event.pos
            end_pos = event.pos

        # Обновление прямоугольника при движении мыши
        elif event.type == pygame.MOUSEMOTION and drawing:
            end_pos = event.pos

        # Завершение рисования
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            end_pos = event.pos

        # Переключение режима заливки
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start_pos and end_pos:
                filled = not filled

    # Отрисовка прямоугольника
    if start_pos and end_pos:
        rect = pygame.Rect(*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
        rect.normalize()
        if filled:
            pygame.draw.rect(screen, RED, rect)
        else:
            pygame.draw.rect(screen, RED, rect, 2)

    pygame.display.flip()
    clock.tick(60)

# Завершение Pygame
pygame.quit()
