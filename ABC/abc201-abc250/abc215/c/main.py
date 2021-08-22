# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    s, k = map(str, input().split())
    k = int(k) - 1
    t = sorted(set(list(permutations(s))))
    print(''.join(map(str, t[k])))


if __name__ == "__main__":
    main()
