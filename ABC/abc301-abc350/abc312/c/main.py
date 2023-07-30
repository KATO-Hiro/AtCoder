# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ng = 0
    ok = 10**9 + 1

    def binary_search(ok, ng):
        while abs(ok - ng) > 1:
            wj = (ok + ng) // 2

            if is_met_conditions(wj):
                ok = wj
            else:
                ng = wj

        return ok

    def is_met_conditions(wj):
        count1, count2 = 0, 0

        for ai in a:
            if wj >= ai:
                count1 += 1

        for bi in b:
            if wj <= bi:
                count2 += 1

        if count1 >= count2:
            return True
        else:
            return False

    result = binary_search(ok=10**9 + 1, ng=0)
    print(result)


if __name__ == "__main__":
    main()
