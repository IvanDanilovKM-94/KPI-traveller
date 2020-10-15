from abc import ABC
import pygame

class Character:
	def __init__(self, hp, name, icon, lvl):
		self.__health = hp
		self.__name = name
		self.__icon = icon
		self.__level = lvl

	def get_health(self):
		return self.__health

	def reduce_health(self):
		self.__health -= 1

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, new_name):
		self.__name = new_name

	@property
	def icon(self):
		return self.__icon

	@icon.setter
	def icon(self, new_icon):
		self.__icon = new_icon

	@property
	def level(self):
		return self.__level

	@level.setter
	def level(self, new_level):
		self.__level = new_level


class GUIElement(ABC):
	def __init__(self, x, y, height, width):
		self.__x = x
		self.__y = y
		self.__height = height
		self.__width = width

	@property	
	def x(self):
		return self.__x

	@x.setter
	def x(self, new_x):
		self.__x = new_x

	@property	
	def y(self):
		return self.__y

	@y.setter
	def y(self, new_y):
		self.__y = new_y

	@property	
	def height(self):
		return self.__height

	@height.setter
	def height(self, new_height):
		self.__height = new_height

	@property	
	def width(self):
		return self.__width

	@width.setter
	def width(self, new_wigth):
		self.__width = new_wigth

class Button(GUIElement):
	def __init__(self, x, y, height, width, image_path, scene):
		super().__init__(x, y, height, width)
		self.__image_path = image_path
		self.__scene = scene

	def draw(self, action=None):
		button_icon = pygame.image.load(self.__image_path)
		button_icon = pygame.transform.scale(button_icon, (self.width, self.height))
		rect = button_icon.get_rect(center=(self.x, self.y))
		self.__scene.blit(button_icon, rect)

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if self.x < mouse[0] < self.x + self.width:
			if self.y < mouse[1] < self.y + self.height:
				if click[0] == 1 and action is not None:
					action_on_click()
