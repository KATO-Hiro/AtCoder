# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, t = map(int, input().split())
    ans = 0

    for a in range(100 + 1):
        for b in range(100 + 1):
            for c in range(100 + 1):
                if (a + b + c <= s) and (a * b * c <= t):
                    ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
