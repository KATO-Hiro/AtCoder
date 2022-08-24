# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t_large = map(int, input().split())
    t = list(map(int, input().split()))
    ans = t_large

    for first, second in zip(t, t[1:]):
        ans += min(t_large, second - first)
    
    print(ans)


if __name__ == "__main__":
    main()
