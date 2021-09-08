# -*- coding: utf-8 -*-


def main():
    d = {"ABC": 0, "ARC": 0, "AGC": 0, "AHC": 0}

    for i in range(3):
        si = input()
        d[si] += 1
    
    for key, value in d.items():
        if value == 0:
            print(key)
            exit()


if __name__ == "__main__":
    main()
