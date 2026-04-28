# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, q = map(int, input().split())
    parents = defaultdict(int)
    children = defaultdict(int)
    pending = 10**9

    for i in range(1, n + 1):
        parents[i] = pending
        children[i] = pending

    for _ in range(q):
        ci, pi = map(int, input().split())

        children[pi] = ci

        parent = parents[ci]

        if parent != pending:
            children[parent] = pending

        parents[ci] = pi

    ans = []

    for j in range(1, n + 1):
        if parents[j] != pending:
            ans.append(0)
        else:
            pos = j
            count = 1

            while children[pos] != pending:
                pos = children[pos]
                count += 1

            ans.append(count)

    print(*ans)


if __name__ == "__main__":
    main()
