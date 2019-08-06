# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ws = list(input().split())
    table = {'b': '1', 'c': '1', 'd': '2', 'w': '2', 't': '3', 'j': '3',
             'f': '4', 'q': '4', 'l': '5', 'v': '5', 's': '6', 'x': '6',
             'p': '7', 'm': '7', 'h': '8', 'k': '8', 'n': '9', 'g': '9',
             'z': '0', 'r': '0'}

    ans = ['' for _ in range(n)]

    for j, w in enumerate(ws):
        string = ''

        for i, wi in enumerate(w):
            if wi.lower() in table.keys():
                string += table[wi.lower()]
            else:
                string += ''

        if string == '' or j == n - 1:
            ans[j] = string
        else:
            ans[j] = string + ' '

    print(''.join(ans))


if __name__ == '__main__':
    main()
