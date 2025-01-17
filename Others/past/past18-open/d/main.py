# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = 10**18
    atk = [inf] * (n + 1)
    ans = [0] * (n + 1)

    for _ in range(m):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            x, y = qi[1], qi[2]
            atk[y] = x
        else:
            z = qi[1]
            ans[z] -= 1

            if atk[z] == inf:
                continue

            ans[atk[z]] += 1
            atk[z] = inf

    print(*ans[1:])


if __name__ == "__main__":
    main()
