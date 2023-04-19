import numpy as np
from scipy import ndimage

def inp_mat(built_in=False):
    mat = []
    while (inp := input()) != 'q':
        rw = inp.split("\n")
        for r in rw:
            r = r.strip()
            if not r:
                continue
            sp = r.split("\t")
            if len(sp)==1:
                sp=r.split(" ")
            row = []
            for i in sp:
                try:
                    row.append(int(i))
                except Exception as e:
                    # print(e)
                    pass
            mat.append(row)
    print(mat)
    if built_in:
        return mat
    else:
        return np.array(mat)


def conv(mat, fil, mode='constant'):
    '''
    mode{‘reflect’, ‘constant’, ‘nearest’, ‘mirror’, ‘wrap’}, optional
    '''
    fil=np.array(fil,dtype=np.float_)
    mat=np.array(mat,dtype=np.float_)
    return ndimage.convolve(mat, fil[::-1, ::-1],  mode=mode)


def dy(mat,b='reflect'):
    return conv(mat, np.array([[-0.5, 0, 0.5]]).T, mode=b)


def dx(mat,b='reflect'):
    return conv(mat, [[-0.5,0,0.5]], mode=b)


def d2(mat,b='constant'):
    return conv(mat,[[0,1,0],[1,-4,1],[0,1,0]],mode=b)


def box(mat,size=3,b='reflect'):
    fil=np.ones((size,size))
    return conv(mat, fil, mode=b)


def seq_frac():
    arr=[]
    while True:
        try:
            i=input("num: ")
            if i.find("/")>-1:
                i=eval(i)
            arr.append(float(i))
        except:
            break
    print(arr)
    return arr