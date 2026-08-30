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
