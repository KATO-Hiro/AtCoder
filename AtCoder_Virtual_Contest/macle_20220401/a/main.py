# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())

    for a in range(101):
        for b in range(101):
            if (a + b) == x and (2 * a + 4 * b) == y:
                print("Yes")
                exit()
    
    print("No")


if __name__ == "__main__":
    main()
