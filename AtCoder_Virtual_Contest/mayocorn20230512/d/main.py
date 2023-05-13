# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    s = set(a)
    m = len(s)
    inf = 10**12
    # 同じ巻 / n + 1巻以上は、他の巻を買うために使う
    # = infとして扱う
    # △: n + 1巻以上の場合も重複があるパターンを見逃し
    d = deque(sorted(s) + [inf] * (n - m))

    ans = 0
    size = n

    for vol in range(1, n + 1):
        ans += 1

        if size >= 1 and vol == d[0]:
            d.popleft()
            size -= 1
        else:
            if size >= 2:
                d.pop()
                d.pop()
                size -= 2
            else:
                ans -= 1
                break

    print(ans)


if __name__ == "__main__":
    main()
