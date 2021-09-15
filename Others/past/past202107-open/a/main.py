# -*- coding: utf-8 -*-


def main():
    s = input()
    total = 0

    for index, si in enumerate(s, 1):
        if index % 2 == 1:
            if index == 15:
                if total % 10 == int(si):
                    print('Yes')
                else:
                    print('No')
            else:
                total += 3 * int(si)
        else:
            total += int(si)


if __name__ == "__main__":
    main()
