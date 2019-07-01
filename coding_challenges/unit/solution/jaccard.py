from __future__ import division


# jaccard function
def j(A, B):

    num = set(A) & set(B)
    dem = set(A) | set(B)
    return float(len(num) / len(dem))
