# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    s = input().rstrip()
    d = deque(s)
    count1, count2 = 0, 0

    for si in s:
        if si == "a":
            count1 += 1
        else:
            break

    for sj in s[::-1]:
        if sj == "a":
            count2 += 1
        else:
            break

    if count2 > count1:
        for i in range(count2 - count1):
            d.appendleft("a")

    if list(d) == list(d)[::-1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
