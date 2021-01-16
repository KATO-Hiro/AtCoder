# -*- coding: utf-8 -*-


def main():
    p = int(input())
    f = [0 for _ in range(2 * 10 ** 5 + 100)]
    f[1] = 1
    f[2] = 1

    if p == 1:
        print(1)
        exit()

    for i in range(2, 2 * 10 ** 5):
        f[i] = (f[i - 1] + f[i - 2]) % p

    for j in range(1, 2 * 10 ** 5):
        if f[j] == 0:
            print(j)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
