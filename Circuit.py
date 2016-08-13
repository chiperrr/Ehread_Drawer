def  Findcircuit(mass,width,height):
    queue = []
    circuit = []
    for i in range(width):
        for j in range(height):
            if mass[i,j] == False:
                queue.append([i,j])
    length = len (queue)

    for i in range(length):
        if mass[(queue[i][0]-1)][queue[i][1]] or mass[(queue[i][0]+1)][queue[i][1]] or mass[(queue[i][0])][queue[i][1]-1] or mass[(queue[i][0])][queue[i][1]+1]:
            circuit.append([queue[i][0],queue[i],[1]])

    return circuit




