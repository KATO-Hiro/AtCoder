# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w = int(input())

    # m進数で考える (解法を見れば納得だが、どうやって思いついている?)
    # w = 999のときは、9 * 3 = 27個の整数で表現可能
    # w = 10 ** 6のケースは、m = 100と考えれば良さそう
    # n = (a * 10 ** 4) + (b * 10 ** 2) + (c * 1)
    # a = [1, 100], b = [1, 99], c = [1, 99]
    ans = [10 ** 6]

    for i in range(1, 100):
        ans.append(i)
        ans.append(i * 10 ** 2)
        ans.append(i * 10 ** 4)
    
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
