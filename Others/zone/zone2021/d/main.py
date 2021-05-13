# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = deque()
    r_count = 0

    for si in s:
        if si == "R":
            r_count += 1
        else:
            if r_count % 2 == 0:
                if t and t[-1] == si:
                    t.pop()
                else:
                    t.append(si)
            else:
                if t and t[0] == si:
                    t.popleft()
                else:
                    t.appendleft(si)

    ans = list(t)

    if r_count % 2 == 1:
        ans = reversed(ans)

    print("".join(ans))


if __name__ == "__main__":
    main()
