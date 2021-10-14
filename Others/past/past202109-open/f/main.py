# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()

    ans = [i for i in range(1, n + 1)]
    tmp = ans[:]
    indices = [index for index, si in enumerate(s) if si == '0']

    if len(indices) == 1:
        print(-1)
        exit()
    
    for i in range(len(indices)):
        ans[indices[i]] = tmp[indices[i - 1]]

    print(*ans)


if __name__ == "__main__":
    main()
