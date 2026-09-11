# Template: arial-letter

- **Type:** Cover letter
- **Source extension:** .docx
- **Engine/toolchain:** LibreOffice headless (`soffice`) — Office Open XML, not LaTeX
- **Page limit:** 1 page (hard rule)
- **Fonts:** Arial throughout (system font — must be installed)
- **Class/packages:** none — plain OOXML; styling lives in `word/styles.xml` inside `template.docx`

## Compile command

    cd <output dir> && soffice --headless --convert-to pdf --outdir . <file>.docx

On macOS use `/Applications/LibreOffice.app/Contents/MacOS/soffice` if `soffice` is not on `PATH`.

## How to fill it

Same mechanic as the CV template: unpack, rewrite the text runs in `word/document.xml`,
repack. Use `fill_template.py` in this folder. Never rebuild with a docx generator.

### Token inventory

| Token | Meaning |
|---|---|
| `YOUR_NAME`, `YOUR_EMAIL`, `YOUR_PHONE`, `YOUR_LINKEDIN_URL`, `YOUR_LOCATION` | Header block |
| `DATE` | Letter date, written out (e.g. "August 17, 2026") |
| `RECIPIENT_LINE` | e.g. "Hiring Team, Product" |
| `COMPANY_NAME` | Company on its own line under the recipient |
| `SALUTATION` | e.g. "Dear <Company> Product Team," — named person when the posting gives one |
| `PARA_1_HOOK` | Opening: name the specific surface this role owns and why it matters |
| `PARA_2_EVIDENCE` | Concrete build: system, metric, constraint |
| `PARA_3_AI_HONESTY` | What shipped in production vs. prototyped only — stated, never blurred |
| `PARA_4_LEVEL_OR_MOTIVATION` | Answers the unspoken objection (level optics, or why this company) |
| `PARA_5_GAP` | Honest gap, then the adjacent thing that has been owned |
| `CLOSING`, `YOUR_NAME_SIGNATURE` | Sign-off |

## Style rules

- **Five body paragraphs, in this order.** The structure is the argument: hook → evidence →
  AI precision → the unspoken objection → the honest gap. Extracted from the Garner Employer
  Experience letter, which is the most developed example in the archive.
- **Paragraph 3 is non-negotiable on any AI role.** State production scope (voice agents that
  take actions, OCR) against prototyped-only scope (LLM/retrieval). Precision over impressiveness.
- **Paragraph 4 pre-empts, never defends.** On an IC req below Director, answer "why is a
  Director applying down" before the reader asks it. On a VP req, reframe as level-me-on-evidence.
- **Paragraph 5 names the gap first, then the adjacent owned thing.** Never the reverse, and
  never dress the gap up.
- Reference **Claude Code** by name wherever AI-assisted development comes up.

## Known pitfalls

- XML-escape all replacement values; an unescaped `&` corrupts the document. `fill_template.py`
  handles this.
- Paragraph length drives page fit. Five paragraphs at roughly 4-6 lines each fills one page;
  much beyond that spills to page 2. Trim the lowest-relevance paragraph rather than shrinking
  type or margins.
- LibreOffice prints `Task policy set failed` on stderr on macOS — noise, not failure.
