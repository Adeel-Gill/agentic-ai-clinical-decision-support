# Presentation Design Guide
### The Superior University — MS Artificial Intelligence Presentation Design System

**Version 1.0** · Single source of truth for all thesis, IEEE conference, and research presentations.

> *An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support*
> Faculty of Computer Science & Information Technology · The Superior University, Lahore

---

## 0 · How to Use This Guide

This document defines a **complete, reusable design system** — not a single deck. Every presentation you build from now on inherits from it, so that a supervisor, committee, external examiner, or IEEE audience immediately recognises the work as *yours* and as *Superior University's*, without loud branding.

The system targets the aesthetic intersection of:

| Reference | What we borrow |
|---|---|
| **Apple Keynote** | Radical whitespace, one idea per slide, restraint |
| **Microsoft Build** | Clear content hierarchy, confident type |
| **Google DeepMind** | Calm scientific tone, structured diagrams |
| **Nature** | Figure discipline, captions, citation rigor |
| **IEEE Conference** | Density done cleanly, credibility, no gimmicks |

**Golden rule:** *When in doubt, remove something.* Whitespace is the primary design element, not a leftover.

---

## 1 · Design Principles

Ten principles govern every decision. If a slide violates one, redesign the slide — not the principle.

1. **Clarity over decoration.** Every mark on the slide must carry meaning. Decoration that carries no information is deleted.
2. **One idea per slide.** A slide answers exactly one question. If it answers two, it becomes two slides.
3. **Whitespace is structural.** A minimum of ~40% of every content slide is empty space. Crowding reads as amateur.
4. **Restraint in colour.** White is the canvas. Red is a scalpel, not a paintbrush. Purple appears only to highlight.
5. **Type is the interface.** Hierarchy is created by size, weight, and space — never by boxes, shadows, or colour alone.
6. **Consistency is credibility.** The same element looks identical on slide 3 and slide 33. The 8-point grid enforces this.
7. **Academic, not corporate.** No stock photos of handshakes, no 3D charts, no swooshes, no motivational gradients.
8. **Evidence-forward.** Claims are paired with citations, figures with captions, numbers with units and sources.
9. **Colour-independent meaning.** Never rely on colour alone to communicate. Pair it with a label, icon, or position.
10. **Design for the back row.** If the smallest text is unreadable from 10 metres, it is too small — or it does not belong on the slide.

**Anti-goals (never do these):** default PowerPoint templates · WordArt · clip art · emojis · saturated colour blocks · drop-shadowed text · dark themes on content slides · animated bullet reveals with motion paths · more than 6 lines of text on a slide.

---

## 2 · Colour System

### 2.1 Official Palette

Superior University brand colours, extended with a neutral and semantic scale for academic use.

| Role | Name | HEX | RGB | Usage |
|---|---|---|---|---|
| **Primary Accent** | Superior Red | `#D72924` | 215, 41, 36 | Table headers, accent bars, key emphasis, section numbers |
| **Secondary Accent** | Rose | `#CB725E` | 203, 114, 94 | Secondary data, supporting elements, subtle fills |
| **Highlight** | Purple | `#6C1C74` | 108, 28, 116 | Highlights only — a single word, a key metric, a callout |
| **Background** | Pure White | `#FFFFFF` | 255, 255, 255 | Primary background of all content slides |
| **Primary Text** | Almost Black | `#222222` | 34, 34, 34 | Titles and body text |
| **Secondary Text** | Slate | `#555555` | 85, 85, 85 | Captions, sub-labels, secondary body |
| **Surface** | Light Gray | `#F5F5F5` | 245, 245, 245 | Card fills, alternating table rows, figure backgrounds |
| **Border** | Hairline | `#EAEAEA` | 234, 234, 234 | Dividers, card outlines, table separators |
| **Success** | Muted Green | `#3F8A5B` | 63, 138, 91 | Positive results, "approve", improvements |
| **Warning** | Muted Orange | `#C8781E` | 200, 120, 30 | Caution, limitations, "modify" |
| **Dark Canvas** | Ink | `#1A1113` | 26, 17, 19 | *Optional* title / section slides only |

### 2.2 Colour Usage Rules

- **60 / 30 / 10 rule.** ~60% white, ~30% neutral text & light-gray surfaces, ~10% brand colour. Never invert this.
- **Red is punctuation.** Use it for the accent bar, the table header, and *one* emphasis per slide — not as a fill behind large areas.
- **Purple is the highlight pen.** It marks the single most important word, number, or node on a slide. If everything is purple, nothing is.
- **Rose is the "second voice."** Use it for the secondary series in a chart, supporting cards, or the "before" state in a comparison.
- **No gradients, no glows, no transparency tricks.** Flat fills only.
- **Semantic colours are muted by design.** Success/warning never appear at full saturation; they must sit calmly beside brand red.
- **Dark backgrounds** are permitted *only* on the title slide and section dividers, and even then are optional. Content is always dark-on-white.

### 2.3 Accessibility Contrast (WCAG 2.1)

All combinations below meet or exceed the stated level. Verify any new pairing before use.

| Foreground | Background | Ratio | Level |
|---|---|---|---|
| `#222222` on `#FFFFFF` | 15.9 : 1 | AAA (all text) |
| `#555555` on `#FFFFFF` | 7.5 : 1 | AAA (normal text) |
| `#FFFFFF` on `#D72924` | 4.6 : 1 | AA (large & UI text) — use ≥14 pt |
| `#FFFFFF` on `#6C1C74` | 9.9 : 1 | AAA |
| `#222222` on `#F5F5F5` | 14.4 : 1 | AAA |

> **Rule:** White text on Superior Red must be **≥ 14 pt and medium weight** to stay AA-compliant. Never place small red text on light-gray.

---

## 3 · Typography

### 3.1 Type Family

| Priority | Font | When |
|---|---|---|
| **Preferred** | **Aptos** | Default on Microsoft 365 (2024+). Modern, humanist, calm. |
| Alternative 1 | **Calibri** | Fallback where Aptos is unavailable. |
| Alternative 2 | **Segoe UI** | System fallback on Windows. |

Never substitute Times New Roman, Arial, or decorative fonts. Embed fonts in the `.pptx` (File → Options → Save → *Embed fonts in the file*) so the deck renders identically on the examiner's machine.

### 3.2 Type Scale & Hierarchy

| Element | Size | Weight | Colour | Notes |
|---|---|---|---|---|
| Slide Title | **36–40 pt** | Semibold / Medium | `#222222` | One line preferred; two lines max |
| Section Header (on divider) | **28 pt** | Medium | `#555555` | Subtitle under section number |
| On-slide sub-header | **24 pt** | Medium | `#222222` | Groups content within a slide |
| Body | **18–22 pt** | Regular / Medium | `#222222` | Max 6 lines per slide |
| Caption | **14–16 pt** | Regular | `#555555` | Figure & table captions |
| Footnote / Citation | **11–12 pt** | Regular | `#555555` | Footer, sources, references |

### 3.3 Typography Rules

- **Medium weight is the default.** Reserve **Semibold** for titles and the *single* emphasised word per slide. Never set whole paragraphs bold.
- **Never use ALL CAPS** for body text. Small-caps or Medium weight for the occasional label (e.g. section eyebrow) is fine.
- **Line spacing:** 1.15–1.25 for body, 1.0 for titles. Space *between* bullets (12–16 pt `space_after`) does the visual work — not blank bullet lines.
- **Line length:** aim for 45–75 characters per line. Constrain body text boxes to ~60% slide width when paired with a graphic.
- **Numerals:** use tabular/lining figures for tables and metrics so columns align.
- **No text shadows, outlines, reflections, or WordArt — ever.**
- **Punctuation:** use proper en/em dashes (–, —) and true quotation marks. Avoid trailing full stops on short bullet fragments (be consistent per deck).

---

## 4 · Layout & Grid

### 4.1 Canvas

- **Aspect ratio:** 16:9 — `13.333 in × 7.5 in` (33.87 cm × 19.05 cm).
- **Safe margins:** 0.7 in left/right, 0.6 in top/bottom on content slides. Nothing critical touches the edge except intentional accent bars.

### 4.2 The 8-Point Spacing System

All spacing, padding, and offsets are multiples of **8 pt** (≈ 0.083 in). This is non-negotiable — it is what makes the system feel engineered rather than assembled.

```
Spacing tokens:   4 · 8 · 16 · 24 · 32 · 48 · 64  (pt)
Card padding:     24 pt inner padding, minimum
Gap between cards: 24 pt
Title → body gap:  32–40 pt
Corner radius:     12 pt (cards) · 8 pt (chips/buttons) · 16 pt (large figure frames)
```

### 4.3 Column Grid

A 12-column grid with 24 pt gutters. Common spans:

- **Full bleed:** 12 cols
- **Content Left / Right:** text = 6 cols, graphic = 6 cols (with a 1-col gutter)
- **Two column:** 6 / 6
- **Three column:** 4 / 4 / 4
- **Sidebar + main:** 3 / 9

### 4.4 Vertical Rhythm (content slide anatomy)

```
┌────────────────────────────────────────────────────────┐
│ ▌ EYEBROW / SECTION LABEL              [ logo ]         │  ← 0.6 in top margin
│                                                          │
│ Slide Title (36–40 pt, #222)                             │  ← red accent bar to left
│ ──────────                                               │
│                                                          │
│   Content region (cards / text / figure)                │  ← 40%+ whitespace
│                                                          │
│                                                          │
│ ────────────────────────────────────────────────────── │  ← hairline #EAEAEA
│ Thesis short-title        Superior University       12  │  ← footer, 11 pt #555
└────────────────────────────────────────────────────────┘
```

### 4.5 Layout Rules

- **Left-align by default.** Centre only titles on the Title Slide and Section Dividers, and single large takeaways (Conclusion).
- **Optical alignment beats mathematical alignment** for the accent bar and logo — nudge until it *looks* aligned.
- **One focal point per slide.** The eye should know instantly where to land.
- **Never fill a slide to the edges** just because there is room. Empty space is the design.

---

## 5 · Master Layouts (Reusable Templates)

Fifteen master layouts. Each is a slide-master/layout you build once and reuse. Dimensions are given in inches for `python-pptx`.

### L1 · Title Slide
- **Optional dark canvas** (`#1A1113`) *or* white. Choose one and keep it consistent across a deck series.
- Centred university logo (top, ~3.6 in wide).
- Thin red accent bar (3 pt × 3 in) above the title.
- Title 32–36 pt Semibold, centred. Subtitle 16 pt.
- Meta block: Presenter · Degree · Supervisor · Faculty · University · Date.

### L2 · Agenda
- Minimal vertical or horizontal **timeline**: numbered nodes (01–05) connected by a hairline.
- Each node: number in Rose, label in `#222`, one-line descriptor in `#555`.
- No bullets, no boxes — just aligned type and a thin connecting line.

### L3 · Section Divider
- Large **section number** (e.g. `03`) in light `#F0F0F0` set huge (200 pt+) behind or beside a Medium-weight section title.
- Red accent bar. Optional dark canvas.
- Small subtitle giving the one-line purpose of the section.

### L4 · Content Left (text left · graphic right)
- Text: 6 cols left. Figure card: 6 cols right on `#F5F5F5` with 12 pt radius.

### L5 · Content Right (graphic left · text right)
- Mirror of L4. Alternate L4/L5 through a deck to create rhythm.

### L6 · Two Column
- 6 / 6. Use for compare/contrast, before/after, or definition/example.
- Optional thin vertical divider (`#EAEAEA`) between columns.

### L7 · Three Column
- 4 / 4 / 4 cards. Ideal for "three contributions", "three pillars", "three phases".

### L8 · Research Gap
- **Comparison table** (see §9) with a final highlighted column/row marking "The Gap" in Purple.
- Or a Venn / matrix of existing approaches vs. the missing intersection.

### L9 · Literature Review
- **Research-paper cards** in a 2×2 or 3-up grid. Each card: framework/paper name (Medium), one-line contribution (`#222`), one-line limitation (`#555`), citation chip.

### L10 · Architecture
- **Large centred figure** on a light frame, with a short (≤3 line) explanation beneath or to the side. The figure is the hero — minimise text.

### L11 · Methodology
- **Horizontal process flow**: 3–5 rounded-rectangle stages connected by consistent arrows. Phase label + one-line description in each.

### L12 · Timeline / Roadmap
- Horizontal spine with phase markers; optional Gantt-style bars. Muted colours; current/target phase marked in Red.

### L13 · Results
- **Metric cards** (see §7.3): 2–4 big numbers with labels, units, and deltas. One insight sentence below.

### L14 · Conclusion
- **Single large takeaway** sentence (28–32 pt), generous margins, one Purple-highlighted phrase. Optional 3 tiny supporting points beneath.

### L15 · Thank You / Q&A
- Elegant close: "Thank you" or "Questions & Discussion", contact line, logo. Mirror the Title Slide styling for bookend symmetry.

---

## 6 · Component Library

Reusable building blocks. Build each once as a grouped shape; copy across slides.

### 6.1 Accent Bar
- **Vertical:** 4 pt wide × height of the title, Superior Red, sitting to the left of a slide title. The signature brand mark.
- **Horizontal:** 3 pt tall × 2–3 in, above titles on dividers/title slide.

### 6.2 Eyebrow Label
- Small Medium-weight label above a title (12–14 pt, letter-spaced, `#555` or Red). Names the section: `LITERATURE REVIEW`, `METHODOLOGY`.

### 6.3 Card (Soft Card)
- Fill `#FFFFFF` or `#F5F5F5`; border `#EAEAEA` 1 pt (or borderless on light-gray); **12 pt radius**; soft shadow (see §11); **24 pt inner padding**.
- Anatomy: optional icon (top-left) → title (Medium 18–20 pt) → body (16 pt `#555`) → optional footer chip.

### 6.4 Chip / Tag
- Small rounded rectangle, 8 pt radius, `#F5F5F5` fill, 12 pt Medium text. Used for citations `[12]`, status, or category labels.

### 6.5 Divider
- 1 pt hairline `#EAEAEA`, full or partial width. Never thicker than 1.5 pt. Used above the footer and between logical blocks.

### 6.6 Icon Tile
- 40–48 px outline icon inside an optional 12 pt-radius `#F5F5F5` tile. Icon stroke in `#222` or Red for emphasis.

### 6.7 Callout / Key Insight
- A card with a 4 pt left border in Purple, `#F5F5F5` fill, holding one sentence. Reserved for the single most important statement on a slide.

### 6.8 Footer (mandatory on every content slide)
- Above it: full-width hairline divider.
- Three zones, 11 pt `#555`:
  - **Left:** thesis short-title (e.g. *Agentic AI · Clinical Decision Support*)
  - **Centre:** *The Superior University*
  - **Right:** page number
- Footer is absent only on L1 (Title) and L15 (Thank You).

---

## 7 · Cards, Tables & Metrics

### 7.1 Table Style

- **Header row:** Superior Red `#D72924` fill, white text, Medium 14–16 pt, 12 pt vertical padding.
- **Body rows:** alternating `#FFFFFF` / `#F5F5F5` ("zebra"), text `#222`, 14–16 pt.
- **Separators:** thin `#EAEAEA` horizontal lines only. **No vertical gridlines.**
- **Outer border:** rounded (approximate with a rounded rectangle behind the table, since native PPTX tables are square-cornered).
- **Alignment:** text left, numbers right, headers match their column.
- **Emphasis:** highlight a decisive cell/column with a pale Purple tint (`#F3E9F5`) rather than bold.

### 7.2 Figure Cards

- Light-gray `#F5F5F5` background, 16 pt radius, soft shadow, no thick borders.
- Academic caption *below* the figure (see §13): **Figure N.** Description. `[source]`.
- Keep 24 pt padding between the figure and the card edge.

### 7.3 Metric Cards (Results)

```
┌─────────────────┐
│  ▌               │  ← 4pt red top or left accent
│  87.4%           │  ← big number, 40–48 pt Semibold #222
│  Diagnostic F1   │  ← label, 16 pt #555
│  ▲ +6.2 vs base  │  ← delta, 13 pt muted green/orange
└─────────────────┘
```
- 2–4 cards in a row, equal width, 24 pt gaps.
- Number is the hero; keep everything else quiet. Units always shown. Source in caption below the row.

---

## 8 · Diagrams & Charts

A shared visual language across all diagram types.

### 8.1 Universal Diagram Rules
- **Nodes:** rounded rectangles, 12 pt radius, `#FFFFFF` or `#F5F5F5` fill, 1 pt `#EAEAEA` border, `#222` Medium label.
- **Emphasis node:** the key component gets a Red or Purple 1.5 pt border (never a saturated fill).
- **Arrows:** single consistent style — 1.5 pt line, `#555`, with a small solid arrowhead. **Rounded elbow connectors** where lines turn.
- **No 3D, no shadows on connectors, no gradient fills.**
- **Spacing:** nodes on the 8-pt grid; equal gaps; align to a shared baseline.
- **Labels on arrows:** 12 pt `#555`, on a small white plate so the line doesn't cut the text.

### 8.2 Diagram Type Styles

| Type | Style |
|---|---|
| **Flowchart** | Left-to-right or top-down; rounded nodes; decision points as rounded diamonds; one path colour. |
| **Architecture** | Stacked horizontal layers (light-gray bands) with a vertical "Trust/Cross-cutting" pillar; components as cards inside layers. |
| **Pipeline** | Horizontal chevrons or rounded stages with arrows; stage number eyebrow + one-line label. |
| **Comparison table** | See §7.1; final column = "The Gap" in Purple tint. |
| **Taxonomy** | Horizontal tree, rounded nodes, hairline connectors; root in Red border, branches neutral; max 3 levels. |
| **Timeline / Roadmap** | Horizontal spine, phase markers, muted Gantt bars; current phase in Red. |
| **Research gap (Venn)** | 2–3 pale overlapping circles (`#F5F5F5` + tints), the intersection labelled as the contribution. |
| **Evaluation metrics** | Bar or line charts per §8.3; metric cards per §7.3 for headline numbers. |

### 8.3 Chart Style
- **Chart types:** bar, horizontal bar, line, and small-multiples only. **No pie, no doughnut, no radar, no 3D.**
- **Series colours (in order):** Red `#D72924` → Rose `#CB725E` → Purple `#6C1C74` → Slate `#555555`. Add a hairline-separated legend; never more than 4 series.
- **Axes:** thin `#EAEAEA` gridlines, `#555` labels, no chart border, no background fill. Start bar axes at zero.
- **Data-ink:** remove chart junk — no data-point shadows, no heavy gridlines, no redundant legends. Label directly where possible.
- **Accessibility:** distinguish series by *both* colour and pattern/label; the palette above is colour-blind safe when paired with direct labels.
- See the repository `dataviz` skill for detailed chart construction guidance.

---

## 9 · Research-Specific Styles

### 9.1 Research Gap Style
- Comparison matrix: rows = existing approaches (ReAct, AutoGen, MetaGPT, MedRAG…), columns = clinical requirements (Memory, SOPs, Retrieval, Oversight, Longitudinal).
- Cells: ✓ (Muted Green), partial (Rose), ✗ (`#EAEAEA`/blank) — **always paired with a text label or symbol**, never colour alone.
- Final row/column highlights the unmet intersection in Purple: *"The proposed framework."*

### 9.2 Literature Matrix Style
- Paper cards or a table with columns: **Work · Contribution · Method · Limitation · Ref**.
- Citation chip in each card (`[n]`), consistent with §12 citation style.
- Keep to one screen; if longer, split by theme (Agentic Frameworks / RAG & Healthcare).

### 9.3 Taxonomy Style
- Rounded-node horizontal tree, max 3 depth levels, hairline connectors, root node Red-bordered.
- Consistent sibling spacing; align leaves to a common baseline.

### 9.4 Pipeline / Methodology Style
- 3–5 stages, equal-width rounded stages, consistent arrows, phase eyebrow labels (`PHASE 1`).

---

## 10 · Icons

- **Style:** outline / line icons only. Uniform 1.5–2 px stroke, no fills, rounded joins.
- **Allowed packs (pick ONE per deck, never mix):** **Material Symbols** (Outlined), **Lucide**, or **Feather**.
- **Size:** 24–48 px on the 8-pt grid; consistent within a slide.
- **Colour:** `#222` default; Red for a single emphasised icon; never multicolour icons.
- **Usage:** functional only — to label a card or step. **No decorative icons, no emoji, no clip art.**
- Export as SVG; recolour to the brand palette; embed as PNG at 2× if SVG import is unreliable.

---

## 11 · Depth, Shadows & Corners

- **Corner radius:** 12 pt cards · 8 pt chips · 16 pt large figure frames. Be consistent.
- **Shadow (soft only):** colour `#000000` at **8–12% opacity**, blur 12–18 pt, y-offset 4–6 pt, no visible spread. It should whisper, not announce.
- **No hard shadows, no glow, no bevel, no reflection, no 3D extrusion.**
- Borders and shadows are alternatives, not companions — a card uses a hairline border *or* a soft shadow, rarely both.

---

## 12 · Animation Guide

Motion is used to *pace* the talk, never to entertain.

- **Allowed:** **Fade** (in/out), **Appear**, and **Morph** for transforming a diagram between two slides.
- **Transitions:** Fade or Morph only, ≤ 0.4 s.
- **Banned:** Fly-in, Bounce, Spin, Zoom-blast, Swivel, motion paths, animated GIFs, entrance sounds.
- **Build discipline:** reveal at the *group* level (one card / one row at a time) to control attention — never letter-by-letter or per-bullet-with-motion.
- **Timing:** 0.2–0.4 s per build. On click, not automatic, so you control pace during Q&A.
- **Rule:** if the animation is the thing the audience remembers, delete it.

---

## 13 · Images & Figures

### 13.1 Image Placement Rules
- Full-bleed only on dividers/title; on content slides, images live inside figure cards with margins.
- Maintain aspect ratio — **never stretch**. Crop intentionally to a 3:2 or 16:9 frame.
- Minimum resolution 150 dpi at display size; prefer vector (SVG/EMF) for diagrams.
- Align image edges to the column grid; leave 24 pt breathing room.
- Screenshots get a 1 pt `#EAEAEA` frame and 12 pt radius so they sit in the system.

### 13.2 Figure Caption Style
- Placement: **below** the figure, left-aligned, 14 pt `#555`.
- Format: **Figure N.** Sentence-case description. *(Source / adapted from [n].)*
- Every figure is numbered and referenced at least once in the spoken narrative.
- Tables caption **above**: **Table N.** Description.

---

## 14 · Citation Style

- **In-slide citations:** bracketed numeric `[12]` in a chip or superscript, 11–12 pt `#555`, matching IEEE.
- **Attribution on figures:** *(adapted from [12])* in the caption.
- **References slide (optional, near the end):** IEEE format, 11–12 pt, two columns if long:
  `[12] A. Author, B. Author, "Title," *Venue*, vol. X, no. Y, pp. 1–10, 2024.`
- Never paste full URLs on slides; cite the work, keep the URL in speaker notes if needed.
- Consistency with the thesis reference list is mandatory — same numbering scheme where practical.

---

## 15 · Speaker Notes Style

Speaker notes are a separate, formatted deliverable (see `build_presentation.py` → `build_notes_pdf`).

- **Per slide:** a **Pacing** line (target time + energy), then 2–4 short talking-point paragraphs in a natural spoken voice — not the bullet text read aloud.
- Bold the *one* phrase per slide you must land.
- Include anticipated questions inline where a slide is likely to draw them (cross-reference `Defense_Examiner_QA.md`).
- Total time budget stated at the top; each Pacing line sums toward it.
- Rendered as a clean A4 booklet: Purple headings, light-purple pacing callout boxes, generous leading (see the reportlab styles in `build_presentation.py`).

---

## 16 · Branding Rules

- **Signature mark:** the 4 pt vertical **Superior Red accent bar** beside every slide title. This alone identifies the deck.
- **Logo:** top-right on content slides at ~1.5 in, on a white plate if placed over any non-white band; centred on Title/Thank-You. Never distort, recolour, or add effects to the logo.
- **Red** = brand punctuation. **Purple** = highlight. **Rose** = secondary information. Hold this discipline everywhere.
- **Presence, not volume:** branding should be *felt* (colour, type, the accent bar, the footer) more than *seen*. No watermarks, no logo on every corner, no branded backgrounds.
- **Bookend symmetry:** Title and Thank-You slides share styling; the deck opens and closes as one object.

---

## 17 · Accessibility Checklist

Run this before every defense/submission:

- [ ] All body text ≥ 18 pt; nothing critical below 14 pt.
- [ ] Text/background contrast ≥ 4.5:1 (≥ 3:1 for ≥ 24 pt). White-on-Red text ≥ 14 pt.
- [ ] No information conveyed by colour alone (labels/icons/position accompany it).
- [ ] Charts distinguishable in greyscale and for colour-blind viewers.
- [ ] Reading order is logical (check the Selection Pane tab order) for screen readers.
- [ ] Every image has alt text; every figure/table has a caption.
- [ ] Fonts embedded; deck opens correctly on a machine without Aptos.
- [ ] Line length 45–75 chars; generous line and paragraph spacing.
- [ ] Readable from 10 m — dry-run on the actual projector/room if possible.

---

## 18 · Do's and Don'ts

**Do**
- Leave 40%+ of each content slide empty.
- Use one idea, one focal point, one emphasis colour per slide.
- Align everything to the 8-pt grid.
- Pair every claim with evidence and every figure with a caption.
- Use Medium weight; reserve Semibold for titles and one emphasis.
- Alternate Content-Left / Content-Right for rhythm.

**Don't**
- Read bullets verbatim — bullets are anchors, you are the narration.
- Use more than 6 lines of text or 3 cards per slide.
- Mix icon packs, or use filled/multicolour icons.
- Use pie/3D/radar charts, gradients, glows, or drop-shadowed text.
- Put dark backgrounds on content slides.
- Let red or purple cover large areas.
- Stretch images or use clip art, stock handshakes, or emojis.

---

## 19 · Implementation Notes (python-pptx)

This system is codified in `build_presentation.py`. Key constants to standardise:

```python
# ---- Superior University Design System v1.0 ----
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor

# Palette
RED       = RGBColor(0xD7, 0x29, 0x24)   # primary accent
ROSE      = RGBColor(0xCB, 0x72, 0x5E)   # secondary accent
PURPLE    = RGBColor(0x6C, 0x1C, 0x74)   # highlight only
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)   # background
INK       = RGBColor(0x22, 0x22, 0x22)   # primary text
SLATE     = RGBColor(0x55, 0x55, 0x55)   # secondary text
SURFACE   = RGBColor(0xF5, 0xF5, 0xF5)   # cards / zebra rows
HAIRLINE  = RGBColor(0xEA, 0xEA, 0xEA)   # borders / dividers
GREEN     = RGBColor(0x3F, 0x8A, 0x5B)   # success
ORANGE    = RGBColor(0xC8, 0x78, 0x1E)   # warning
DARK      = RGBColor(0x1A, 0x11, 0x13)   # optional title canvas

FONT      = "Aptos"          # fallback: "Calibri", "Segoe UI"

# Canvas 16:9
SLIDE_W, SLIDE_H = Inches(13.333), Inches(7.5)
MARGIN_X, MARGIN_Y = Inches(0.7), Inches(0.6)

# Type scale (pt)
T_TITLE, T_SECTION, T_SUBHEAD = 38, 28, 24
T_BODY, T_CAPTION, T_FOOT     = 20, 15, 11

# 8-pt spacing tokens (pt)
SP = {"xs":4, "sm":8, "md":16, "lg":24, "xl":32, "2xl":48, "3xl":64}
RADIUS_CARD, RADIUS_CHIP, RADIUS_FIG = Pt(12), Pt(8), Pt(16)
```

**Migration note:** the current `build_presentation.py` uses a legacy dark-purple theme (`DARK_BG`, `PURPLE`, header bands). To adopt v1.0, switch content slides to white backgrounds, replace the purple header band with a title + red accent bar + top-right logo, add the mandatory footer, and adopt the constants above. Keep the dark canvas only for the Title and Section-Divider layouts.

Reusable helpers to build: `add_rounded_rect(...)`, `add_accent_bar(...)`, `add_footer(slide, short_title, page)`, `add_card(...)`, `add_metric_card(...)`, `soft_shadow(shape)`.

---

## 20 · Future Expansion Guidelines

- **Adding a layout?** It must inherit the margins, footer, accent bar, and 8-pt grid. Document it here as L16+ before use.
- **Adding a colour?** Only if a semantic need exists (e.g. a second "info" state). Mute it, contrast-test it, add it to §2 — never introduce an ad-hoc colour on a single slide.
- **New deck types (poster, journal graphical abstract, lecture):** reuse the palette, type scale, and components; adapt the grid to the medium. A conference poster is this system at A0 with larger type and the same restraint.
- **Versioning:** bump the version at the top and add a dated changelog entry when you change a token, colour, or rule. All decks reference the version they were built against.
- **Consistency audit:** before any submission, spot-check three random slides against §17 and §18. If any fail, the template — not just the slide — likely needs a fix.

---

### Changelog
- **v1.0** (2026-07-24) — Initial design system: palette, typography, 15 master layouts, component library, diagram/table/figure/citation/animation/accessibility standards, and `python-pptx` implementation tokens.

---

*This guide is the single source of truth. Every future Superior University MS-AI presentation — thesis defense, IEEE conference, or research talk — follows it for complete visual consistency.*
