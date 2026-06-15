# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    candidates = []

    for _ in range(n):
        ci = int(input())
        v = sorted(list(map(int, input().split())))
        vi = v[ci // 2]

        if vi < 0:
            continue

        candidates.append(vi)

    candidates.sort(reverse=True)
    size = len(candidates)
    ans = sum(candidates[: min(k, size)])
    print(ans)


if __name__ == "__main__":
    main()
