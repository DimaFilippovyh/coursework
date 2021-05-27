import os
import time
from icecream import ic
import sys
from turtle import *
import pyautogui
import numpy as np
import func_vir as fv

WIDTH = 600
HEIGHT = 500


class Lines:
    def __init__(self, color):
        self.color = color



def draw_coord():
    cor = Turtle()
    cor.speed(0)
    cor.up()
    cor.goto(0, -HEIGHT)
    cor.down()
    cor.goto(0, HEIGHT)

    cor.up()
    cor.goto(-WIDTH, 0)
    cor.down()
    cor.goto(WIDTH, 0)


def draw_line(lst_point, line_cls):
    turt = Turtle()
    turt.speed(0)
    turt.up()
    turt.hideturtle()

    Y_SCALE = HEIGHT * 0.9
    X_SCALE = (WIDTH * 2 / lst_point[5]) * 0.9
    flag = False

    def tmp_func(k):
        nonlocal flag
        turt.up()
        x_cor = -WIDTH

        turt.color(line_cls[k].color)
        for i, p in enumerate(lst_point[k]):
            x_cor += X_SCALE
            if i % 15 == 0:
                turt.goto(x_cor, p * Y_SCALE)
                turt.down()
                if i >= lst_point[4] and k == 0 and flag is False:
                    turt.write(str(lst_point[3]) + "___" + str(lst_point[4]), font=("Arial", 10, "normal"))
                    flag = True

    tmp_func(0)
    tmp_func(1)
    tmp_func(2)


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

    cor = Turtle()
    cor.speed(0)
    cor.up()
    x_cor = -WIDTH
    cor.goto(x_cor, 0)
    cor.down()

    lst_param = []

    if param == "A":
        for i in np.arange(nach, end, st):
            tmp = proliferation_virus(rec, leng, i)[3:]
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

    def temp_func_draw(num, size, color, text):
        cor.up()
        x_cor = -WIDTH
        cor.goto(x_cor, 0)
        Y_SCALE = max(lst_param, key=lambda x: abs(x[num]))
        Y_SCALE = (HEIGHT / abs(Y_SCALE[num])) * 0.9
        X_SCALE = (WIDTH * 2 / len(lst_param)) * 0.8
        for ind, i in enumerate(lst_param):
            x_cor += X_SCALE
            if num != 3:
                cor.goto(x_cor, i[num] * Y_SCALE)
            else:
                cor.goto(x_cor, 0)
            cor.down()
            cor.color(color)
            cor.dot(size, color)
            if ind % 7 == 0:
                if num == 2 and i[num] == 8000:
                    cor.write(f"+inf", font=("Arial", 10, "normal"))
                elif num == 0 or (num == 3 and param != "K"):
                    cor.write(f"{i[num]:5.4}", font=("Arial", 10, "normal"))
                else:
                    cor.write(i[num], font=("Arial", 10, "normal"))
            # x_cor += 10
        cor.write(text, font=("Arial", 10, "normal"))

    temp_func_draw(0, 2, 'red', "           Макс. людей заразилось")
    temp_func_draw(1, 6, 'green', "           День в который макс. заразилось")
    temp_func_draw(2, 4, 'blue', "           Всего дней до выздоровления")
    temp_func_draw(3, 4, 'black', "           Значение параметра")


def enum_param(): # Доделать
    pass


def proliferation_virus(k_recuperation, length_vir, count_contakt=0.04):
    """
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    n_day - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    rec_people - выздоровевшие
    """
    infected_people = [0.0 for i in range(length_vir)]
    none_infected_people = [1 for i in range(length_vir)]
    rec_people = [0 for i in range(length_vir)]
    count_contakt = count_contakt  # 0.04 top par
    n_day = length_vir
    infected_people.append(0.001)
    none_infected_people.append(1)
    rec_people.append(0)
    max_infected, day_max = 0, 0
    flag = False

    while True:
        tmp_infected_people = count_contakt * infected_people[n_day] * none_infected_people[n_day]
        tmp_rec_people = k_recuperation * infected_people[n_day - length_vir]

        tomr_infected_people = tmp_infected_people - tmp_rec_people + infected_people[n_day]

        tomr_none_infected_people = none_infected_people[n_day] - tmp_infected_people

        tomr_rec_people = rec_people[n_day] + tmp_rec_people

        infected_people.append(tomr_infected_people)
        none_infected_people.append(tomr_none_infected_people)
        rec_people.append(tomr_rec_people)

        if (flag is False) and (tomr_infected_people < infected_people[n_day]):
            day_max, max_infected = n_day, infected_people[n_day]
            flag = True

        # print("infected_people: ", infected_people)
        # print("none_infected_people: ", none_infected_people)
        # print("rec_people: ", rec_people)
        # print("n_day: ", n_day - length_vir)
        # print("\n")

        if none_infected_people[n_day] < 0.002:
            print("All people infected")

        if rec_people[n_day] > 0.97 or n_day == 8000:
            print("All people recuperation!!!")
            break

        n_day += 1

        # time.sleep(1)
    return [infected_people, none_infected_people, rec_people, max_infected, day_max, n_day]


def proliferation_virus_test_rec(length_vir):
    """
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    n_day - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    rec_people - выздоровевшие
    """
    ####
    inf = Turtle()
    ni = Turtle()
    r = Turtle()
    inf.speed(0)
    ni.speed(0)
    r.speed(0)
    inf.color('red')
    ni.color('blue')
    r.color('green')

    inf.up()
    ni.up()
    r.up()
    inf.goto(-WIDTH, 0)
    ni.goto(-WIDTH, HEIGHT)
    r.goto(-WIDTH, 0)
    inf.down()
    ni.down()
    r.down()
    ####
    infected_people = [0.0 for i in range(length_vir + 3)]
    none_infected_people = [1 for i in range(length_vir + 3)]
    rec_people = [0 for i in range(length_vir + 3)]
    lst_chance_of_recovery = [1 / 16, 1 / 16, 1 / 8, 1 / 2, 1 / 8, 1 / 16, 1 / 16]
    count_contakt = 0.3  # top par
    n_day = length_vir + 3
    infected_people.append(0.001)
    none_infected_people.append(1)
    rec_people.append(0)
    max_infected, day_max = 0, 0
    flag = False

    while True:
        tmp_infected_people = count_contakt * infected_people[n_day] * none_infected_people[n_day]
        # tmp_none_infected_people = k_recuperation * infected_people[n_day - length_vir]

        # tmp_none_infected_people = sum(
        #     [infected_people[n_day - length_vir - 3 + i] * lst_chance_of_recovery[i] for i in range(7)])

        # tmp_rec_people = [abs(
        #     none_infected_people[n_day - length_vir - 3 + i] - none_infected_people[n_day - length_vir - 3 + i - 1]) * \
        #                   lst_chance_of_recovery[i] for i in range(7)]
        # tmp_rec_people = sum(tmp_rec_people)

        tmp_rec_people = [count_contakt * infected_people[n_day - length_vir - 3 + i] * 
                        none_infected_people[n_day - length_vir - 3 + i] * 
                        lst_chance_of_recovery[i] for i in range(7)]
        tmp_rec_people = sum(tmp_rec_people)

        tomr_infected_people = tmp_infected_people - tmp_rec_people + infected_people[n_day]

        tomr_none_infected_people = none_infected_people[n_day] - tmp_infected_people

        tomr_rec_people = rec_people[n_day] + tmp_rec_people

        infected_people.append(tomr_infected_people)
        none_infected_people.append(tomr_none_infected_people)
        rec_people.append(tomr_rec_people)

        if (flag is False) and (tomr_infected_people < infected_people[n_day]):
            max_infected = str(infected_people[n_day])
            day_max = str(n_day)
            inf.write(str(max_infected) + "___" + str(n_day), font=("Arial", 10, "normal"))
            flag = True

        # print("infected_people: ", infected_people)
        # print("none_infected_people: ", none_infected_people)
        # print("rec_people: ", rec_people)
        # print("n_day: ", n_day - length_vir)
        # print("\n")

        ni.goto(-WIDTH + n_day, none_infected_people[n_day] * HEIGHT)
        inf.goto(-WIDTH + n_day, infected_people[n_day] * HEIGHT)
        r.goto(-WIDTH + n_day, rec_people[n_day] * HEIGHT)

        if none_infected_people[n_day] < 0.002:
            print("All people infected")

        if rec_people[n_day] > 0.97 or n_day == 1100:
            print("All people recuperation!!!")
            break

        n_day += 1

        # time.sleep(1)
    return infected_people, none_infected_people, rec_people, max_infected, day_max


def main():
    t = Turtle()
    t.screen.setup(WIDTH * 2, HEIGHT * 2)
    t.screen.title("Welcome to the coursework!")
    t.speed(0)
    t.hideturtle()
    draw_coord()

    inf = Lines('red')
    ni = Lines('blue')
    r = Lines('green')

    while True:
        os.system("clear")
        print("""
        1. Рисунок с параметром А
        2. Рисунок с параметром В
        3. Рисунок с параметром К
        4. Новое выздоровление
        5. Отрисовка графиков
        Другое. Выйти
        """)
        n = int(input("Что хотите увидеть? \n"))

        t.screen.clearscreen()
        draw_coord()

        if n == 1:
            graf_param_all("A")
            pyautogui.screenshot('draw_param_A.png')

        elif n == 2:
            graf_param_all("B")
            pyautogui.screenshot('draw_param_B.png')

        elif n == 3:
            graf_param_all("K")
            pyautogui.screenshot('draw_param_K.png')

        elif n == 4:
            lst_vir_res = proliferation_virus_test_rec(8)
            draw_line(lst_vir_res, (inf, ni, r))

        elif n == 5:
            lst_vir_res = proliferation_virus(0.005, 14)
            draw_line(lst_vir_res, (inf, ni, r))
            pyautogui.screenshot('draw_lines_virus.png')
        else:
            print("bye-bye")
            break

    t.screen.exitonclick()
    t.screen.mainloop()


if __name__ == "__main__":
    main()




def proliferation_virus_for_par(k_recuperation, length_vir, cc_tmp):
    """
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    n_day - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    rec_people - выздоровевшие
    """
    infected_people = [0 for i in range(length_vir)]
    none_infected_people = [1 for i in range(length_vir)]
    rec_people = [0 for i in range(length_vir)]
    count_contakt = cc_tmp
    n_day = length_vir
    infected_people.append(0.001)
    none_infected_people.append(1)
    rec_people.append(0)
    max_infected, day_max = 0, 0
    flag = False

    while True:
        tmp_infected_people = count_contakt * infected_people[n_day] * none_infected_people[n_day]
        tmp_rec_people = k_recuperation * infected_people[n_day - length_vir]

        tomr_infected_people = tmp_infected_people - tmp_rec_people + infected_people[n_day]

        tomr_none_infected_people = none_infected_people[n_day] - tmp_infected_people

        tomr_rec_people = rec_people[n_day] + tmp_rec_people

        infected_people.append(tomr_infected_people)
        none_infected_people.append(tomr_none_infected_people)
        rec_people.append(tomr_rec_people)

        if (flag is False) and (tomr_infected_people < infected_people[n_day]):
            max_infected = infected_people[n_day]
            day_max = n_day
            flag = True

        # if none_infected_people[n_day] < 0.002:
        #     print("All people infected")

        if rec_people[n_day] > 0.97 or n_day == 1100:
            # print("All people recuperation!!!")
            break

        n_day += 1

        # time.sleep(1)
    return [max_infected, day_max, n_day]



def proliferation_virus(k_recuperation, length_vir):
    """
    на всякий случай
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    n_day - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    rec_people - выздоровевшие
    """
    infected_people = [0.0 for i in range(length_vir)]
    none_infected_people = [1 for i in range(length_vir)]
    rec_people = [0 for i in range(length_vir)]
    count_contakt = 0.04  # top par
    n_day = length_vir
    infected_people.append(0.001)
    none_infected_people.append(1)
    rec_people.append(0)
    max_infected, day_max = 0, 0
    flag = False

    while True:
        tmp_infected_people = count_contakt * infected_people[n_day] * none_infected_people[n_day]
        tmp_none_infected_people = k_recuperation * infected_people[n_day - length_vir]

        tomr_infected_people = tmp_infected_people - tmp_none_infected_people + infected_people[n_day]

        tomr_none_infected_people = none_infected_people[n_day] - tmp_infected_people

        tomr_rec_people = rec_people[n_day] + tmp_none_infected_people

        infected_people.append(tomr_infected_people)
        none_infected_people.append(tomr_none_infected_people)
        rec_people.append(tomr_rec_people)

        if (flag is False) and (tomr_infected_people < infected_people[n_day]):
            inf.write(str(infected_people[n_day]) + "___" + str(n_day), font=("Arial", 10, "normal"))
            flag = True

        print("infected_people: ", infected_people)
        print("none_infected_people: ", none_infected_people)
        print("rec_people: ", rec_people)
        print("n_day: ", n_day - length_vir)
        print("\n")

        ni.goto(-WIDTH + n_day, none_infected_people[n_day] * HEIGHT)
        inf.goto(-WIDTH + n_day, infected_people[n_day] * HEIGHT)
        r.goto(-WIDTH + n_day, rec_people[n_day] * HEIGHT)

        if none_infected_people[n_day] < 0.002:
            print("All people infected")

        if rec_people[n_day] > 0.97:
            print("All people recuperation!!!")
            break

        n_day += 1

        # time.sleep(1)
    return infected_people, none_infected_people, rec_people


def graf_param_for_A():
    cor = Turtle()
    cor.speed(0)
    cor.up()
    x_cor = -500
    cor.goto(x_cor, 0)

    for i in np.arange(0.02, 2.00, 0.02):
        lst_param = fv.proliferation_virus_for_par(0.005, 14, i)
        cor.goto(x_cor, lst_param[0] * 400)
        cor.dot(2, "red")
        if x_cor % 70 == 0:
            cor.write(f"{lst_param[0]:4.3}", font=("Arial", 10, "normal"))

        cor.goto(x_cor, lst_param[1] / 3)
        cor.dot(6, "green")
        if x_cor % 70 == 0:
            cor.write(lst_param[1], font=("Arial", 10, "normal"))

        cor.goto(x_cor, lst_param[2] / 3)
        cor.dot(4, "blue")
        if x_cor % 70 == 0:
            cor.write(lst_param[2], font=("Arial", 10, "normal"))

        if x_cor % 70 == 0:
            cor.goto(x_cor, -50)
            cor.write(i, font=("Arial", 10, "normal"))

        x_cor += 10
        cor.goto(x_cor, 0)


def graf_param_for_B():
    cor = Turtle()
    cor.speed(0)
    cor.up()
    x_cor = -500
    cor.goto(x_cor, 0)

    for i in np.arange(0.001, 2.00, 0.001):
        lst_param = fv.proliferation_virus_for_par(i, 14, 0.04)
        cor.goto(x_cor, lst_param[0] * 400)
        cor.dot(2, "red")
        if x_cor % 30 == 0:
            cor.write(f"{lst_param[0]:4.3}", font=("Arial", 10, "normal"))

        cor.goto(x_cor, lst_param[1] / 3)
        cor.dot(6, "green")
        if x_cor % 70 == 0:
            cor.write(lst_param[1], font=("Arial", 10, "normal"))

        cor.goto(x_cor, lst_param[2] / 3)
        cor.dot(4, "blue")
        if x_cor % 30 == 0:
            cor.write(lst_param[2], font=("Arial", 10, "normal"))

        if x_cor % 30 == 0:
            cor.goto(x_cor, -50)
            cor.write(i, font=("Arial", 10, "normal"))

        x_cor += 10
        cor.goto(x_cor, 0)


def graf_param_for_K():
    cor = Turtle()
    cor.speed(0)
    cor.up()
    x_cor = -500
    cor.goto(x_cor, 0)

    for i in range(1, 20, 1):
        lst_param = proliferation_virus_for_par(0.005, i, 0.04)
        cor.goto(x_cor, lst_param[0] * 400)
        cor.dot(2, "red")
        if x_cor % 70 == 0:
            cor.write(f"{lst_param[0]:4.3}", font=("Arial", 10, "normal"))

        cor.goto(x_cor, lst_param[1] / 3)
        cor.dot(6, "green")
        if x_cor % 70 == 0:
            cor.write(lst_param[1], font=("Arial", 10, "normal"))

        cor.goto(x_cor, lst_param[2] / 3)
        cor.dot(4, "blue")
        if x_cor % 70 == 0:
            cor.write(lst_param[2], font=("Arial", 10, "normal"))

        if x_cor % 70 == 0:
            cor.goto(x_cor, -50)
            cor.write(i, font=("Arial", 10, "normal"))

        x_cor += 10
        cor.goto(x_cor, 0)


def proliferation_virus_00(all_people, k_recuperation, length_vir):
    """
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    n_day - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    rec_people - выздоровевшие
    """
    infected_people = [0 for i in range(length_vir)]
    none_infected_people = [all_people for i in range(length_vir)]
    rec_people = [0 for i in range(length_vir)]
    # count_contakt = 0.0015 
    # count_contakt = 0.0007
    count_contakt = 0.00025
    n_day = length_vir
    infected_people.append(50)
    none_infected_people.append(all_people)
    rec_people.append(0)

    while True:
        tmp_infected_people = count_contakt * infected_people[n_day] * none_infected_people[n_day] - \
                              k_recuperation * infected_people[n_day - length_vir] + infected_people[n_day]

        if tmp_infected_people < 0:
            infected_people.append(0)
        else:
            infected_people.append(round(tmp_infected_people))

        tmp_none_infected_people = none_infected_people[n_day] - count_contakt * infected_people[n_day] * \
                                   none_infected_people[n_day]

        none_infected_people.append(round(tmp_none_infected_people))

        tmp_rec_people = rec_people[n_day] + k_recuperation * infected_people[
            n_day - length_vir]  # rec_people[n_day - length_vir]

        rec_people.append(round(tmp_rec_people))

        # count_contakt = # fix
        # k_recuperation = #fix

        print("infected_people: ", infected_people)
        print("none_infected_people: ", none_infected_people)
        print("rec_people: ", rec_people)
        print("n_day: ", n_day - length_vir)

        print("\n")

        if none_infected_people[n_day] < 1:
            print("All people infected")

        if rec_people[n_day] > all_people:
            print("All people recuperation")
            break

        n_day += 1

        time.sleep(1)


def proliferation_virus_05(k_recuperation, length_vir):
    """
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    n_day - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    rec_people - выздоровевшие
    """
    infected_people = [0 for i in range(length_vir)]
    none_infected_people = [100 for i in range(length_vir)]
    rec_people = [0 for i in range(length_vir)]
    # count_contakt = 0.0015 
    # count_contakt = 0.0007
    # count_contakt = 1.001
    count_contakt = 0.07
    n_day = length_vir
    infected_people.append(0.005)
    none_infected_people.append(100)
    rec_people.append(0)

    while True:
        tmp_infected_people = count_contakt * infected_people[n_day] * none_infected_people[n_day] / 100
        tmp_none_infected_people = k_recuperation * infected_people[n_day - length_vir]

        tomr_infected_people = tmp_infected_people - tmp_none_infected_people + infected_people[n_day]

        tomr_none_infected_people = none_infected_people[n_day] - tmp_infected_people

        tomr_rec_people = rec_people[n_day] + tmp_none_infected_people

        infected_people.append(tomr_infected_people)
        none_infected_people.append(tomr_none_infected_people)
        rec_people.append(tomr_rec_people)

        # count_contakt = # fix
        # k_recuperation = #fix

        print("infected_people: ", infected_people)
        print("none_infected_people: ", none_infected_people)
        print("rec_people: ", rec_people)
        print("n_day: ", n_day - length_vir)

        print("\n")

        if none_infected_people[n_day] < 1:
            print("All people infected")

        if rec_people[n_day] > 100:
            print("All people recuperation")
            break

        n_day += 1

        time.sleep(1)


def proliferation_virus_3(all_people, k_recuperation, length_vir):
    """
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    n_day - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    rec_people - выздоровевшие
    """
    infected_people = [0 for i in range(length_vir)]
    none_infected_people = [all_people for i in range(length_vir)]
    rec_people = [0 for i in range(length_vir)]
    # count_contakt = 0.0015 
    # count_contakt = 0.0007
    count_contakt = 0.05
    n_day = length_vir
    infected_people.append(round(3 if all_people * 0.0001 < 1 else all_people * 0.0001))
    none_infected_people.append(all_people)
    rec_people.append(0)

    while True:
        tmp_infected = (count_contakt * infected_people[n_day] * none_infected_people[n_day]) / all_people
        tmp_infected_people = tmp_infected - k_recuperation * infected_people[n_day - length_vir] + infected_people[
            n_day]

        if tmp_infected_people < 0:
            infected_people.append(0)
        else:
            infected_people.append(round(tmp_infected_people))

        tmp_none_infected_people = none_infected_people[n_day] - tmp_infected

        none_infected_people.append(round(tmp_none_infected_people))

        tmp_rec_people = rec_people[n_day] + k_recuperation * infected_people[
            n_day - length_vir]  # rec_people[n_day - length_vir]

        rec_people.append(round(tmp_rec_people))

        # count_contakt = # fix
        # k_recuperation = #fix

        print("infected_people: ", infected_people)
        print("none_infected_people: ", none_infected_people)
        print("rec_people: ", rec_people)
        print("n_day: ", n_day - length_vir)

        m.goto(-600 + n_day, none_infected_people[n_day] / 1600)
        s.goto(-600 + n_day, infected_people[n_day] / 1600)
        g.goto(-600 + n_day, rec_people[n_day] / 1600)

        print("\n")

        if none_infected_people[n_day] < 1:
            print("All people infected")

        if rec_people[n_day] > all_people:
            print("All people recuperation")
            break

        n_day += 1

        # time.sleep(1)


def proliferation_virus_test_rec(length_vir):
    """
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    n_day - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    rec_people - выздоровевшие
    """
    infected_people = [0.0 for i in range(length_vir + 3)]
    none_infected_people = [1 for i in range(length_vir + 3)]
    rec_people = [0 for i in range(length_vir + 3)]
    lst_chance_of_recovery = [1 / 16, 1 / 16, 1 / 8, 1 / 2, 1 / 8, 1 / 16, 1 / 16]
    count_contakt = 0.08  # top par
    n_day = length_vir + 3
    infected_people.append(0.001)
    none_infected_people.append(1)
    rec_people.append(0)
    max_infected, day_max = 0, 0
    flag = False

    while True:
        tmp_infected_people = count_contakt * infected_people[n_day] * none_infected_people[n_day]
        # tmp_none_infected_people = k_recuperation * infected_people[n_day - length_vir]

        # tmp_none_infected_people = sum(
        #     [infected_people[n_day - length_vir - 3 + i] * lst_chance_of_recovery[i] for i in range(7)])

        tmp_rec_people = [infected_people[n_day - length_vir - 3 + i] * lst_chance_of_recovery[i] for i in range(7)]

        tmp_rec_people = sum(tmp_rec_people)

        tomr_infected_people = tmp_infected_people - tmp_rec_people + infected_people[n_day]

        tomr_none_infected_people = none_infected_people[n_day] - tmp_infected_people

        tomr_rec_people = rec_people[n_day] + tmp_rec_people

        infected_people.append(tomr_infected_people)
        none_infected_people.append(tomr_none_infected_people)
        rec_people.append(tomr_rec_people)

        if (flag is False) and (tomr_infected_people < infected_people[n_day]):
            max_infected = infected_people[n_day]
            day_max = n_day
            inf.write(str(max_infected) + "___" + str(n_day), font=("Arial", 10, "normal"))
            flag = True

        print("infected_people: ", infected_people)
        print("none_infected_people: ", none_infected_people)
        print("rec_people: ", rec_people)
        print("n_day: ", n_day - length_vir)
        print("\n")

        ni.goto(-WIDTH + n_day, none_infected_people[n_day] * HEIGHT)
        inf.goto(-WIDTH + n_day, infected_people[n_day] * HEIGHT)
        r.goto(-WIDTH + n_day, rec_people[n_day] * HEIGHT)

        if none_infected_people[n_day] < 0.002:
            print("All people infected")

        if rec_people[n_day] > 0.97:
            print("All people recuperation!!!")
            break

        n_day += 1

        time.sleep(1)
    return infected_people, none_infected_people, rec_people


def proliferation_virus_4(all_people, k_recuperation, length_vir):
    Susceptible = [all_people]
    Infected = [25]
    Resistant = [0]
    rateSI = 0.05
    rateIR = 0.01

    for step in range(1, 1000):
        S_to_I = (rateSI * Susceptible[-1] * Infected[-1]) / all_people
        I_to_R = Infected[-1] * rateIR
        Susceptible.append(round(Susceptible[-1] - S_to_I))
        Infected.append(round(Infected[-1] + S_to_I - I_to_R))
        Resistant.append(round(Resistant[-1] + I_to_R))

        print(Susceptible)
        print(Infected)
        print(Resistant)

        time.sleep(1)
