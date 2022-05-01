# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    index = 0

    for i in range(3):
        index = a[index]
    
    print(index)


if __name__ == "__main__":
    main()
