# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    s = input().rstrip()
    d = deque(s)
    q = int(input())
    rev = 0

    for _ in range(q):
        qi = input().rstrip().split()

        if qi[0] == "1":
            rev += 1
        else:
            fi, ci = qi[1:]

            if fi == "1":
                if rev % 2 == 0:
                    d.appendleft(ci)
                else:
                    d.append(ci)
            else:
                if rev % 2 == 0:
                    d.append(ci)
                else:
                    d.appendleft(ci)

    if rev % 2 == 1:
        d = list(reversed(d))

    print("".join(d))


if __name__ == "__main__":
    main()
