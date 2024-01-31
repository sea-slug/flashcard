# flashcard

## 概要

## チュートリアル
### 実行環境
Ubuntu 22.04.3 上の Python 3.10.12 で，以下の手順で動作することを確認しています．

以下の説明ではUbuntuのBashで作業することを想定しています．
他の環境で作業する場合は，適宜読み替えてください．

### 本システムのダウンロード
githubのソースコードをcloneします．
```bash
$ git clone https://github.com/sea-slug/flashcard.git
```

特定のフォルダ名で保存したい場合は以下のようにディレクトリ名を指定してcloneします．
```bash
$ git clone https://github.com/sea-slug/flashcard.git <ディレクトリ名>
```

フォルダ名を指定しない場合は，`flashcard`というディレクトリ名になります．

### Pythonライブラリのインストール
- 作成したディレクトリ（デフォルトでは`flashcard`）に移動します．
```bash
$ cd flashcard
```

- 必要に応じて仮想環境を構築します．必要なければこのステップは飛ばして構いません．
以下はvenvを用いた例です．
```bash
$ python -m venv venv # 仮想環境をvenvという名前で構築
$ . venv/bin/activate
```

- 必要なPythonライブラリをインストールします．
```bash
$ pip install -r requirements.txt 
```

### discord botの作成
- discord botを作成します．

### 設定ファイルの編集
- `conf.yaml`を編集し，作成したbotのTOKENを指定します．
```yaml
# Botアカウントの設定
token: "<TOKEN>"
```

- `conf.yaml`を編集し，語彙ファイルを指定します．
```yaml
# 語彙ファイルの設定
datafile:
    - "<語彙ファイル1>"
    - "<語彙ファイル2>" # 複数ファイルを指定するときはこの下に続けて記載する
```

### 起動
```bash
$ python main.py conf.yaml
```

## レファレンス
