
#正三角形
n=int(input())
output=''
p=n-1
for i in range(1,(n*2),2):
    text=''+'_'*p
    for k in range(i):
        text+='*'
    output+=text+'_'*p+'\n'
    p-=1
print(output)
