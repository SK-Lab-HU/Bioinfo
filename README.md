# Bioinfo
バイオインフォマティクスの基本操作を通したPythonチュートリアル

# 塩基配列のランダム生成

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




