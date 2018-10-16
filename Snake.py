import tkinter
from Food import Food
from RealSnake import Snake

def loop():
    if snake.update(food):
        top.after(50, loop)
    else:
        print("Game over!")

def key(event, err=""):
    if event.char == "w":
        snake.upwards()
    elif event.char == "a":
        snake.left()
    elif event.char == "s":
        snake.down()
    elif event.char == "d":
        snake.right()

top = tkinter.Tk()

heigth, width = 600, 600
canvas = tkinter.Canvas(top, height=heigth, width=width)

food = Food(canvas, width, heigth)
snake = Snake(canvas, width, heigth)

top.bind_all('<Key>', key)

canvas.pack()
top.after(0, loop)

top.mainloop()