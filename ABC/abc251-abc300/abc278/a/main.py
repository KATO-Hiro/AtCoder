# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = deque(a)

    for i in range(k):
        d.popleft()
        d.append(0)
    
    print(*d)
    

if __name__ == "__main__":
    main()
