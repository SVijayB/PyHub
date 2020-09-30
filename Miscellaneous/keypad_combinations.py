def getString(d):
    if d==2:
        return 'abc'
    if d==3:
        return 'def'
    if d==4:
        return 'ghi'
    if d==5:
        return 'jkl'
    if d==6:
        return 'mno'
    if d==7:
        return 'pqrs'
    if d==8:
        return 'tuv'
    if d==9:
        return 'wxyz'
    
def keypad(n):
    if n==0:
        return [""]
    smallint=n//10
    remainder=n%10
    smallout=keypad(smallint)
    options=getString(remainder)
    output=[]
    for s in smallout:
        for i in options:
            output.append(s+i)
    return output
    pass

n = int(input("Enter the number:"))
ans = keypad(n)
for s in ans:
    print(s)