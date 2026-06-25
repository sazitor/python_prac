
# Python学習ポートフォリオ

PythonとAI・機械学習を独学で学習し、YouTubeコメントの感情分析ツールを作成しました。

## メインプロジェクト

### キーワード型YouTube感情分析ツール(`youtubesearch.py`)
キーワードを入力するとYouTubeで関連動画を自動検索し、日本語コメントを収集して感情分析を行い、結果を円グラフで可視化するツールです。

**使用技術**: YouTube Data API v3 / janome / scikit-learn / langdetect / matplotlib

**実行方法**:
## その他の作成物

### 基礎課題
- `counter.py` - 四則演算電卓(エラー処理対応)
- `todo.py` - TODOリスト管理アプリ
- `jancain.py` - じゃんけんゲーム
- `error.py` - エラーハンドリング練習

### 機械学習
- `iris.py` - irisデータセットを使った花の品種分類(KNeighborsClassifier)
- `mind.py` - 日本語感情分析モデル(chABSA-dataset約3000件、精度75〜80%)
- `youtubeapi.py` - 特定のYouTube動画のコメントを感情分析・可視化

## 学んだこと
- 機械学習はデータ量が精度に直結すること
- テキストデータを数値化して学習させる流れ(tokenize→vectorize→fit)
- 外部APIとの連携・エラー処理・セキュリティ管理(.env)
- 複数の機能を関数化して組み合わせる設計の考え方