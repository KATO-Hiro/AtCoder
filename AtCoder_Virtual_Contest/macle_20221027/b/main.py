# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    q = int(input())
    d = deque(s)
    reversed_count = 0 

    for i in range(q):
        qi = list(input().rstrip().split())

        if qi[0] == "1":
            reversed_count += 1
        else:
            fi, ci = qi[1:]


            if reversed_count % 2 == 0:
                if fi == "1":
                    d.appendleft(ci)
                else:
                    d.append(ci)
            else:
                if fi == "1":
                    d.append(ci)
                else:
                    d.appendleft(ci)

    if reversed_count % 2 == 1:
        d = reversed(d)

    print(*d, sep="")


if __name__ == "__main__":
    main()
