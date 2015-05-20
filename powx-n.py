# @param x, a float
# @param n, a integer
# @return a float
def power(x,n):
    if n == 0:
        return 1.0
    v = power(x, n // 2)
    if n%2 == 0:
        return v*v
    else:
        return v*v*x

def pow(x, n):
    if n == 0:
        return 1.0
    if x == 0:
        return 0.0
    if n < 0:
        n = -n
        x = 1.0/x
    return power(x,n)
