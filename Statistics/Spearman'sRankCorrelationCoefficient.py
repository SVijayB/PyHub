n=int(input())
X=list(map(float,input().split()))
Y=list(map(float,input().split()))

Xr=[sorted(X).index(i) for i in X]
Yr=[sorted(Y).index(i) for i in  Y]

D=[(Xr[i]-Yr[i])**2 for i in range(n)]
xyr=1-((6*sum(D)/(n*(pow(n,2)-1))))

print(round(xyr,3))
