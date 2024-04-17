

def reverse_complement(seq: str) -> str:
    map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(map.get(base, '') for base in reversed(seq))

def sanitize(seq: str) -> str:
    map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(base for base in seq if base in map)


def translate(s: str) -> str:
    seq = sanitize(s)
    DNA_to_Codon = {
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "TGT": "C", "TGC": "C",
        "GAT": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "TTT": "F", "TTC": "F",
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        "CAT": "H", "CAC": "H",
        "ATA": "I", "ATT": "I", "ATC": "I",
        "AAA": "K", "AAG": "K",
        "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        "ATG": "M",
        "AAT": "N", "AAC": "N",
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAA": "Q", "CAG": "Q",
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        "TGG": "W",
        "TAT": "Y", "TAC": "Y",
        "TAA": "_", "TAG": "_", "TGA": "_"
    }
    protein = "".join(DNA_to_Codon.get(seq[i:i+3], '') for i in range(0, len(seq) - 2, 3))
    return protein

def orf(seq: str) -> list[str]:
    seq_r = reverse_complement(seq)
    orfs = []
    for i in range(len(seq)):
        if seq[i:i+3] == "ATG":
            orf_candidates = translate(seq[i:]).split("_")
            if len(orf_candidates) > 1:
                orfs.append(orf_candidates[0])
        if seq_r[i:i+3] == "ATG":
            orf_candidates = translate(seq_r[i:]).split("_")
            if len(orf_candidates) > 1:
                orfs.append(orf_candidates[0])
    return list(set(orfs))


print(orf("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"))

