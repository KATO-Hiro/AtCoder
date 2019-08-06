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


# <a href='https://atcoder.jp/contests/abc047/tasks/arc063_b'>AtCoder Beginner Contest D - 高橋君と見えざる手 / An Invisible Hand (400点)</a>

## 問題に関するタグ
**<details><summary>注：ネタバレの可能性あり</summary>**
    TODO: 問題に関するタグを記載
    タグ1、タグ2、...
</details>


## 解法に至るまでの考察
+ 高橋君がりんごの売買で利益を最大化するための行動
    + 売る：ある町iでAiを選択
    + 買う：町iよりも前に位置していて，Aiが最小となる町kを選ぶ
    + 利益：Bi = Ai - min(A1, A2, ..., Ai-1)
    + Bxが最大となるような町xで，それよりも手前の町kで買ったりんごをすべて売ると，利益も最大となる
+ 青木君が高橋君の利益を1円以上下げるために，必要なコストを最小化するように行動
    + Biが最大になる町xでAiを少なくとも絶対値をだけ1減らす
        + 青木君が操作する前のAiはそれぞれ異なることから，高橋君の購入金額の最小値が一つに決まる
        + 青木君が支払うコストが最小を最小にしつつ，高橋君の利益を減らす
        + 青木君は，町xでの高橋君の購入費を1増やすか，売却費を1下げる必要がある
    + Biの最大値も複数存在する可能性はあるが，制約条件から，互いに影響しない
    + 青木君はBiの最大値が複数存在する場合も，それぞれコスト1で変更できる
+ 求める答えは，Biが最大値となる町の数


## 実装のポイント
+ Biの最大値を見つける
    + 愚直に実装すると，aiとaiのグリッドとなるため，計算量はO(N^2)
    + N = 10 ^ 5であるため，計算量がO(N)もしくはO(NlogN)でないと，TLEになる
    + aiを一つずつ見る
    + そのときの最小値がどうなるかを，変数や配列などで管理
        + a0の値で初期化
        + a1の場合，a1とa0を比較して，小さい方の値を採用
        + 以降同様に
    + aiとaiにおける最小値の差分を取ることで，利益が最大となる候補の値が求まる
+ Biの最大値がいくつあるかを数える

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

+ D問題
    + ○：売却金額と購入金額の最大値の個数だけ，変更すればいいことには気がつけた
    + ▲：Aiがそれぞれ異なることにより，購入費用の最小値が一つに決まるという考えに至らず，かつ理解が不十分なまま
    + ▲：実装で，O(N^2)からO(N)にする方法が分からず
        + 解説通りに実装
        + aiを1つずつ見る
        + 各位置におけるaiの最小値をai-1と比較して更新

## 得られた知見
+ See:https://atcoder.jp/contests/abc047/submissions/4023448

```py3:
    from itertools import accumulate
    list(accumulate(a, func=min))
```

+ accumulateは累積和だけじゃない
+ funcに任意の関数入れられる
    + この場合だと，各項の最小値を取ってくれる

## つまづきポイント（○印が該当を表す）

|問題|解けず|理解|発想|方針|実装|
|:--:|:--:|:--:|:--:|:--:|:--:|
|D|◯||||◯|

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
