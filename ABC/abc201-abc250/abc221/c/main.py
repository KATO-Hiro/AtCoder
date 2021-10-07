# -*- coding: utf-8 -*-


def main():
    from itertools import product

    n = list(input())
    m = len(n)
    patterns = product([0, 1], repeat=m)
    ans = 0

    for pattern in patterns:
        former = list()
        latter = list()

        for index, p in enumerate(pattern):
            if p == 0:
                former.append(n[index])
            else:
                latter.append(n[index])
        
        if len(former) == 0:
            continue
        if len(latter) == 0:
            continue

        ans = max(ans, int(''.join(sorted(former, reverse=True))) * int(''.join(sorted(latter, reverse=True))))

    print(ans)


if __name__ == "__main__":
    main()
