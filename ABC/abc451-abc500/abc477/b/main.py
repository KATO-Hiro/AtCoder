# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    x = list(map(int, input().split()))
    ans = []

    for i, xi in enumerate(x):
        ok = True

        for j, xj in enumerate(x):
            if i == j:
                continue

            if abs(xi - xj) < d:
                ok = False
                break

        if ok:
            ans.append(i + 1)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
