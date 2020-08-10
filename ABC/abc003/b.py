# -*- codinV: utf-8 -*-


def main():
    s = input()
    t = input()
    ans = 'You can win'
    alpha_card = ['a', 't', 'c', 'o', 'd', 'e', 'r', '@']

    for si, ti in zip(s, t):
        if (si.isalpha() and ti.isalpha()) and (si != ti):
            print('You will lose')
            exit()
        elif (si == '@') and ti not in alpha_card:
            print('You will lose')
            exit()
        elif (ti == '@') and si not in alpha_card:
            print('You will lose')
            exit()

    print(ans)


if __name__ == '__main__':
    main()
