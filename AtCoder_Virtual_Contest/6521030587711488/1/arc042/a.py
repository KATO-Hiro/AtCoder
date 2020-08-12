# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)][::-1]
    memo = [0 for _ in range(n + 1)]

    for ai in a:
        if memo[ai] == 1:
            continue
        else:
            memo[ai] = 1
            print(ai)

    for index, m in enumerate(memo):
        if index == 0:
            continue

        if m == 0:
            print(index)


if __name__ == '__main__':
    main()
