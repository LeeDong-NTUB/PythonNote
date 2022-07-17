
#正三角形
n=int(input())
o=''
t=n-1
for i in range(1,(n*2),2):
    tmp=''+'_'*t
    for k in range(i):
        tmp+='*'
    o+=tmp+'_'*t+'\n'
    t-=1
print(o)