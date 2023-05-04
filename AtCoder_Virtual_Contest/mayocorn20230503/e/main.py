# -*- coding: utf-8 -*-


# See:
# https://atcoder.jp/contests/abc189/submissions/19610180
def mul_matrix(left_matrix, right_matrix):
    m, n, o = len(left_matrix), len(left_matrix[0]), len(right_matrix[0])
    results = [[0] * o for _ in range(m)]

    for i in range(m):
        for k in range(n):
            for j in range(o):
                results[i][j] += left_matrix[i][k] * right_matrix[k][j]

    return results

def mul_vector(matrix, vector):
    m, n = len(matrix), len(vector)
    results = [0] * m

    for i in range(m):
        s = 0

        for k in range(n):
            s += matrix[i][k] * vector[k]

        results[i] = s

    return results


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]

    m = int(input())

    identity_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    matrices = [identity_matrix]
    op1 = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
    op2 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]

    def op3(x_axis_base): 
        return [[-1, 0, 2 * x_axis_base], [0, 1, 0], [0, 0, 1]]

    def op4(y_axis_base): 
        return [[1, 0, 0], [0, -1, 2 * y_axis_base], [0, 0, 1]]

    for _ in range(m):
        op = list(map(int, input().split()))
        prev_matrix = matrices[-1]

        if op[0] == 1:
            cur_matrix = mul_matrix(op1, prev_matrix)
        elif op[0] == 2:
            cur_matrix = mul_matrix(op2, prev_matrix)
        elif op[0] == 3:
            p = op[1]
            cur_matrix = mul_matrix(op3(p), prev_matrix)
        else:
            p = op[1]
            cur_matrix = mul_matrix(op4(p), prev_matrix)
        
        matrices.append(cur_matrix)
    
    q = int(input())

    for _ in range(q):
        ai, bi = map(int, input().split())
        bi -= 1

        cur_matrix = matrices[ai]
        xi, yi = xy[bi]
        ans_x, ans_y, _ = mul_vector(cur_matrix, [xi, yi, 1])
        print(ans_x, ans_y)


if __name__ == "__main__":
    main()
