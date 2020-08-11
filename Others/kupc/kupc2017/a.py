# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    total = 0

    for key, ai in enumerate(a, 1):
        total += ai

        if total >= k:
            print(key)
            exit()

    print(-1)


if __name__ == '__main__':
    main()
