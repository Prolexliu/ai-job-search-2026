# Search Queries for Job Scraper

<!-- SETUP: Customize these queries based on your skills, target roles, and location -->

## Installed portal CLIs (primary for `/scrape`)

`/scrape` discovers every portal skill under `.agents/skills/*/SKILL.md` and runs its CLI first. Shipped country-agnostic CLIs include `linkedin-search` and `freehire-search`; Danish demos and any skill you add with `/add-portal` are included the same way. You do **not** need a matching `site:` line below for those CLIs to run.

The `site:` query templates in this file are the **WebSearch fallback** — for portals without a CLI, company career pages, or when a CLI fails.

**Language scope:** write every query category in every language listed in your CLAUDE.md Languages table (typically 1-2, sometimes more). A posting requiring a language you have *not* declared, as a job condition, is excluded before scoring; a posting requiring a *higher level* than you declared in a language you *do* work in is flagged for your own judgment, not excluded — see `04-job-evaluation.md`'s Language Gate, the single source of truth for this rule. Translate each category's keywords rather than machine-translating word-for-word (e.g. "Frontend Developer" -> "Desarrollador Frontend", not a literal word-for-word translation) if you work in more than one language.

## Search Sites

Primary (your market's job boards - scaffold one with `/add-portal`):
- **builtinnyc.com** - Built In NYC, the highest-yield general board in the archive (7 sourced applications)
- **linkedin.com/jobs** - LinkedIn job listings (filter: United States / New York, NY, and Remote); also covered by the `linkedin-search` CLI
- **greenhouse.io / ashbyhq.com / lever.co** - the ATS platforms most target companies post on directly; often the only place a req is genuinely live
- **freehire.me** - tech aggregator, covered by the `freehire-search` CLI (multi-market, structured results)

Secondary (company career pages via Google):
- Direct Google searches with `site:` filters for known target companies

## Query Categories

Queries are grouped by priority. Write **each category in every language from your Languages table** (see Language scope above). Combine each query with your location terms (e.g. your city, region, or metro area) where the site supports it.

**Organize by function, not job title.** The same underlying work carries different titles across companies and markets (a "Data Scientist" role at one employer may be posted as "Insights Analyst" or "Data Consultant" at another). Name each priority category after the function it covers, and list several plausible job titles as query variants within that category rather than betting an entire priority tier on one exact title string.

### Priority 1: Healthcare product leadership (AI-native and platform)

Strongest and most desired direction. All three past interviews came from **leadership-scope**
roles — weight this tier highest.

```
site:linkedin.com/jobs "Director of Product" healthcare AI "New York"
site:linkedin.com/jobs "VP of Product" healthcare "New York" OR remote
site:linkedin.com/jobs "Head of Product" health OR clinical "New York"
site:linkedin.com/jobs "Group Product Manager" healthcare "New York"
site:linkedin.com/jobs "Principal Product Manager" health AI remote
site:greenhouse.io OR site:ashbyhq.com "Director, Product" healthcare AI
```

### Priority 2: Healthcare domain — EHR, interoperability, revenue cycle

Domain expertise where Alex is strongest and least substitutable.

```
site:linkedin.com/jobs Epic OR "EHR integration" product manager "New York"
site:linkedin.com/jobs HL7 OR FHIR OR interoperability product "New York" OR remote
site:linkedin.com/jobs "revenue cycle" OR "prior authorization" product manager remote
site:linkedin.com/jobs "clinical workflow" product manager "New York"
site:linkedin.com/jobs "health system" OR payer product manager "New York"
```

### Priority 3: Forward-deployed / applied AI (frontier-AI companies)

Adjacent direction with real traction in the archive — Anthropic ×4, OpenAI ×2, Microsoft AI ×3.

```
site:linkedin.com/jobs "forward deployed" engineer OR "solutions architect" "New York"
site:linkedin.com/jobs "applied AI" architect OR engineer healthcare "New York" OR remote
site:linkedin.com/jobs "technical program manager" AI "New York"
site:linkedin.com/jobs "deployment strategist" OR "solutions engineer" health remote
```

### Priority 4: Engineering leadership

Wider net. Uses the technical-depth-plus-healthcare combination as the differentiator.

```
site:linkedin.com/jobs "Head of Engineering" OR "Director of Engineering" health "New York"
site:linkedin.com/jobs "Engineering Manager" healthcare AI "New York"
site:linkedin.com/jobs "Senior Engineering Manager" health remote
```

### Channel weighting (from `04-job-evaluation.md` calibration)

All three interviews to date came through **recruiters**; zero came from ~45 cold applications.
Treat recruiter-sourced and referral-sourced roles as materially higher-yield, and flag when a
scrape run surfaces only cold ATS listings.

## Location Filter

**Relocation is a hard FAIL** — it is the single most common reason past applications were
withdrawn (AWS, Hippocratic AI, Commure, Microsoft AI RAMP/Redmond, Assort Health/SF). Apply this
filter *before* investing in a fit evaluation.

- **Ideal:** New York, NY — Manhattan, Brooklyn, Queens; NYC hybrid or on-site
- **Acceptable:** Fully remote (US); remote-first with occasional NYC or travel
- **Borderline:** Northern New Jersey / Westchester / Long Island (commutable, confirm cadence)
- **Too far — auto-exclude:** Anywhere requiring relocation. San Francisco Bay Area, Seattle/Redmond, California generally, and any "on-site in <other metro>" req, regardless of fit strength.

## Language Filter

Your working languages and levels are in CLAUDE.md's Languages table. When filtering scraped results, apply `04-job-evaluation.md`'s Language Gate: a posting requiring a language you haven't declared at all is excluded; a posting requiring a higher level than you declared in a language you do work in is not excluded, flag it clearly instead (see `job-scraper/SKILL.md`'s Step 3 "Quick Fit Assessment" for how the flag surfaces in `/scrape` output). Postings simply *written* in a language you don't work in, that don't require it on the job, are fine.

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- "/scrape [focus_area]" -> relevant category queries + custom focus-specific queries
