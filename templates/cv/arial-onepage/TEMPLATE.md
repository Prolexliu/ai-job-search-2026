# Template: arial-onepage

- **Type:** CV
- **Source extension:** .docx
- **Engine/toolchain:** LibreOffice headless (`soffice`) — Office Open XML, not LaTeX
- **Page limit:** 1 page (hard rule)
- **Fonts:** Arial throughout (system font — must be installed; present by default on macOS and Windows)
- **Class/packages:** none — plain OOXML. Styling lives in `word/styles.xml` inside `template.docx`.

## Compile command

    cd <output dir> && soffice --headless --convert-to pdf --outdir . <file>.docx

On macOS `soffice` is at `/Applications/LibreOffice.app/Contents/MacOS/soffice`; use the
full path if it is not on `PATH`.

## Format spec (locked)

| Element | Spec |
|---|---|
| Page | US Letter, 1 page (hard rule) |
| Font | Arial throughout |
| Name | 18 pt, bold, centered |
| Section headers | 11 pt, bold, centered, horizontal rule above |
| Body / bullets | 9 pt |
| Margins | 0.3" top · 0.3" bottom · 0.5" left/right |
| Dates | right-aligned on the job-title line, tab stop at 9026 twips |

## How to fill it

`template.docx` carries `[TOKEN]` placeholders in its text runs. Fill them with the
helper in this folder, which unpacks the docx, rewrites the text runs in
`word/document.xml`, and repacks:

    python3 -c "import sys; sys.path.insert(0,'templates/cv/arial-onepage'); \
      from fill_template import fill; \
      fill('templates/cv/arial-onepage/template.docx', 'cv/main_<company>_<role>.docx', VALUES)"

`VALUES` is a dict of token name (no brackets) to replacement string.

### Token inventory

| Token | Meaning |
|---|---|
| `YOUR_NAME`, `YOUR_EMAIL`, `YOUR_PHONE`, `YOUR_LINKEDIN_URL`, `YOUR_LOCATION` | Contact header |
| `PROFILE_STATEMENT` | Career summary paragraph |
| `COMPANY_<n>`, `CITY_STATE_<n>`, `JOB_TITLE_<n>`, `DATES_<n>` | Roles 1–5, most recent first |
| `ROLE_<n>_BULLET_<m>_LEAD` | Bold lead-in phrase, rendered before the colon |
| `ROLE_<n>_BULLET_<m>_TEXT` | Bullet body |
| `INSTITUTION_<n>`, `DEGREE_<n>`, `EDU_LOCATION_<n>`, `YEARS_<n>` | Education entries 1–2 |
| `LANGUAGES`, `PRODUCT_AND_AI_SKILLS`, `ENGINEERING_AND_ARCHITECTURE_SKILLS`, `TECHNICAL_STACK`, `DOMAIN_SYSTEMS`, `VOLUNTEER_LINE` | Additional Information block |

Bullet slots per role, as the skeleton ships: role 1 has 5, role 2 has 1, role 3
has 2, role 4 has 1, role 5 has 1. Adding a bullet means duplicating its `<w:p>`
element in `word/document.xml`, not appending text to an existing run.

## Style rules

- **Select, don't rewrite.** Bullets are chosen from the candidate profile to match the
  posting's emphasis; 4–6 per recent role. A resume wins on selection, not volume.
- **Resequence the Additional Information lines by relevance to the posting** on every
  build — most relevant category first. This is a required step, not a polish pass.
- **Never remove the location from the contact line** to win space. A contact line with a
  non-local area code and no city reads as an out-of-area candidate and is a silent
  screen-out on in-office reqs.
- Space-saving levers, in order: collapse a two-title role to one line, drop the oldest
  role, drop the Volunteer line, trim older roles to 4 bullets.
- Bold lead-in on every bullet, followed by a colon and the body text in regular weight.

## Known pitfalls

- **Never rebuild this file with `python-docx`, `docx-js`, or any generator.** It breaks
  the approved formatting. The only supported mechanic is unpack → edit text runs in
  `word/document.xml` → repack, which is what `fill_template.py` does.
- **XML-escape replacement values.** An unescaped `&`, `<`, or `>` corrupts the document
  and LibreOffice will fail to open it. `fill_template.py` handles this.
- **Education location tokens are separate from experience location tokens**
  (`EDU_LOCATION_<n>` vs `CITY_STATE_<n>`). They looked interchangeable during
  registration and were not — reusing one for the other silently prints the wrong city.
- LibreOffice emits `Task policy set failed` on stderr on macOS. It is noise, not a
  failure; check the exit code and the output PDF instead.
- The first `soffice` run after install can take ~20 s while it builds its profile.
