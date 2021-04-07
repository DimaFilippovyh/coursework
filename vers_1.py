import time
from icecream import ic
import sys
from turtle import *



t = Turtle()

t.screen.setup( 1200, 1000 )
t.screen.title( "Welcome to the lab 2!" )
# t.screen.bgpic("world map.png")
t.speed( 0 )

i = Turtle()
ni = Turtle()
r = Turtle()
i.speed( 0 ) 
ni.speed( 0 )
r.speed( 0 )
i.color( 'red' )
ni.color( 'blue' )
r.color( 'green' )

i.up()
i.goto( -600, 0 )
ni.up()
ni.goto( -600, 400 )
r.up()
r.goto( -600, 0 )
i.down()
ni.down()
r.down()




def proliferation_virus( k_recuperation, length_vir ):
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
    # count_contakt = 0.0015 
    # count_contakt = 0.0007
    # count_contakt = 1.001
    count_contakt = 0.04
    # count_contakt = 0.1
    n_day = length_vir
    infected_people.append(0.001)
    none_infected_people.append(1)
    rec_people.append(0)

    while True:
        tmp_infected_people = count_contakt * infected_people[n_day] * none_infected_people[n_day]
        tmp_none_infected_people = k_recuperation * infected_people[n_day - length_vir] 


        tomr_infected_people = tmp_infected_people - tmp_none_infected_people + infected_people[n_day]

        tomr_none_infected_people = none_infected_people[n_day] - tmp_infected_people

        tomr_rec_people = rec_people[n_day] + tmp_none_infected_people


        infected_people.append(tomr_infected_people)
        none_infected_people.append(tomr_none_infected_people)
        rec_people.append(tomr_rec_people)


        print("infected_people: ", infected_people)
        print("none_infected_people: ", none_infected_people)
        print("rec_people: ", rec_people)
        print("n_day: ", n_day - length_vir)
        print("\n")


        ni.goto(-600+n_day, none_infected_people[n_day] * 400)
        i.goto(-600+n_day, infected_people[n_day] * 400)
        r.goto(-600+n_day, rec_people[n_day] * 400)


        if none_infected_people[n_day] < 0.002:
            print("All people infected")

        if rec_people[n_day] > 0.98:
            print("All people recuperation!!!")
            break

        n_day += 1

        # time.sleep(1)





def main():
    t.screen.setup( 1200, 1000 )
    t.screen.title( "Welcome to the lab 3!" )
    t.speed( 0 )
    t.hideturtle()

    proliferation_virus( 0.005, 14 )

    t.screen.exitonclick()
    t.screen.mainloop()






if __name__ == "__main__":
    main()





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

