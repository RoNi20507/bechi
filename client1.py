import pygame
import sys
import math
import socket


REFRESH_RATE = 60
LEFT = 1
RED_PLACE = (100, 250)
YELLOW_PLACE = (250, 250)
GREEN_PLACE = (400, 250)
BLUE_PLACE = (100, 400)
PURPLE_PLACE = (250, 400)
PINK_PLACE = (400, 400)

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BUL PGIAA")
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance1


def return_color(point):
    if distance(RED_PLACE, point) <= 50:
        return 0
    elif distance(YELLOW_PLACE, point) <= 50:
        return 1
    elif distance(GREEN_PLACE, point) <= 50:
        return 2
    elif distance(BLUE_PLACE, point) <= 50:
        return 3
    elif distance(PURPLE_PLACE, point) <= 50:
        return 4
    elif distance(PINK_PLACE, point) <= 50:
        return 5
    return 6


def send_lst(lst):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    client_socket.connect((host, port))
    data = ','.join(map(str, lst))
    client_socket.send(data.encode())
    response = client_socket.recv(1024).decode()
    print("Response from server:", response)
    client_socket.close()


circle_radius = 50
circle_positions = [
    RED_PLACE,
    YELLOW_PLACE,
    GREEN_PLACE,
    BLUE_PLACE,
    PURPLE_PLACE,
    PINK_PLACE
]
circle_colors = [RED, YELLOW, GREEN, BLUE, PURPLE, PINK]

# Main loop
while True:

    FONT = pygame.font.Font(None, 48)

    # Clear the screen
    screen.fill(WHITE)
    #write on screen
    text = FONT.render("Enter your code", True, (0,0,0))
    text_rect = text.get_rect(center=(250, 100))
    screen.blit(text, text_rect)
    # Draw circles
    for i in range(len(circle_positions)):
        pygame.draw.circle(screen, circle_colors[i], circle_positions[i], circle_radius)
    count = 0
    list_numbers = []
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                place = pygame.mouse.get_pos()
                if count < 4:
                    num = return_color(place)
                    if num < 6:
                        count += 1
                        list_numbers.append(num)
                        print("hi")
        pygame.display.flip()
        clock.tick(REFRESH_RATE)
        send_lst(list_numbers)
    pygame.quit()
