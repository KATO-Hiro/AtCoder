# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    num_max = 300

    for a in range(1, num_max + 1):
        for b in range(1, num_max + 1):
            for c in range(1, num_max + 1):
                d = x - (a + b + c)

                if d <=0:
                    break

                if 1 <= d <= n and a * b * c * d == y:
                    print('Yes')
                    exit()
    
    print('No')


if __name__ == "__main__":
    main()
