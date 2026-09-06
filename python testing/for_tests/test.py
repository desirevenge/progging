angle = 180

if angle % 90 == 0:
    if angle == 0:
        print('Нулевой')
    elif angle == 90:
        print('Прямой')
    elif angle == 180:
        print('Развёрнутый')
else:
    if 0 < angle < 90:
        print('Острый')
    elif 90 < angle < 180:
        print('Тупой')
    elif 180 < angle < 270:
        print('Выпуклый')
    else:
        print('Ни острый, ни тупой, ни выпуклый')

