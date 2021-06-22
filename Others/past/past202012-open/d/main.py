# -*- coding: utf-8 -*-


def main():
    n = int(input())
    d = dict()

    for i in range(n):
        si = input().rstrip()
        si_int = int(si)
        si_int_size = len(list(str(si_int)))
        si_str_size = len(list(si))

        if si_int in d.keys():
            d[si_int].append(si_str_size - si_int_size)
        else:
            d[si_int] = [si_str_size - si_int_size]

    for key in sorted(d.keys()):
        for k in sorted(d[key], reverse=True):
            print("0" * k + str(key))


if __name__ == "__main__":
    main()
