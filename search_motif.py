import collections

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



substring_list = [] 
#最長モチーフの候補を格納するリストを作成
for i in range(len(sequences)):
    for j in range(len(sequences)):
        if i != j:
            common_sub_str = find_common_substr(sequences[i],sequences[j])
            print(i)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            substring_list.append(common_sub_str)

#collectionsのCounterクラスを使用してsubstring_list中の頻度順に辞書d_substrに登録
d_substr = collections.Counter(substring_list)
lcs = next(iter(d_substr))
print(d_substr)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(lcs)
# すべての配列の部分列であるかを検証
for n,i in enumerate(sequences):
    if lcs in i:
        print(n)
        
