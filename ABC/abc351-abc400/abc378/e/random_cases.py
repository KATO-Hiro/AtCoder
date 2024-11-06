# ランダムケースの生成
# random_cases.py

from random import randint

# 制約条件を乱数で生成
# 一部の制約条件は、愚直な解法で間に合うように調整する
n = randint(1, 100)
m = randint(1, 10**5)
a = [randint(0, 10**9) for _ in range(n)]

# 制約条件に関する内容を出力
print(n, m)
print(*a)  # リストの場合は、展開しておく必要がある

# 順列の並べ替え（numpy）や木のテストケース作成（networkx）などもできる