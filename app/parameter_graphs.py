from turtle import *
import numpy as np
from constans import HEIGHT, WIDTH
from proliferation_virus import proliferation_virus


def temp_func_draw(num, size, color, text, cor, lst_param, param):
        cor.up()
        x_cor = -WIDTH
        cor.goto(x_cor, 0)
        Y_SCALE = max(lst_param, key=lambda x: abs(x[num]))
        Y_SCALE = (HEIGHT * 2 / abs(Y_SCALE[num])) * 0.9

        X_SCALE = (WIDTH * 2 / len(lst_param)) * 0.8
        for ind, i in enumerate(lst_param):
            x_cor += X_SCALE
            if num != 3:
                cor.goto(x_cor, -HEIGHT + i[num] * Y_SCALE)
            else:
                cor.goto(x_cor, -HEIGHT)
            cor.down()
            cor.color(color)
            cor.dot(size, color)
            if ind % 2 == 0:
                if num == 2 and i[num] == 8000:
                    cor.write(f"+inf", font=("Arial", 18, "normal"))
                elif num == 0 or (num == 3 and param != "K"):
                    cor.write(f"{round(i[num],3)}", font=("Arial", 18, "normal"))
                else:
                    cor.write(i[num], font=("Arial", 18, "normal"))

        cor.write(text, font=("Arial", 20, "normal"))


def init_turtle():
    cor = Turtle()
    cor.speed(0)
    cor.up()
    x_cor = -WIDTH
    cor.goto(x_cor, 0)
    cor.down()
    return cor

def graf_param_all(param, rec=0.005, leng=14, con=0.04):
    if param == "A":
        nach = 0.02
        end = 2.00
        st = 0.02
    elif param == "B":
        nach = 0.001
        end = 2.00
        st = 0.001
    else:
        nach = 1
        end = 20
        st = 1

    cor = init_turtle()

    lst_param = []

    if param == "A":
        for i in np.arange(nach, end, st):
            tmp = proliferation_virus(rec, leng, i)[3:]
            if tmp[0] > 1:
                break
            tmp.append(i)
            lst_param.append(tmp)
    elif param == "B":
        for i in np.arange(nach, end, st):
            tmp = proliferation_virus(i, leng, con)[3:]
            tmp.append(i)
            lst_param.append(tmp)
            if tmp[0] < 0.01:
                break
    else:
        for i in np.arange(nach, end, st):
            tmp = proliferation_virus(rec, i, con)[3:]
            tmp.append(i)
            lst_param.append(tmp)

    temp_func_draw(0, 2, 'red', "           Макс. людей заразилось", cor, lst_param, param)
    temp_func_draw(1, 6, 'green', "           День в который макс. заразилось", cor, lst_param, param)
    temp_func_draw(2, 4, 'blue', "           Всего дней до выздоровления", cor, lst_param, param)
    temp_func_draw(3, 4, 'black', "           Значение параметра", cor, lst_param, param)