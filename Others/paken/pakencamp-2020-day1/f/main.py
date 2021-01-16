# -*- coding: utf-8 -*-


def main():
    p = int(input())
    f = [0, 1, 1]

    for i in range(1, 10 ** 5):
        f.append(f[-1] + f[-2])

    for j in range(1, 10 ** 5):
        if f[j] % p == 0:
            print(j)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
