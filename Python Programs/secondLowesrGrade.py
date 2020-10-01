if __name__ == '__main__':

    arr=[]
    res=[]
    cnt=0
    n=int(input())
    if n>=2 and n<=5:
        for _ in range(n):
            name = input()
            score = float(input())
            arr.append([score, name])

    arr.sort()
    for i in range(1,n):
        if arr[i-1][0]!=arr[i][0]:
            res.append(arr[i][1])
            i+=1
            cnt+=1
            while(arr[i-1][0]==arr[i][0] and i<n):
                res.append(arr[i][1])
                i+=1
                cnt+=1
            break
    res.sort()            
    for i in range(0,cnt):
        print(res[i])

