# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = deque()
    d.append((a[0], 1))
    ball_count = 1
    print(ball_count)

    for i in range(1, n):
        ai = a[i]

        if ball_count >= 1:
            value, count = d.pop()
            ball_count -= count

            if ai == value:
                if count + 1 == value:
                    pass
                else:
                    d.append((value, count + 1))
                    ball_count += count + 1
            else:
                d.append((value, count))
                d.append((ai, 1))
                ball_count += count + 1
        else:
            d.append((ai, 1))
            ball_count += 1

        print(ball_count)


if __name__ == "__main__":
    main()
