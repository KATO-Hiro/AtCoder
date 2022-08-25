# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    for i in range(1, 10001):
        if (i * 8 // 100) == a and (i * 10 // 100) == b:
            print(i)
            exit()
    
    print(-1)


if __name__ == "__main__":
    main()
