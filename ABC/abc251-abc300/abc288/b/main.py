# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = sorted([input().rstrip() for _ in range(n)][:k])

    print(*s, sep="\n")
    

if __name__ == "__main__":
    main()
