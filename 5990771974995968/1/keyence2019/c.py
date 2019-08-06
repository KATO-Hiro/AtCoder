# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if sum(a) < sum(b):
        print(-1)
    else:
        c = [a[i] - b[i] for i in range(n)]
        minus = [ci for ci in c if ci < 0]
        plus = sorted([ci for ci in c if ci > 0], reverse=True)
        ans = len(minus)
        total = sum(minus)

        if total != 0:
            for index, p in enumerate(plus, 1):
                total += p
                ans += 1

                if total >= 0:
                    print(ans)
                    exit()
        else:
            print(ans)


if __name__ == '__main__':
    main()
