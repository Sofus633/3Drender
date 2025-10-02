import pygame
class Point:
	def __init__(self, position, radius=5, color=(100, 100, 0)):
		self.position = position
		self.radius = radius
		self.color = color
	def display(self, screen):
		pygame.draw.circle(screen,  self.color,  self.position.get(),self.radius)


