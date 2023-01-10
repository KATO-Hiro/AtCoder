# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0

        for ai in a:
            if ai % 2 == 1:
                count += 1
    
        print(count)
    

if __name__ == "__main__":
    main()
