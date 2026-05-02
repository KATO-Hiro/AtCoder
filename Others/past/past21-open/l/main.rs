use proconio::input;
use ac_library::dsu::Dsu;

fn main() {
    input! {
        n: usize,
        xy: [(i64, i64); n],
    }

    let mut edges: Vec<(f64, usize, usize)> = Vec::new();

    for i in 0..n {
        let (xi, yi) = xy[i];

        for j in (i + 1)..n {
            let (xj, yj) = xy[j];
            let d = (((xi - xj) * (xi - xj) + (yi - yj) * (yi - yj)) as f64).sqrt();
            edges.push((d, i, j));
        }
    }

    input! {
        p: [f64; n],
    }

    for i in 0..n {
        edges.push((p[i], n, i));
    }

    edges.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

    let mut dsu = Dsu::new(n + 1);
    let mut ans = 0.0;

    for (d, i, j) in edges {
        if dsu.same(i, j) {
            continue;
        }

        dsu.merge(i, j);
        ans += d;
    }

    println!("{}", ans);
}
