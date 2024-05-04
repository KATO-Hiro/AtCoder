from random import randint

# 制約条件を乱数で生成
# 一部の制約条件は、愚直な解法で間に合うように調整する
n = randint(2, 10)

# 制約条件に関する内容を出力
print(n)

for _ in range(n):
    ai = randint(1, 10**9)
    bi = randint(ai, 10**9)
    print(ai, bi)

# 順列の並べ替え（numpy）や木のテストケース作成（networkx）などもできる
