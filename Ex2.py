with open("travels.txt", "r") as file:
    day1=0
    day2=0
    day3=0
    lipki=0
    distance_in_day=0
    departure_points = {}
    destination_points = {}
    fuel_consumption = {}


    lines = file.readlines()
    for line in lines:

        point = line.strip().split(" ")
        date = point[0]
        departure = point[2]
        destination = point[3]
        distance = int(point[4])
        fuel = int(point[5])
        cargo = int(point[6])



        if date == '1':
            day1+=cargo
            distance_in_day+=distance
        if date == '2':
            day2+= cargo
        if date == '3':
            day3+cargo

        if point[2]=='Липки':
            lipki+=cargo

        if departure in departure_points:
            departure_points[departure] += cargo
        else:
            departure_points[departure] = cargo

        # Добавляем пункт назначения и его массу груза в словарь destination_points
        if destination in destination_points:
            destination_points[destination] += cargo
        else:
            destination_points[destination] = cargo

        # Добавляем пункт назначения и его средний расход бензина в словарь fuel_consumption
        if destination in fuel_consumption:
            fuel_consumption[destination].append(fuel/distance)
        else:
            fuel_consumption[destination] = [fuel/distance]



    if day2 <= day1 >= day3:
            print('1 октября перевезено больше всего грузов и его суммарный объем:', day2)
    elif day1 <= day2 >= day3:
            print('2 октября перевезено больше всего грузов и его суммарный объем:', day2)
    elif day1 <= day3 >= day2:
            print('3 октября перевезено больше всего грузов и его суммарный объем:', day2)

    print('Масса всех грузов, отправленных из поселка «Липки»:',lipki)
    print('Расстояние за 1 октября:',distance_in_day)

    print("Количество различных пунктов отправления:", len(departure_points))
    print("Названия различных пунктов отправления:", list(departure_points.keys()))
    print("Масса грузов, отправленных из каждого пункта отправления:")
    for departure, cargo in departure_points.items():
        print(departure, "-", cargo)

    print("Количество различных пунктов назначения:", len(destination_points))
    print("Названия различных пунктов назначения:", list(destination_points.keys()))
    print("Масса грузов, отправленных в каждый пункт назначения:")
    for destination, cargo in destination_points.items():
        print(destination, "-", cargo)

    max_avg_fuel_consumption = 0
    destination_with_max_avg_fuel_consumption = ""

    for destination, fuel_list in fuel_consumption.items():
        avg_fuel_consumption = sum(fuel_list) / len(fuel_list)
        if avg_fuel_consumption > max_avg_fuel_consumption:
            max_avg_fuel_consumption = avg_fuel_consumption
            destination_with_max_avg_fuel_consumption = destination

    print("Пункт назначения с наибольшим средним расходом бензина:", destination_with_max_avg_fuel_consumption)