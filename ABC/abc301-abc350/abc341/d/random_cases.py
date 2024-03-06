# ランダムケースの生成
# random_cases.py

from random import randint

# 制約条件を乱数で生成
# 一部の制約条件は、愚直な解法で間に合うように調整する
n = randint(1, 10**3)
m = randint(1, 10**3)

while m == n:
    m = randint(1, 10**3)

k = randint(1, 10**3)

# 制約条件に関する内容を出力
print(n, m, k)
