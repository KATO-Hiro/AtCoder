# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ans = list()

    def f(a, j):
        if len(a) == n:
            ans.append(a[:])
            return

        for cur in range((j - 1) * 10 + 1, m - (n - j) * 10 + 1):
            if j >= 2:
                prev = a[-1]

                if cur - prev < 10:
                    continue

            a.append(cur)
            f(a, j + 1)
            a.pop()

    f([], 1)

    print(len(ans))

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
