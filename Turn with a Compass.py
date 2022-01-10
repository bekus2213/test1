def direction(facing, turn):
    compas = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')    #  Задаем начальный компас с 8 ветрами
    if facing not in compas:                                 #  Проверка принадлежности facing нашему компасу
        print('Неверно задано начальное направление')
        return
    if turn < -1080 or turn > 1080:                          #  Проверка границ поворота
        print('Величина поворота выходит за установленные границы')
        return
    if turn % 45 != 0:                                       #  Проверка кратности поворота 45
        print('Поворот не кратен 45')
        return

    position = compas.index(facing) * 45                     #  Заданная стороны света в градусах
    turn1 = (position + turn) % 360 // 45                    #  Новая позиция стороны света
    return compas[turn1]
