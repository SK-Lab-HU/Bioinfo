# Bioinfo
バイオインフォマティクスの基本操作を通したPythonチュートリアル

## 塩基配列のランダム生成

以下のコードで塩基配列をランダムに生成することができる。


```python
import random 

nucleotides : list[str] = ["A", "C", "G", "T"]

def generate_sequence_ver1(length: int) -> str:
    DNA = ""
    for _ in range(length):
        DNA += random.choice(nucleotides)
    return DNA

print(generate_sequence_ver1(10))
```

上記のコードを高速化・コンパクト化すると以下のようになる。

```Python
import random 

nucleotides : list[str] = ["A", "C", "G", "T"]

def generate_sequence_ver2(length: int) -> str:
    return "".join([random.choice(nucleotides) for _ in range(length)])

print(generate_sequence_ver2(10))
```

## DNA中のヌクレオチドの数

pythonでは以下のcount構文で文字列Sに含まれる文字Aの数を数えることができる。

```Python
S = "13121"

#値はint型で取得できる。
count_A : int = S.count("1")

#この場合は3となる。
print(count_A)
```

上記構文を利用してDNA中のヌクレオチドの数を数えることができる。

```python
DNA : str = "CGGAAGCGTGGCTTTTATTCCTCGTGACAC"
print(DNA.count("A"))
print(DNA.count("C"))   
print(DNA.count("G"))
print(DNA.count("T"))
```
## GC rateの計算

Count構文を応用すると塩基配列中のGC rateは以下のように求めることができる。
ここで、lenは、ある文字列Sの長さを取得する関数。

```python
DNA : str = "CGGAAGCGTGGCTTTTATTCCTCGTGACAC"

gc_rate : float = (DNA.count("G") + DNA.count("C")) / len(DNA)
print(gc_rate)

```

## 転写

Pythonのreplace構文を使用して、"T"を"U"に変更することで転写を再現することができる。

```python
DNA : str = "CGGAAGCGTGGCTTTTATTCCTCGTGACAC"
mRNA : str = DNA.replace("T", "U")
```

## 翻訳

Pythonの辞書(dict型)を使用すると、コドンをアミノ酸にマッピングすることができる。

以下にpythonの辞書の例を示す。

```Python
d : dict = {"A":"1","B":"2"}

# "A"をキーとして"1"が呼び出される。
val1 = d["A"]
print(val1)
```

つまり、以下のようにコドン表を辞書に落とし込めば、コドンに応じたアミノ酸配列をいつでも呼び出すことができる。

```Python
codon_table= {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop', 
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W', 
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

```

## ハミング距離

ハミング距離は2つの文字列S1とS2がどれだけ異なっているかを表す指標。
これを利用することで、例えば遺伝子の変異の個数を表すことができる。

```python
S1 : str = "GAGCCTACTAACGGGAT"
S2 : str = "CATCGTAATGACGGCCT"

def d_h(S1: str, S2: str) -> int:
    hamming_distance = 0
    # s1とs2をそれぞれ同時に左から巡回
    for i,j in zip(S1, S2):
        if i != j:
            hamming_distance += 1
    return hamming_distance

print(d_h(S1, S2))
```

上記の処理を高速化すると以下のようになる。

```python
S1 : str = "GAGCCTACTAACGGGAT"
S2 : str = "CATCGTAATGACGGCCT"

hamming_distance = sum([1 for i in range(len(S1)) if S1[i] != S2[i]])
print(hamming_distance)
```

## モチーフの探索

例えば以下のような塩基配列のうち、モチーフMの開始indexは以下のようになる。
(pythonのインデックスは1ではなく0からスタートすることに注意)
```Python
DNA : str = "GATATATGCATATACTT"
M : str = "ATAT" 

#モチーフの開始インデックスは
# 1, 3, 9の3つ
```

上記のようなモチーフの開始インデックスを探索する方法について考える。
無数の方法があるが、シンプルでわかりやすい方法を考えた。

始めに、pythonのリストのappend構文の例を示す。

```python
a : list = []
a.append(1)
a.append(2)
a.append(3)

# a = [1,2,3]

b : list = []
for i in range(1,4):
    b.append(i)

# b = [1,2,3]
```

モチーフ探索アルゴリズム

```python
DNA : str = "GATATATGCATATACTT"
M : str = "ATAT" 

def find_motif_1(DNA: str, M: str) -> list:
    motif_indices = []
    for i in range(len(DNA)-len(M)+1):
        if DNA[i:i+len(M)] == M:
            motif_indices.append(i)
    return motif_indices

print(find_motif_1(DNA, M))
```

言葉で説明すれば、モチーフMをDNA配列の左側から一つずつ右にずらしながら比較し、一致する場合にそのインデックスをmotif_indicesにappendする。

このような処理をシンプルに書くと以下のようになる。

```python
def find_motif_2(DNA: str, M: str) -> list:
    return [i for i in range(len(DNA)-len(M)+1) if DNA[i:i+len(M)] == M]

print(find_motif_2(DNA, M))
```

## 最長共通モチーフの探索アルゴリズム

複数の塩基配列から共通するモチーフのうち最長のものを探索する場合について考える。

### ファイルの読み込み

FASTAフォーマットで与えられるテキストデータをpythonで読み込むには、以下のファイル読み込みの構文を使用する。この構文はcsvやexcelなどさまざまなファイルを読み込む際にも使用するため、頻出。
今回はこのレポジトリにある配列データ[data.txt](./data.txt)を例にとる。

```python
with open("data.txt") as f:
    lines = [i.replace("\n","") for i in f.readlines()]
```
上記構文ではlinesには行を一つの文字列として、すべての文字列が上から順にリストとして格納されている状態である。

ここで、FASTAフォーマットでの配列の識別子として">"を採用して、以下のようにすべての配列を順にリストに格納する。

```python
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
print(sequences)
```
ループを抜けると、すべての配列がsequencesに格納された状態となる。

### 最長共通モチーフの探索

複数の塩基配列の中から共通するモチーフのうち最長のものを探索するアルゴリズムについて考える。
最長共通モチーフ探索に使用する配列群は、上記で取得したsequencesとする。

始めに、以下のように２つの塩基配列のうち最長の共通部分を返す関数を作成する。

```Python
def find_common_substr(s_1:str,s_2:str) -> str:
    for i in range(len(s_2),0,-1):
        for j in range(len(s_2)-i+1):
            substr = s_2[j:j+i]
            if substr in s_1:
                return(substr)
    return ""
```

次に、すべての配列のペアについて、上記の探索を行った結果を最長モチーフの候補に格納する。

```python
substring_list = [] 
#最長モチーフの候補を格納するリストを作成
for i in range(len(sequences)):
    for j in range(len(sequences)):
        if i != j:
            common_sub_str = find_common_substr(sequences[i],sequences[j])
            print(i)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            substring_list.append(common_sub_str)

```

最後に、候補のうち、最頻値を取得する。

```python
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
```

## オープンリーディングフレーム

Mを翻訳開始点、終始コドンを翻訳終了点として、これらに挟まれた配列部分は翻訳されるポテンシャルを備えている。これらの配列の総称をORFと言う。ここでは、mRNAスプライシングを無視して任意のDNAに関するORFの探索を行う。また、逆相補鎖まで考慮する。

始めに、逆相補鎖を求める関数を作成する。

```python
def reverse_complement(seq: str) -> str:
    map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(map.get(base, '') for base in reversed(seq))
```

また、配列にACGT以外の文字列が入ったケースを除外するために、文字列をサニタイズする関数を作成する。
```python
def sanitize(seq: str) -> str:
    map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(base for base in seq if base in map)
```

次に、引数に渡されたDNA配列をポリペプチドのコードに変換する関数を作成する。

```Python

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
```

最後に、与えられた配列およびその逆相補鎖について、開始コドンをアンカーとして、ORFを探索する関数を作成する。

```python
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
```

上記の実行結果は以下のとおりである。

```bash
['M', 'MTPRLGLESLLE', 'MLLGSFRLIPKETLIQVAGSSPCNLS', 'MGMTPRLGLESLLE']
```

## DNAのアセンブリ

DNA断片から元のDNA配列を組み立てるアルゴリズムについて考える。
「DNA断片を組み立てて一つの配列にする」ということをアルゴリズム風に言い換えると、「全断片の中で共有部分が最長である２配列を組み合わせていき最終的に一つの長い配列を作る」となる。もちろん、このアルゴリズムに従うと必ず一意に組み立てが完了するわけではないため、不確実性があるが、DNA断片の長さの最小値を上げることでこれを防ぐことが可能である。

組み立て前のDNA断片を以下のように定義する。

```bash
fragments_raw = ['ATTAGACCTG','CCTGCCGGAA','AGACCTGCCG','GCCGGAATAC']
fragments = sorted(fragments)
```







