# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    minus = 0
    value_min = float('inf')
    ans = 0

    # 偶奇性を活用
    # 最終的に、負の数は0か1つにできる
    # 前から貪欲法
    for ai in a:
        if ai < 0:
            minus += 1
        
        value_min = min(value_min, abs(ai))
        ans += abs(ai)
    
    if minus % 2 == 1:
        ans -= value_min * 2  # 正の数にした分も引く
    
    print(ans)


if __name__ == "__main__":
    main()
