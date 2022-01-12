# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x, y = [0] * n, [0] * n

    for i in range(n):
        xi, yi = map(int, input().split())
        x[i], y[i] = xi, yi
    
    ans = 0.0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            ans = max(ans, dist ** 0.5)
    
    print(ans)
    


if __name__ == "__main__":
    main()
