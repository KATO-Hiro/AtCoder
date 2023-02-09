# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    s = list(input().rstrip())
    t = s * 2
    ans = float("inf")

    for i in range(n):
        candidate = a * i

        u = t[i:i + n]
        v = u[::-1]
        count = 0

        for ui, vi in zip(u, v):
            if ui != vi:
                count += 1
        
        candidate += b * count // 2
        ans = min(ans, candidate)

    print(ans)
    

if __name__ == "__main__":
    main()
