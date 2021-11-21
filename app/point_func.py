from turtle import *
from constans import HEIGHT, WIDTH


class Lines:
    def __init__(self, color):
        self.color = color


def draw_coord(X_SCALE, Y_SCALE):
    Y_SCALE /= 5 
    X_SCALE *= 100 
    cor = Turtle()
    cor.speed(0)
    cor.up()
    for i in range(6):
        cor.goto(-WIDTH, -HEIGHT + 20 + i * Y_SCALE)
        cor.up()
        cor.goto(-WIDTH - 25, -HEIGHT + 20 + i * Y_SCALE)
        cor.write(str(i*20), font=("Arial", 16, "normal"))
        cor.goto(-WIDTH, -HEIGHT + 20 + i * Y_SCALE)
        cor.down()

    cor.setheading(90)
    cor.stamp()

    for i in range(10):
        cor.goto(-WIDTH + i * X_SCALE, -HEIGHT + 20)
        print(-WIDTH + i * X_SCALE)
        cor.up()
        cor.goto(-WIDTH + i * X_SCALE, -HEIGHT)
        cor.write(str(i*100), font=("Arial", 16, "normal"))
        cor.goto(-WIDTH + i * X_SCALE, -HEIGHT + 20)
        cor.down()

    cor.setheading(0)
    cor.stamp()

    # cor.goto(-WIDTH, -HEIGHT)
    # cor.down()
    # cor.goto(-WIDTH, HEIGHT)

    # cor.up()
    # cor.goto(-WIDTH, -HEIGHT + 20)
    # cor.down()
    # cor.goto(WIDTH, -HEIGHT + 20)


def draw_line(lst_point, line_cls):
    turt = Turtle()
    turt.speed(0)
    turt.up()
    turt.hideturtle()

    print(lst_point[-1])

    Y_SCALE = HEIGHT * 2 * 0.93
    X_SCALE = (WIDTH * 2 / lst_point[5]) * 0.9
    flag = False
    draw_coord(X_SCALE, Y_SCALE)

    def tmp_func(k, text):
        nonlocal flag
        turt.up()
        x_cor = -WIDTH

        turt.color(line_cls[k].color)
        for i, p in enumerate(lst_point[k]):
            x_cor += X_SCALE
            if i % 5 == 0:
                turt.goto(x_cor, -HEIGHT + 20 + p * Y_SCALE)
                turt.down()
                if i >= lst_point[4] and k == 0 and flag is False:
                    turt.write(str(f"Пик больных в %: {int(round(lst_point[3],2) * 100)}") + "__ День: " + str(lst_point[4]), font=("Arial", 16, "normal"))
                    flag = True

        turt.write(text, font=("Arial", 20, "normal"))

    tmp_func(0, "           Зараженные люди")
    tmp_func(1, "           Здоровые люди")
    tmp_func(2, "           Переболевшие люди")