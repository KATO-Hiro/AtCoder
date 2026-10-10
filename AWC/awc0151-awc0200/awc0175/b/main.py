# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, k = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    k -= 1
    ans = ""

    for si in s:
        ans += si[k]

    print(ans)


if __name__ == "__main__":
    main()
