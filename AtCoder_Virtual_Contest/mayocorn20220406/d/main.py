# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    k = int(input())

    # 文字列で条件を満たす値をk個生成
    d = deque([str(i) for i in range(1, 10)])
    ans = [str(i) for i in range(1, 10)]
    count = 0

    while count < k:
        di = d.popleft()
        digit_end = di[-1]

        for i in range(10):
            if abs(int(digit_end) - i) <= 1:
                new_di = di + str(i)
                d.append(new_di)
                ans.append(new_di)

                count += 1

    print(ans[k - 1])


if __name__ == "__main__":
    main()
