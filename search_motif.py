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

def LCS(s_1:str,s_2:str) -> str:
    for i in range(len(s_2),0,-1):
        for j in range(len(s_2)-i+1):
            substr = s_2[j:j+i]
            if substr in s_1:
                return(substr)
    return ""
