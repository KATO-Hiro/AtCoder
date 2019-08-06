# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    a = Counter(map(int, input().split()))
    key_count = len(a.keys())
    keys_values = a.most_common()

    if key_count == 1:
        if keys_values[0][0] == 0:
            print('Yes')
        else:
            print('No')
    elif key_count == 2:
        if keys_values[0][0] == 0 or keys_values[1][0] == 0:
            if n % 3 == 0:
                if keys_values[1][0] == 0:
                    if keys_values[0][1] // keys_values[1][1] == 2 and keys_values[0][1] % keys_values[1][1] == 0:
                        print('Yes')
                    else:
                        print('No')
                elif keys_values[0][0] == 0:
                    if keys_values[1][1] // keys_values[0][1] == 2 and keys_values[1][1] % keys_values[0][1] == 0:
                        print('Yes')
                    else:
                        print('No')
                else:
                    print('No')
            else:
                print('No')
        else:
            print('No')
    elif key_count == 3:
        if keys_values[0][1] == keys_values[1][1] == keys_values[2][1]:
            xors = keys_values[0][0] ^ keys_values[1][0] ^ keys_values[2][0]

            if xors == 0:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')





if __name__ == '__main__':
    main()
