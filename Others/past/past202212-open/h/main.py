# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    d = int(input())
    # 昇順 + 累積和
    a = sorted(map(int, input().rstrip()))
    ans = 0
    acc = 0

    for i, ai in enumerate(a):
        ans += ai * i - acc
        acc += ai

    print(ans)


if __name__ == "__main__":
    main()
