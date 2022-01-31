n,m = map(int, input().split())
if n<m: n,m = m,n
c = 0
while m != 1:
    if n<m: n,m = m,n
    elif n==m: 
        c+=1-n
        break
    c += 1
    n,m = n-m,m
    print(c, n, m)
c += n
print(c)