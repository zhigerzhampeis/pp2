import pygame, sys

pygame.init()

BUTTON_WIDTH = 50
BUTTON_HEIGHT = 40

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Paint")
window.fill('white')

# Set drawing color and shape
DRAW_COLOR = 'black'
DRAW_SHAPE = "rectangle"
# Set start position for drawing shapes
ERASER_SIZE = 20
erasing = False
start_pos = None

while True:
    # For each key press chnage the DRAW_SHAPE and DRAW_COLOR
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                DRAW_SHAPE = "circle"
            elif event.key == pygame.K_r:
                DRAW_SHAPE = "rectangle"
            elif event.key == pygame.K_t:
                DRAW_SHAPE = "triangle"
            elif event.key == pygame.K_s:
                DRAW_SHAPE = "square"
            elif event.key == pygame.K_h:
                DRAW_SHAPE = "rhombus"
            elif event.key == pygame.K_e:
                DRAW_SHAPE = "erase"
            elif event.key == pygame.K_g:
                DRAW_COLOR = 'green'
            elif event.key == pygame.K_b:
                DRAW_COLOR = 'blue'
            elif event.key == pygame.K_y:
                DRAW_COLOR = 'yellow'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #getting start position to create shapes
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            #for each shape use draw method
            if DRAW_SHAPE == "rectangle":
                end_pos = event.pos
                rect_width = abs(end_pos[0] - start_pos[0])
                rect_height = abs(end_pos[1] - start_pos[1])
                rect_x = min(start_pos[0], end_pos[0])
                rect_y = min(start_pos[1], end_pos[1])
                rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
                pygame.draw.rect(window, DRAW_COLOR, rect, 3)
            elif DRAW_SHAPE == "circle":
                end_pos = event.pos
                radius = ((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5
                pygame.draw.circle(window, DRAW_COLOR, start_pos, int(radius), 3)
            elif DRAW_SHAPE == "triangle":
                    end_pos = event.pos
                    pygame.draw.polygon(window, DRAW_COLOR, [(start_pos[0], end_pos[1]), end_pos, start_pos], 3)
            elif DRAW_SHAPE == "square":
                end_pos = event.pos
                side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
                pygame.draw.rect(window, DRAW_COLOR, rect, 3)
            elif DRAW_SHAPE == "rhombus":
                end_pos = event.pos
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                points = [(start_pos[0] + width // 2, start_pos[1]), 
                    (start_pos[0] + width, start_pos[1] + height // 2), 
                    (start_pos[0] + width // 2, start_pos[1] + height),
                    (start_pos[0], start_pos[1] + height // 2)]
                pygame.draw.polygon(window, DRAW_COLOR, points, 3)
            else:
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(window, 'white', (x, y), ERASER_SIZE)
        #for continuous erasing
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if DRAW_SHAPE=='erase':
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(window, 'white', (x, y), ERASER_SIZE)
        pygame.display.update()