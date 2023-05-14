# ランダムケースの生成
# random_cases.py

from random import randint

# 制約条件を乱数で生成
# 一部の制約条件は、愚直な解法で間に合うように調整する
pattern = "01?"
m = randint(1, 20)
s = [pattern[randint(0, 2)] for _ in range(m)]
n = randint(1, 10**6)

# 制約条件に関する内容を出力
print("".join(s))  # リストの場合は、展開しておく必要がある
print(n)
