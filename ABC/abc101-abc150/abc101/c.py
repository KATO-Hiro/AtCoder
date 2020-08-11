# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = (n - 1) // (k - 1)

    if (n - 1) % (k - 1) == 0:
        print(ans)
    else:
        print(ans + 1)
