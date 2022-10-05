# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    a = [int(input()) for _ in range(n)]
    visited = [False] * n
    pos = 0
    ans = 0
    
    while True:
        pos = a[pos]
        ans += 1

        if pos == 2:
            print(ans)
            exit()
        
        pos -= 1

        if visited[pos]:
            print(-1)
            exit()

        visited[pos] = True


if __name__ == "__main__":
    main()
