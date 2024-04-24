# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    pos = defaultdict(int)

    for i, ai in enumerate(a, 1):
        pos[i] = ai

    ans = list()

    for i in range(1, n + 1):
        while pos[i] != i:
            j = pos[i]
            pos[i], pos[j] = pos[j], pos[i]
            ans.append((i, j))

    print(len(ans))

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
