# 競馬 AI 班

[![build](https://github.com/ritscc/rcc-keiba-2020/workflows/build/badge.svg)](https://github.com/ritscc/rcc-keiba-2020/actions)
[![Twitter](https://img.shields.io/badge/Twitter-競馬AI班-blue?style=flat-square&logo=twitter)](https://twitter.com/search?q=%23rcc_keiba)

RCC 2020 年度プロジェクト活動

## 実行環境

- Ubuntu 20.04
- Python ~> 3.8.0
- TensorFlow 2.2

## インストール

```sh
$ git clone <this repo>
$ cd <this repo>

$ docker-compose build
```

### 使用方法

#### テストを実行

```sh
$ cd src/
$ python -m unittest discover tests
```

#### 競馬予想結果をツイート
```sh
$ docker-compose up
```

## 開発者

- [Averak](https://github.com/averak)
