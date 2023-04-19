import numpy as np


def intra_class_var(img,threshold):
    ir=img.ravel()
    c1=ir[np.flatnonzero(ir<threshold)]
    c2=ir[np.flatnonzero(ir>=threshold)]
    return (len(c1)/len(ir))*c1.var()+(len(c2)/len(ir))*c2.var()