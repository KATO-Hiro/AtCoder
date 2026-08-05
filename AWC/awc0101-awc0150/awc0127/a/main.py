# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    t = [si for si in s if si >= k]
    size = len(t)

    if size == 0:
        print(-1)
    else:
        print(sum(t) / size)


if __name__ == "__main__":
    main()
