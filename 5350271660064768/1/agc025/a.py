# -*- coding: utf-8 -*-


def main():
    n = input()
    ans = float('inf')

    for i in range(1, int(n)):
        a = i
        b = int(n) - i
        summed_a = sum(list(map(int, list(str(a)))))
        summed_b = sum(list(map(int, list(str(b)))))
        ans = min(ans, summed_a + summed_b)

    print(ans)


if __name__ == '__main__':
    main()
