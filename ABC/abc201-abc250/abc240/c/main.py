# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    dp = 1

    for _ in range(n):
        ai, bi = map(int, input().split())
        dp = dp << ai | dp << bi
    
    if dp >> x & 1:
        print("Yes")
    else:
        print("No")    


if __name__ == "__main__":
    main()
