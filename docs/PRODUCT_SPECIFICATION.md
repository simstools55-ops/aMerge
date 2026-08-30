# Product Specification

SIMS Mergeは、複数の既存記事を比較し、安全に1本へ統合して**統合後の完成原稿まで作成する処置担当製品**です。単純な連結ではなく、検索意図・クエリ・本文・評価・独自価値・収益要素を比較し、Primary Articleを基準に必要な情報だけを吸収・再構成します。

## 責務

1. Cannibalization / 重複の評価
2. Primary Articleの決定
3. Preservation Mapの作成
4. Query Mappingの作成
5. 統合後構成の設計
6. **Primary Articleの統合後完成原稿の執筆**
7. Preservation Validation / 重複除去 / Scope Validation
8. Publication Sequence / Rollback Planの作成
9. SBMへ`SIMS_MERGE_TREATMENT_RESULT_V1`を返却

## 出力判断

- `MERGE_REQUIRED`
- `ROLE_SEPARATION_REQUIRED`
- `KEEP_BOTH`
- `REDIRECT_CANDIDATE`
- `NOINDEX_CANDIDATE`
- `DELETE_CANDIDATE`
- `EVIDENCE_INSUFFICIENT`

`MERGE_REQUIRED`では、Writerへ原稿化をReferralせず、Merge自身が`merged_article`を完成させます。Creator Referralは、統合対象から分離すべき別検索意図がEvidenceで確認された場合のみSBM向け候補として返せます。

## 安全境界

- Redirect / noindex / deleteは自動実行しない
- 高リスク処置は`USER_DECISION_REQUIRED`として扱う
- Doctor/SBMのblocked_scopeを越えて事実・金額・地域データ等を書き換えない
- Evidenceにない事実、体験、権威性、数値を創作しない
- 広告、アフィリエイトリンク、独自体験、比較表などの保護対象を無断で破壊しない
