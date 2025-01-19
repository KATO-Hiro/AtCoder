# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r = int(input())
    r2 = r**2
    count = list()

    def f(i, j):
        met = True

        for dy in [-0.5, 0.5]:
            for dx in [-0.5, 0.5]:
                if (i + dy) ** 2 + (j + dx) ** 2 > r2:
                    met = False
                    break

        return met

    ans = 0

    for i in range(r):
        ok, ng = 0, 10**6 + 100

        while abs(ng - ok) > 1:
            wj = (ok + ng) // 2

            if f(i, wj):
                ok = wj
            else:
                ng = wj

        count.append(ok)

    ans = sum(count) * 4
    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
