fragments = sorted(['ATTAGACCTG','CCTGCCGGAA','AGACCTGCCG','GCCGGAATAC'])

def find_overlap(seq1,seq2):
    t_1 = ''
    t_2 = ''
    for i in range(len(seq1)):
        if seq1[:i] == seq2[-i:]:
            t_1 = seq1[:i]
    for i in range(len(seq2)):
        if seq2[:i] == seq1[-i:]:
            t_2 = seq2[:i]
    if len(t_1) > len(t_2):
        return t_1
    elif len(t_1) < len(t_2):
        return t_2
    elif len(t_1) == len(t_2):
        return t_1

def seq_overlay(s_1,s_2,seq_overlapped):
    if seq_overlapped == s_1[:len(seq_overlapped)]:
        s_n = s_2 + s_1[len(seq_overlapped):]
    elif seq_overlapped == s_2[:len(seq_overlapped)]:
        s_n = s_1 + s_2[len(seq_overlapped):]
    return s_n

def assembly(fragments: list[str]):
    while len(fragments) !=1:
        lcs_len = [0]
        for i in range(len(fragments)):
            t_i = fragments[i]
            for j in range(len(fragments)):
                t_j = fragments[j]
                if j!=i and len(find_overlap(t_i,t_j))>lcs_len[-1]:
                    lcs_len.append(len(find_overlap(t_i,t_j)))
                    s_1 = t_i
                    s_2 = t_j
                else:
                    pass 
        fragments.remove(s_1)
        fragments.remove(s_2)
        fragments.append(seq_overlay(s_1,s_2,find_overlap(s_1,s_2)))
    return fragments


print(assembly(fragments))
