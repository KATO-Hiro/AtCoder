# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    k = int(input())
    d = deque()

    for i in range(1, 10):
        d.append(str(i))

    n = 0
    ans = [str(i) for i in range(1, 10)]

    while n < k:
        di = d.popleft()
        end_digit = di[-1]

        for i in range(10):
            if abs(int(end_digit) - i) <= 1:
                new_di = di + str(i)
                ans.append(new_di)
                d.append(new_di)

                n += 1

    print(ans[k - 1])


if __name__ == '__main__':
    main()
