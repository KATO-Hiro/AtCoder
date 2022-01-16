# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    size = dict()
    values = dict()

    for index, ai in enumerate(a, 1):
        if ai not in size.keys():
            size[ai] = 1
            values[ai] = [index]
        else:
            size[ai] += 1
            values[ai].append(index) 
    
    for i in range(q):
        xi, ki = map(int, input().split())

        if xi not in size.keys() or size[xi] < ki:
            print(-1)
        else:
            print(values[xi][ki - 1])


if __name__ == "__main__":
    main()
