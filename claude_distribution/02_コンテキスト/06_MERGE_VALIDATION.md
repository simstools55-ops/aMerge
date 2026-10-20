# aMerge v2.0.2 — 06_MERGE_VALIDATION.md

以下のSOURCE見出しは元資料の識別名です。ファイルシステム上のパスではありません。


---
## SOURCE: validation/MERGE_VALIDATION.md

# Merge Validation

Identity / Evidence / Decision / Preservation / Safety / Rollbackを検証します。

## RC3 Publication Quality Validation

MERGE_REQUIREDでは以下を追加検証する。

- `publication_assessment.status`が存在する。
- `HOLD_FOR_VERIFICATION`なのに`publication_ready=true`になっていない。
- `verification_required`に重要項目がある場合、公開可能と断定していない。
- 完成原稿に根拠のない保証表現（例：「必ず解決」）を残さない。
- Fact Checkできなかった事実を「確認済み」と偽らない。


---
## SOURCE: validation/RC3_PUBLICATION_QUALITY_ACCEPTANCE.md

# RC3 Publication Quality Acceptance

MERGE_REQUIREDの最終回答で次を検査する。

1. 完成原稿全文がcontent_markdownに入っている。
2. 統合で追加・再構成したfact claimを確認した。
3. 根拠のない「必ず」「絶対」「確実」等を残していない。
4. publication_assessment.statusが存在する。
5. verification_requiredが残る場合はHOLD_FOR_VERIFICATIONかつpublication_ready=false。
6. PUBLIC_OK_WITH_FIXESなら修正済み本文をcontent_markdownへ反映済み。
7. Writer Referralで逃げない。


---
## SOURCE: validation/SAFETY_VALIDATION.md

# Safety Validation

自動削除・自動Redirect・自動noindexは禁止。Primary公開前に吸収記事を変更しません。



## RC2 Machine Result Gate（プロジェクト指示との整合）
- `MERGE_REQUIRED` の `payload.merged_article.content_markdown` には完成原稿全文を入れる。
- 「上記参照」「省略」等の参照文字列のみではSUCCESSを返さない。
- `payload.publication_assessment.status` が `HOLD_FOR_VERIFICATION` の場合は `payload.merged_article.publication_ready=false` とする。
- 公開判定は原稿の準備状況であり、Redirect/noindex/deleteの自動実行を意味しない。
