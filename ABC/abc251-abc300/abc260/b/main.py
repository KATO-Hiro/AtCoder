# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    math = sorted([(ai, i) for i, ai in enumerate(a)], key=lambda x: (x[0], -x[1]), reverse=True)
    english = sorted([(bi, i) for i, bi in enumerate(b)], key=lambda x: (x[0], -x[1]), reverse=True)
    both = sorted([(ai + bi, i) for i, (ai, bi) in enumerate(zip(a, b))], key=lambda x: (x[0], -x[1]), reverse=True)
    ok = [False] * n
    ans = list()

    def judge(test, limit):
        if limit == 0:
            return

        i, count = 0, 0
        
        while i < n:
            _, t = test[i]

            if not ok[t]:
                ans.append(t + 1)
                ok[t] = True
                count += 1

                if count == limit:
                    return

            i += 1
    
    judge(math, x)
    judge(english, y)
    judge(both, z)

    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
