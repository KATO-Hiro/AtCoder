# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    b1, r1, b2, r2, t = map(int, input().split())
    size_max = 11000
    t1 = [False] * size_max
    t2 = [False] * size_max
    a1, a2 = b1 + r1, b2 + r2

    for i in range(1, t + 1):
        if 1 <= i % a1 <= b1:
            t1[i] = True
        if 1 <= i % a2 <= b2:
            t2[i] = True

    ans = 0

    for t1i, t2i in zip(t1, t2):
        if t1i and t2i:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
