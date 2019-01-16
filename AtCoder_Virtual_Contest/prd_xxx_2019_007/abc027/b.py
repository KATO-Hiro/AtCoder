# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    summ_a = sum(a)

    if summ_a % n != 0:
        print(-1)
    else:
        from itertools import accumulate

        ave = summ_a // n
        accumulate_a = list(accumulate([0] + a))
        ans = 0

        # https://www.slideshare.net/chokudai/abc027
        # Verify the left side of the bridge.
        for i in range(1, n):
            current = accumulate_a[i] - accumulate_a[0]
            need = ave * i

            if current != need:
                ans += 1

        print(ans)


if __name__ == '__main__':
    main()
