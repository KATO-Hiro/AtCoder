# -*- coding: utf-8 -*-


def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))

    diff = n * m - sum(a)

    if diff > k:
        print(-1)
    elif diff < 0:
        print(0)
    else:
        print(diff)



if __name__ == '__main__':
    main()
