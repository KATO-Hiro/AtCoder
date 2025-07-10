# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    ans = set()

    for i, si in enumerate(s):
        for j, sj in enumerate(s):
            if i == j:
                continue

            ans.add(si + sj)

    print(len(ans))


if __name__ == "__main__":
    main()
