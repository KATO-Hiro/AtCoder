# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if j - i != k - j:
                    continue
                if s[i] != "A":
                    continue
                if s[j] != "B":
                    continue
                if s[k] != "C":
                    continue

                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
