# -*- coding: utf-8 -*-


def main():
    from sys import setrecursionlimit

    setrecursionlimit(10 ** 7)

    p = int(input())
    f = [0 for _ in range(10 ** 4)]
    f[1] = 1
    f[2] = 1

    def rec(i):
        if i > 10 ** 4:
            return -1

        f[i + 2] = f[i + 1] + f[i]

        for ii in range(i, i + 3):
            if f[ii] % p == 0:
                return ii

        i += 1

        return rec(i)

    print(rec(1))


if __name__ == "__main__":
    main()
