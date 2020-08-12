# -*- coding: utf-8 -*-


def main():
    pair_count = [1 for _ in range(50)]
    n = int(input())

    for i in range(2, n):
        pair_count[i + 2] = pair_count[i] + pair_count[i + 1]

    ans = sum(pair_count[:n + 1])

    if n != 0:
        ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
