# -*- coding: utf-8 -*-


def main():
    from string import ascii_uppercase
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    alpha = ascii_uppercase
    ans = list()

    for hi in range(h):
        tmp = list()

        for wj in range(w):
            ai = a[hi][wj]

            if ai == 0:
                tmp.append(".")
            else:
                tmp.append(alpha[ai - 1])
    
        ans.append(tmp)
    
    for si in ans:
        print(''.join(si))
    

if __name__ == "__main__":
    main()
