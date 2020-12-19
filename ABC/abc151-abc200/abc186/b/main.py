# -*- coding: utf-8 -*-


def main():
    import numpy as np
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    a = np.array(a)
    print(np.sum(a - np.min(a)))


if __name__ == "__main__":
    main()
