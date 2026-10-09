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
- **Cost per scan was a key north-star metric** at Medmo. A unit-economics model of the workflow identified which steps carried the most cost; the two largest were **prior authorization** and **patient engagement**, and roadmap tradeoffs were evaluated by whether they drove cost per scan down (confirmed 2026-09-17, Parachute HM mock prep). Alex's personal ownership of the model vs. the team's is still to confirm.
- Built the first product operating system, cutting time-to-ship 30%
- Scaled the cross-functional organization from 4 to 15+ across product, engineering, QA, DevOps, and IT; under 10% attrition
- Architected a HIPAA/SOC 2 microservices platform — 40% faster deployment cycles, 60% lower latency; three foundational 0→1 platforms
- Built a data-driven prior-auth auto-advance flow clearing ~20% of volume past the ~3-day payer-wait bottleneck; cost-per-scan down ~20%
- Auto-advance criterion and guardrails: for the initial phase, used historical data to select payer/procedure combinations where ≥90% of cases came back as **not requiring prior authorization** — mostly low-modality radiology such as X-ray and ultrasound — and auto-advanced them instead of holding them for the auth check (criterion clarified by Alex 2026-09-15; earlier notes called it an approval-rate threshold, and the submitted UiPath CV says "consistently high approval rates" — the precise version is "auth not required"). Accepted the risk that fewer than 10% of auto-advanced cases might hit an issue (confirmed 2026-09-15). Catches: a pre-appointment checklist three days before the appointment that could flag a case that needed auth (confirmed 2026-09-15); every auto-advanced case flagged and tracked in a daily operational report for several days to catch denials or RFIs (confirmed 2026-09-07); if a case was denied, operations worked with the patient to reschedule and moved it into the normal authorization process (confirmed 2026-09-15). Thresholds were narrowed when a sub-category proved riskier than its bucket assumed (e.g., brain X-rays split out from the broader X-ray/ultrasound category for tighter scrutiny) (confirmed 2026-09-07, TailorMed mock interview prep)
- Prior-auth requests were submitted through a **third-party vendor** that obtained authorizations from sources such as **Availity** or directly from insurers (confirmed 2026-09-15)
- The prior-auth service **started as a client pilot run on a simple spreadsheet**, not a platform build (confirmed 2026-09-17, Parachute HM mock prep). At the outset the only known requirements were collecting the patient's insurance and the modality, calling the insurer to determine next steps, and tracking prior-auth status, so confidence in a full UI/backend spec was low relative to other core features in the pipeline; roughly a month of platform build was deferred in favor of other core work while the pilot generated real cases. The pilot surfaced intake requirements not known upfront, including **imaging center NPI, Tax ID, and diagnosis codes**, which became the detailed requirements for the platform build. Still to confirm: how PHI was handled in the pilot spreadsheet, whether Alex personally made the pilot-vs-build call, and whether the pilot's data fed the later auto-advance flow.
- Built an identity-verification gate that confirmed the patient's date of birth before any patient information was provided (confirmed 2026-09-13, Microsoft Privacy PM recruiter-screen debrief). Ran as a name + DOB + phone-on-file match that gated an SMS-based patient portal flow (confirmed 2026-09-14). Whether the match happened before any PHI appeared in the SMS body itself (vs. only after clicking into an authenticated session), and mismatch handling, still to confirm.
- Set up Medmo's HIPAA environment on AWS: accepted the AWS BAA, evaluated and restricted usage to HIPAA-eligible services only, configured encryption at rest and in transit, enabled logging (confirmed 2026-09-14). Alex's own characterization: this followed AWS's standard HIPAA guidance to get started rather than a bespoke security program — accurate framing for interviews.
- Medmo was a **Business Associate** to imaging centers and health plans; Medmo's own AI/cloud vendors (e.g., AWS) were subcontractor BAs to Medmo (confirmed 2026-09-14)
- Was one of the main points of contact for Medmo's **SOC 2 Type I and Type II** engagements — worked with audit vendor **Thoropass** to establish policy, designed the evidence/artifact-collection workflow integrated into day-to-day operations, coordinated cross-department control implementation (HR background checks, HIPAA training rollout), and coordinated the annual penetration test with the vendor (confirmed 2026-09-14). Scope (Security-only vs. also Privacy/Confidentiality trust criteria) and whether certification landed on schedule still to confirm.
- Worked with **outside counsel** on legal/compliance matters but was not the direct point of contact and has no personal story of a specific legal negotiation or escalation to tell (confirmed 2026-09-14) — his compliance-partnership depth is the Thoropass/audit-vendor relationship, not outside counsel.
- Built a **patient consent + Release of Information (ROI) workflow** to retrieve radiology reports from imaging centers after a visit and return them to the original referring provider (confirmed 2026-09-14). Legal basis: permitted without separate authorization under HIPAA's treatment exception, but many imaging centers required patient consent anyway per their own release-of-information policies, so Alex built consent capture to satisfy the stricter standard. Consent was captured two ways — web portal or phone call — and logged with a timestamp as an artifact; the system auto-generated the ROI form from that artifact to formally request the report from the imaging center. Scaled to **5,000+ reports collected monthly**. Whether consent was captured per order/report or as a standing authorization reused across future visits is still to confirm.
- Managed distributed engineering pods across time zones (Ukraine and Bolivia)
- **Difficult client executive, regional underperformance** (stated by Alex 2026-09-24, UiPath Colleen mock; the only external difficult-stakeholder story on file). A client regional VP pushed ownership of a region's worst-in-client performance onto the Medmo team. Root cause: the region's dominant imaging center organization refused to work with Medmo and complained to the client that Medmo had engaged them rudely. Medmo pulled and listened to sample calls and found no evidence of it. Scheduling with that organization continued only by faxing the details and waiting for the center to start the engagement. Alex acknowledged ownership, laid out the attempts to coordinate with the imaging organization, said Medmo had reached the limit of what it could fix without the client communicating directly with the organization, and kept the conversation on shared patient access. The VP of Operations agreed to reach out from the client's side and acknowledged Medmo was still **~20% above the client's baseline booking rate**. *Still to confirm:* which region (the Tennessee/Kentucky reference was ambiguous); client type; whether the regional VP and VP of Operations are one person; the exact definition of the 20%; whether Alex personally reviewed the calls; the outcome of the outreach; the year.
- OCR read **physician radiology orders and requisitions**, plus the supporting clinical documentation establishing medical necessity for the referral (confirmed by Alex 2026-08-18)
- Owned **order intake by fax and API**, and the **reporting and monitoring layer** that tracked each radiology order's status, next step, and progression once in the system (confirmed 2026-08-18)
- A **provider-facing ordering UI existed only in Medmo's earliest days** and is no longer the intake path; do not claim ongoing ownership of a clinician-facing order-entry front end (confirmed 2026-08-18)
- **Voice-of-customer reached product through client success and sales**, not direct discovery with referring clinicians. Do not claim clinician-facing user research or site visits; the honest adjacent claim is discovery with clinical operators and practice administrators (confirmed 2026-08-18)
- *Mirrored from MASTER-RESUME-REFERENCE §5 on 2026-09-23 (Alpaca Health build), so these are grounded for the audit:* owned product for Medmo's multi-sided marketplace connecting patients, imaging providers, and insurers, navigating insurance eligibility, in-network coverage, and prior authorization end to end; the product operating system spanned engineering, design, and QA (roadmap, sprint cadences, QA gates, release playbooks); hired, managed, and developed a **2-person PM team**, shifting from decision-maker to coach (unblocking rather than deciding); the three 0→1 platforms were built in React, Node.js, TypeScript on MySQL schemas; A/B tests covered scheduling flows, provider matching, and funnel conversion
- **Cost-per-scan −20% attribution conflict (unresolved):** the Key Metrics table below ties it to the auto-advance flow; MASTER §5 attributes it to a blend of AI voice agents, automation, and outsourced staffing. Drafts use the neutral "one of several levers" until Alex settles it

### Engineering & Architecture Advisor - Laurel Health & radEmploy (2024 - Present)
New York, NY
- Advising two early-stage VC-backed healthcare companies on HIPAA-compliant system architecture, engineering process, and product strategy at PMF stage

### Technical Architect | Senior Information Technology Engineer - New York-Presbyterian Hospital (2017 - 2021)
New York, NY
- Directed a $1B Epic EHR integration across 12 systems with a 25-person cross-functional team; drove alignment across clinical, engineering, legal, compliance, and operations. Top 5% performance org-wide
- Accelerated the COVID-19 go-live by one month — re-sequenced the critical path and consolidated 500+ clinical interfaces to ~100 (80%) via a 48-hour clinical-safety triage and a critical-path-only sprint; zero patient-safety incidents from deferred work (per MASTER §5 ⭐#4)
- Reengineered clinical workflows for radiation oncology and cardiology, supporting centralized access to clinical data across service lines (per MASTER §5)
- Owned registration, eligibility, coverage, and HB/PB billing interface integration; the HB/PB interfaces carried the actual charge information as HL7 **DFT** (detailed financial transaction) messages (confirmed 2026-09-15). This is interface-level exposure to charge flow — not ownership of charge capture as an operation
- **ARIA radiation oncology integration** (stated by Alex 2026-09-24, UiPath Colleen mock). ARIA controls the treatment machines (treatment location and dose), so Epic could not replace it. Epic sent patient demographic and clinical data to ARIA; ARIA sent back treatment data and per-visit billing as HL7 DFT messages. Alex built, configured, and mapped the HL7 messages; coordinated the Epic Patient Access, Orders, and Billing teams on the end-to-end workflow with department leadership; and was the main point of contact to radiation oncology leadership for status, build validation, and the go-live plan. Kicked off with a **"Directional" session** with radiation oncology physicians, clinicians, and administrative leaders from all hospital locations to lock decisions that are hard to change later (e.g., core order sets used everywhere with no customization; an agreed monthly billing period). Go-lives were phased by hospital, with per-hospital working sessions. **Lesson:** he started strict on identical workflows across hospitals; the second hospital was inpatient-heavy vs. the first's outpatient mix, so he changed the method. Directional decisions became the line, and changing one required every leadership party to realign. For anything else: understand what's driving the request, offer the standard workflow first, build site-specific only if needed. The inpatient-heavy hospital sent ARIA a different billing ID and went out through a different claim route. *Still to confirm:* number of hospitals and phases; what the billing ID was; the two claim routes; why monthly; whether any FHIR was involved at NYP (say HL7 unless confirmed); the result.
- **Post-go-live exception handling for the ARIA DFT interface** (stated 2026-09-24): an interface error work queue caught messages the system couldn't process. In the first weeks the dominant error was **unmapped billing codes**, a billing configuration gap, so Alex went to his Epic billing team counterpart and they set a routing rule sending those errors directly to the billing team's own work queue. The integration team kept true interface faults (e.g., invalid message type), which went to the vendor. *Still to confirm:* whether charge reconciliation existed and who owned it; why testing didn't catch the unmapped codes; error volumes; whether Alex proposed the routing rule.

### Application Consultant - Oracle Cerner (2015 - 2017)
Brooklyn, NY
- Delivered an EHR to HIMSS Level 7; led roadmaps for 140+ HL7 interfaces and 180+ medical device integrations at 10,000+ messages/day and 99.9% uptime
- Cut manual clinical documentation time 70% through device integration and documentation workflow redesign (per MASTER §5)
- The delivery pattern standardized across engagements was for **medical device integration**, applicable to any device (confirmed 2026-09-15; the pattern's specific steps are not yet recorded)

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
Epic, Cerner Millennium, Allscripts, ARIA Radiation Oncology, HL7 v2 (ADT, ORM/ORU, DFT charges, HB/PB billing), FHIR R4, HIPAA/SOC 2

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
| Prior-auth auto-advance (auth-not-required cases) | ~20% of pipeline cleared past ~3-day wait; cost-per-scan −20% |

## Publications
*(none on file)*

## Awards
*(none on file)*

## References
*(none on file — `documents/references/` is empty)*

More references available upon request.
