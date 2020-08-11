# -*- coding: utf-8 -*-


def main():
    n, p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    odd_count = sum([1 for ai in a if ai % 2 == 1])

    # See:
    # https://www.youtube.com/watch?v=5usHNxVUzqk
    if odd_count == 0:
        if p == 0:
            print(2 ** n)
        else:
            print(0)
    else:
        print(2 ** (n - 1))


if __name__ == '__main__':
    main()
