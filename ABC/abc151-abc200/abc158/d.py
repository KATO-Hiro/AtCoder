# -*- coding: utf-8 -*-


def main():
    from collections import deque

    s = input()
    q = int(input())
    d = deque()
    d.append(s)
    reverse_count = 0

    for i in range(q):
        qi = input().split()

        if qi[0] == '1':
            reverse_count += 1
        else:
            if reverse_count % 2 == 0:
                if qi[1] == '1':
                    d.appendleft(qi[2])
                else:
                    d.append(qi[2])

            else:
                if qi[1] == '1':
                    d.append(qi[2])
                else:
                    d.appendleft(qi[2])

    c = ''.join(map(str, d))

    if reverse_count % 2 == 1:
        c = c[::-1]

    print(c)


if __name__ == '__main__':
    main()
