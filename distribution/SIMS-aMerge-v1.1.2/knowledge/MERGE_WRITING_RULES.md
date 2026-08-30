# Merge Writing Rules

## 原則

- Primary Articleを正本として編集する。ゼロから別記事へ作り替えない。
- Absorbed ArticleからはPreservation Mapで指定された固有価値を移植する。
- 同義の説明、重複FAQ、重複表は1つに統合する。
- Primary Articleの既存検索意図を壊さない。
- Query MappingでPrimaryへ集約すると決めた主要クエリを自然にカバーする。

## Preservation

無断削除禁止の例：
- 独自体験・検証
- 実測データ
- 比較表
- 広告・アフィリエイト導線
- 読者に有用な具体例
- Doctor/SBMが明示した保護対象

## 禁止

- Evidenceにない数値・体験・専門資格を創作しない
- blocked_scopeの内容を書き換えない
- Redirect/noindex/deleteを本文編集と同時に実行した扱いにしない
- Merge本文編集をWriterへ丸投げしない

## 完成原稿

原則として部分差分だけでなく、Primary Articleへそのまま反映できる統合後の完成本文を返す。元記事にHTML/広告コード等の保護要素があり、Markdown完全再現で失われる危険がある場合は、保護要素の位置を明示して維持する。


## JSON完全性
Human-readableで完成原稿を書いた場合、その全文を`payload.merged_article.content_markdown`にも格納する。プレースホルダー・参照文・省略記号で代替しない。SBM登録用JSONだけで統合後完成原稿を復元できることを合格条件とする。

## RC3 Publication Quality Gate

統合後完成原稿は、Preservationと重複整理が成功していても、そのまま公開可能とは限らない。最終返却前に以下を検査する。

### 1. Post-Merge Fact Check
- 統合によって新規追加・再構成した設定手順、数値、仕様、制度、料金、ポート番号、バージョン依存情報、製品挙動などは検証対象とする。
- SBM Package内Evidenceで裏付けられる場合はそのEvidenceを優先する。
- Packageだけでは現行性を確認できず、外部確認が必要な場合は可能なら一次情報・公式情報を確認する。
- 外部確認不能・Evidence不足の場合は、未確認事実を断定したまま`PUBLIC_OK`にしない。

### 2. Overclaim Guard
以下のような根拠を超える保証表現を禁止する。
- 「必ず成功する」「必ず解決できる」「必ず原因を特定できる」
- 「絶対に」「確実に」など、Evidenceが保証していない断定

必要なら「解決につながる可能性があります」「原因を切り分けやすくなります」等へ弱める。

### 3. Publication Readiness
完成原稿には次の公開判定を付ける。
- `PUBLIC_OK`：Fact Check済みで、公開阻害事項なし。
- `PUBLIC_OK_WITH_FIXES`：Merge自身が必要修正を完成原稿へ反映済み。修正後は公開可能。
- `HOLD_FOR_VERIFICATION`：重要な事実確認が残り、そのまま公開させてはいけない。

`publication_ready=true`は`PUBLIC_OK`または`PUBLIC_OK_WITH_FIXES`に限る。`HOLD_FOR_VERIFICATION`では必ずfalseとする。
