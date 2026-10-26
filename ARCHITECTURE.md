---

### File 3: `ARCHITECTURE.md` (Satisfies Technical Design Document & Diagrams Checklist)[cite: 3]
Create a new file named `ARCHITECTURE.md` in your repo and paste this:

```markdown
# Technical Design Document: SwasthyaSetu AI

## 1. System Architecture Diagram
```mermaid
flowchart LR
    A[Citizen / ASHA Worker] -->|Uploads Rx Image| B(PWA Frontend UI)
    B -->|Image Base64 / OCR| C{AI Vision & NLP Engine}
    C -->|Gemini 2.5 Flash API| D[Rx Entity Extractor]
    D -->|Brand Name + Dosage| E[(Jan Aushadhi Salt DB)]
    E -->|Chemical Salt Match| F[Cost Savings & Welfare Engine]
    F -->|Structured JSON| G[Vernacular TTS Generator]
    G -->|Hindi / Bhojpuri Audio + UI| A
