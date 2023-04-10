# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    t = list(map(int, input().split()))

    for t1, t2 in zip(t, t[1:]):
        if t2 - t1 <= d:
            print(t2)
            exit()
    
    print(-1)
    

if __name__ == "__main__":
    main()
