# -*- coding: utf-8 -*-


def main():
    from collections import deque, Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    b = list()
    inf = 10 ** 12

    for key, value in c.items():
        if value > 1:
            for i in range(value - 1):
                b.append(inf)

        b.append(key)

    d = deque(sorted(b))
    cur = 1
    ans = 0

    # コーナーケース
    # 同じaiが2つ以上ある場合やai > nの場合をinfとして扱う
    while n > 0:
        now = d[0]

        if cur == now:
            d.popleft()
            n -= 1
            ans += 1
            cur += 1
        else:
            if n >= 2:
                n -= 2
                d.pop()
                d.pop()

                ans += 1
                cur += 1
            else:
                print(ans)
                exit()

    print(ans)


if __name__ == "__main__":
    main()
