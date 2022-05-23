# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = list()

    for i in range(n):
        ai, bi = map(int, input().split())
        ab.append((bi, ai))
    
    ab = sorted(ab)
    time = 0

    for bi, ai in ab:
        if time + ai > bi:
            print("No")
            exit()
        
        time += ai

    print('Yes')


if __name__ == "__main__":
    main()
