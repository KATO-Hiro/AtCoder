# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    b = sorted(a)
    ans = 0
    
    for ai, aj in zip(b, b[1:]):
        ans += abs(aj - ai)
    
    print(ans)


if __name__ == "__main__":
    main()
