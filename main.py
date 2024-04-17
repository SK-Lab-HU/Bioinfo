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
