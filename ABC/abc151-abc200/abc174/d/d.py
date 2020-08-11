# -*- coding: utf-8 -*-


def main():
    n = int(input())
    c = input()
    r_count = c.count('R')
    ans = 0

    # コーナーケース: すべてWのとき
    if r_count == 0:
        print(0)
        exit()

    # 左側にすべてのRを寄せるイメージ
    # 左端からWをRに置き換える
    # 自力ACはしたが、この考え方でよかったのか?
    for ci in c:
        if ci == 'W':
            ans += 1

        r_count -= 1

        if r_count == 0:
            print(ans)
            exit()

    print(ans)


if __name__ == '__main__':
    main()
