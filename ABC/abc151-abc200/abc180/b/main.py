# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    n = int(input())
    x = list(map(lambda y: abs(int(y)), input().split()))

    ans1 = sum(x)
    ans2 = sqrt(sum([j ** 2 for j in x]))
    ans3 = max(x)

    print(ans1)
    print(ans2)
    print(ans3)


if __name__ == "__main__":
    main()
