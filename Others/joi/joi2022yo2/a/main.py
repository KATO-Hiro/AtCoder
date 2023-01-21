# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    q = int(input())
    d = deque()
    ans = list()

    for _ in range(q):
        si = input().rstrip()

        if si == "READ":
            di = d.popleft()
            ans.append(di)
        else:
            d.appendleft(si)
    
    for si in ans:
        print(si)


if __name__ == "__main__":
    main()
