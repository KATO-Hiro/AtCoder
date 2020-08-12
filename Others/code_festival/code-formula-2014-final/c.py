# -*- coding: utf-8 -*-


def main():
    s = input().split()
    ans = list()

    for si in s:
        if '@' in si:
            is_at = False
            string = ''

            for sii in si:
                if sii == '@':
                    if string != '':
                        ans.append(string)

                    string = ''
                    is_at = True
                elif is_at and sii != '@':
                    string += sii

            if string != '':
                ans.append(string)

    print('\n'.join(map(str, sorted(set(ans)))))


if __name__ == '__main__':
    main()
