# Merge Validation

Identity / Evidence / Decision / Preservation / Safety / Rollbackを検証します。

## RC3 Publication Quality Validation

MERGE_REQUIREDでは以下を追加検証する。

- `publication_assessment.status`が存在する。
- `HOLD_FOR_VERIFICATION`なのに`publication_ready=true`になっていない。
- `verification_required`に重要項目がある場合、公開可能と断定していない。
- 完成原稿に根拠のない保証表現（例：「必ず解決」）を残さない。
- Fact Checkできなかった事実を「確認済み」と偽らない。
