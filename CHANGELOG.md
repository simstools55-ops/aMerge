# Changelog

## 1.1.0-RC3
- Added mandatory post-merge Fact Check gate.
- Added overclaim detection and prohibition of unsupported guarantee language.
- Added publication_assessment with PUBLIC_OK / PUBLIC_OK_WITH_FIXES / HOLD_FOR_VERIFICATION.
- publication_ready is now tied to the publication assessment.
- Preserved RC2 machine-result completeness gate and Merge-owned manuscript generation.

## 1.1.0-RC2
- Machine JSON must contain the complete merged manuscript.
- Placeholder/reference-only content_markdown is prohibited.
- Added completeness gate and regression test.
- Shared snapshot remains 3.3.0 pending actual Shared 3.5.0 source.


## 1.1.0-RC1
- Merge responsibility expanded from planning-only to planning + merged-article writing.
- Removed Writer referral for MERGE_REQUIRED manuscript creation.
- Added `merged_article` result artifact and Merge Writing Rules.
- Redirect/noindex/delete remain user decisions.

# Changelog

## [1.0.0-RC1] - 2026-08-05

- SIMS Mergeを新規作成
- Shared Editorial Knowledge 3.3.0へ同期
- Merge Treatment Request / Result / Plan Contractへ対応
- Primary Article評価、Preservation Map、Query Mapping、Rollback Planの参照実装を追加
- 12件以上の回帰試験を追加
