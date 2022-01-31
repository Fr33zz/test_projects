
n = int(input())
al = list(map(int, input().split()))
al = sorted(al, reverse=True)

x = 0
for i in range(n):
    x += al[i]
    x = x**(1/2)
x = abs(x)
if x%1>0: x=x//1+1
print(int(x))