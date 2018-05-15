import pygame

screen = pygame.display.set_mode((500, 500))
running = True

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False
		
screen = pygame.display.set_mode((480, 640))

width_input = input("W?")
height_input = input("H?")
screen = pygame.display.set_mode((width_input, height_input))

