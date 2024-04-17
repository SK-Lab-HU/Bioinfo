with open("data.txt") as f:
    lines = [i.replace("\n","") for i in f.readlines()]

sequences: list = []
seq : list = []
for i in lines:
    if ">" in i: 
        sequences.append("".join(seq))
        seq = []
    else:
        seq.append(i)
sequences.append("".join(seq))
sequences = sequences[1:]

shortest_seq: str = sequences[0]
shortest_seq_length : int = len(sequences[0])

for i in sequences:
    if len(i) < shortest_seq_length:
        shortest_seq = i
        shortest_seq_length = len(i)

print(shortest_seq_length)

def find_common_substr(s_1:str,s_2:str) -> str:
    for i in range(len(s_2),0,-1):
        for j in range(len(s_2)-i+1):
            substr = s_2[j:j+i]
            if substr in s_1:
                return(substr)
    return ""


import collections
substring_list = [] 
#最長モチーフの候補を格納するリストを作成
for i in range(len(sequences)-1):
    s_1 = sequences[i]
    s_2 = sequences[i+1]
    common_sub_str = find_common_substr(s_1,s_2)
    print(common_sub_str)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    substring_list.append(common_sub_str)

#collectionsのCounterクラスを使用してsubstring_list中の頻度順に辞書d_substrに登録
d_substr = collections.Counter(substring_list)
lcs = next(iter(d_substr))
print(d_substr)
for n,i in enumerate(sequences):
    if lcs in i:
        print(n)
        
