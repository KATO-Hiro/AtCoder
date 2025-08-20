# ランダムケースの生成
# random_cases.py

from random import randint

# 制約条件を乱数で生成
# 一部の制約条件は、愚直な解法で間に合うように調整する
n = randint(1, 100)
r = [randint(1, 100) for _ in range(n)]
c = [randint(1, 100) for _ in range(n)]

# 制約条件に関する内容を出力
print(n)

for ri, ci in zip(r, c):
    print(ri, ci)

# 順列の並べ替え（numpy）や木のテストケース作成（networkx）などもできる
