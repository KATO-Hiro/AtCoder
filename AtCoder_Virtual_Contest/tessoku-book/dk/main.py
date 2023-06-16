# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    height1, height2 = [1] * n, [1] * n
    streak1, streak2 = 1, 1

    # 下限値の見積もり
    # <
    for i, si in enumerate(s):
        if si == "A":
            streak1 += 1
        else:
            streak1 = 1

        height1[i + 1] = streak1

    # >, sを逆順に
    for i, si in enumerate(s[::-1]):
        if si == "B":
            streak2 += 1
        else:
            streak2 = 1

        height2[i + 1] = streak2

    ans = 0

    for h1, h2 in zip(height1, height2[::-1]):
        ans += max(h1, h2)

    print(ans)


if __name__ == "__main__":
    main()
