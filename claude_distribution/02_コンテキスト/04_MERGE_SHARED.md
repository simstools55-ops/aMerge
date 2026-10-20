# aMerge v2.0.2 — 04_MERGE_SHARED.md

以下のSOURCE見出しは元資料の識別名です。ファイルシステム上のパスではありません。


---
## SOURCE: shared/SNAPSHOT_MANIFEST.json

```json
{
  "shared_version": "3.3.0",
  "snapshot_for": "MERGE",
  "generated_at": "2026-08-05T18:00:00+09:00",
  "included_paths": [
    "contracts/common/common-envelope-v1.schema.json",
    "contracts/merge/merge-treatment-request-v1.schema.json",
    "contracts/merge/merge-treatment-result-v1.schema.json",
    "contracts/merge/merge-plan-v1.schema.json",
    "contracts/platform/platform-error-v1.schema.json",
    "enums/treatment-type.json",
    "enums/result-status.json",
    "enums/priority.json"
  ],
  "excluded_paths": [
    "runtime/doctor",
    "runtime/writer",
    "runtime/creator"
  ],
  "compatible_product_versions": [
    "1.0.x"
  ]
}

```

---
## SOURCE: shared/contracts/common/common-envelope-v1.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": [
    "envelope",
    "payload"
  ],
  "properties": {
    "envelope": {
      "type": "object",
      "required": [
        "platform",
        "platform_version",
        "contract_name",
        "contract_version",
        "message_type",
        "message_id",
        "correlation_id",
        "created_at",
        "source_product",
        "target_product",
        "shared_version"
      ],
      "properties": {
        "platform": {
          "const": "SIMS_EDITORIAL_PLATFORM"
        },
        "platform_version": {
          "type": "string"
        },
        "contract_name": {
          "type": "string"
        },
        "contract_version": {
          "type": "string"
        },
        "message_type": {
          "enum": [
            "REQUEST",
            "RESULT",
            "EVENT",
            "ERROR",
            "ACKNOWLEDGEMENT"
          ]
        },
        "message_id": {
          "type": "string",
          "minLength": 1
        },
        "correlation_id": {
          "type": "string",
          "minLength": 1
        },
        "causation_id": {
          "type": [
            "string",
            "null"
          ]
        },
        "created_at": {
          "type": "string"
        },
        "source_product": {
          "type": "object"
        },
        "target_product": {
          "type": "object"
        },
        "shared_version": {
          "type": "string"
        },
        "locale": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        }
      }
    },
    "payload": {
      "type": "object"
    }
  }
}

```

---
## SOURCE: shared/contracts/merge/merge-plan-v1.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "SIMS_MERGE_PLAN_V1",
  "type": "object",
  "additionalProperties": true,
  "required": [
    "primary_article_id",
    "absorbed_article_ids",
    "preserved_sections",
    "new_structure",
    "publication_sequence",
    "rollback_plan"
  ],
  "properties": {
    "primary_article_id": {
      "type": "string"
    },
    "absorbed_article_ids": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "preserved_sections": {
      "type": "array"
    },
    "new_structure": {
      "type": "array"
    },
    "publication_sequence": {
      "type": "array"
    },
    "rollback_plan": {
      "type": "array",
      "minItems": 1
    }
  }
}

```

---
## SOURCE: shared/contracts/merge/merge-treatment-request-v1.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": [
    "envelope",
    "payload"
  ],
  "properties": {
    "envelope": {
      "type": "object",
      "required": [
        "platform",
        "platform_version",
        "contract_name",
        "contract_version",
        "message_type",
        "message_id",
        "correlation_id",
        "created_at",
        "source_product",
        "target_product",
        "shared_version"
      ],
      "properties": {
        "platform": {
          "const": "SIMS_EDITORIAL_PLATFORM"
        },
        "platform_version": {
          "type": "string"
        },
        "contract_name": {
          "const": "SIMS_MERGE_TREATMENT_REQUEST_V1"
        },
        "contract_version": {
          "type": "string"
        },
        "message_type": {
          "enum": [
            "REQUEST",
            "RESULT",
            "EVENT",
            "ERROR",
            "ACKNOWLEDGEMENT"
          ]
        },
        "message_id": {
          "type": "string",
          "minLength": 1
        },
        "correlation_id": {
          "type": "string",
          "minLength": 1
        },
        "causation_id": {
          "type": [
            "string",
            "null"
          ]
        },
        "created_at": {
          "type": "string"
        },
        "source_product": {
          "type": "object"
        },
        "target_product": {
          "type": "object"
        },
        "shared_version": {
          "type": "string"
        },
        "locale": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        }
      }
    },
    "payload": {
      "type": "object",
      "required": [
        "case_id",
        "treatment_request_id",
        "treatment_type",
        "primary_article_candidate",
        "target_articles",
        "objective",
        "evidence"
      ],
      "additionalProperties": true,
      "properties": {
        "case_id": {},
        "treatment_request_id": {},
        "treatment_type": {},
        "primary_article_candidate": {},
        "target_articles": {},
        "objective": {},
        "evidence": {}
      }
    }
  },
  "title": "SIMS_MERGE_TREATMENT_REQUEST_V1"
}

```

---
## SOURCE: shared/contracts/merge/merge-treatment-result-v1.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": [
    "envelope",
    "payload"
  ],
  "properties": {
    "envelope": {
      "type": "object",
      "required": [
        "platform",
        "platform_version",
        "contract_name",
        "contract_version",
        "message_type",
        "message_id",
        "correlation_id",
        "created_at",
        "source_product",
        "target_product",
        "shared_version"
      ],
      "properties": {
        "platform": {
          "const": "SIMS_EDITORIAL_PLATFORM"
        },
        "platform_version": {
          "type": "string"
        },
        "contract_name": {
          "const": "SIMS_MERGE_TREATMENT_RESULT_V1"
        },
        "contract_version": {
          "type": "string"
        },
        "message_type": {
          "enum": [
            "REQUEST",
            "RESULT",
            "EVENT",
            "ERROR",
            "ACKNOWLEDGEMENT"
          ]
        },
        "message_id": {
          "type": "string",
          "minLength": 1
        },
        "correlation_id": {
          "type": "string",
          "minLength": 1
        },
        "causation_id": {
          "type": [
            "string",
            "null"
          ]
        },
        "created_at": {
          "type": "string"
        },
        "source_product": {
          "type": "object"
        },
        "target_product": {
          "type": "object"
        },
        "shared_version": {
          "type": "string"
        },
        "locale": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        }
      }
    },
    "payload": {
      "type": "object",
      "required": [
        "case_id",
        "treatment_request_id",
        "treatment_result_id",
        "result_status",
        "merge_decision",
        "merge_plan"
      ],
      "additionalProperties": true,
      "properties": {
        "case_id": {},
        "treatment_request_id": {},
        "treatment_result_id": {},
        "result_status": {},
        "merge_decision": {},
        "merge_plan": {}
      }
    }
  },
  "title": "SIMS_MERGE_TREATMENT_RESULT_V1"
}

```

---
## SOURCE: shared/contracts/platform/platform-error-v1.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": [
    "envelope",
    "payload"
  ],
  "properties": {
    "envelope": {
      "type": "object",
      "required": [
        "platform",
        "platform_version",
        "contract_name",
        "contract_version",
        "message_type",
        "message_id",
        "correlation_id",
        "created_at",
        "source_product",
        "target_product",
        "shared_version"
      ],
      "properties": {
        "platform": {
          "const": "SIMS_EDITORIAL_PLATFORM"
        },
        "platform_version": {
          "type": "string"
        },
        "contract_name": {
          "const": "SIMS_PLATFORM_ERROR_V1"
        },
        "contract_version": {
          "type": "string"
        },
        "message_type": {
          "enum": [
            "REQUEST",
            "RESULT",
            "EVENT",
            "ERROR",
            "ACKNOWLEDGEMENT"
          ]
        },
        "message_id": {
          "type": "string",
          "minLength": 1
        },
        "correlation_id": {
          "type": "string",
          "minLength": 1
        },
        "causation_id": {
          "type": [
            "string",
            "null"
          ]
        },
        "created_at": {
          "type": "string"
        },
        "source_product": {
          "type": "object"
        },
        "target_product": {
          "type": "object"
        },
        "shared_version": {
          "type": "string"
        },
        "locale": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        }
      }
    },
    "payload": {
      "type": "object",
      "required": [
        "error_code",
        "severity",
        "recoverable",
        "message"
      ],
      "additionalProperties": true,
      "properties": {
        "error_code": {},
        "severity": {},
        "recoverable": {},
        "message": {}
      }
    }
  },
  "title": "SIMS_PLATFORM_ERROR_V1"
}

```

---
## SOURCE: shared/enums/priority.json

```json
{
  "name": "priority",
  "version": "1.0",
  "values": [
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "MONITOR"
  ]
}

```

---
## SOURCE: shared/enums/result-status.json

```json
{
  "name": "result-status",
  "version": "1.0",
  "values": [
    "SUCCESS",
    "PARTIAL_SUCCESS",
    "NO_ACTION",
    "USER_DECISION_REQUIRED",
    "EVIDENCE_INSUFFICIENT",
    "NOT_APPLICABLE",
    "VALIDATION_FAILED",
    "FAILED"
  ]
}

```

---
## SOURCE: shared/enums/treatment-type.json

```json
{
  "name": "treatment-type",
  "version": "1.0",
  "values": [
    "WRITER_PARTIAL_REWRITE",
    "WRITER_FULL_REWRITE",
    "WRITER_CTR_OPTIMIZATION",
    "WRITER_CONTENT_UPDATE",
    "WRITER_INTENT_ALIGNMENT",
    "WRITER_INTERNAL_LINK",
    "CREATOR_NEW_ARTICLE",
    "CREATOR_INTENT_SPLIT",
    "CREATOR_TOPIC_GAP",
    "CREATOR_SUPPORTING_ARTICLE",
    "MERGE_CONTENT_CONSOLIDATION",
    "MERGE_CANNIBALIZATION_RESOLUTION",
    "MERGE_ROLE_SEPARATION",
    "MERGE_REDIRECT_PLAN",
    "MERGE_NOINDEX_PLAN",
    "MERGE_DELETE_PLAN",
    "MONITOR_ONLY",
    "NO_ACTION",
    "USER_DECISION"
  ]
}

```
