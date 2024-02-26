with open('space.txt', encoding='utf8') as f:
    # Открываем файл
    reader = f.readline()
    # Убираем шапку
    spis10 = []
    vrem_spis = []
    korab = []
    # Создаём списки для работы только с номерами и список для работы и с названиями, и с номерами кораблей
    for i in f:
        nom = i.split('*')
        nom1 = nom[0]
        nom2 = nom1.split('-')[1]
        if len(nom2) == 2:
            vrem_spis.append(nom2)
            vrem_spis.sort()
        else:
            spis10.append(nom2)
            spis10.sort()
        korab.append(nom1)
        #   Сортируем номера и создаём список с кораблями и их номерами
    for x in spis10:
        vrem_spis.append(x)
    vrem_spis = vrem_spis[0:10]
    # Сокращаем длину списка с номерами до 10
spis10 = []
for h in korab:
    h = h.split('-')
    spis10.append(h)
    # Заполняем spis10 другими списками, где первый элемент - название корабля, а второй - его номер
for g in vrem_spis:
    for n in spis10:
        # Сравниваем номер корабля из spis10 с тем, который указан в vrem_spis
        if g == n[-1]:
            print(n[0])
            # Выводим подходящие названия кораблей
