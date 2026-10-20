# aMerge v2.0.2 — 07_MERGE_REFERENCE.md

以下のSOURCE見出しは元資料の識別名です。ファイルシステム上のパスではありません。


---
## SOURCE: PRODUCT_IDENTITY.json

```json
{
  "product_code": "MERGE",
  "product_name": "aMerge",
  "repository_name": "SIMS-Merge",
  "repository_type": "PRODUCT",
  "platform": "SIMS Editorial Platform",
  "platform_compatibility": "1.x",
  "current_version": "1.1.2",
  "shared_version": "3.3.0"
}

```

---
## SOURCE: README.md

# aMerge

Version: 1.1.2  
Shared: 3.3.0

SIMS Editorial Platformの統合処置担当製品です。複数記事の競合を評価し、Primary Article選定、Preservation Map、Query Mapping、統合構成、**統合後完成原稿の執筆**まで行います。

標準経路：`SIMS Manager → aDoctor → SIMS Manager → aMerge → SIMS Manager`

Redirect / noindex / deleteは自動実行せず、利用者判断としてSIMS Managerへ返します。

## RC3 Publication QA
統合後原稿は、PreservationだけでなくFact Check・過剰断定・公開可否までMerge自身が最終判定します。

