def CreateMatris(rows,cols):
    m=[]

    while len(m) < rows:
        m.append([])
        while len(m[-1])<cols:
            m[-1].append(0)
            
    return 0


print(CreateMatris(3,3))