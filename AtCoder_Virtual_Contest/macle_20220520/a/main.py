# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(map(int, input().split()))
    candidates = list()

    for a in range(1, 1001):
        for b in range(1, 1001):
            c = 4 * a * b + 3 * a + 3 * b

            if c <= 1000:
                candidates.append(c)
    
    ans = 0
    
    for si in s:
        if si not in candidates:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
