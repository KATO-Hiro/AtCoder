# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    t = 0

    while True:
        if t * (t + 1) // 2 >= x:
            print(t)
            exit()
        
        t += 1


if __name__ == "__main__":
    main()
