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
