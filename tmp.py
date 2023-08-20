def z(x):
    return 0

def s(x):
    return x+1

def k(x):
    return lambda *n: n[x-1]

def P(g, h):
    def t(*x):
        tmp = g(*x[:-1])
        for i in range(x[-1]):
            tmp = h(*x[:-1], i, tmp)
        return tmp
    return t

def C(g, *h):
    return lambda *x: g(*[i(*x)for i in h])

def M(g):
    x = 0
    while g(x): x += 1
    return x
