---
title: AtCoder ABCxxx
tags: 初心者 競技プログラミング AtCoder Python3 復習
author:
slide: false
---

# はじめに
+ AtCoderで解けなかった問題（AtCoder Beginner ContestのC問題、D問題が中心になると思います）を復習しています。

+ 間違いや勘違いなどがございましたら、ご指摘・ご指導いただけると幸いです。

    + 連絡先：<a href="https://twitter.com/k_hiro1818">@k_hiro1818</a>

<br>


# <a href='https://atcoder.jp/contests/abc040/tasks/abc040_c'>AtCoder Beginner Contest 040 C - 柱柱柱柱柱 (100点)</a>

## 問題に関するタグ
**<details><summary>注：ネタバレの可能性あり</summary>**
    DP(Dynamic Programming)、
</details>


## 解法に至るまでの考察
+ Nが大きいため全探索は無理．コストを常に最小とするような貪欲法も，トータルのコストが最小となるとは限らない
+ 動的計画法の最も基本形
    + dp[]という配列を用意．
    + dp[i]：1番目からi番目の柱に移動した時の合計コストの最小値を求める
    + 初期値は，dp[1] = 0
    + 次のステップ：dp[i] = min(dp[i - 2] + abs(a[i - 2] - a[i]), dp[i - 1] + abs(a[i - 1] - a[i]))
    + dp[n]を出力
+ 動的計画法の基本形を自分なりに抽象化
    + 前の状態を使えそうかどうかを判断
    + 答えを格納する配列dp[]を用意
    + 初期値dp[0]を設定
    + dp[i]をdp[i - hoge]と答えが増減する要素を使って更新
        + 配列の参照外とならないように注意
    + dp[imax]を出力

## 実装のポイント
+
+
+

## ソースコードの一例
<a href=''>提出コード</a>


## 類似問題
**<details><summary>ネタバレ注意：類似していると思われる問題があれば載せています。<br>また、過去問で出題されている場合はご一報いただけると幸いです。</summary>**
    TODO: 類似問題であると思われる問題名、URLを記載
</details>


## 派生問題という名の妄想
**<details><summary>注：派生問題の案があれば載せています。<br>すでに過去問で出題されている場合はご一報いただけると幸いです。</summary>**
    TODO: 考えられる派生問題の案を書く
</details>


## 感想
<details><summary>得られた知見・つまづきポイント・要復習</summary><div>

+ ?完?WA遅解き
+ A問題：
    + ○：
    + ▲：

## 得られた知見
+ TODO: Write here!

## つまづきポイント（○印が該当を表す）

|問題|解けず|理解|発想|方針|実装|
|:--:|:--:|:--:|:--:|:--:|:--:|
|A||||||

### 各項目の意味
+ 解けず：自力で解けたどうか
+ 理解：解法を理解するのに時間を要した問題
+ 発想：発想が難しい（思いつけば簡単）な問題
+ 方針：方針を見出すのが難しい問題
+ 実装：実装に手間取った問題
</details>

## 要復習
+ TODO: write here.


# 参考
+ AtCoderの公式解説

    <b id='myfootnote1'>1</b>: https://www.youtube.com/channel/UCtG3StnbhxHxXfE6Q4cPZwQ [↩](#a1)

    <b id='myfootnote2'>2</b>: https://img.atcoder.jp/abcxxx/editorial.pdf [↩](#a2)

+ 分かりやすい競技プログラミングの解説記事

    <b id='myfootnote3'>3</b>: http://drken1215.hatenablog.com/ [↩](#a3)

    <b id='myfootnote4'>4</b>: http://betrue12.hateblo.jp/archive/category/AtCoder [↩](#a4)

記事を執筆された皆さまへ: **掲載不可**の場合はお手数をお掛けしますが、<a href="https://twitter.com/k_hiro1818">@k_hiro1818</a>までご一報ください。
