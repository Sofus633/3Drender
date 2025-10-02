from utils.vector import Vector2
from utils.useful import distance
from utils.point  import Point
from utils.math_vec import intersection
import pygame

class Plane:
	def __init__(self, position1, position2, focal=None):
		self.position1 = position1
		self.position2 = position2
		self.focal = focal
		if (self.focal == None):
			self.focal = Point(((position1 - position2)/2) + position1, 2, (240, 0, 0))	
	
	def get_normal(self):
		pass #TODO get normal of a plane

	def point_on_plane(self, point):
		normal = self.get_normal()
		distance_to_plane = distance(point, self.position1)
		distance_p1 = distance(project_vector(point, normal), point)
		
		#TODO get position on plane with focal 
		return distance_p1 + self.position1
	def display(self, screen):
		pygame.draw.line(screen, (100, 100, 0), self.position1.get(), self.position2.get())
		self.focal.display(screen)
		pygame.draw.circle(screen, ())
		
