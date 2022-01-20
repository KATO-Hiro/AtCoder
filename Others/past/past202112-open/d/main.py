# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = list()

    for i, (ai, bi) in enumerate(zip(a, b), 1):
        ab.append((ai + bi, ai, i))

    ans = list()
    
    for ai, bi, i in sorted(ab, key=lambda x: (-x[0], -x[1], x[2])):
        ans.append(i)
    
    print(*ans)


if __name__ == "__main__":
    main()
