#hamming diactance related to to the SNP being used to identify uri of 9-mers where the hamming distance is at most d times.
#this is used to varify and statistically prove that the ori regions found in the sequence does have high changes to be the desired sequence
import numpy as np
pattern = "GAGG"
gene = "TTTAGAGCCTTCAGAGG"
d = 2
def ori_finder(p, g):
    pattern_dict = {}
    count = 1
    for i in range(len(g)-len(p)+1):
        if g[i:(i+len(p))]== p:
            pattern_dict[g[i:(i+len(p))]] = count + 1
        elif g[i:(i+len(p))] != p:
            pattern_dict[g[i:(i+len(p))]] = count
    return pattern_dict

def hamming(pattern_dict,p,d,g):
    mis = np.empty(0)
    hamming_d = {}
    ham = {}
    ham_p = {}
    lst = np.empty(0)
    m = []
    n = []
    t = []
    for pat in pattern_dict:
        #all the key patterns are appended in the list
        lst = np.append(lst, pat)
    for l in lst:
        #if l pattern from the list of key patterns matches the pattern, well and good.
        if l == p:
            continue
        elif l != p:
            #if not, then the l pattern ana p pattern will be converted into list, checked for all the mismatches, number of mimaches will be dounf doe all l patterns. (in the foem of m and n)
            hamming_d = calling(l,p)
            for kay in hamming_d:
                ham_p[kay] = hamming_d[kay]
    for ele in ham_p:
        if ham_p[ele] <= d:
            ham[ele] = ham_p[ele]
    print("Ptterns having hamming diatance less than " + str(d) + " :" )
    print(ham)
    t = sequence_final_analysis(ham,g)
    return t


def sequence_final_analysis(ham,g):
    len_1 = len(g)
    q = []
    for i in range(len_1):
        for kay in ham :
            if kay == g[i:(i+len(kay))]:
                q.append(i)
    print("The starting positions of the posisible ori regions :")
    print(q)
    return q
                 
    
def calling(l,p):
    mis = np.empty(0)
    hamming_d_calling = {}
    m = []
    n = []
    for i in l:
        m.append(i)
    for j in p:
        n.append(j)
    for k in range(len(m)):
        if m[k] == n[k]:
            continue
        elif m[k] != n[k]:
            #once the mismatches is found, it's length serves as hamming distance. all the hamming distances are saved ad the dictionary for pattern and hamming diastance value
            mis = np.append(mis, m[k])
            hamming_d_calling[l] = len(mis)
    return hamming_d_calling
            
pattern_ditionary_details = ori_finder(pattern, gene)

hamming_disctance_index = hamming(pattern_ditionary_details,  pattern, d, gene)



    
                
                
        
