# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    s = input().rstrip()

    # See:
    # https://atcoder.jp/contests/abc237/submissions/28904376
    t = s.rstrip("a")
    suffix = len(s) - len(t)
    u = t.lstrip("a")
    prefix = len(t) - len(u)

    if u == u[::-1] and prefix <= suffix:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
