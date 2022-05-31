# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    white = "." * b
    black = "#" * b

    for i in range(n):
        if i % 2 == 0:
            for j in range(a):
                s = (white + black) * (n // 2)

                if n % 2 == 1:
                    s += white

                print(s)
        else:
            for j in range(a):
                s = (black + white) * (n // 2)

                if n % 2 == 1:
                    s += black

                print(s)
    

if __name__ == "__main__":
    main()
