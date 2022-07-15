# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    d = deque()
    r_count = 0

    for si in s:
        size = len(d)

        if si == "R":
            r_count += 1
            continue

        if r_count % 2 == 0:
            if size > 0 and d[-1] == si:
                d.pop()
            else:
                d.append(si)
        else:
            if size > 0 and d[0] == si:
                d.popleft()
            else:
                d.appendleft(si)
    
    if r_count % 2 == 1:
        d = reversed(d)
    
    print(''.join(list(d)))


if __name__ == "__main__":
    main()
