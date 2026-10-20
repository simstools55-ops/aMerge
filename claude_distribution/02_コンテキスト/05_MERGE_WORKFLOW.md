# aMerge v2.0.2 — 05_MERGE_WORKFLOW.md

以下のSOURCE見出しは元資料の識別名です。ファイルシステム上のパスではありません。


---
## SOURCE: docs/MERGE_WORKFLOW.md

# Merge Workflow

## 標準フロー

`SBM → Doctor → SBM → Merge → SBM`

1. Request / Evidence Validation
2. Cannibalization評価
3. Primary Article Selection
4. Preservation Map
5. Query Mapping
6. New Structure
7. **Merged Article Writing**
8. Preservation / Scope / Duplication Validation
9. Publication Sequence
10. Rollback Plan
11. `SIMS_MERGE_TREATMENT_RESULT_V1`返却

## Merged Article Writing

Primary Articleを土台にし、吸収記事からPreservation Mapで必要と判定した内容のみを移植・統合します。重複段落は削除し、検索意図ごとの役割を1本の記事内で明確にします。

完成原稿は`merged_article.content_markdown`として返し、SEOタイトル、meta description、H1、変更要約、吸収元対応表も同梱します。

## Merge後の処置

本文反映後、内部リンク張替え、301、noindex、削除などをPublication SequenceとしてSBMへ返します。高リスク処置は利用者判断であり、Merge自身は実行しません。


---
## SOURCE: docs/PRIMARY_ARTICLE_SELECTION.md

# Primary Article Selection

参考スコア:

- SEO Performance: 35%
- URL Authority: 20%
- Content Value: 30%
- Strategic Fit: 15%

スコアは唯一の決定根拠ではありません。収益記事、被リンクURL、ブランド重要URL、僅差の場合は利用者判断を必須とします。


---
## SOURCE: docs/PRODUCT_SPECIFICATION.md

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


---
## SOURCE: docs/REDIRECT_NOINDEX_DELETE_POLICY.md

# Redirect / noindex / Delete Policy

- 自動実行禁止
- Primary Article公開前の吸収記事処置禁止
- 独自情報・収益要素・被リンクを確認
- Redirect先とRollback手順を必須化
- データ不足時に削除を推奨しない


---
## SOURCE: docs/VALIDATION_RULES.md

# Validation Rules

Identity、Evidence、Decision、Preservation、Safety、Rollbackの6段階で検証します。

FAIL条件:
- Primary Article不明
- Rollback Plan欠落
- 独自情報を保存せず削除候補化
- Redirect先不明
- Evidence不足で高リスク処置を確定

