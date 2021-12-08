# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    balls = [i + 1 for i in range(n)]

    for i in range(m):
        xi, yi = map(int, input().split())
        xi -= 1

        balls[xi] = yi
    
    print('\n'.join(map(str, balls)))


if __name__ == "__main__":
    main()
