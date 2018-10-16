from collections import deque

class Snake:
    def __init__(self, canvas, width, height):
        self.__width = width
        self.__height = height
        self.__canvas = canvas
        self.__body = deque([self.__canvas.create_rectangle(0, 0, 10, 10, fill="blue")])
        self.__move = {"x": 0, "y": 0}

    def upwards(self):
        if self.__move["y"] != 10:
            self.__move["x"] = 0
            self.__move["y"] = -10

    def down(self):
        if self.__move["y"] != -10:
            self.__move["x"] = 0
            self.__move["y"] = 10

    def left(self):
        if self.__move["x"] != 10:
            self.__move["x"] = -10
            self.__move["y"] = 0

    def right(self):
        if self.__move["x"] != -10:
            self.__move["x"] = 10
            self.__move["y"] = 0

    def __eat(self, food):
        coords = self.__canvas.coords(self.__body[0])
        if coords[0] == food.get_x() and coords[1] == food.get_y():
            coords = self.__canvas.coords(self.__body[len(self.__body) - 1])
            self.__body.append(self.__canvas.create_rectangle(coords[0], coords[1], coords[0] + 10, coords[1] + 10, fill="black"))
            food.recalc_position()

    def __check_wall_collision(self, coords, head):
        if coords[0] >= self.__width:
            self.__canvas.move(head, -self.__width, 0)
            coords = self.__canvas.coords(head)

        elif coords[0] < 0:
            self.__canvas.move(head, self.__width, 0)
            coords = self.__canvas.coords(head)

        elif coords[1] >= self.__height:
            self.__canvas.move(head, 0, -self.__height)
            coords = self.__canvas.coords(head)

        elif coords[1] < 0:
            self.__canvas.move(head, 0, self.__height)
            coords = self.__canvas.coords(head)
        return coords

    def __check_self_collision(self, coords):
        first = True
        for bodypart in self.__body:
            if not first and self.__canvas.coords(bodypart) == coords:
                return False
            else:
                first = False

        return True
    
    def update(self, food):
        self.__eat(food)

        first = self.__body[0]
        last = self.__body.pop()

        coords_first = self.__canvas.coords(first)
        coords_last = self.__canvas.coords(last)

        delta_x = coords_first[0] - coords_last[0] + self.__move["x"]
        delta_y = coords_first[1] - coords_last[1] + self.__move["y"]
        self.__canvas.move(last, delta_x, delta_y)

        coords_after_move = self.__canvas.coords(last)
        coords_after_move = self.__check_wall_collision(coords_after_move, last)

        self.__canvas.itemconfig(first, fill="black")
        self.__canvas.itemconfig(last, fill="blue")

        self.__body.appendleft(last)

        return self.__check_self_collision(coords_after_move)
