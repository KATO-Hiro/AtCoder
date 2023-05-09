# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(map(int, input().split()))
    t = set()

    for a in range(1, 401):
        for b in range(1, 401):
            ti = 4 * a * b + 3 * (a + b)

            if ti <= 1000:
                t.add(ti)

    ans = 0

    for si in s:
        if not si in t:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
