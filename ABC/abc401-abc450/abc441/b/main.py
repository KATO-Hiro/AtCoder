# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = set(input().rstrip())
    t = set(input().rstrip())
    q = int(input())

    for _ in range(q):
        wi = input().rstrip()
        takahashi = True
        aoki = True

        for wij in wi:
            if wij not in s:
                takahashi = False
            elif wij not in t:
                aoki = False

        if takahashi and not aoki:
            print("Takahashi")
        elif not takahashi and aoki:
            print("Aoki")
        else:
            print("Unknown")


if __name__ == "__main__":
    main()
