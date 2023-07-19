#hamming diatance problem
import numpy as np

g_1 = "GGGCCGTTGGT"
g_2 = "GGACCGTTGAC"

def hamming(g1, g2):
    mismatches = np.empty(0)
    g1_lst = []
    g2_lst = []
    for i in g1:
        g1_lst.append(i)
    for j in g2:
        g2_lst.append(j)
    for k in range(len(g1_lst)):
        if g1_lst[k] == g2_lst[k]:
            continue
        else:
            mismatches = np.append(mismatches, g1_lst[k])
    hamming_d = len(mismatches)
    return hamming_d
p = hamming(g_1, g_2)
print(p)
