# aMerge v2.0.2 — 01_MERGE_RUNTIME.md

以下のSOURCE見出しは元資料の識別名です。ファイルシステム上のパスではありません。


---
## SOURCE: runtime/MERGE_RUNTIME.md

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


---
## SOURCE: runtime/OUTPUT_PROTOCOL.md

# Output Protocol

Human-readable resultの後に`SIMS_MERGE_TREATMENT_RESULT_V1`形式のJSONを返します。

## MERGE_REQUIRED時のHuman-readable出力

1. Merge Decision
2. Preservation Map
3. Query Mapping
4. 統合内容の要約
5. **統合後完成原稿**
6. Publication Sequence
7. User Decision Items
8. Rollback Plan
9. **Publication Quality Assessment**
10. SBM登録用JSON

## `merged_article`

JSONの`payload.merged_article`には最低限以下を含めます。

- `article_id`：Primary ArticleID
- `article_url`：Primary URL
- `seo_title`
- `meta_description`
- `h1`
- `content_markdown`：統合後の完成本文全文。Human-readable出力と同一内容を省略せず格納
- `absorbed_from_article_ids`
- `preservation_trace`：どの保護内容をどこへ統合したか
- `change_summary`
- `publication_ready`

`publication_ready=true`は本文編集成果物として公開可能品質を意味します。301/noindex/deleteの実行完了を意味しません。

削除、noindex、Redirectは常に利用者判断項目へ分類します。

## Contract Compatibility

`SIMS_MERGE_TREATMENT_RESULT_V1`は`additionalProperties`を許容しているため、v1.1.0ではContract名・Versionを変更せず`payload.merged_article`を後方互換の拡張フィールドとして使用します。Shared 3.3.0のSchema自体は変更しません。


### Machine Result完全性ルール
- `payload.merged_article.content_markdown`には統合後完成原稿全文を実データとして格納する。
- Human-readableの完成原稿とJSON内`content_markdown`を同一内容にする。
- 「上記参照」「上記セクション参照」「上記の完成原稿を格納」「省略」等のプレースホルダーは禁止する。
- JSON単体で統合後Primary Articleを再現できなければResultは未完成とする。

## RC3 `publication_assessment`

MERGE_REQUIRED時は`payload.publication_assessment`を追加する。

最低限：
- `status`: `PUBLIC_OK` / `PUBLIC_OK_WITH_FIXES` / `HOLD_FOR_VERIFICATION`
- `fact_check_status`: `VERIFIED` / `PARTIALLY_VERIFIED` / `NOT_VERIFIED`
- `verified_claims`: 確認済みの主要claim
- `verification_required`: 公開前に確認が必要なclaim。なければ空配列
- `overclaim_fixes`: 過剰断定をどのように修正したか
- `notes`: 公開可否の短い理由

`merged_article.publication_ready`との整合性：
- `PUBLIC_OK` → true
- `PUBLIC_OK_WITH_FIXES` → true（必要修正を原稿へ反映済みの場合のみ）
- `HOLD_FOR_VERIFICATION` → false

ContractはadditionalProperties許容のため、Contract名・Versionは変更しない。

