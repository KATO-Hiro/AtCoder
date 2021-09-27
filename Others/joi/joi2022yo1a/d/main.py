# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = set(list(map(int, input().split())))
    ans = [False for _ in range(n)]

    for index, ai in enumerate(a):
        if ai in b:
            ans[index] = True
    
    print(sum(ans))


if __name__ == "__main__":
    main()
