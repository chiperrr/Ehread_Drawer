def IntMassToBool (mass,width,height,x):
    massiv = []
    for i in range(width):
        massiv.append([])
        for j in range(height):
            if mass[i][j] >= x :
                massiv[i].append(True)
            else:
                massiv[i].append(False)
    return  massiv