# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n, m = map(int, input().split())
    total = n + m
    a = deque(list(map(int, input().split())))
    b = deque(list(map(int, input().split())))

    count = 0
    c = list()

    while count < total:
        if (len(a) == 0):
            ci = b.popleft()
            c.append(ci)
        elif (len(b) == 0):
            ci = a.popleft()
            c.append(ci)
        elif a[0] > b[0]:
            ci = b.popleft()
            c.append(ci)
        elif a[0] < b[0] or a[0] == b[0]:
            ci = a.popleft()
            c.append(ci)

        count += 1

    print('\n'.join(map(str, c)))


if __name__ == '__main__':
    main()
