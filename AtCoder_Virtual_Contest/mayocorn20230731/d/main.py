# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    # TODO: Change lower value if necessary.
    def binary_search(ok, ng, a):
        while abs(ok - ng) > 1:
            wj = (ok + ng) // 2

            if is_met_conditions(wj, a):
                ok = wj
            else:
                ng = wj

        return ok

    def is_met_conditions(b, a) -> bool:
        # TODO: Write here.

        x = a**3 + (a**2 * b) + (a * b**2) + b**3

        # Condition is True.
        if x >= n:
            return True
        else:
            return False

    ans = float("inf")

    for a in range(10**6 + 1):
        ng = -1
        ok = 10**6 + 1

        b = binary_search(ok=ok, ng=ng, a=a)
        ans = min(ans, a**3 + a**2 * b + a * b**2 + b**3)
        # print(ans)

    print(ans)


if __name__ == "__main__":
    main()
