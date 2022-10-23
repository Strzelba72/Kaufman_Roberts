import math

#define variables
M=2
V=3
a=[0.4,1]
t=[1,2]
M2=2
V2=3
a2=[1.2,0.6]
t2=[1,2]
M3=2
V3=3
a3=[1.6,0.4]
t3=[1,2]
M4=2
V4=3
a4=[0.8,0.8]
t4=[1,2]
#funkcji obliczająca wartości X
def calc_x(V,M,a,t):
    x=[1]*(V+1)
    for n in range(1,V+1):
        sum=0
        for i in range(0,M):
            if n>=t[i]:
                sum += a[i]*t[i]*x[n-t[i]]
        #print(x)
        x[n]=sum/n
    return x
#obliczenie P0 
def calc_p0(x):
    return 1/sum(x)
#funkcja obliczająca pozostałe wartości P
def calc_pn(X,V,M,a,t):
    P=[1]*(V+1)
    P[0]=calc_p0(X)
    for i in range(1,V+1):
        P[i]=(P[0]*X[i])
    return P
#funkcja obliczająca wartości B
def calc_bn(P,V,t,M):
    B=[]
    
    for i in range (1,M+1):
        sum=0
        for n in range(V-t[i-1]+1,V+1):
            sum+=P[n]
        B.append(sum)
    return B
#funkcja calc_all zawierająca wszystkie funkcje potrzebne do wyznaczenia wyniku
def calc_all(V,t,a,M):
    print("Wartości X")
    X=calc_x(V,M,a,t)
    print(X)
    print("Wartości P")
    P=calc_pn(X,V,M,a,t)
    print(P)
    print("Wartości B")
    print(calc_bn(P,V,t,M))
    
print("Wartości M=2, V=3, a=[0.4,1], t=[1,2]")
calc_all(V,t,a,M)
print("Wartości M2=2, V2=3, a2=[1.2,0.6], t2=[1,2]")
calc_all(V2,t2,a2,M2)
print("Wartości M3=2, V3=3, a3=[1.6,0.4], t3=[1,2]")
calc_all(V3,t3,a3,M3)
print("Wartości M4=2, V4=3, a4=[0.8,0.8], t4=[1,2]")
calc_all(V4,t4,a4,M4)