"""
n= int(input('num'))
d=dict()
toplam=0
for x in range(1,n+1):
    d[x]=x*x
    toplam+=x*x
    print(d)
    print(toplam)

    """



def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)


def fibo(n):
    d = dict()
    toplam = 0
    for x in range(1, n + 1):
        a = F(x - 1)
        d[x] = a
        toplam += a
    print(d)
    print(toplam)
num = int(input("num"))
fibo(num)
