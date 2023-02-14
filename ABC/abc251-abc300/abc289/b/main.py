# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = deque()

    if m > 0:
        a = list(map(int, input().split()))
    else:
        a = []
    
    ans = list()
    
    for i in range(1, n + 1):
        d.append(i)

        if not i in a:
            while d:
                di = d.pop()
                ans.append(di)
    
    print(*ans)
    

if __name__ == "__main__":
    main()
