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




