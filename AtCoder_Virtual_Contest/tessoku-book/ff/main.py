# -*- coding: utf-8 -*-


def f(x, y):
    diff = 0

    for xi, yi in zip(x, y):
        if xi != yi:
            diff += 1

    if diff == 0:
        return "1"
    elif diff == 1:
        return "2"
    else:
        return "3"


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    st = [input().rstrip().split() for _ in range(n)]
    ans = list()

    # 当選番号を仮定して、全探索
    for id in range(10**4):
        id = str(id).zfill(4)
        ok = True

        for si, ti in st:
            if f(si, id) != ti:
                ok = False
                break

        if ok:
            ans.append(id)

    if len(ans) == 1:
        print(*ans)
    else:
        print("Can't Solve")


if __name__ == "__main__":
    main()
