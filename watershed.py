import numpy as np


def is_4conn(row, col, row_id, col_id):
    """
    Parameters :
    row            - row index of pixel
    col            - col index of pixel
    row_id         - row index of neighbour pixel
    col_id         - col index of neighbour pixel

    Returns         :  Boolean. Whether pixel at location [row_id, col_id] is a 4 connected neighbour of pixel at location [row, col]

    """

    return (abs(row - row_id) + abs(col - col_id)) == 1

def is_8conn(row,col,row_id,col_id):
    return (abs(row - row_id) + abs(col - col_id)) <= 2

def getSmallestNeighborIndex(img, row, col, f_conn=is_4conn):
    """
    Parameters :
    img            - image
    row            - row index of pixel
    col            - col index of pixel

    Returns         :  The location of the smallest 4-connected neighbour of pixel at location [row,col]

    """

    min_row_id = -1
    min_col_id = -1
    min_val = np.inf
    h, w = img.shape
    for row_id in range(row - 1, row + 2):
        if row_id < 0 or row_id >= h:
            continue
        for col_id in range(col - 1, col + 2):
            if col_id < 0 or col_id >= w:
                continue
            if row_id == row and col_id == col:
                continue
            if f_conn(row, col, row_id, col_id):
                if img[row_id, col_id] < min_val:
                    min_row_id = row_id
                    min_col_id = col_id
                    min_val = img[row_id, col_id]
    return min_row_id, min_col_id




# TO - DO: Complete the function getRegionalMinima
def getRegionalMinima(img, f_conn):
    markers = np.zeros(img.shape, dtype=np.int32)
    h, w = img.shape
    v_ori=[]
    # Your code here
    cur_m = 0
    for x in range(h):
        for y in range(w):
            sx, sy = getSmallestNeighborIndex(img, x, y, f_conn)
            if img[sx, sy] >= img[x, y]:
                cur_m += 1
                markers[x, y] = cur_m
                v_ori.append(img[x,y])

    return markers, v_ori


# TO - DO: Complete the function iterativeMinFollowing
def iterativeMinFollowing(img, markers, f_conn=is_4conn):
    """
    Parameters :
    img          - image
    markers      - returned from function getRegionalMinima(img)


    Returns       :  final labels (markers_copy)

    """
    markers_copy = np.copy(markers)
    h, w = img.shape

    # i here is for printing iteration
    # i=1

    while True:

        # Number of pixels unmarked (label value is still 0)
        n_unmarked_pix = 0

        for row in range(h):
            for col in range(w):

                # Your code here

                if markers_copy[row, col]:
                    continue
                else:
                    sx, sy = getSmallestNeighborIndex(img, row, col, f_conn)
                    if markers_copy[(sx, sy)]:
                        markers_copy[row, col] = markers_copy[(sx, sy)]
                    else:
                        n_unmarked_pix += 1

        # NOTE!!: Please make sure to comment the below two print statements and i+=1 before submitting.
        # Feel free to un-comment them while working on the assignment and observing how iterativeMinFollowing works
        # print(f"labels after iteration {i}:")
        # print(markers_copy)
        # i+=1

        # print('n_unmarked_pix: ', n_unmarked_pix)
        if not n_unmarked_pix:
            break

    return markers_copy

def watershed(img,f_conn=is_4conn):
    mk,ori=getRegionalMinima(img,f_conn)
    imf=iterativeMinFollowing(img,mk,f_conn)
    vproc=np.vectorize(lambda x: ori[x-1])
    imfv=vproc(imf)
    print("marker")
    print(mk)
    print("result")
    print(imfv)