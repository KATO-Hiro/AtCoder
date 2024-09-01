use std::collections::VecDeque;
use std::io::{self, BufRead};

fn to_hash(pos: &[(usize, usize); 2], n: usize) -> usize {
    let (p00, p01) = pos[0];
    let (p10, p11) = pos[1];

    let mut value = p00;
    value = value * n + p01;
    value = value * n + p10;
    value = value * n + p11;

    value
}

fn to_pos(hash: usize, n: usize) -> [(usize, usize); 2] {
    let mut hash = hash;
    let p11 = hash % n;
    hash /= n;
    let p10 = hash % n;
    hash /= n;
    let p01 = hash % n;
    hash /= n;
    let p00 = hash % n;

    [(p00, p01), (p10, p11)]
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let n: usize = input.next().unwrap().unwrap().trim().parse().unwrap();
    let mut s: Vec<Vec<char>> = Vec::new();
    let mut pos: Vec<(usize, usize)> = Vec::new();

    for i in 0..n {
        let line: Vec<char> = input.next().unwrap().unwrap().chars().collect();
        s.push(line);
        
        for j in 0..n {
            if s[i][j] == 'P' {
                pos.push((i, j));
            }
        }
    }

    let n4 = n * n * n * n;
    let inf = 1001001001;

    let mut dist = vec![inf; n4];
    let id = to_hash(&[pos[0], pos[1]], n);
    dist[id] = 0;

    let mut q = VecDeque::new();
    q.push_back(id);
    let dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)];

    while let Some(cur_id) = q.pop_front() {
        let pos = to_pos(cur_id, n);
        let d = dist[cur_id];

        for &(dx, dy) in &dxy {
            let mut npos = [(0, 0); 2];

            for (i, &(y, x)) in pos.iter().enumerate() {
                let nx = (x as isize + dx) as usize;
                let ny = (y as isize + dy) as usize;

                if nx >= n || ny >= n || s[ny][nx] == '#' {
                    npos[i] = (y, x);
                } else {
                    npos[i] = (ny, nx);
                }
            }

            let nid = to_hash(&npos, n);

            if dist[nid] != inf {
                continue;
            }

            dist[nid] = d + 1;
            q.push_back(nid);
        }
    }

    let mut ans = inf;

    for (id, &di) in dist.iter().enumerate() {
        let pos = to_pos(id, n);

        if pos[0] == pos[1] {
            ans = ans.min(di);
        }
    }

    if ans == inf {
        ans = -1;
    }

    println!("{}", ans);
}