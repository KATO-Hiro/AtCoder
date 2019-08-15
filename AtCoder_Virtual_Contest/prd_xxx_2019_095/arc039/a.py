# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    mod_a1 = list(str(a))
    mod_a1[0] = 9
    mod_a1 = int(''.join(map(str, mod_a1)))
    mod_b1 = list(str(b))
    mod_b1[0] = 1
    mod_b1 = int(''.join(map(str, mod_b1)))
    mod_a2 = list(str(a))
    mod_a2[1] = 9
    mod_a2 = int(''.join(map(str, mod_a2)))
    mod_b2 = list(str(b))
    mod_b2[1] = 0
    mod_b2 = int(''.join(map(str, mod_b2)))
    mod_a3 = list(str(a))
    mod_a3[2] = 9
    mod_a3 = int(''.join(map(str, mod_a3)))
    mod_b3 = list(str(b))
    mod_b3[2] = 0
    mod_b3 = int(''.join(map(str, mod_b3)))
    print(max(mod_a1 - b, a - mod_b1, a - b, mod_a2 - b, a - mod_b2, mod_a3 - b, a - mod_b3))


if __name__ == '__main__':
    main()
