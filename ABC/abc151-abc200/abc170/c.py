# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    candidate = [i for i in range(-100, 200)]

    ans = list()

    for c in candidate:
        if c not in p:
            diff = abs(c - x)

            ans.append((diff, c))

    print(sorted(ans)[0][1])


if __name__ == '__main__':
    main()
