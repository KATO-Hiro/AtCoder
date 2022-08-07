# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    size = 10
    count = [[0] * size for _ in range(size)]

    for i in range(1, n + 1):
        digit = list(str(i))
        top, bottom = int(digit[0]), int(digit[-1])
        count[top][bottom] += 1
    
    ans = 0
    
    for top in range(1, size):
        for bottom in range(1, size):
            ans += count[top][bottom] * count[bottom][top]
    
    print(ans)


if __name__ == "__main__":
    main()
