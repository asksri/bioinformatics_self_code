tex ="CAAGATGCCAAGATGCCTGTCCATCAGATTTTACATGATTTAAGATTTTACATGATTTACTGTCCATCCAAGATGCATGATTTACTGTCCATCCAAGATGCATGATTTAAGATTTTACATGATTTAGCTGCACCAGATTTTACATGATTTACAAGATGCCAAGATGCCTGTCCATCATGATTTAAGATTTTACCAAGATGCCAAGATGCCTGTCCATCCAAGATGCATGATTTACTGTCCATCGCTGCACCGCTGCACCGCTGCACCGCTGCACCCAAGATGCCAAGATGCATGATTTAAGATTTTACCTGTCCATCCAAGATGCAGATTTTACGCTGCACCAGATTTTACCTGTCCATCAGATTTTACCAAGATGCATGATTTAGCTGCACCCTGTCCATCATGATTTACAAGATGCATGATTTAATGATTTACAAGATGCCAAGATGCATGATTTACTGTCCATCCTGTCCATCCTGTCCATCCTGTCCATCGCTGCACCGCTGCACCAGATTTTACGCTGCACCCAAGATGCCAAGATGCGCTGCACCGCTGCACCATGATTTAAGATTTTACGCTGCACCCTGTCCATCCAAGATGCGCTGCACCCTGTCCATCCAAGATGCGCTGCACCCAAGATGCCAAGATGCGCTGCACCCTGTCCATCGCTGCACCGCTGCACCAGATTTTACCAAGATGCCAAGATGCCAAGATGCGCTGCACCAGATTTTACGCTGCACCATGATTTACAAGATGCCTGTCCATCGCTGCACCGCTGCACCAGATTTTACATGATTTAAGATTTTACAGATTTTACCAAGATGCAGATTTTACGCTGCACCCAAGATGCCAAGATGCCTGTCCATCGCTGCACCGCTGCACCCTGTCCATCCTGTCCATCCAAGATGCATGATTTAATGATTTAGCTGCACCATGATTTAATGATTTACTGTCCATCGCTGCACCCTGTCCATCCAAGATGC"

k_mer = 14
freq_dict = {}
arr =[]
def table(text,k):
    for i in range(len(text)- k +1):
        pattern = text[i:(i+k)]
        if pattern in freq_dict:
            freq_dict[pattern] = freq_dict[pattern] + 1
        elif pattern not in freq_dict:
            freq_dict[pattern] = 1
    return freq_dict

def max_t(freq_dict):
    for patterns in freq_dict:
        if freq_dict[patterns] == max(freq_dict.values()):
            arr.append(patterns)
    print(arr)

f = table(tex,k_mer)
max_t(f)

