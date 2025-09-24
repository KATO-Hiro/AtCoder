# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    l = list(map(int, input().split()))
    ans1 = [True] * (n + 1)
    ans2 = [True] * (n + 1)
    is_open1 = True
    is_open2 = True

    for i, li in enumerate(l, 1):
        if li == 1:
            is_open1 = False

        if not is_open1:
            ans1[i] = False

    for i, li in enumerate(l[::-1], 1):
        if li == 1:
            is_open2 = False

        if not is_open2:
            ans2[i] = False

    ans2 = ans2[::-1]
    count = 0

    for ans_i, ans_j in zip(ans1, ans2):
        if ans_i or ans_j:
            continue

        count += 1

    print(count)


if __name__ == "__main__":
    main()
