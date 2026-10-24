# Architecture Preparation Roadmap

A project-led preparation guide for:

- Azure Solutions Architect
- AI Solutions Architect
- Forward Deployed Engineer
- Staff/Principal Engineer

The roadmap combines architecture fundamentals, distributed systems, Azure platform design, APIs and integrations, reliability, security, agentic AI, communication practice, and a certification strategy aligned to current architecture roles.

## Files

- [`ARCHITECTURE_PREPARATION_ROADMAP.pdf`](ARCHITECTURE_PREPARATION_ROADMAP.pdf) — publication-ready guide
- [`ARCHITECTURE_PREPARATION_ROADMAP.md`](ARCHITECTURE_PREPARATION_ROADMAP.md) — editable source
- [`AI_EVAL_INTERVIEW_QA.md`](AI_EVAL_INTERVIEW_QA.md) — AI-evaluation interview Q&A with worked examples
- [`print.html`](print.html) — print-ready HTML
- [`scripts/build_pdf.py`](scripts/build_pdf.py) — reproducible PDF build
- [`citations/ledger.json`](citations/ledger.json) — source-to-citation ledger

## Recommended certification order

1. **AZ-104** — Azure Administrator Associate
2. **AZ-305** — Azure Solutions Architect Expert
3. **AI-103** — Azure AI Apps and Agents Developer Associate
4. **AB-100** — Agentic AI Business Solutions Architect Expert

Add AZ-400, SC-500/SC-100, Terraform Associate, CKA, or TOGAF only when the target role requires that specialization.

> AI-102 and AZ-500 are retired. The guide points to the current AI-103 and SC-500 paths.

## Study method

- Duration: 12 weeks
- Ratio: approximately 30% study and 70% hands-on work
- Capstone: C#/.NET commerce platform with a governed AI customer-operations agent
- Weekly evidence: diagram, ADR, failure analysis, implementation slice, and spoken explanation

## Build the PDF

Requirements:

- Python 3
- `markdown`
- `pypdf`
- Google Chrome

Run:

```bash
python scripts/build_pdf.py
```

The script generates `print.html`, prints it to PDF using headless Chrome, adds document metadata and bookmarks, and verifies page text plus hyperlink annotations.

## Scope note

The certification ranking is based on a targeted scan of current Azure and AI architecture postings, not a statistical census of the entire market. Certifications validate knowledge; they do not replace production evidence or architecture judgment.
