n,m = map(int, input().split())

a = 2*n-m-1
b = 2*m-n-1

a = a/3
b = b/3

count = 0

def rec(x,y):
    if x==0 and y==0: return 1
    c = 0 if (x<0 or y<0) else 1
    if c==0: return 0
    else:
        c += rec(x-1,y) + rec(x,y-1) -1
        return c
    

if (a<0 or b<0) or (a%1!=0 and b%1!=0): print(count)
elif n==1 and m==1: print(1)
else:
    count = rec(a,b)
    print(count)