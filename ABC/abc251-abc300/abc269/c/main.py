# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = n
    ans = [0]

    while m > 0:
        ans.append(m)
        m = (m - 1) & n # 天才的な解法
    
    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
