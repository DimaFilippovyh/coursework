from turtle import *
from constans import HEIGHT, WIDTH



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

        if none_infected_people[n_day] < 0.002:
            print("All people infected")

        if rec_people[n_day] > 0.97 or n_day == 8000:
            print("All people recuperation!!!")
            break

        n_day += 1

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

        if rec_people[n_day] > 0.97 or n_day == 1100:
            print("All people recuperation!!!")
            break

        n_day += 1

    return infected_people, none_infected_people, rec_people, max_infected, day_max