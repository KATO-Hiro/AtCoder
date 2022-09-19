# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x, y = 1, 1

    # 各軸に対して二分探索
    for ti in range(2):
        wa, ac = 0, n

        while (wa + 1) < ac:
            wj = (ac + wa) // 2

            if ti == 0:
                print("?", 1, wj, 1, n, flush=True)
            else:
                print("?", 1, n, 1, wj, flush=True)

            result = int(input())

            if result != wj:
                ac = wj
            else:
                wa = wj
            
        x = ac
        x, y = y, x

    print("!", x, y, flush=True)



if __name__ == "__main__":
    main()
