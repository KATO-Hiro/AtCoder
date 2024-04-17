# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l, r = map(int, input().split())
    ans = list()

    while l < r:
        for i in range(60, -1, -1):
            width = 1 << i

            if l % width != 0:
                continue
            if l + width > r:
                continue

            ans.append((l, l + width))

            l += width

            break

    print(len(ans))

    for li, ri in ans:
        print(li, ri)


if __name__ == "__main__":
    main()
