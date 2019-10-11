# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list(input())

    # 1番目と2番目を決め打ち
    # SS，SW，WW，WS
    # 1文字目とn + 1文字目が一致するかどうか
    for pair in ['SS', 'SW', 'WW', 'WS']:
        ans = ['' for _ in range(n + 1)]

        for index, p in enumerate(pair):
            ans[index] = p

            for j in range(1, n):
                if s[j] == 'o':
                    if ans[j] == 'S':
                        ans[j + 1] = ans[j - 1]
                    else:
                        if ans[j - 1] == 'S':
                            ans[j + 1] = 'W'
                        else:
                            ans[j + 1] = 'S'
                else:
                    if ans[j] == 'S':
                        if ans[j - 1] == 'S':
                            ans[j + 1] = 'W'
                        else:
                            ans[j + 1] = 'S'
                    else:
                        ans[j + 1] = ans[j - 1]

        if ans[0] == ans[-1]:
            # 気がつけなかった点
            # 2文字目とN文字目が矛盾していないかチェック
            if ans[n - 1] == ans[1] and ((s[0] == 'o' and ans[0] == 'S') or (s[0] == 'x' and ans[0] == 'W')):
                print(''.join(ans[:-1]))
                break
            elif ans[n - 1] != ans[1] and ((s[0] == 'o' and ans[0] == 'W') or (s[0] == 'x' and ans[0] == 'S')):
                print(''.join(ans[:-1]))
                break
    else:
        print(-1)


if __name__ == '__main__':
    main()
