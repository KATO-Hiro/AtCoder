# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())

    for a in range(x + 1):
        b = x - a

        if (2 * a + 4 * b) == y:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
