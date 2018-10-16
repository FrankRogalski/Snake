from random import random

class Food:
    def __init__(self, canvas, width, height):
        self.__width = width
        self.__height = height
        self.__canvas = canvas
        self.__x = int(random() * (width // 10)) * 10
        self.__y = int(random() * (height // 10)) * 10
        self.__rect = self.__canvas.create_rectangle(self.__x, self.__y, self.__x + 10, self.__y + 10, fill="green")

    def recalc_position(self):
        self.__x = int(random() * (self.__width // 10)) * 10
        self.__y = int(random() * (self.__height // 10)) * 10
        self.__canvas.delete(self.__rect)
        self.__rect = self.__canvas.create_rectangle(self.__x, self.__y, self.__x + 10, self.__y + 10, fill="green")

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y