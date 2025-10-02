import pygame
from utils.vector import Vector2
from utils.settings import screen
from utils.point import Point
from utils.plane import Plane

point1 = Point(Vector2(150, 40))
plane1 = Plane(Vector2(100, 10), Vector2(100, 110), Point(Vector2(50, 55), 2, (240, 0 , 0)))

Running = True
while Running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Running = False
	plane1.display(screen)
	point1.display(screen)
	pygame.display.flip()
	screen.fill((200, 200, 200))

