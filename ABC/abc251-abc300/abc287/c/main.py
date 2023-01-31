# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    degree = [0] * n
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        degree[ai] += 1
        degree[bi] += 1
    
    c = Counter(degree)

    if c[1] == 2 and c[2] == n - 2:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
