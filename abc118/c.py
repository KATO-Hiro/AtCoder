# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    mod_a = a
    mod = min(a)
    index = 0

    while True:
        for idx, ai in enumerate(a):
            if idx != index:
                mod_a[idx] %= mod

                if 0 < mod_a[idx] < mod:
                    mod = mod_a[idx]
                    index = idx

        if mod_a.count(0) >= n - 1:
            break

    print(max(min(a), max(mod_a)))


if __name__ == '__main__':
    main()
