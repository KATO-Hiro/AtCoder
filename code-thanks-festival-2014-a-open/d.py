# -*- coding: utf-8 -*-


def main():
    n, q = map(int, input().split())
    ans = [0 for _ in range(q)]

    for i in range(q):
        ai, bi, si, ti = map(int, input().split())

        if ti < ai or si > bi:
            ans[i] = (ti - si) * 100
        elif si < ai and ti > bi:
            ans[i] = (ti - bi + ai - si) * 100
        elif si >= ai and ti > bi:
            ans[i] = (ti - bi) * 100
        elif si < ai and ti <= bi:
            ans[i] = (ai - si) * 100

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
