import time
from icecream import ic
import sys
from turtle import *



t = Turtle()

t.screen.setup(1200, 1000)
t.screen.title("Welcome to the lab 2!")
t.speed(0)

m = Turtle()
s = Turtle()
g = Turtle()
m.speed(0)
s.speed(0)
g.speed(0)
m.color('red')
s.color('blue')
g.color('green')

m.up()
m.goto(-600, 0)
s.up()
s.goto(-600, 0)
g.up()
g.goto(-600, 0)
m.down()
s.down()
g.down()




def proliferation_virus(all_people, k_recuperation, length_vir):
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

        tmp_rec_people = rec_people[n_day] + k_recuperation * infected_people[n_day - length_vir]  #  rec_people[n_day - length_vir]

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
    count_contakt = 1.001
    n_day = length_vir
    infected_people.append(0.005)
    none_infected_people.append(100)
    rec_people.append(0)

    while True:
        tmp_infected_people = count_contakt * infected_people[n_day] * none_infected_people[n_day] - \
            k_recuperation * infected_people[n_day - length_vir] + infected_people[n_day]

        if tmp_infected_people < 0:
            infected_people.append(0)
        else:
            infected_people.append(tmp_infected_people)


        tmp_none_infected_people = none_infected_people[n_day] - count_contakt * infected_people[n_day] * \
            none_infected_people[n_day]

        none_infected_people.append(tmp_none_infected_people)

        tmp_rec_people = rec_people[n_day] + k_recuperation * infected_people[n_day - length_vir]  #  rec_people[n_day - length_vir]

        rec_people.append(tmp_rec_people)

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
    infected_people.append(round(3 if all_people*0.0001 < 1 else all_people*0.0001))
    none_infected_people.append(all_people)
    rec_people.append(0)

    while True:
        tmp_infected = (count_contakt * infected_people[n_day] * none_infected_people[n_day]) / all_people
        tmp_infected_people = tmp_infected - k_recuperation * infected_people[n_day - length_vir] + infected_people[n_day]

        if tmp_infected_people < 0:
            infected_people.append(0)
        else:
            infected_people.append(round(tmp_infected_people))


        tmp_none_infected_people = none_infected_people[n_day] - tmp_infected

        none_infected_people.append(round(tmp_none_infected_people))

        tmp_rec_people = rec_people[n_day] + k_recuperation * infected_people[n_day - length_vir]  #  rec_people[n_day - length_vir]

        rec_people.append(round(tmp_rec_people))

        # count_contakt = # fix
        # k_recuperation = #fix


        print("infected_people: ", infected_people)
        print("none_infected_people: ", none_infected_people)
        print("rec_people: ", rec_people)
        print("n_day: ", n_day - length_vir)

        m.goto(-600+n_day, none_infected_people[n_day]/1600)
        s.goto(-600+n_day, infected_people[n_day]/1600)
        g.goto(-600+n_day, rec_people[n_day]/1600)

        print("\n")

        if none_infected_people[n_day] < 1:
            print("All people infected")

        if rec_people[n_day] > all_people:
            print("All people recuperation")
            break

        n_day += 1

        #time.sleep(1)


def proliferation_virus_4(all_people, k_recuperation, length_vir):
    Susceptible = [all_people]
    Infected = [25]
    Resistant = [0]
    rateSI=0.05
    rateIR=0.01

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



def main():
    
    t.screen.setup(1200, 1000)
    t.screen.title("Welcome to the lab 3!")
    t.speed(0)
    t.hideturtle()

    # proliferation_virus(600000, 0.01, 14)
    proliferation_virus_05(0.01, 14)
    # proliferation_virus_2(1000, 0.01, 14)
    proliferation_virus_3(600000, 0.01, 14)
    # proliferation_virus_4(600000, 0.01, 14)

    t.screen.exitonclick()
    t.screen.mainloop()


if __name__ == "__main__":
    main()









