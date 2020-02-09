# -*- coding: utf-8 -*-


def main():
    s = input()
    ans = list()
    count = 0

    for si in s:
        if count % 2 == 0 and si == 'I':
            ans.append(si)
            count += 1
        elif count % 2 == 1 and si == 'O':
            ans.append(si)
            count += 1


    # コーナーケース
    if len(ans) == 0:
        pass
    elif ans[-1] == 'O':
        count -= 1

    print(count)


if __name__ == '__main__':
    main()
