# -*- coding: utf-8 -*-


def main():
    from collections import deque

    s = input()
    t = input()
    n = len(s)
    count = 0

    if s == t:
        print(0)
        exit()
    elif len(s) != len(t):
        print(-1)
        exit()

    d = deque()

    for si in s:
        d.append(si)

    for i in range(n):
        count += 1

        di = d.pop()
        d.appendleft(di)

        result = ''.join(map(str, d))

        if result == t:
            print(count)
            exit()

    print(-1)



if __name__ == '__main__':
    main()
