# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = Counter(list(map(int, input().split())))
    b = Counter(list(map(int, input().split())))

    for key, value in b.items():
        if key not in a.keys():
            print("No")
            exit()
        
        if a[key] < value:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
