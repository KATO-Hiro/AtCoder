# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    x = list(input().rstrip())
    n = len(x)
    summed = 0
    ans = [0] * (n + 1)

    for i, xi in enumerate(x, 1):
        summed += int(xi)

        yi = summed
        pos = i

        while yi > 0:
            p, q = divmod(yi, 10)
            ans[pos] += q

            yi = p
            pos -= 1
    
    # 繰り上がりの処理
    for i in range(n, 0, -1):
        value = ans[i]
        pos = i

        if value < 10:
            continue

        while value > 0:
            pass
            ans[pos] -= value
            p, q = divmod(value, 10)

            ans[pos] += q
            ans[pos - 1] += p
            value = p
        
    if ans[0] == 0:
        ans = ans[1:]

    print(''.join(map(str, ans)))


if __name__ == "__main__":
    main()
