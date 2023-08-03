# -*- coding: utf-8 -*-


def ok(size, d, k):
    return size**2 - max(d.values()) <= k


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w, k = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    ans = 1

    for size in range(2, min(h, w) + 1):
        for i in range(h):
            if i + size > h:
                break

            d = defaultdict(int)

            for y in range(i, i + size):
                for x in range(size):
                    d[s[y][x]] += 1

            if ok(size, d, k):
                ans = size
                break

            for x in range(size, w):
                for y in range(i, i + size):
                    d[s[y][x]] += 1
                    d[s[y][x - size]] -= 1

                if ok(size, d, k):
                    ans = size
                    break

    print(ans)


if __name__ == "__main__":
    main()
