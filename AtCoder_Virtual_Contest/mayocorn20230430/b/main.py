# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    summed = sum(t)
    
    for _ in range(m):
        pi, xi = map(int, input().split())
        pi -= 1

        tmp = summed
        tmp -= t[pi]
        tmp += xi
        print(tmp)


if __name__ == "__main__":
    main()
