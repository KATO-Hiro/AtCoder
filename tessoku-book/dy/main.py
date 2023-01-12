# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    x -= 1
    a = list(input().rstrip())
    a[x] = "@"
    d = deque()
    d.append(x)

    while d:
        pos = d.popleft()

        if ((pos - 1) >= 0) and a[pos - 1] == ".":
            a[pos - 1] = "@"
            d.append(pos - 1)
        if ((pos + 1) < n) and a[pos + 1] == ".":
            a[pos + 1] = "@"
            d.append(pos + 1)
    
    print(''.join(a))
   

if __name__ == "__main__":
    main()
