# -*- coding: utf-8 -*-


def main():
    s = input()
    alphabets = {'O': '0', 'D': '0', 'I': '1', 'Z': '2', 'S': '5', 'B': '8'}

    for mod, ori in alphabets.items():
        if mod in s:
            s = s.replace(mod, ori)

    print(s)


if __name__ == '__main__':
    main()
