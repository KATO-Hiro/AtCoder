# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ok = [False] * n

    for i in range(n):
        if s[i] != "G":
            continue

        ni = i - 1

        if ni >= 0:
            ok[ni] = True

        ok[i] = True

        ni = i + 1

        if ni < n:
            ok[ni] = True

    ans = ok.count(False)
    print(ans)


if __name__ == "__main__":
    main()
