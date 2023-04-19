class Node:
    def __init__(self,p,i=None):
        self.i=i
        self.p=p
        self.l=None
        self.r=None

    def __lt__(self, other):
        return (self.p,-self.i)<(other.p,-other.i)

    def __repr__(self):
        return "(p={}, i={})".format(self.p,self.i)


def huff_tree(a):
    id=[i for i in range(len(a))]
    a = zip(a,id)
    a = [Node(*i) for i in a]
    while len(a)>1:
        a = sorted(a)
        x = a.pop(0)
        y = a.pop(0)
        n=Node(x.p+y.p)
        n.l=x
        n.r=y
        a.append(n)
    root=a[0]
    return root


def trace(node,i,s):
    if not node:
        return None
    if node.i==i:
        return s
    return trace(node.l,i,s+"1") or trace(node.r,i,s+"0")



def huff(a):
    l=len(a)
    r=huff_tree(a)
    rs=[trace(r,i,"") for i in range(l)]
    return rs


