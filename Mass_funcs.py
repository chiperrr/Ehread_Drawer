def MaxBright (mass,width,height):        #Максимальное значение яркости
    Maximum = 0
    for i in range(width):
        for j in range(height):
            if Maximum < mass[i][j]:
                Maximum = mass[i][j]
    return Maximum
def MinBright (mass,width,height):        #Минимальное значение яркости
    Minimum = 256
    for i in range(width):
        for j in range(height):
            if Minimum > mass[i][j]:
                Minimum = mass[i][j]
    return Minimum

def MassMovementToMax(mass,width,height,shift,minimum):       #Сдвиг к максимуму со сдвигом вниз
    factor  = 255 - minimum
    for i in range(width):
        for j in range(height):
            mass[i][j] = mass[i][j] + factor - shift
            if mass[i][j] > 255:
                mass[i][j] = 255
    return mass

def BlackAndWhite (mass,width,height,factor):                     #Разделение на черный и белый
    for i in range(width):
        for j in range(height):
            if mass[i][j] <= factor:
                mass[i][j] = 0
            else:
                mass[i][j] = 255
    return mass





def MassMovementToMaxBright(mass,width,height,max):    #Смещение значений к самому яркому
    factor = 255- max
    for i in range(width):
        for j in range(height):
            mass[i][j] = mass[i][j] + factor
    return mass

def MassToBool(mass,width,height):
    for i in range(width):
        for j in range(height):
            if mass[i][j] == 255:
                mass[i][j] = True
            else:
                mass[i][j] = False
    return mass



