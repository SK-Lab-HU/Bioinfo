import random 

nucleotides = ["A", "C", "G", "T"]

def generate_sequence(length: int) -> str:
    return "".join([random.choice(nucleotides) for _ in range(length)])

print(generate_sequence(10))

def generate_sequence_ver2(length: int) -> str:
    DNA = ""
    for _ in range(length):
        DNA += random.choice(nucleotides)
    return DNA
    
