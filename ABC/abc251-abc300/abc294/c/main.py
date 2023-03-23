# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = {ci: i for i, ci in enumerate(sorted(a + b), 1)}
    
    print(*[c[ai] for ai in a])
    print(*[c[bi] for bi in b])
    

if __name__ == "__main__":
    main()
