# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans1 = 0

    for ai, bi in zip(a, b):
        if ai == bi:
            ans1 += 1
    
    print(ans1)
    print(len(set(a) & set(b)) - ans1)


if __name__ == "__main__":
    main()
