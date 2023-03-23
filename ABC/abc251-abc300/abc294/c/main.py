# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list()

    for ai in a:
        c.append((ai, 1))
    for bi in b:
        c.append((bi, 2))

    ans_a, ans_b = list(), list()
    
    for i, (ci, case) in enumerate(sorted(c), 1):
        if case == 1:
            ans_a.append(i)
        else:
            ans_b.append(i)
    
    print(*ans_a)
    print(*ans_b)
    

if __name__ == "__main__":
    main()
