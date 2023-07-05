# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter, deque

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list()
    inf = 10**18
    c = Counter(a)

    # A[n]がnより大きい(重複を含む) or n以下で重複がある場合は売って、不足している巻を買う
    # 前者のケースの重複分も考慮しているのに、WAになるのはなぜ?
    # in: 1 1 3、out: 2となることが期待されるが、出力は1
    for key, value in c.items():
        if key > n:
            b += [inf] * value
        elif value >= 2:
            b += [key]
            b += [inf] * (value - 1)
        else:
            b += [key]

    d = deque(sorted(b))
    ans = 0

    for i in range(1, n + 1):
        ans += 1

        if len(d) > 0 and d[0] == i:
            d.popleft()
        else:
            if len(d) >= 2:
                d.pop()
                d.pop()
            else:
                ans -= 1
                break

    print(ans)


if __name__ == "__main__":
    main()
