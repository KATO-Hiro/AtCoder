# -*- coding: utf-8 -*-


def main():
    n, m, k, e = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = [e] + sorted(list(map(int, input().split())), reverse=True)
    sum_a = sum(a)
    sum_b = sum(b[:k + 1])
    count = 0
    total = 0

    if sum_b >= sum_a:
        print('Yes')

        for i in range(k + 1):

            if total + b[i] >= sum_a:
                break
            else:
                total += b[i]
                count += 1
    else:
        print('No')

        for i in range(n):
            if total + a[i] <= sum_b:
                count += 1
                total += a[i]
            else:
                break

    print(count)


if __name__ == '__main__':
    main()
