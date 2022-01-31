n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
#n = 10
#a = [0,1,2,3,5,5,6,7,8,5]
#b = [9,8,7,1,5,4,3,2,0,0]

l = [-1]*n


def check(i,k):
    ret = []
    for j in range(a[i]):
        forward = j+1
        if i-forward<0: ret.append(1)
        backward = b[i-forward]
        pos = i-forward+backward
        if pos>=n: ret.append(-1)
        elif l[pos]==k: ret.append(k+1)
        else: ret.append(-1)
    if len(ret)>0: return max(ret)
    else: return 0

flag = -1
count = 1
empty = 1
while count>0 and empty>0:
    flag += 1
    count = 0
    empty = 0
    #print(flag)
    for i in range(n):
        if l[i]!=flag: 
            l[i] = check(i,flag)
            if l[i]==flag+1: count+=1
        if l[i]==-1: empty += 1

print(l[-1])






#for i in l:
#    print(i)
'''
flag = 0
count = 0
for i in range(n):
    if l[i]!=flag: 
        l[i] = check(i,flag)
        if l[i]==flag+1: count+=1
    print(l[i])

flag = 1
count = 0
empty = 0
for i in range(n):
    if l[i]!=flag: 
        l[i] = check(i,flag)
        if l[i]==flag+1: count+=1
    if l[i]==-1: empty += 1
    print(l[i])


print('count=',count)
'''
    
