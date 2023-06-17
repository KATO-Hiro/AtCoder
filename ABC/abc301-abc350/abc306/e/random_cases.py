# ランダムケースの生成
# random_cases.py

from random import randint

# 制約条件を乱数で生成
# 一部の制約条件は、愚直な解法で間に合うように調整する
n = randint(1, 10**2)
k = randint(1, n)
# k = n
q = randint(1, 10**2)

# 制約条件に関する内容を出力
print(n, k, q)

for _ in range(q):
    xi, yi = randint(1, n), randint(0, 10**6)
    print(xi, yi)
