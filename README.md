# Dwi Fikri Aditya

[![Live portfolio](https://img.shields.io/badge/portfolio-live_site-0c5e56?style=flat-square)](https://dwifikriaditya13.github.io/ai-eval-portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-dwifikriaditya-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dwifikriaditya)
[![GitHub](https://img.shields.io/badge/GitHub-Dwifikriaditya13-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Dwifikriaditya13)
[![Email](https://img.shields.io/badge/email-fikkri.adittya%40gmail.com-555555?style=flat-square)](mailto:fikkri.adittya@gmail.com)
[![Based in](https://img.shields.io/badge/based_in-Lumajang%2C_Indonesia-6b4f2a?style=flat-square)](https://dwifikriaditya13.github.io/ai-eval-portfolio/#contact)

**AI Trainer | LLM Evaluation | Data Annotation | Data Engineering**

Freelance AI trainer based in Lumajang, East Java, Indonesia. I score and refine language-model outputs, review retrieval for RAG and supervised fine-tuning, and annotate speech, image, and video. The data-engineering side of the same work is newer: public-data pipelines, personal-data filtering, LoRA fine-tuning, and automated scoring for an agent benchmark.

**Live site:** [dwifikriaditya13.github.io/ai-eval-portfolio](https://dwifikriaditya13.github.io/ai-eval-portfolio/)

Annotation and AI-training project work runs from early 2025 through October 2026 (about 1 year 10 months), with freelance micro-tasks from 2022 and independent rule-based systems since 2021. Self-directed study in computer science, algorithms, and AI/LLM systems since 2021, alongside full-time work. Vocational high school (SMK Teknik Audio Video), graduated 2012.

Figures below are copied from specific roles. They are not a combined total.

| Figure | Where it applies |
|---|---|
| 95%+ accuracy standard | Rubric scoring, Appen (CrowdGen) |
| 20–22 responses / 6-hour day | Rubric scoring, Appen (CrowdGen) |
| 40 combined intent tasks / 6-hour day (average) | Intent and rationale annotation, Appen (CrowdGen) |
| 30 complex scenarios, strict deadline | Personalization evaluation, Welocalize |
| ±500 ms timestamp tolerance | Indonesian verbatim audio, OneForma (Centific) |

## Featured work

| Work | What it shows |
|---|---|
| [Mercor — image evaluation and data-engineering contract](https://dwifikriaditya13.github.io/ai-eval-portfolio/#mercor) | Pairwise image checks (prompt adherence, defects, aspect ratio, multilingual text) and an agent benchmark: public instruction data, PII filtering, dedup, length limits, GPU LoRA fine-tuning, automated scoring, CI. |
| [Response scoring rubric](rubrics/response-scoring-rubric-template.md) | Public 0–3 template: relevance, factual accuracy, coherence, tone. Not a client rubric. |
| [Worked scoring example](sample-evaluations/example-response-scoring.md) | Four invented answers, a 12/12 tie, and a golden response written from the tie. |
| [Query intent guideline](annotation-guidelines/query-intent-annotation-guideline-example.md) | Informational, navigational, and transactional intent, plus ambiguity handling. |
| [Synthetic grounded scores](samples/rubric-scoring-example.md) | Three invented answers checked only against a fake product card. |
| [Toy PII filter and dedup](samples/pii_filter_dedup.py) | Length limit, obvious email/phone redaction, and duplicate removal on hard-coded fake rows. |

## Skills

| Area | Skills |
|---|---|
| AI and evaluation | RAG evaluation, LLM fine-tuning (SFT), data annotation and QA, rubric-based scoring, AI model evaluation, personalization evaluation, image generation evaluation, hallucination detection, prompt engineering, AI tools and automation |
| Systems and data | Python, PyTorch, LoRA fine-tuning, Docker, GitHub Actions CI, GPU workloads (H100), data pipelines, process automation, rule-based systems, Git/GitHub |
| Platforms | Mercor, Appen/CrowdGen, OneForma/Centific, Welocalize, Remotasks/Scale AI, Labelbox/Alignerr |
| Productivity | Lark, Microsoft Excel, Google Workspace, remote work |
| Languages | Indonesian (native), Javanese (native/regional), English (professional working) |

## Experience

| Period | Organization | Role |
|---|---|---|
| Oct 2026 – Present | Mercor | AI Image Evaluation Specialist |
| Oct 2026 | Mercor | Task Creator — Data Engineering (contract) |
| Jun 2026 – Present | Appen (CrowdGen) | AI Rubric Scoring and Response Refinement Specialist |
| Oct 2025 – May 2026 | Appen (CrowdGen) | Search Relevance and Content Evaluation Rater |
| Jul 2026 – Present | OneForma (Centific) | Audio Transcription and Segmentation Annotator |
| Jul 2026 – Aug 2026 | Welocalize | AI Evaluation Specialist — Personalization and Response Quality |
| Jan 2025 – Sep 2025 | Remotasks (Scale AI) | Data Annotator (robotics video) |
| 2022 – 2025 | Prodege (Swagbucks / ySense) | Freelance task contributor and AI feedback |
| 2021 – Present | Independent | Rule-based systems and process automation |

Concept-level write-ups of RAG and SFT evaluation, rubric scoring, search relevance, Indonesian verbatim audio, robotics video, hand-action captioning, image evaluation, personalization, and the agent benchmark are on the [live site](https://dwifikriaditya13.github.io/ai-eval-portfolio/#case-studies).

## Certifications

Both completed in July 2026. Copies: [github.com/Dwifikriaditya13/certificates](https://github.com/Dwifikriaditya13/certificates).

- Anthropic Academy — Claude 101
- Anthropic Academy — AI Capabilities and Limitations

## Repository map

```
index.html                     Portfolio page (GitHub Pages)
assets/                        Styles, script, fonts, favicon, social image
rubrics/                       Public response-scoring template
annotation-guidelines/         Public query-intent guideline
sample-evaluations/            Invented end-to-end scoring example
samples/                       Extra synthetic scoring note and toy cleaning script
```

Preview locally:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080`. The cleaning demo runs with:

```bash
python3 samples/pii_filter_dedup.py
```

## What is not in this repo

Client and project code names, confidential guidelines, real prompts, and real task data are omitted on purpose. Every sample is labeled synthetic. A phone number is not published here.

## Contact

- Email: [fikkri.adittya@gmail.com](mailto:fikkri.adittya@gmail.com)
- LinkedIn: [linkedin.com/in/dwifikriaditya](https://www.linkedin.com/in/dwifikriaditya)
- GitHub: [github.com/Dwifikriaditya13](https://github.com/Dwifikriaditya13)
