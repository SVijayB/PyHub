def gamingArray(arr):
    players=['ANDY', 'BOB']
    maxval=0
    i=0
    for v in arr:
        if v > maxval:
            maxval=v
            i+=1
    return players[bool (i%2)]

