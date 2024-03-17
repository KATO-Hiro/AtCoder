# ランダムケースの生成
# random_cases.py

from random import randint
from string import ascii_lowercase

# 制約条件を乱数で生成
# 一部の制約条件は、愚直な解法で間に合うように調整する
n = randint(2, 10**2)
t = [ascii_lowercase[randint(0, 25)] for _ in range(n)]
s = "".join(t)

# 制約条件に関する内容を出力
print(s)

# 順列の並べ替え（numpy）や木のテストケース作成（networkx）などもできる
