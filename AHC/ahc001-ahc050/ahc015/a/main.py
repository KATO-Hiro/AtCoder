# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = list(map(int, input().split()))

    for _ in range(100):
        pt = int(input())
        print("L", flush=True)


if __name__ == "__main__":
    main()
