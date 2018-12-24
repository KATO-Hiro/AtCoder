# -*- coding: utf-8 -*-


def main():
    n, d = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)

    if n < d:
        print(0)
    else:
        members = [0] + a[:(n // d) * d]
        print(sum(members[::d]))


if __name__ == '__main__':
    main()
