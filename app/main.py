import os
from turtle import *
import pyautogui
from constans import WIDTH, HEIGHT
from point_func import Lines, draw_line
from parameter_graphs import graf_param_all
from proliferation_virus import proliferation_virus, proliferation_virus_test_rec


def init_turtle():
    t = Turtle()
    t.screen.setup(WIDTH * 2, HEIGHT * 2)
    t.screen.title("Welcome to the coursework!")
    t.speed(0)
    t.hideturtle()
    t.goto(0, -HEIGHT)
    t.dot(5)
    return t

def main():
    t = init_turtle()

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

        match n:
            case 1:
                graf_param_all("A")
                # pyautogui.screenshot('draw_param_A.png')
            case 2:
                graf_param_all("B")
                # pyautogui.screenshot('draw_param_B.png')
            case 3:
                graf_param_all("K")
                # pyautogui.screenshot('draw_param_K.png')
            case 4:
                lst_vir_res = proliferation_virus_test_rec(8)
                draw_line(lst_vir_res, (inf, ni, r))
            case 5:
                lst_vir_res = proliferation_virus(0.005, 14)
                draw_line(lst_vir_res, (inf, ni, r))
                # pyautogui.screenshot('draw_lines_virus.png')
            case _:
                print("bye-bye")
                break

    t.screen.exitonclick()
    t.screen.mainloop()


if __name__ == "__main__":
    main()