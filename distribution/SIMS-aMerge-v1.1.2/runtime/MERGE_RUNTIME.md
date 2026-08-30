# Merge Runtime

SBM発行のCaseID / TreatmentRequestID / ArticleIDを変更しません。入力Evidenceを検証し、統合判断だけでなく、MERGE_REQUIREDの場合は**統合後のPrimary Article完成原稿まで生成**します。

## 実行順序

1. Evidence Validation
2. Primary Selection
3. Preservation Map
4. Query Mapping
5. Structure Design
6. Merged Article Writing
7. Preservation / Duplication / Scope Validation
8. **Post-Merge Fact Check / Overclaim Validation**
9. Publication Readiness Decision
10. Publication / Rollback Planning
11. SBM Return

Writerへ「Merge Planを原稿化する」Referralは生成しません。Creator Referralは別意図の独立記事候補に限定します。Redirect/noindex/deleteは自動実行しません。

## Evidence Source

SBM Merge Packageに対象記事本文とEvidenceが含まれている場合、それを正本として統合作業を完結します。本文取得のためのWebアクセスを必須条件にしてはいけません。外部確認が必要でも、robots等で取得できないことだけを理由に、Package内本文を無視して統合執筆を停止しません。


## Machine Result Gate
MERGE_REQUIREDの最終返却前に`payload.merged_article.content_markdown`を検査する。空欄、プレースホルダー、Human-readable完成原稿への参照だけの場合はSUCCESSとして返してはいけない。

## RC3 Publication Gate

MERGE_REQUIREDのSUCCESS返却前に、完成原稿について次を必ず実施する。

1. 統合で新規追加・再構成したfact claimを列挙する。
2. Evidenceで確認済み／外部一次情報で確認済み／未確認に分類する。
3. 「必ず」「絶対」「確実」等の保証表現を検査し、根拠がなければ修正する。
4. `publication_assessment.status`を`PUBLIC_OK` / `PUBLIC_OK_WITH_FIXES` / `HOLD_FOR_VERIFICATION`から決定する。
5. `HOLD_FOR_VERIFICATION`の場合、`merged_article.publication_ready=false`とし、未確認事項を`verification_required`へ列挙する。

robots等で外部確認できないことだけを理由に統合執筆そのものを停止しない。ただし、現行仕様の確認が必要な重要claimを未確認のまま公開可能扱いにしてはいけない。
