def fattoriale(n):
    if n>1:
        return n*fattoriale(n-1)
    else:
        return 1

def max_factor_greater_than(n, d):
    if (n%d==0):
        return d
    else:
        return max_factor_greater_than(n, d+1)

def prime(n):
    return max_factor_greater_than(n,2)==n

def mcd(a, b):
    if a==b:
        return a
    if a>b:
        return mcd(a, a-b)
    

