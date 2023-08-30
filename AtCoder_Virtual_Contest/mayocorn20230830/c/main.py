# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    size = 1001
    ans = 10**12

    for i in range(10):
        count = [0] * size

        for si in s:
            index = si.index(str(i))
            count[index] += 1

        for i, ci in enumerate(count):
            if ci >= 2:
                count[i] = 1
                count[i + 10] += ci - 1

        candidate = 0

        for i, ci in enumerate(count):
            if ci == 1:
                candidate = i

        ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
