# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    summed_a = sum(a)
    t %= summed_a

    for index, ai in enumerate(a, 1):
        if t < ai:
            print(index, t)
            exit()
        else:
            t -= ai
    

if __name__ == "__main__":
    main()
