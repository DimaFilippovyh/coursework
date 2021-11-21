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
        tmp_none_infected_people = k_recuperation * infected_people[n_day - length_vir]

        tomr_infected_people = tmp_infected_people - tmp_none_infected_people + infected_people[n_day]

        tomr_none_infected_people = none_infected_people[n_day] - tmp_infected_people

        tomr_rec_people = rec_people[n_day] + tmp_none_infected_people

        infected_people.append(tomr_infected_people)
        none_infected_people.append(tomr_none_infected_people)
        rec_people.append(tomr_rec_people)

        if (flag is False) and (tomr_infected_people < infected_people[n_day]):
            max_infected = infected_people[n_day]
            day_max = n_day
            flag = True

        if none_infected_people[n_day] < 0.002:
            print("All people infected")

        if rec_people[n_day] > 0.97:
            print("All people recuperation!!!")
            break

        n_day += 1

        # time.sleep(1)
    return max_infected, day_max, n_day


def proliferation_virus(k_recuperation, length_vir):
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
    count_contakt = 0.04  # top par
    # count_contakt = 0.1
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
            max_infected = infected_people[n_day]
            day_max = n_day
            inf.write(str(max_infected) + "___"+ str(n_day), font=("Arial", 10, "normal"))
            flag = True

        print("infected_people: ", infected_people)
        print("none_infected_people: ", none_infected_people)
        print("rec_people: ", rec_people)
        print("n_day: ", n_day - length_vir)
        print("\n")

        ni.goto(-600 + n_day, none_infected_people[n_day] * 400)
        inf.goto(-600 + n_day, infected_people[n_day] * 400)
        r.goto(-600 + n_day, rec_people[n_day] * 400)

        if none_infected_people[n_day] < 0.002:
            print("All people infected")

        if rec_people[n_day] > 0.97:
            print("All people recuperation!!!")
            break

        n_day += 1

        # time.sleep(1)
    return max_infected, day_max, n_day