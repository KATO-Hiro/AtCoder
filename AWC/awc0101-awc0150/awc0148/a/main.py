# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d, k = map(int, input().split())
    count = [0] * 101

    for _ in range(d):
        _, *s = map(int, input().split())

        for si in s:
            count[si] += 1

    ans = []

    for i, ci in enumerate(count[1:], 1):
        if ci < k:
            continue

        ans.append(i)

    if len(ans) == 0:
        print(-1)
    else:
        print(*ans)


if __name__ == "__main__":
    main()
