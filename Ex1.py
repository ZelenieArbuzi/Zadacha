user_input = input("Введите годы в формате 'гггг-гггг' (например, 1980-1990): ")
start_year, end_year = map(int, user_input.split("-"))

with open("Perepis.txt", "r") as file:
    count = 0
    before_1978_count = 0

    lines = file.readlines()
    for line in lines:

        count+=1
        print(line.strip())
        data = line.strip().split(".")
        name = line.strip().split(" ")

        data.reverse()
        if int(data[0]) < 1978:
            before_1978_count+=1

        if start_year <= int(data[0]) <= end_year:
            print("Родился в указанном диапозоне человек с ФИО:", name[0], name[2], name[4])
            print("Дата рождения: ", data[0])


print('Всего жителей:', count)
print('Жители родившиеся раньше 1978 года:', before_1978_count)


