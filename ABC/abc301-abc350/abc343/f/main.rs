use proconio::input;
use std::collections::HashMap;

fn ceil_pow2(n: usize) -> usize {
    let mut x = 0;
    while (1 << x) < n {
        x += 1;
    }
    x
}

#[derive(Clone, Debug)]
struct SegTree {
    n: usize,
    size: usize,
    log: usize,
    d: Vec<(i64, i64, i64, i64)>,
    e: (i64, i64, i64, i64),
    op: fn((i64, i64, i64, i64), (i64, i64, i64, i64)) -> (i64, i64, i64, i64),
}

impl SegTree {
    fn new(
        op: fn((i64, i64, i64, i64), (i64, i64, i64, i64)) -> (i64, i64, i64, i64),
        e: (i64, i64, i64, i64),
        v: Vec<(i64, i64, i64, i64)>,
    ) -> Self {
        let n = v.len();
        let log = ceil_pow2(n);
        let size = 1 << log;
        let mut d = vec![e; 2 * size];

        let mut seg_tree = SegTree { n, size, log, d, e, op };

        for i in 0..n {
            seg_tree.d[size + i] = v[i].clone();
        }
        for i in (1..size).rev() {
            seg_tree.update(i);
        }

        seg_tree
    }

    fn update(&mut self, k: usize) {
        self.d[k] = (self.op)(self.d[2 * k].clone(), self.d[2 * k + 1].clone());
    }

    fn set(&mut self, p: usize, x: (i64, i64, i64, i64)) {
        let mut p = p + self.size;
        self.d[p] = x;
        for i in 1..=self.log {
            self.update(p >> i);
        }
    }

    fn get(&self, p: usize) -> (i64, i64, i64, i64) {
        self.d[p + self.size].clone()
    }

    fn prod(&self, left: usize, right: usize) -> (i64, i64, i64, i64) {
        let mut sml = self.e.clone();
        let mut smr = self.e.clone();
        let mut left = left + self.size;
        let mut right = right + self.size;

        while left < right {
            if left & 1 != 0 {
                sml = (self.op)(sml, self.d[left].clone());
                left += 1;
            }
            if right & 1 != 0 {
                right -= 1;
                smr = (self.op)(self.d[right].clone(), smr);
            }
            left >>= 1;
            right >>= 1;
        }
        (self.op)(sml, smr)
    }
}

fn main() {
    input! {
        n: usize,
        q: usize,
        a: [i64; n],
    }

    const INF: i64 = 10_i64.pow(18);

    fn op(x: (i64, i64, i64, i64), y: (i64, i64, i64, i64)) -> (i64, i64, i64, i64) {
        let mut value_count = HashMap::new();

        for &(value, count) in &[(x.0, x.1), (x.2, x.3), (y.0, y.1), (y.2, y.3)] {
            if value != -INF {
                *value_count.entry(value).or_insert(0) += count;
            }
        }

        let mut sorted_values: Vec<_> = value_count.into_iter().collect();
        sorted_values.sort_by(|a, b| b.0.cmp(&a.0));

        let first = sorted_values[0];
        let second = if sorted_values.len() > 1 {
            sorted_values[1]
        } else {
            (-INF, 0)
        };

        (first.0, first.1, second.0, second.1)
    }

    let e = (-INF, 0, -INF + 1, 0);
    let mut seg = SegTree::new(op, e, a.into_iter().map(|ai| (ai, 1, -INF, 0)).collect());

    for _ in 0..q {
        input! {
            qi: usize,
        }

        if qi == 1 {
            input! {
                p: usize,
                x: i64,
            }
            seg.set(p - 1, (x, 1, -INF, 0));
        } else {
            input! {
                l: usize,
                r: usize,
            }
            let (_, _, _, second_count) = seg.prod(l - 1, r);
            println!("{}", second_count);
        }
    }
}
