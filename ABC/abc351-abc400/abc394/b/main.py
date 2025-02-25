# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list()

    for _ in range(n):
        si = input().rstrip()
        s.append((len(si), si))

    ans = ""

    for _, si in sorted(s):
        ans += si

    print(ans)


if __name__ == "__main__":
    main()
