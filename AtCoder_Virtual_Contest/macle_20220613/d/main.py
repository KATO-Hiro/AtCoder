# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for op1, op2, op3 in list(product([1, -1], repeat=3)):
        tmp = [0] * n

        for index, value in enumerate(xyz):
            tmp[index] = sum([op1 * value[0], op2 * value[1], op3 * value[2]])
        
        candidates = sorted(tmp, reverse=True)
        ans = max(ans, sum(candidates[:m]))
    
    print(ans)


if __name__ == "__main__":
    main()
