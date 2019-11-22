# -*- coding: utf-8 -*-


def sum_digit(number):
    return sum(list(map(int, list(str(number)))))


def main():
    n = int(input())
    count = 0
    ans = list()

    # f(x) = n - xと変形
    # f(x)による増加分は，制約条件から多くても9 * 19 < 200
    # 探索範囲を絞る
    for x in range(max(1, n - 200), n + 1):
        if x + sum_digit(x) == n:
            count += 1
            ans.append(x)

    m = len(ans)

    print(m)

    if m > 0:
        print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
