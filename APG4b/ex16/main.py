# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))

    for first, second in zip(a, a[1:]):
        if first == second:
            print("YES")
            exit()
    
    print("NO")


if __name__ == "__main__":
    main()
