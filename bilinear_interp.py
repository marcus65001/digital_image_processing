if __name__ == '__main__':

    a=[]
    for i in range(4):
        a.append(float(input("({}, {}): ".format(i//2,i%2))))

    x=(input("x: "))
    y=(input("y: "))

    f=lambda a: eval(a) if a.find("/")>-1 else float(a)

    x=f(x)
    y=f(y)

    print(x,y)

    h1=(a[2]-a[0])*x+a[0]
    h2=(a[3]-a[1])*x+a[1]
    v=(h2-h1)*y+h1

    print(v)
