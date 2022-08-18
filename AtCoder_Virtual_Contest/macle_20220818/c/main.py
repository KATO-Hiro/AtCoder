# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    k = int(input())
    ans = set()

    for i in range(1, k + 1):
        for j in range(n - i + 1):
            t = s[j:j + i]
            ans.add(t)
    
    print(sorted(ans)[k - 1])


if __name__ == "__main__":
    main()
