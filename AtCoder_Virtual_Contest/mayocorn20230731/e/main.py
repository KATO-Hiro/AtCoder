# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # TODO: Change lower value if necessary.
    ok = 10 ** (-12)
    ng = 10**9 + 1

    def binary_search(ok, ng):
        for _ in range(100):
            wj = (ok + ng) / 2

            if is_met_conditions(wj):
                ok = wj
            else:
                ng = wj

        return ok

    def is_met_conditions(wj) -> bool:
        # TODO: Write here.

        count = 0

        for ai in a:
            if ai > wj:
                count += ceil(ai / wj) - 1

        # print(wj, count)

        # Condition is True.
        if count > k:
            return True
        else:
            return False

    ans = binary_search(ok=ok, ng=ng)
    print(ceil(ans))


if __name__ == "__main__":
    main()
