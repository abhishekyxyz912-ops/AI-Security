# AI Security

A guardrail layer that sits in front of an LLM:

1. **Prompt injection detection**: blocks malicious prompts
2. **PII detection and redaction**: removes personal data before the model sees it
3. **Model routing**: simple prompts go to an SLM, complex ones to an LLM (saves cost)

## Versions

| Version | Goal |
|---------|------|
| V1.0 | Blank repo with structure |
| V1.1 | Four guardrails: injection, PII, routing, model choice |
| V1.2 | FastAPI backend |
| V1.3 | GUI integration |
| V1.4 | Production ready |
| V2.0 | Industry / deployment version |

## Pipeline

```
prompt -> injection check -> PII redaction -> router -> SLM / LLM -> answer
```

## Setup

```
pip install -r requirements.txt
pytest
```
