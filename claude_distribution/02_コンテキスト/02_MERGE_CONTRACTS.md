# aMerge v2.0.2 — 02_MERGE_CONTRACTS.md

以下のSOURCE見出しは元資料の識別名です。ファイルシステム上のパスではありません。


---
## SOURCE: contracts/common-envelope-v1.schema.json

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
## SOURCE: contracts/merge-plan-v1.schema.json

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
## SOURCE: contracts/merge-treatment-request-v1.schema.json

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
## SOURCE: contracts/merge-treatment-result-v1.schema.json

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
## SOURCE: contracts/platform-error-v1.schema.json

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
