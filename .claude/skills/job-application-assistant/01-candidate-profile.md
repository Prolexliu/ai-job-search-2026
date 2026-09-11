---
framework_version: 1.1.1
---

# Candidate Profile

<!-- Populated by /setup (Path A) on 2026-08-17 from documents/cv/MASTER-RESUME-REFERENCE.md,
documents/cv/Alex-Liu-Resume-TEMPLATE.docx, documents/linkedin/, and 94 archived applications.
MASTER-RESUME-REFERENCE.md is the authoritative source: where anything disagrees with it, it wins. -->

## Identity
- **Name:** Alex Liu
- **Location:** New York, NY
- **Phone:** 408-823-0000
- **Email:** prolexliu@gmail.com
- **LinkedIn:** linkedin.com/in/AlexLiuHealthcare
- **GitHub:** *(none on file)*
- **Status:** Position eliminated 2026-06-17 in post-acquisition restructuring (Medmo acquired by Covera Health). Actively searching.
- **Compensation floor:** **$180,000+ base.** Hard filter — check the posted band before drafting. Declined Inovalon ($112.6K–$155K) and Cotiviti ($140K–$180K) on this basis, 2026-08-18.
- **Constraints:** New York, NY. **Does not relocate** — has declined roles on this basis repeatedly (AWS, Hippocratic AI, Commure/California, Microsoft AI RAMP/Redmond, Assort Health/SF). NYC metro on-site, hybrid, or remote only.

> ⚠️ **Active non-compete until 2027-06-17.** The 2021 Non-Competition and Non-Solicitation
> Agreement bars work for a business competitive with Medmo (AI-powered medical imaging
> scheduling and prior authorization) in healthcare/medical services, requires 10 business
> days' notice to Medmo before starting healthcare-related work, and requires disclosure to
> prospective employers. **It has not been evaluated by an attorney.** Treat any direct
> imaging-scheduling or radiology-workflow competitor as a flag for the candidate's judgment,
> not an automatic exclusion — but never let a posting through without surfacing it.

### Languages

| Language | Level | Notes |
|----------|-------|-------|
| English | Native | |
| Mandarin Chinese | Native fluency | Grew up in Taipei; deep cultural familiarity with Taiwan work culture. A language and cultural asset for companies with Greater-China operations — **not** a claim of having led a Taiwan-based team. |

## Education

| Degree | Period | Institution | Key Topics |
|--------|--------|-------------|------------|
| MBA (Johnson) & MS, Healthcare Leadership, Policy & Research (Weill Cornell) | 2020–2022 | Cornell University | Healthcare policy, leadership, research methods |
| BS, Biomedical Engineering | 2009–2013 | Georgia Institute of Technology | |

*Short form when space is tight: "MBA & MS, Healthcare Policy." **Exception:** on policy-forward
and privacy/responsible-AI roles, always spell out "MS in Healthcare Leadership, Policy & Research
(Weill Cornell)" — the policy credential is the differentiator for those teams.*

## Professional Experience

### Director of Product and Engineering | Senior Technical Product Manager - Medmo Inc. (2021 - 2026)
New York, NY — AI-powered radiology scheduling & prior-authorization platform
*Reference form shows the promotion: Director of Product and Engineering 2023–2026; Senior Technical
Product Manager 2021–2023. Resume form collapses to one line, 2021–2026. **Never write "Present."***
- Led the B2C→B2B pivot that doubled ARR year over year — secured product-market fit, landed the first enterprise client (700+ employees), and established the revenue foundation for the Covera acquisition
- Shipped AI in production to scale operations 10x without added headcount: OCR for clinical document extraction and AI voice agents for operational automation, in HIPAA/SOC 2, with phased sign-off-gated rollout and human-in-the-loop escalation
- Built the company's first historical-data schema, reporting module, and revenue and operations data products from zero, including data classification and retention decisions; finance and operations closed against it
- Built the first analytics and experimentation infrastructure — A/B tests on scheduling flows, provider matching, and funnel conversion; 50% improvement in resource utilization
- Built the first product operating system, cutting time-to-ship 30%
- Scaled the cross-functional organization from 4 to 15+ across product, engineering, QA, DevOps, and IT; under 10% attrition
- Architected a HIPAA/SOC 2 microservices platform — 40% faster deployment cycles, 60% lower latency; three foundational 0→1 platforms
- Built a data-driven prior-auth auto-approval flow clearing ~20% of volume past the ~3-day payer-wait bottleneck; cost-per-scan down ~20%
- Auto-approval guardrails: bucketed cases by historical payer/policy/procedure approval rate and routed only combinations clearing a ~90% confidence threshold to auto-approval; every auto-approved case was flagged and tracked in a daily operational report for several days to catch denials or RFIs; thresholds were narrowed when a sub-category proved riskier than its bucket assumed (e.g., brain X-rays split out from the broader X-ray/ultrasound category for tighter scrutiny) (confirmed 2026-09-07, TailorMed mock interview prep)
- Managed distributed engineering pods across time zones (Ukraine and Bolivia)
- OCR read **physician radiology orders and requisitions**, plus the supporting clinical documentation establishing medical necessity for the referral (confirmed by Alex 2026-08-18)
- Owned **order intake by fax and API**, and the **reporting and monitoring layer** that tracked each radiology order's status, next step, and progression once in the system (confirmed 2026-08-18)
- A **provider-facing ordering UI existed only in Medmo's earliest days** and is no longer the intake path; do not claim ongoing ownership of a clinician-facing order-entry front end (confirmed 2026-08-18)
- **Voice-of-customer reached product through client success and sales**, not direct discovery with referring clinicians. Do not claim clinician-facing user research or site visits; the honest adjacent claim is discovery with clinical operators and practice administrators (confirmed 2026-08-18)

### Engineering & Architecture Advisor - Laurel Health & radEmploy (2024 - Present)
New York, NY
- Advising two early-stage VC-backed healthcare companies on HIPAA-compliant system architecture, engineering process, and product strategy at PMF stage

### Technical Architect | Senior Information Technology Engineer - New York-Presbyterian Hospital (2017 - 2021)
New York, NY
- Directed a $1B Epic EHR integration across 12 systems with a 25-person cross-functional team; drove alignment across clinical, engineering, legal, compliance, and operations. Top 5% performance org-wide
- Accelerated the COVID-19 go-live by one month — re-sequenced the critical path and consolidated 500+ clinical interfaces to ~100 (80%)
- Owned registration, eligibility, coverage, and HB/PB billing interface integration

### Application Consultant - Oracle Cerner (2015 - 2017)
Brooklyn, NY
- Delivered an EHR to HIMSS Level 7; led roadmaps for 140+ HL7 interfaces and 180+ medical device integrations at 10,000+ messages/day and 99.9% uptime
- Cut manual clinical documentation time 70%

### Program Developer - Medical Information Technology, Inc. (Meditech) (2013 - 2015)
Atlanta, GA
- Delivered 10+ CMS/HIPAA-aligned features for HomeCare software; led team adoption of Agile

## Independent Projects
- **Volunteer — MillionLives.org**: Distributed tens of thousands of masks and PPE to healthcare facilities worldwide during COVID-19

## Technical Skills

### Programming & ML
- **Python**, **TypeScript/JavaScript**, **Node.js**, **React.js**, PHP
- **PostgreSQL / MySQL**, REST APIs, microservices, data schema & pipeline design
- **AWS** (incl. Bedrock), **GCP**, CI/CD, DevOps
- **Claude Code** and AI-assisted development workflows (used daily)

### AI — honest scope (locked 2026-07-15, never soften)
- **Built and shipped in production:** AI voice/conversational agents that take actions (tool use, orchestration, human-in-the-loop escalation under 15s, <8% escalation rate) and OCR document automation. Zero HIPAA incidents in 18+ months.
- **Prototyped only:** LLM and retrieval — POCs with tools like NotebookLM to consolidate internal SOPs, evaluated and declined before building.
- **Never claim** a production RAG or LLM-eval pipeline that Alex built or engineered. Frame retrieval as hands-on prototyping plus the product judgment to evaluate fit before building. Voice agents are the legitimate agentic-AI proof.
- **Not held:** Kubernetes, Databricks, Spark, IaC, observability tooling, BigQuery.

### Domain Expertise
- Clinical workflows, EHR/EMR, healthcare operations
- Revenue cycle (HB/PB interface integration), registration/eligibility & coverage interfaces
- Utilization management (prior authorization), in-network steerage
- Multi-sided healthcare marketplaces (patients, providers, payers, employers)
- **Do NOT claim fintech** as a domain of expertise.

### Software & Tools
Epic, Cerner Millennium, Allscripts, ARIA Radiation Oncology, HL7 v2 (ADT, ORM/ORU, HB/PB billing), FHIR R4, HIPAA/SOC 2

*Epic/FHIR honesty note: deep hands-on = HL7 v2 + go-live delivery + HB/PB interface integration;
strong on FHIR R4 + stakeholder management; **ramping, not expert** on SMART on FHIR, CDS Hooks,
In Basket/SendMessage API. No Epic module certifications.*

## Key Metrics (validated — see MASTER-RESUME-REFERENCE.md §3)

| Metric | Value |
|--------|-------|
| Career length | 13 years (2013–2026) |
| Medmo ARR growth post-pivot | Doubled year over year |
| Ops traffic absorbed via AI | 10x, no added headcount |
| First enterprise client | 700+ employees |
| Team growth at Medmo | 4 → 15+ |
| Deployment cycle / latency / time-to-ship | −40% / −60% / −30% |
| Resource utilization | +50% |
| NYP Epic deployment | $1B, 12 systems, 25-person team, top 5% org-wide |
| COVID go-live | 1 month early; 500+ → ~100 interfaces (80%) |
| Cerner | 140+ HL7 interfaces, 180+ devices, 10,000+ msgs/day, −70% manual documentation |
| AI in production | 0 HIPAA incidents in 18+ months; <8% escalation rate |
| Prior-auth auto-approval | ~20% of pipeline cleared past ~3-day wait; cost-per-scan −20% |

## Publications
*(none on file)*

## Awards
*(none on file)*

## References
*(none on file — `documents/references/` is empty)*

More references available upon request.
