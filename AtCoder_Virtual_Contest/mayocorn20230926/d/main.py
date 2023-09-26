# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    c, d = a, b
    ans = 0

    # 隣り合う偶数と奇数のxorを取ると1になる
    if a % 2 == 1:
        c = a + 1
        ans ^= a

    if b % 2 == 0:
        d = b - 1
        ans ^= b

    if ((d - c + 1) // 2) % 2 == 0:
        ans ^= 0
    else:
        ans ^= 1

    print(ans)


if __name__ == "__main__":
    main()
