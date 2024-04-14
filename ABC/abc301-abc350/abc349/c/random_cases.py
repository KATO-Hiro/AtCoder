# ランダムケースの生成
# random_cases.py


def add_offset_to_alphabet(offset: int, base_alphabet: str = "A") -> str:
    """Add offset to the base_alphabet.

    Args:
        offset: Difference from the base alphabet.
        base_alphabet: The base alphabet to use.

    Returns:
        Corrected alphabet.

    See:
    https://docs.python.org/3.11/library/functions.html?highlight=chr#ord
    """

    return chr(ord(base_alphabet) + offset)


from random import randint

# 制約条件を乱数で生成
# 一部の制約条件は、愚直な解法で間に合うように調整する
n = randint(3, 10**2)
s = "".join(map(str, [add_offset_to_alphabet(randint(0, 25), "a") for _ in range(n)]))
t = "".join(map(str, [add_offset_to_alphabet(randint(0, 25), "a") for _ in range(3)]))

# 制約条件に関する内容を出力
print(s)  # リストの場合は、展開しておく必要がある
print(t)

# 順列の並べ替え（numpy）や木のテストケース作成（networkx）などもできる
