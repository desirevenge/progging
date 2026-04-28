print('x y w z')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                if ((x <= y) or (y==w)) and ((x or z) == w) == True:
                    print(x, y, w, z)
