# Python学習ポートフォリオ

Python初学者として、基礎からAI・機械学習までの学習過程をまとめたリポジトリです。

## 作成したもの

### 基礎課題
- `counter.py` - 四則演算電卓(エラー処理対応)
- `todo.py` - TODOリスト管理アプリ
- `jancain.py` - じゃんけんゲーム
- `error.py` - エラーハンドリング練習
- `dictionary.py` - 文字列内の文字出現回数を集計し、最頻出文字を出力
- `paiza.py` - 文字列の連続文字数を圧縮表示する処理

### 機械学習
- `iris.py` - irisデータセットを使った花の品種分類(KNeighborsClassifier)
- `mind.py` - 日本語感情分析(chABSA-datasetを使用、約3000件のデータで学習、精度約75〜80%)
- `youtubeapi.py` - YouTube Data API v3でコメントを取得し、日本語感情分析モデルで判定・可視化(ポジティブ/ネガティブの円グラフ表示)
- `youtubesearch.py` - キーワードを入力するとYouTubeで関連動画を検索し、日本語コメントを収集して感情分析・可視化するツール

## 使用技術
- Python
- scikit-learn
- janome(日本語形態素解析)
- YouTube Data API v3
- matplotlib(結果の可視化)

## 学んだこと
- 機械学習はデータ量が精度に直結すること
- テキストデータを数値化して学習させる流れ(tokenize→vectorize→fit)
- 言語判定(langdetect)を使って日本語コメントのみに絞り込む方法
- 複数の機能を関数化して組み合わせる設計の考え方