def f0(a):
    a = 20
    f1(a)
    return a

def f1(a):
    a = 100
    return a

c = f0(100)
print(c)