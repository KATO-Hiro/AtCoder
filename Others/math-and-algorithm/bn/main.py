# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0
    lr = [tuple(map(int, input().split())) for _ in range(n)]
    lr = sorted(lr, key=lambda x: x[1])
    prev = 0

    for li, ri in lr:
        if li >= prev:
            ans += 1
            prev = ri
    
    print(ans)


if __name__ == "__main__":
    main()
