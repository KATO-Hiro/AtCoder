# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, a = map(int, input().split())
    s = input().rstrip()
    pos = a
    ans = 0

    # aを基準に#が左側 / 右側にあるか?
    # aの近くにある#から順に、右側→左側→右側・・・と移動するはず
    # 端部の扱いに注意
    left = deque()
    right = deque()

    for i, si in enumerate(s, 1):
        if si == ".":
            continue

        if i < a:
            left.append(i)
        else:
            right.append(i)

    # print(left, right)

    i = 0

    while True:
        if len(left) == 0 and len(right) == 0:
            break

        if i % 2 == 0:
            if len(right) > 0:
                ri = right.popleft()
                ans += ri - pos
                pos = ri
            else:
                ans += n + 1 - pos
                pos = n + 1
        else:
            if len(left) > 0:
                li = left.pop()
                ans += pos - li
                pos = li
            else:
                ans += pos
                pos = 0

        i += 1

    print(ans)


if __name__ == "__main__":
    main()
