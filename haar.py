import numpy as np
import pywt


def haar2d(a,keep_steps=False):
    a=np.array(a)
    h,w=a.shape
    b=np.zeros_like(a)
    c=b.copy()
    for x in range(0,h):
        for y in range(0,w//2):
            b[x,y]=a[x,y*2]+a[x,y*2+1]
            b[x,w//2+y]=a[x,y*2]-a[x,y*2+1]
    if keep_steps:
        print("Along row:\n 1/sqrt(2)*\n{}".format(b))
    for x in range(0, h//2):
        for y in range(0, w):
            c[x,y]=b[x*2,y]+b[x*2+1,y]
            c[h//2+x,y]=b[x*2,y]-b[x*2+1,y]
    if keep_steps:
        print("Along column:\n1/2*\n{}".format(c))
    return c/2


def inv_haar2d(a,keep_steps=False):
    a=np.array(a)
    h,w=a.shape
    b=np.zeros_like(a)
    c=b.copy()
    for x in range(0, h//2):
        for y in range(0, w):
            b[x * 2, y] = (a[x,y]+a[h//2+x,y])/np.sqrt(2)
            b[x * 2 + 1, y] = (a[x,y]-a[h//2+x,y])/np.sqrt(2)
    if keep_steps:
        print("Along column:\n1/2*\n{}".format(b))
    for x in range(0,h):
        for y in range(0,w//2):
            c[x, y * 2] = (b[x,y]+b[x,w//2+y])/np.sqrt(2)
            c[x, y * 2 + 1] = (b[x,y]-b[x,w//2+y])/np.sqrt(2)
    if keep_steps:
        print("Along row:\n 1/sqrt(2)*\n{}".format(c))
    return c


def haar1d(f):
    a,d=pywt.dwt(f,"Haar")
    sa = np.array2string(a / np.sqrt(2), formatter={"float_kind": lambda x: "%.2f" % x})
    sd = np.array2string(d / np.sqrt(2), formatter={"float_kind": lambda x: "%.2f" % x})
    print("A: sqrt(2)*",sa)
    print("D: sqrt(2)*",sd)
    return a,d

def inv_haar1d(a,d):
    f=pywt.idwt(a,d,"Haar")
    print("Inverse Haar 1D from a and d:")
    print(f)
    return f


if __name__ == '__main__':
    from utils import inp_mat
    a=inp_mat()
    print(haar2d(a))