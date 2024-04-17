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


