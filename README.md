# sample-tensorflow

Sample for Tensorflow

## 開発環境構築

### Python3

```bash
pip3 install pipenv
```

### vscode

```bash
# python
code --install-extension ms-python.python

# japanese
code --install-extension ms-ceintl.vscode-language-pack-ja

# git
code --install-extension mhutchie.git-graph
code --install-extension eamodio.gitlens
code --install-extension codezombiech.gitignore

# markdown
code --install-extension yzhang.markdown-all-in-one
code --install-extension davidanson.vscode-markdownlint
```

## 使い方

### 初期設定

#### 仮想環境の作成

```bash
export PIPENV_VENV_IN_PROJECT=true
pipenv --python 3
```

#### 仮想環境のアクティベート

```bash
python3 -m pipenv shell
```

#### Pipfileからのパッケージ復元

```bash
pipenv install
```

#### 動作確認

```bash
python3 mnist.py
```

### パッケージ追加

#### Dependencyの場合

```bash
pipenv install tensorflow
```

#### Development Dependencyの場合

```bash
pipenv install flake8 --dev
```

### 仮想環境でのコマンドの実行

```bash
pipenv run
```
