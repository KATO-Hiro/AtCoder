# ランダムケースの生成
# random_cases.py

from random import randint

# 制約条件を乱数で生成
# 一部の制約条件は、愚直な解法で間に合うように調整する
a = randint(1, 10**6)
x = randint(1, 10**3)
m = randint(1, 10**6)

# 制約条件に関する内容を出力
print(a, x, m)
