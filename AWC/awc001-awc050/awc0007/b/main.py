# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ids = defaultdict(int)
    count = 0
    ws = []

    for _ in range(n):
        m = int(input())
        w = input().rstrip().split()
        x = []

        for wi in w:
            if wi not in ids:
                count += 1
                ids[wi] = count

            x.append(ids[wi])

        ws.append(x)

    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            if len(set(ws[i]) & set(ws[j])) >= k:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
