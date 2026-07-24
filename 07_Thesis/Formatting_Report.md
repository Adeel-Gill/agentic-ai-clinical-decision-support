# Formatting Report — Thesis_Ch1_Ch2.docx

**Date:** 2026-07-24
**Source of truth:** *MS/M.Phil Thesis Template and Thesis Writing Guidelines — Version 1* (DOPS, Superior University)
**Build script:** [07_Thesis/Compiled/build_thesis_docx.py](Compiled/build_thesis_docx.py)
**Output:** [07_Thesis/Thesis_Ch1_Ch2.docx](Thesis_Ch1_Ch2.docx)

> No research content was rewritten or paraphrased. All changes below are formatting, structure, styles, numbering, and layout only.

---

## 1. Decisions on brief-vs-template conflicts

Three items in the request conflicted with the official DOPS template. Resolved with the user:

| # | Item | Brief said | Template said | **Decision** |
|---|------|-----------|---------------|--------------|
| 1 | References | APA 7th, alphabetical | APA by default, **IEEE permitted for Computer Science** | **Keep IEEE numbered** (this is a CS/AI thesis; IEEE already fully wired into both chapters). |
| 2 | Heading sizes & indent | L1 = 14 pt; 0.5″ first-line indent | All section headings 12 pt bold; block (no indent) | **Follow the brief** — L1 = 14 pt bold, L2 = 12 pt bold, L3 = 12 pt bold-italic; 0.5″ first-line indent on chapter body paragraphs. |
| 3 | Title-page dept/faculty | Faculty of Computing / Dept of AI | — | **Keep current values** (Dept of Computer Science / Faculty of CS & IT). |

---

## 2. Changes performed

### 2.1 Title page
- **Logo replaced.** The bracketed placeholder text was replaced with the embedded vertical Superior University logo, centered.
- Logo generated fresh as a **vertical/stacked lockup** (network icon on top, single-line "SUPERIOR UNIVERSITY" wordmark below in the official purple `RGB(112,26,115)`, Times New Roman) — matching the template cover, not the horizontal asset. Generator: [Images/make_vertical_logo.py](Images/make_vertical_logo.py); asset: [Images/superior_logo_vertical.png](Images/superior_logo_vertical.png).
- Logo sized to **5 cm × 7.43 cm** exactly (verified in the output XML). The PNG is pre-padded to the same 5:7.43 aspect ratio, so both dimensions are fixed **without distortion**.
- Main title: Times New Roman, **16 pt, not bold, Capitalize Each Word, centered** (unchanged — already compliant).
- Degree block (14 pt, ALL CAPS), student name (14 pt, not bold), roll number, session, supervisor (14 pt, not bold), and department/faculty/university (14 pt, ALL CAPS) — all confirmed against template.
- **Session updated** to `2025-2026`.

### 2.2 Headings
- **Chapter titles** — two centered ALL-CAPS 16 pt bold lines (`CHAPTER ONE` / `INTRODUCTION`); unchanged, compliant.
- **Section headings now leveled** (previously all 12 pt bold):
  - `## x.y` → **14 pt bold**
  - `### x.y.z` → **12 pt bold**
  - `#### x.y.z.w` → **12 pt bold italic**
- All section headings left-aligned; `keep_with_next` set to prevent **orphan headings** at page bottoms.

### 2.3 Body text
- Times New Roman 12 pt, justified, 1.5 line spacing (unchanged).
- **0.5″ first-line indent** added to chapter body paragraphs. Front matter (abstract, acknowledgements, declarations, certificates) intentionally left non-indented per template convention.

### 2.4 Automatic fields (TOC & lists)
- All headings and front-matter titles now carry **Word outline levels** (chapters/front-matter = level 0, `x.y` = level 1, `x.y.z` = level 2), so the **Table of Contents field auto-populates** with correct hierarchy. Previously the TOC field would have returned nothing because headings used direct formatting, not Heading styles.
- **List of Figures** and **List of Tables** converted from static placeholder text to real `TOC \c "Figure"` / `TOC \c "Table"` fields that populate from Word caption SEQ fields.
- The Table of Contents' own title is excluded from the TOC (no self-listing).

> **Action required in Word:** open the document, select all (`Ctrl+A`), press `F9`, choose *Update entire table* to render the TOC / lists. (Fields ship with a placeholder prompt until updated.)

### 2.5 References
- IEEE style retained: `[key]` → `[n]` numbered by order of first appearance; only cited works emitted, in citation order.
- Hanging indent (0.5″) confirmed. **34 references** emitted.

### 2.6 Document-wide settings (verified, unchanged)
- A4 (8.27″ × 11.69″), portrait; margins 1″ all sides except **left 1.25″**.
- Three sections: title page (unnumbered) → front matter (**upper-case Roman**, I, II, …) → body (**decimal**, restart at 1), page number bottom-right.

---

## 3. Verification (automated checks on the built file)

| Check | Result |
|-------|--------|
| Logo dimensions | 5.0 cm × 7.43 cm ✓ |
| L1 section heading size/weight | 14 pt, bold ✓ |
| Body first-line indent | 0.5″ ✓ |
| Outline levels present | L0 ×13, L1 ×20, L2 ×13 ✓ |
| References count | 34 ✓ |
| Build | No errors ✓ |

---

## 4. Open items for the student before submission

1. **Update fields in Word** (`Ctrl+A` → `F9`) to render TOC, List of Figures, List of Tables.
2. Fill the remaining bracketed placeholders (dedication text, acknowledgements, examiner names, dates, signatures).
3. Insert real figures/tables using **References → Insert Caption** (label `Figure` / `Table`) so the lists populate.
4. Confirm **degree/subject/session** fields once more against the enrollment letter.
5. Confirm **IEEE vs APA** with the supervisor if the FRB requires APA (a switch is a separate task).
6. Run the plagiarism check (SIRC) as required by DOPS.
