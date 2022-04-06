# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = [input().rstrip() for _ in range(3)]
    t = input().rstrip()
    ans = ""

    for ti in t:
        ans += s[int(ti) - 1]
    
    print(ans)


if __name__ == "__main__":
    main()
