# Bioinfo
バイオインフォマティクスの基本操作を通したPythonチュートリアル

# 塩基配列のランダム生成

以下のコードで塩基配列をランダムに生成することができる。


```Python
import random 

nucleotides = ["A", "C", "G", "T"]

def generate_sequence(length: int) -> str:
    return "".join([random.choice(nucleotides) for _ in range(length)])

print(generate_sequence(10))
```
