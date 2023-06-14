---
marp: true
---

# Google Colaboratoryの基礎

---

## Google Colaboratoryについて

> Google Colaboratory（通称Colab）は、Googleが提供するオンラインのJupyterノートブック環境です。ノートブック環境とは、コードやテキストを組み合わせたインタラクティブな文書形式でプログラミングを行うことができる環境のことです。

> Colabは、ブラウザ上で動作し、Googleのクラウド上にある仮想マシン上でPythonコードを実行できます。また、GPUやTPUを利用することができ、機械学習やデータ分析などの高度な計算を行うことができます。

> Colabは無料で利用でき、Googleアカウントを持っているだけで利用できます。また、Colabには、Googleが提供する機械学習ライブラリであるTensorFlowやPyTorchなどが最初からインストールされているため、これらのライブラリを使ったプログラムの開発や実行も容易に行うことができます。

---

## Colabの起動

[https://colab.research.google.com/](https://colab.research.google.com/)にアクセスすると以下の画面が表示されますので，右上からGoogleアカウントでログインできます．これでColab使えるようになります。

![bg right:60% w:700](https://computational-sediment-hyd.github.io/NonUniformFlowModelUsingPython/00_orientation/ref/d01s.png)

---

ログインすると次の画面が表示されますがとりあえずキャンセルします。

![bg right:60% w:700](https://computational-sediment-hyd.github.io/NonUniformFlowModelUsingPython/00_orientation/ref/d02s.png)

---

## Colabの実行



トップに表示される「Colaboratory へようこそ.ipynb」の中段くらいの次のソースを実行してみます．
セルを選択すると次のように画面になるので、左の三角ボタンをクリックするとセル内のpythonコードが実行できます。

初回起動時はランタイムに接続するため、実行に時間がかかりますが、一度接続すると2回目は実行速度のみで実行できます。

![bg right:50% w:550](https://computational-sediment-hyd.github.io/NonUniformFlowModelUsingPython/00_orientation/ref/d03s.png)

---

### 90分ルール・12時間ルール
以下のルールに従って、ランタイムがリセットされますが、ライトユーザーにとってはほとんど問題ないです。
有料版であるPro／Pro+／Pay As You Goのユーザーの場合、90分ルールはなくなり、12時間→24時間ルールになるようです。
なお、各時間は最長とのことです。

#### 90分ルール
ノートブックのインスタンス起動後に、セッションが切断されて９０分経過するとランタイムリセットされます。つまり、90分間何も触らないとランタイムが切断されます。

#### 12時間ルール
ノートブック起動後、12時間経過するとランタイムがリセットされます。



---

## Colabのファイル形式、保存先、Google Driveの活用

Colabのファイル形式は、[Jupyter Notebook](https://jupyter.org/)（詳細は後述）の形式（拡張子.ipynb）です。

Colab上で作成したファイルは[Google Drive](https://drive.google.com/drive/)直下のColab Notebooksフォルダ内に保存されます。

また、[Google Drive](https://drive.google.com/drive/)上でipynbファイルをクリックすると[Colab](https://colab.research.google.com/)が起動します。そのため、[Google Drive](https://drive.google.com/drive/)上でColab用ファイルを管理することをおすすめします。

![w:800](https://computational-sediment-hyd.github.io/NonUniformFlowModelUsingPython/00_orientation/ref/d04s.png)

---

## Colabの独自コマンド

[Colab](https://colab.research.google.com/)では、Jupyter Notebookと同様にPythonコードを動かすことはできますが、それに加えて以下のコマンドを使用することができます。



### Linuxコマンドの使用

各コマンドの先頭に!又は%を付けることにより基本的なLinuxコマンドを使用することができます。
apt等によるパッケージ管理も可能です


```python
!ls -al
# or  %ls -al

# total 16
# drwxr-xr-x 1 root root 4096 Jun 12 13:36 .
# drwxr-xr-x 1 root root 4096 Jun 14 04:01 ..
# drwxr-xr-x 4 root root 4096 Jun 12 13:35 .config
# drwxr-xr-x 1 root root 4096 Jun 12 13:36 sample_data
```


---

### ライブラリをインストール

Colabには多くの主要ライブラリが最初からインストールされています。
インストールされていないライブラリを使用する場合は、以下のとおり、pipコマンド（[pythonパッケージの管理コマンド](https://www.python.jp/install/windows/pip.html))によるインストールが可能です。

例：geopandasをインストールする場合


```python
%pip -q install geopandas
# or !pip -q install geopandas

#     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 15.4 MB/s eta 0:00:00
#     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.4/16.4 MB 58.0 MB/s eta 0:00:00
#     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 55.8 MB/s eta 0:00:00
```


---

### Google Driveをマウント

ファイル操作を行なう場合はGoogle Drive上でファイルを管理します。
ファイルにアクセスするためには、以下のコマンドによりGoogle Driveをマウントする必要があります。


```python
from google.colab import drive
drive.mount('/content/drive')
```
