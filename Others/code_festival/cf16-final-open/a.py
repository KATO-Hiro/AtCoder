# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    s = [list(map(str, input().split())) for _ in range(h)]
    alpha = [chr(ord('A') + i) for i in range(26)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == 'snuke':
                print(alpha[j] + str(i + 1))
                exit()


if __name__ == '__main__':
    main()
