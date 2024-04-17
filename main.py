import random 

nucleotides = ["A", "C", "G", "T"]

def generate_sequence_ver1(length: int) -> str:
    DNA = ""
    for _ in range(length):
        DNA += random.choice(nucleotides)
    return DNA

print(generate_sequence_ver1(30))
    
def generate_sequence_ver2(length: int) -> str:
    return "".join([random.choice(nucleotides) for _ in range(length)])

print(generate_sequence_ver2(30))

DNA = "CGGAAGCGTGGCTTTTATTCCTCGTGACAC"

print(DNA.count("A"))
print(DNA.count("C"))   
print(DNA.count("G"))
print(DNA.count("T"))

DNA = "CGGAAGCGTGGCTTTTATTCCTCGTGACAC"

gc_rate = (DNA.count("G") + DNA.count("C")) / len(DNA)
print(gc_rate)


DNA = "CGGAAGCGTGGCTTTTATTCCTCGTGACAC"

mRNA = DNA.replace("T", "U")


S1 = "GAGCCTACTAACGGGAT"
S2 = "CATCGTAATGACGGCCT"

def d_h(S1: str, S2: str) -> int:
    hamming_distance = 0
    for i,j in zip(S1, S2):
        if i != j:
            hamming_distance += 1
    return hamming_distance

print(d_h(S1, S2))



hamming_distance = sum([1 for i in range(len(S1)) if S1[i] != S2[i]])
print(hamming_distance)


DNA : str = "GATATATGCATATACTT"
M : str = "ATAT" 

def find_motif_1(DNA: str, M: str) -> list:
    motif_indices = []
    for i in range*len(DNA):
        if DNA[i:i+len(M)] == M:
            motif_indices.append(i)
    return motif_indices

print(find_motif_1(DNA, M))


def find_motif_2(DNA: str, M: str) -> list:
    return [i for i in range(len(DNA)) if DNA[i:i+len(M)] == M]

print(find_motif_2(DNA, M))
