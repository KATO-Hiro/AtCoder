# -*- coding: utf-8 -*-


def main():
    n = int(input())
    d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""

    if n < 36:
        print(d[n])
        exit()

    for i in range(2, -1, -1):
        p, q = divmod(n, 36 ** i)

        if i == 2 and p == 0:
            continue

        ans += d[p]

        n = q

    print(ans)


if __name__ == "__main__":
    main()
