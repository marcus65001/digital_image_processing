import numpy as np


def histogram(img, K=8,bins=8, normalize=False):
    hist = np.zeros(bins, dtype=np.int64)
    interval = K // bins
    for i in img.ravel():
        hist[i // interval] += 1
    if normalize:
        return hist/hist.sum()
    return hist


def cum_hist(img, K=8, bins=8, normalize=False):
    hist=histogram(img,K,bins)
    ch=np.cumsum(hist)
    if normalize:
        return ch/ch.max()
    return ch


def hist_eq(img,K=8,bins=8):
    h,w=img.shape
    img2 = np.zeros(img.shape, dtype=np.uint8)
    ch=cum_hist(img,K,bins)
    binsize=K//bins

    for i in np.arange(h):
        for j in np.arange(w):
            img2[i, j] = np.floor(((K-1) / (h * w)) * ch[img[i, j]//binsize] + 0.5)

    return img2


def hist_spec(norm_cum_hist_in, norm_cum_hist_ref, K=8):
    # lookup
    lu_dtn = np.zeros(K, dtype=np.uint8)
    ap = 0
    for i in np.arange(K):
        while (norm_cum_hist_in[i] > norm_cum_hist_ref[ap]) and (ap < K):
            ap += 1
        lu_dtn[i] = ap

    return lu_dtn


def hist_spec_with_lookup(img, lookup):
    h,w=img.shape
    mod_inp = np.zeros(img.shape, dtype=np.uint8)
    for i in np.arange(h):
        for j in np.arange(w):
            mod_inp[i, j] = lookup[img[i, j]]
    return mod_inp

def hist_spec_img(img_in,img_ref, K=8, bins=8):
    norm_cum_hist_in=cum_hist(img_in,K=K,bins=bins,normalize=True)
    norm_cum_hist_ref = cum_hist(img_ref, K=K, bins=bins, normalize=True)

    lu_dtn=hist_spec(norm_cum_hist_in,norm_cum_hist_ref)

    return hist_spec_with_lookup(img_in,lu_dtn)


def bhattacharya(norm_hist1,norm_hist2):
    # match - 1;  mis - 0;
    return np.sqrt(norm_hist1*norm_hist2).sum()