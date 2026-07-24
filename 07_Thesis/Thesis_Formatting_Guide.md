# Superior University Thesis Formatting Guide

Official formatting standard for this thesis project and all future work — Chapters 1–5,
research papers, journal/conference submissions, progress reports, and presentations.

**Basis:** *MS/M.Phil Thesis Template and Thesis Writing Guidelines — Version 1* (Directorate of
Postgraduate Studies, Superior University). Where a house preference deviates from the DOPS
template it is flagged **[house]**; everything else is **[DOPS]** and mandatory for submission.

The `.docx` is generated programmatically by
[Compiled/build_thesis_docx.py](Compiled/build_thesis_docx.py); treat that script as the
executable form of this guide.

---

## 1. Document Settings

| Setting | Value |
|---------|-------|
| Paper size | A4 — 8.27″ × 11.69″ (21 × 29.7 cm) **[DOPS]** |
| Orientation | Portrait |
| Margins | 1″ top / bottom / right; **1.25″ left** (binding) **[DOPS]** |
| Font | Times New Roman throughout **[DOPS]** |
| Body size | 12 pt, black |
| Line spacing | 1.5 **[DOPS]** |
| Paragraph spacing | 6 pt after; 0 pt before (12 pt before headings) |
| Body alignment | Justified |
| First-line indent | 0.5″ on chapter body paragraphs **[house]**; front matter non-indented |
| Header | None **[DOPS]** |
| Footer | Page number only |

---

## 2. Cover / Title Page Formatting

Order top-to-bottom, all centered:

| Element | Font / size | Case / weight |
|---------|-------------|---------------|
| Thesis title | TNR 16 pt | Capitalize Each Word, **not bold** |
| University logo | — | **5 cm wide × 7.43 cm tall**, centered, undistorted |
| Purpose statement ("A Thesis submitted in partial fulfillment / of the requirements for the degree of") | TNR 12 pt | Sentence case |
| Degree name (`MASTER OF SCIENCE` / `IN` / `ARTIFICIAL INTELLIGENCE`) | TNR 14 pt | ALL CAPS |
| "Submitted By" | TNR 12 pt | — |
| Student name | TNR 14 pt | Capitalize Each Word, **not bold** |
| Roll number | TNR 14 pt | immediately below name |
| Session (`Session: 2025-2026`) | TNR 12 pt | not bold |
| "Supervised By" | TNR 12 pt | — |
| Supervisor name | TNR 14 pt | **not bold** |
| Department / Faculty / University | TNR 14 pt | ALL CAPS |

**Logo asset:** [Images/superior_logo_vertical.png](Images/superior_logo_vertical.png), regenerated
by [Images/make_vertical_logo.py](Images/make_vertical_logo.py). Vertical lockup (icon over
single-line wordmark), official purple `RGB(112, 26, 115)`. The PNG is pre-padded to a 5:7.43
aspect ratio so the 5 cm × 7.43 cm placement never stretches the artwork.

> **Print note [DOPS]:** final hard-bound copies use **black** binding with **golden** title-page
> text; the spine carries Degree (MS Thesis), Student Name, and Session.

---

## 3. Heading Hierarchy

| Level | Example | Format | Alignment |
|-------|---------|--------|-----------|
| Chapter title | `CHAPTER ONE` / `INTRODUCTION` | TNR 16 pt **bold**, ALL CAPS, two lines | Centered |
| Section (`x.y`) | `1.1 Background` | TNR **14 pt bold** **[house]** | Left |
| Subsection (`x.y.z`) | `1.1.1 Artificial Intelligence` | TNR **12 pt bold** | Left |
| Sub-subsection (`x.y.z.w`) | `1.1.1.1 …` | TNR **12 pt bold italic** **[house]** | Left |
| Body | — | TNR 12 pt, justified, 1.5 | Justified |

> **[DOPS] baseline:** the template specifies *all* section headings at 12 pt bold. The 14 pt L1
> and italic L3 above are a house refinement for readability — switch to uniform 12 pt bold if the
> FRB requires strict template compliance.

Every chapter's **first paragraph** must overview the whole chapter (what it covers, contents,
structure) **[DOPS]**. Start each chapter on a new page. Headings use `keep_with_next` to avoid
orphaning at page bottoms.

---

## 4. Page Numbering

| Section | Format | Start | Position |
|---------|--------|-------|----------|
| Title page | none | — | — |
| Front matter (Author's Declaration → Abbreviations) | Upper-case Roman `I, II, III…` **[DOPS]** | I at Author's Declaration | bottom-right |
| Body (Abstract → Annexure) | Decimal `1, 2, 3…` **[DOPS]** | 1 at Abstract | bottom-right |

Implemented with **section breaks** and field codes (`PAGE`, `pgNumType`) — never typed manually.

---

## 5. Tables

- Caption **above** the table.
- Format: `Table 2.1` (label + number) then the caption; TNR 11 pt, centered **[house]**.
- Insert via **References → Insert Caption → label "Table"** so the List of Tables auto-builds.
- Consistent single-line borders; centered on the page.

---

## 6. Figures

- Caption **below** the figure.
- Format: `Figure 3.2` in italics + caption (non-italic), same line; TNR 11 pt, centered **[house]**.
- Insert via **References → Insert Caption → label "Figure"**.
- Every figure centered; high-resolution vector/PNG (see §13).

---

## 7. Table of Contents

- **Automatic** — Word `TOC \o "1-3"` field; collects outline levels 0–2.
- Never typed by hand. Update with `Ctrl+A` → `F9` → *Update entire table*.
- Chapters appear as top-level entries; `x.y` / `x.y.z` sections nest beneath.

---

## 8. List of Figures

- **Automatic** — `TOC \c "Figure"` field, populated from Figure caption SEQ fields.
- Update with `F9`. Empty until captioned figures are inserted.

---

## 9. List of Tables

- **Automatic** — `TOC \c "Table"` field, populated from Table caption SEQ fields.
- Update with `F9`.

---

## 10. Citations & References

- **This thesis: IEEE** (permitted by DOPS for Computer Science). In-text `[n]` numbered by order
  of first appearance; reference list in citation order; hanging indent 0.5″.
- **DOPS default elsewhere: APA 7th** — alphabetical by author, hanging indent 0.5″.

APA 7 examples (for non-CS work):

```
Journal:    Author, A. A., & Author, B. B. (Year). Title of article. Journal Name,
            Volume(Issue), pages. https://doi.org/xx.xxxx/xxxxx
Book:       Author, A. A. (Year). Title of work: Capital letter for subtitle. Publisher.
Conference: Author, A. A. (Year). Title of paper. In Proceedings Name (pp. xx–xx). Publisher.
```

- Always include a **DOI** as `https://doi.org/...` when available.
- Never modify citation content when reformatting — style only.

---

## 11. Appendix / Annexure Formatting

- Placed at the very end, after References **[DOPS]**.
- Heading `ANNEXURE` / `APPENDIX A` — centered, 16 pt bold, ALL CAPS.
- Appendix figures/tables numbered `Figure A.1`, `Table A.1` (letter = appendix).
- Same font, spacing, and caption rules as the main body.

---

## 12. Academic Writing Standards

- Formal academic English; objective, third-person tone.
- Human-written style — avoid AI-tell patterns and repetitive sentence openings.
- Clear and concise; no unnecessary verbosity or filler.
- Consistent terminology (define each acronym once, in parentheses, on first use; then reuse).
- Do not abbreviate a term used 3 or fewer times **[DOPS]**.
- Past tense for methods/results; active voice preferred **[DOPS]**.
- Every borrowed idea cited — plagiarism is a zero-tolerance offense **[DOPS]**.

---

## 13. Figure Design Standards

For all thesis diagrams:

- White background.
- IEEE / Springer academic style.
- Blue-and-gray academic palette.
- Rounded rectangles; consistent typography (match body font family).
- High-resolution **vector** graphics (SVG/PDF) exported to PNG ≥ 300 dpi.
- Minimal icons; clean, generous spacing.

---

## 14. Presentation Design Standards

For defense and conference decks:

- White theme, minimalist layout, consistent across slides.
- Superior University brand colors:
  - Primary Red `#D72924`
  - Secondary Coral `#CB725E`
  - Accent Purple `#6C1C74`
- Large readable fonts; limited text per slide.
- Professional icons and high-quality diagrams (reuse thesis figures).
- Suited to thesis defense and research conferences.

---

## 15. Final Submission Checklist

- [ ] Cover page complete (title, logo, degree, name, roll, session, supervisor, dept/faculty/university)
- [ ] Logo dimensions 5 cm × 7.43 cm, undistorted
- [ ] Times New Roman throughout; body 12 pt
- [ ] Margins 1″ / 1.25″ left; A4 portrait
- [ ] 1.5 line spacing; justified body; 0.5″ first-line indent
- [ ] Heading hierarchy correct (16 / 14 / 12 / 12-italic)
- [ ] Table of Contents updated (`F9`)
- [ ] List of Figures updated
- [ ] List of Tables updated
- [ ] Front matter in upper-case Roman numerals (I at Author's Declaration)
- [ ] Body in decimal numerals (1 at Abstract)
- [ ] References formatted (IEEE for CS) — count matches in-text citations
- [ ] Figure numbering + captions below
- [ ] Table numbering + captions above
- [ ] Appendix/Annexure placed last
- [ ] Formatting consistency swept (fonts, sizes, spacing, indentation, no stray manual formatting)
- [ ] Ready for plagiarism checking (SIRC certificate)
- [ ] Ready for final submission (four black hard-bound copies, golden title text)
