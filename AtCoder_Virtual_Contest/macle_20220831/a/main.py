# -*- coding: utf-8 -*-


def main():
    from string import ascii_lowercase
    import sys

    input = sys.stdin.readline

    p = list(map(int, input().split()))
    s = ascii_lowercase
    ans = ""

    for pi in p:
        pi -= 1
        ans += s[pi]
    
    print(ans)


if __name__ == "__main__":
    main()
