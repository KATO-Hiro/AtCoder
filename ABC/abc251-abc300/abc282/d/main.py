# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)

    # See:
    # https://prd-xxx.hateblo.jp/entry/2017/10/13/004256
    no_color, black, white = 0, 1, -1
    colors = [no_color] * n # 0: 未着色、1: 黒、-1: 白

    def is_bipartite(i, black_count = 0, white_count = 0):
        stack = [(i, black)] # 頂点、色

        while stack:
            vertex, color = stack.pop()

            if colors[vertex] != no_color:
                continue

            colors[vertex] = color

            if color == black:
                black_count += 1
            else:
                white_count += 1
        
            for to in graph[vertex]:
                if colors[to] == color:
                    return False, 0, 0
                
                if colors[to] == no_color:
                    stack.append((to, -color)) # 色を反転

        return True, black_count, white_count
    

    def nC2(n):
        return n * (n - 1) // 2
    
    ans = nC2(n) - m
    
    # 各頂点を始点として、二部グラフか判定(連結成分が複数であることへの対応)
    for i in range(n):
        if colors[i] != no_color:
            continue

        flag, black_count, white_count = is_bipartite(i)

        if flag:
            ans -= nC2(black_count)
            ans -= nC2(white_count)
        else:
            print(0)
            exit()

    print(ans)
    

if __name__ == "__main__":
    main()
