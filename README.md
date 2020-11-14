# 競馬 AI 班

![test](https://github.com/ritscc/rcc-keiba-2020/workflows/test/badge.svg)
![code check](https://github.com/ritscc/rcc-keiba-2020/workflows/code%20check/badge.svg)
[![Twitter](https://img.shields.io/badge/Twitter-競馬AI班-blue?style=flat-square&logo=twitter)](https://twitter.com/search?q=%23rcc_keiba)

RCC 2020 年度プロジェクト活動

## 実行環境

- Ubuntu 20.04
- Python ~> 3.8.0
- pipenv

## インストール

```sh
$ git clone <this repo>
$ cd <this repo>

$ cd src
$ pipenv install
```

### 使用方法

#### テストを実行

```sh
$ cd src
$ pipenv run test
```

#### 競馬予想結果をツイート

```sh
$ pipenv run start
```

## 開発者

- [Averak](https://github.com/averak)
