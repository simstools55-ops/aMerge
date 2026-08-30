from __future__ import annotations
from difflib import SequenceMatcher
from typing import Any, Dict, List

REQUIRED_ARTICLE_FIELDS = {"article_id", "url", "article_title", "article_body", "main_query", "clicks", "impressions", "ctr", "position"}

def validate_request(request: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for field in ("case_id", "treatment_request_id", "target_articles"):
        if not request.get(field): errors.append(f"missing:{field}")
    articles = request.get("target_articles") or []
    if len(articles) < 2: errors.append("target_articles:minItems=2")
    ids=set()
    for idx,a in enumerate(articles):
        missing=REQUIRED_ARTICLE_FIELDS-set(a)
        errors += [f"target_articles[{idx}].missing:{x}" for x in sorted(missing)]
        aid=a.get("article_id")
        if aid in ids: errors.append(f"duplicate_article_id:{aid}")
        ids.add(aid)
    return errors

def _query_overlap(a: Dict[str, Any], b: Dict[str, Any]) -> float:
    qa=set([a.get("main_query","")] + list(a.get("queries",[])))
    qb=set([b.get("main_query","")] + list(b.get("queries",[])))
    qa={x.strip().lower() for x in qa if x}; qb={x.strip().lower() for x in qb if x}
    if not qa or not qb: return 0.0
    return len(qa & qb)/len(qa | qb)

def _intent_overlap(a: Dict[str, Any], b: Dict[str, Any]) -> float:
    ia=(a.get("search_intent") or a.get("main_query") or "").lower()
    ib=(b.get("search_intent") or b.get("main_query") or "").lower()
    return SequenceMatcher(None,ia,ib).ratio()

def _content_overlap(a: Dict[str, Any], b: Dict[str, Any]) -> float:
    return SequenceMatcher(None,(a.get("article_body") or "")[:12000],(b.get("article_body") or "")[:12000]).ratio()

def _article_score(a: Dict[str, Any]) -> float:
    clicks=max(float(a.get("clicks",0)),0); impressions=max(float(a.get("impressions",0)),0)
    ctr=max(float(a.get("ctr",0)),0); position=max(float(a.get("position",100)),0.1)
    backlinks=max(float(a.get("backlinks",0)),0); internal=max(float(a.get("internal_link_count",0)),0)
    unique=max(float(a.get("unique_value_score",0.5)),0); strategic=max(float(a.get("strategic_fit_score",0.5)),0)
    seo=min(clicks/1000,1)*0.35 + min(impressions/20000,1)*0.2 + min(ctr/0.1,1)*0.2 + min(10/position,1)*0.25
    authority=min(backlinks/20,1)*0.6 + min(internal/30,1)*0.4
    return round(seo*35 + authority*20 + min(unique,1)*30 + min(strategic,1)*15,2)

def _baseline_merged_article(primary: Dict[str, Any], absorbed: List[Dict[str, Any]], preserved: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Deterministic baseline artifact for repository tests.

    Claude runtime performs semantic rewriting. The Python engine guarantees that a MERGE_REQUIRED
    result carries a concrete merged-article artifact and never delegates manuscript creation to Writer.
    """
    body=(primary.get("article_body") or "").strip()
    additions=[]
    for a in absorbed:
        for item in a.get("preservation_items",[]):
            if isinstance(item,dict):
                text=str(item.get("content") or item.get("text") or item.get("item") or "").strip()
            else:
                text=str(item).strip()
            if text and text not in body and text not in additions:
                additions.append(text)
    if additions:
        body += "\n\n" + "\n\n".join(additions)
    return {
        "article_id":primary["article_id"],"article_url":primary["url"],
        "seo_title":primary.get("seo_title") or primary.get("article_title") or "",
        "meta_description":primary.get("meta_description") or "",
        "h1":primary.get("h1") or primary.get("article_title") or "",
        "content_markdown":body,
        "absorbed_from_article_ids":[a["article_id"] for a in absorbed],
        "preservation_trace":preserved,
        "change_summary":["Primary Articleを土台に統合","Preservation Mapの固有価値を吸収","重複内容をPrimaryへ集約"],
        "publication_ready":bool(body)
    }


def _is_complete_merged_content(value: Any) -> bool:
    text = str(value or "").strip()
    if not text:
        return False
    forbidden = ("上記参照", "上記セクション", "上記の統合後完成原稿", "上記の完成原稿", "省略")
    return not any(token in text for token in forbidden)


OVERCLAIM_TOKENS = ("必ず成功", "必ず解決", "必ず原因を特定", "必ず満足", "絶対に", "確実に解決")

def _find_overclaims(text: Any) -> List[str]:
    value=str(text or "")
    return [token for token in OVERCLAIM_TOKENS if token in value]

def _publication_assessment(merged_article: Dict[str, Any], request: Dict[str, Any]) -> Dict[str, Any]:
    body=str((merged_article or {}).get("content_markdown") or "")
    overclaims=_find_overclaims(body)
    verification_required=list(request.get("verification_required") or [])
    verified_claims=list(request.get("verified_claims") or [])
    # Repository engine cannot browse. Any caller-declared verification requirement keeps the result on hold.
    if verification_required:
        status="HOLD_FOR_VERIFICATION"
        fact="PARTIALLY_VERIFIED" if verified_claims else "NOT_VERIFIED"
    elif overclaims:
        status="PUBLIC_OK_WITH_FIXES"
        fact="VERIFIED" if verified_claims else "PARTIALLY_VERIFIED"
    else:
        status="PUBLIC_OK"
        fact="VERIFIED" if verified_claims else "PARTIALLY_VERIFIED"
    return {
        "status":status,
        "fact_check_status":fact,
        "verified_claims":verified_claims,
        "verification_required":verification_required,
        "overclaim_fixes":[{"detected":x,"action":"REWRITE_REQUIRED_BEFORE_PUBLICATION"} for x in overclaims],
        "notes":"外部確認が必要なclaimが残る場合は公開保留。過剰断定は公開前に弱める。"
    }

def assess_merge(request: Dict[str, Any]) -> Dict[str, Any]:
    errors=validate_request(request)
    if errors:
        return {"result_status":"VALIDATION_FAILED","errors":errors,"merge_decision":"EVIDENCE_INSUFFICIENT"}
    articles=request["target_articles"]
    pairs=[]
    for i in range(len(articles)):
        for j in range(i+1,len(articles)):
            q=_query_overlap(articles[i],articles[j]); intent=_intent_overlap(articles[i],articles[j]); content=_content_overlap(articles[i],articles[j])
            pairs.append({"articles":[articles[i]["article_id"],articles[j]["article_id"]],"query_overlap":round(q,3),"intent_overlap":round(intent,3),"content_overlap":round(content,3)})
    qavg=sum(x["query_overlap"] for x in pairs)/len(pairs); iavg=sum(x["intent_overlap"] for x in pairs)/len(pairs); cavg=sum(x["content_overlap"] for x in pairs)/len(pairs)
    evidence_sufficient=all(float(a.get("impressions",0))>=10 or a.get("backlinks",0)>0 for a in articles)
    if not evidence_sufficient: confidence="POSSIBLE"; decision="EVIDENCE_INSUFFICIENT"
    elif qavg>=0.45 and iavg>=0.75 and cavg>=0.45: confidence="CONFIRMED"; decision="MERGE_REQUIRED"
    elif iavg>=0.72 and (qavg>=0.2 or cavg>=0.3): confidence="LIKELY"; decision="MERGE_REQUIRED"
    elif iavg<0.55: confidence="UNLIKELY"; decision="KEEP_BOTH"
    else: confidence="POSSIBLE"; decision="ROLE_SEPARATION_REQUIRED"
    scored=sorted([{"article_id":a["article_id"],"score":_article_score(a)} for a in articles],key=lambda x:x["score"],reverse=True)
    primary=scored[0]["article_id"] if decision!="EVIDENCE_INSUFFICIENT" else None
    absorbed_ids=[a["article_id"] for a in articles if a["article_id"]!=primary] if primary and decision=="MERGE_REQUIRED" else []
    preserved=[]
    for a in articles:
        for item in a.get("preservation_items",[]): preserved.append({"source_article_id":a["article_id"],"item":item,"action":"MOVE_TO_PRIMARY" if a["article_id"]!=primary else "KEEP_AS_IS"})
    user_items=[]
    if decision=="MERGE_REQUIRED":
        if request.get("scope",{}).get("redirect_allowed") or any(a.get("backlinks",0)>0 for a in articles): user_items.append({"type":"REDIRECT_DECISION","required":True})
        user_items.append({"type":"ABSORBED_ARTICLE_DISPOSITION","required":True,"options":["301_REDIRECT","NOINDEX","DELETE_AFTER_REDIRECT"]})
    referrals=[]
    for a in articles:
        if a.get("separate_intent_candidate"): referrals.append({"target_product":"CREATOR","treatment_type":"CREATOR_INTENT_SPLIT","reason":a["separate_intent_candidate"]})
    merged_article=None
    if decision=="MERGE_REQUIRED":
        primary_obj=next(a for a in articles if a["article_id"]==primary)
        absorbed_objs=[a for a in articles if a["article_id"] in absorbed_ids]
        merged_article=_baseline_merged_article(primary_obj,absorbed_objs,preserved)
    publication_assessment=None
    if decision=="MERGE_REQUIRED":
        publication_assessment=_publication_assessment(merged_article,request)
        merged_article["publication_ready"]=publication_assessment["status"] in ("PUBLIC_OK","PUBLIC_OK_WITH_FIXES") and not publication_assessment["verification_required"]
    if decision == "MERGE_REQUIRED" and (not merged_article or not _is_complete_merged_content(merged_article.get("content_markdown"))):
        raise ValueError("MERGED_ARTICLE_CONTENT_INCOMPLETE")
    return {
      "case_id":request["case_id"],"treatment_request_id":request["treatment_request_id"],"result_status":"SUCCESS" if decision!="EVIDENCE_INSUFFICIENT" else "EVIDENCE_INSUFFICIENT",
      "cannibalization_confidence":confidence,"merge_decision":decision,"pair_analysis":pairs,
      "primary_article_id":primary,"article_scores":scored,"absorbed_article_ids":absorbed_ids,
      "merge_plan":{
        "primary_article_id":primary,"absorbed_article_ids":absorbed_ids,"preservation_map":preserved,
        "query_mapping":[],"new_structure":[],
        "publication_sequence":["UPDATE_PRIMARY_WITH_MERGED_ARTICLE","VERIFY_PRIMARY","UPDATE_INTERNAL_LINKS","USER_DECIDES_REDIRECT_NOINDEX_DELETE","START_MONITORING"] if decision=="MERGE_REQUIRED" else [],
        "rollback_plan":["SAVE_ALL_ORIGINAL_ARTICLES","SAVE_METADATA_AND_LINKS","RECORD_REDIRECT_NOINDEX_STATE","DO_NOT_AUTO_ROLLBACK"]
      },
      "merged_article":merged_article,"publication_assessment":publication_assessment,"user_decision_items":user_items,"follow_up_referrals":referrals,
      "recommended_next_status":"USER_ACTION_PENDING" if decision=="MERGE_REQUIRED" else "TREATMENT_REVIEW_PENDING" if decision=="ROLE_SEPARATION_REQUIRED" else "COMPLETED_NO_ACTION" if decision=="KEEP_BOTH" else "EVIDENCE_INSUFFICIENT"
    }
