temp = 9999999
v = 5
G = [[0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]]

selected = [0, 0, 0, 0, 0]
no_edge = 0

selected[0] = True

print("Edge : Weight\n")
while no_edge < (v - 1):
    minimum = temp
    x = 0
    y = 0
    for i in range(v):
        if selected[i]:
            for j in range(v):
                if (not selected[j]) and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j

    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1
