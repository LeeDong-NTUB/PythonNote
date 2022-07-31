def GCD(n1,n2):
    n=max(n1,n2)
    m=min(n1,n2)
    if n%m==0:
        return m
    else:
        return GCD(m,n%m)