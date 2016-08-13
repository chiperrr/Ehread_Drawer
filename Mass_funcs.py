def MaxBright (mass,width,height):        #Максимальное значение яркости
    Maximum = 0
    for i in range(width):
        for j in range(height):
            if Maximum < mass[i][j]:
                Maximum = mass[i][j]
    return Maximum

def MassMovement(mass,width,height,max):    #Смещение значений к самому яркому
    factor = 255- max
    for i in range(width):
        for j in range(height):
            mass[i][j] = mass[i][j] + factor


