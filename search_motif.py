with open("data.txt") as f:
    lines = [i.replace("\n","") for i in f.readlines()]

sequences: list = []
seq : list = []
for i in lines:
    print(seq)
    if ">" in i: 
        sequences.append("".join(seq))
        seq = []
    else:
        seq.append(i)
print(sequences)


    
