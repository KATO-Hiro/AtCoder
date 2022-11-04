# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    size_max = 10 ** 6 + 10
    b = [0] * size_max
    g = 0

    is_pairwise = True

    for ai in a:
        b[ai] += 1
        g = gcd(g, ai)
    
    # 互いに素な要素か確認 = 素数を数える
    # 調和級数なので、計算量はO(aloga)
    for i in range(2, size_max):
        count = 0

        for j in range(i, size_max, i):
            count += b[j]
        
        if count > 1:
            is_pairwise = False
            break
    
    if is_pairwise:
        print("pairwise coprime")
        exit()

    if g == 1:
        print("setwise coprime")
    else:
        print("not coprime")


if __name__ == "__main__":
    main()
