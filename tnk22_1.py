a,b,n = map(int, input().split())

if (a+b)/2%1!=0 or (a-b)/2%1!=0 or (a-b)/2<n: print('NO')
else: print('YES')