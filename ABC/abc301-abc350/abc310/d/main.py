# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, t, m = map(int, input().split())

    # チーム分けの方法を全探索(DFS)
    # 相性の悪いペアを無向グラフとして扱う
    ng = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        ng[ai].append(bi)
        ng[bi].append(ai)

    def dfs(now, teams):
        if now == n:
            if len(teams) == t:
                return 1
            else:
                return 0

        count = 0

        # Tチームのいずれかに配属できるか?
        for team in teams:
            ok = True

            for player in team:
                if player in ng[now]:
                    ok = False
                    break

            if ok:
                team.append(now)
                count += dfs(now + 1, teams)
                team.pop()

        # Tチーム未満の場合、新しいチームに配属
        if len(teams) < t:
            teams.append([now])
            count += dfs(now + 1, teams)
            teams.pop()

        return count

    ans = dfs(0, [])
    print(ans)


if __name__ == "__main__":
    main()
