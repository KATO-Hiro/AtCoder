# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    size = 5001
    ab = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(n):
        ai, bi = map(int, input().split())
        ab[ai][bi] += 1
    
    for j in range(size):
        for i in range(1, size):
            ab[j][i] += ab[j][i - 1]

    for i in range(size):
        for j in range(1, size):
            ab[j][i] += ab[j - 1][i]
    
    ans = 1

    for a in range(1, size):
        max_a = min(5000, a + k)

        for b in range(1, size):
            max_b = min(5000, b + k)
            candidate = ab[max_a][max_b] - ab[max_a][b - 1] - ab[a - 1][max_b] + ab[a - 1][b - 1]
            ans = max(ans, candidate)

    print(ans)
    

if __name__ == "__main__":
    main()
