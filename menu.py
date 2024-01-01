import pygame
import sys
import os
import subprocess


pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Snake")


background_image = pygame.image.load('image/2.jpg')
background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


font = pygame.font.Font(None, 36)




def create_button(x, y, width, height, text, action):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, WHITE, button_rect)
    pygame.draw.rect(screen, BLACK, button_rect, 2)

    
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            action()


def run_user_file_action():
    file_path = "main.py"  
    subprocess.run(["python", file_path])


def run_ia_file_action():
    file_path = "ia.py"  
    subprocess.run(["python", file_path])

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.blit(background, (0, 0))
    pygame.mixer.music.play(1)
    
    create_button(200, 400, 200, 50, "Jouer", run_user_file_action)
    create_button(400, 400, 200, 50, "Jouer IA", run_ia_file_action)

    
    pygame.display.flip()


pygame.quit()
sys.exit()
