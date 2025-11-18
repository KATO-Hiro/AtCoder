# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    results = list()

    for i in range(n):
        si, ei = map(int, input().split())
        results.append((si * m + ei, i + 1))

    ans = [id for _, id in sorted(results)]
    print(*ans)


if __name__ == "__main__":
    main()
