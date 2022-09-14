# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = list()
    x = a[-1]  # 全て単調増加の場合への対処

    # x: 単調増加から初めて減少したときに、直前の値を選ぶ
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            x = a[i]
            break

    for ai in a:
        if ai != x:
            ans.append(ai)
    
    print(*ans)


if __name__ == "__main__":
    main()
