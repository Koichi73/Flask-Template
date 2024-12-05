# Flask-Template
flaskを用いた中規模なアプリ開発用のテンプレート

## プロジェクト構成

    ├── flask_app/
    │   ├── __init__.py             <- 初期設定
    │   ├── app.py                  <- appを読み込む
    │   ├── models.py               <- DBテーブルを定義
    │   ├── static/                 <- 静的ファイルを格納
    │   │   ├── css/
    │   │   └── js/
    │   ├── templates/              <- htmlファイルを格納
    │   │   ├── common/
    │   │   │   └── layout.html
    │   │   ├── index.html
    │   │   ├── sample.html
    │   │   └── ...
    │   └── controllers/            <- コントローラ
    │       ├── index.py
    │       ├── sample.py
    │       └── ...
    ├── instance/                   <- 機密情報を格納
    │   ├── config.py               <- appの設定を書く
    │   └── sampleDB.db
    ├── manage.py                   <- データベース作成用
    ├── .env                        <- 環境変数を定義
    ├── .gitignore
    ├── README.md
    └── requirements.txt

## Getting Started
このテンプレートをローカル環境で設定する手順を以下に示します。

1. venvやcondaなどを使って、Python環境を作成する。<br>※3.10と3.11で動作確認済み

2. テンプレートをクローンする。
    ```sh
    git clone https://github.com/Koichi73/Flask-Template.git
    ```
    
3. requirements.txtからライブラリをインストールする。
    ```sh
    cd Flask-Template
    pip install -r requirements.txt
    ```

4. Flaskを始める。
    ```sh
    flask run
    ```

## Detail
https://qiita.com/Koichi73/items/9d73f062f0ad56d6f953

## Reference
- https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/patterns/appfactories.html
- https://youtu.be/dam0GPOAvVI?si=t9KAntmqxlBKeJJz
- https://ai-can-fly.hateblo.jp/entry/flask-directory-structure

