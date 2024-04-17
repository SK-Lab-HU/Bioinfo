# Bioinfo
バイオインフォマティクスの基本操作を通したPythonチュートリアル

## 塩基配列のランダム生成

以下のコードで塩基配列をランダムに生成することができる。


```python
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

nucleotides = ["A", "C", "G", "T"]

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
DNA = "CGGAAGCGTGGCTTTTATTCCTCGTGACAC"
print(DNA.count("A"))
print(DNA.count("C"))   
print(DNA.count("G"))
print(DNA.count("T"))
```


## 転写

以下のDNA配列について考える。


