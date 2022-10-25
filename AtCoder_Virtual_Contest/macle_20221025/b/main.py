# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    q = int(input())
    d = deque(s)
    reverse_count = 0

    for _ in range(q):
        q = list(input().split())

        if q[0] == "1":
            reverse_count += 1
        else:
            fi, ci = q[1:]

            if reverse_count % 2 == 0:
                if fi == "1":
                    d.appendleft(ci)
                else:
                    d.append(ci)
            else:
                if fi == "1":
                    d.append(ci)
                else:
                    d.appendleft(ci)
    
    if reverse_count % 2 == 1:
        d = list(reversed(d))
    
    print(''.join(d))


if __name__ == "__main__":
    main()
