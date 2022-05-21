# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_max = max(a)

    for i, ai in enumerate(a, 1):
        if ai == a_max and i in b:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
