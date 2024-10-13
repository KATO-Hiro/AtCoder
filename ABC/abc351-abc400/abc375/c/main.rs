use proconio::input;

fn rotate_90_degrees_to_right(array: Vec<Vec<char>>) -> Vec<Vec<char>> {
    let n = array.len();
    let mut rotated = vec![vec![' '; n]; n];

    for i in 0..n {
        for j in 0..n {
            rotated[j][n - i - 1] = array[i][j];
        }
    }

    rotated
}

fn main() {
    input! {
        n: usize,
        s: [String; n],
    }

    let s: Vec<Vec<char>> = s.into_iter().map(|row| row.chars().collect()).collect();

    let s90 = rotate_90_degrees_to_right(s.clone());
    let s180 = rotate_90_degrees_to_right(s90.clone());
    let s270 = rotate_90_degrees_to_right(s180.clone());
    let mut ans = vec![vec![' '; n]; n];

    fn write(k: usize, grid: &Vec<Vec<char>>, ans: &mut Vec<Vec<char>>, n: usize) {
        for j in k..n - k {
            ans[k][j] = grid[k][j];
            ans[n - k - 1][j] = grid[n - k - 1][j];
            ans[j][k] = grid[j][k];
            ans[j][n - k - 1] = grid[j][n - k - 1];
        }
    }

    for i in 1..=n / 2 {
        let i2 = i - 1;

        match i % 4 {
            1 => write(i2, &s90, &mut ans, n),
            2 => write(i2, &s180, &mut ans, n),
            3 => write(i2, &s270, &mut ans, n),
            _ => write(i2, &s, &mut ans, n),
        }
    }

    for ans_i in ans {
        println!("{}", ans_i.into_iter().collect::<String>());
    }
}
