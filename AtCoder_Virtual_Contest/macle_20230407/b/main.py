# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    total = 0
    s = set([0])

    # 累積和を取る + setを使って事実上の二分探索
    for ai in a:
        total += ai

        if (total - r) in s and (total - r - q) in s and (total - r - q - p) in s:
            print("Yes")
            exit()
        
        s.add(total)

    print("No")


if __name__ == "__main__":
    main()
