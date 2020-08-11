# -*- coding: utf-8 -*-


def main():
    s = input()
    joi_count = 0
    ioi_count = 0

    for i in range(len(s) - 2):
        if s[i:i + 3] == 'JOI':
            joi_count += 1
        if s[i:i + 3] == 'IOI':
            ioi_count += 1

    print(joi_count)
    print(ioi_count)


if __name__ == '__main__':
    main()
