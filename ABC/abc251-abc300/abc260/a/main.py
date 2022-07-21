# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    c = Counter(s)

    for key, value in c.items():
        if value == 1:
            print(key)
            exit()
    
    print(-1)


if __name__ == "__main__":
    main()
