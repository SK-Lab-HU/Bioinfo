import random 

nucleotides = ["A", "C", "G", "T"]

def generate_sequence(length: int) -> str:
    return "".join([random.choice(nucleotides) for _ in range(length)])

print(generate_sequence(10))
