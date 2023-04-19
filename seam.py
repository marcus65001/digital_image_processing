import numpy as np
from skimage import color, io
from utils import inp_mat
def seam_carve(img,horizontal=False):
    if horizontal:
        img=img.transpose()
    h,w=img.shape
    e=np.zeros_like(img)
    bt=e.copy()
    e[0,:]=img[0,:]
    for i in range(1,h):
        for j in range(w):
            e[i,j]=img[i,j]+e[i-1,max(0,j-1):min(w,j+2)].min()
            bt[i,j]=max(0,j-1)+e[i-1,max(0,j-1):min(w,j+2)].argmin()
    mark = np.zeros_like(bt)
    ind = np.flatnonzero(e[-1] == e[-1].min()).tolist()
    for x in reversed(range(h)):
        mark[x][ind] = 1
        ind = bt[x][ind]
    if horizontal:
        img=img.transpose()
        e=e.transpose()
        mark=mark.transpose()
        h,w=w,h

    print("Result of the DP (Seam Computation Values):")
    for x in range(h):
        for y in range(w):
            if not mark[x,y]:
                print("{:<4}".format(e[x,y]),end="")
            else:
                print("\033[91m{:<4}\033[0m".format(e[x, y]), end="")
        print()

    print("Result of the DP (Original energy image):")

    for x in range(h):
        for y in range(w):
            if not mark[x, y]:
                print("{:<4}".format(img[x, y]), end="")
            else:
                print("\033[91m{:<4}\033[0m".format(img[x, y]), end="")
        print()
    return e

if __name__ == '__main__':
    img=np.array(inp_mat())
    output = seam_carve(img)
    print(output)