

def romantoint(T):
    sc={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    s=0
    for i in range(len(T)):
        s+=sc[T[i]]
        if i!=0 and sc[T[i-1]] < sc[T[i]]:
            s=s-(sc[T[i-1]]*2)        
    return s

def inttoroman(s):
    num_table = [
    [1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],
    [90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],
    [5,'V'],[4,'IV'],[1,'I']]
    r=''
    for i in num_table:
        r=r+(i[1]*(s//i[0]))
        s=s%i[0]
    return r
        