"""Convert paper/*.md sections to LaTeX body + trim References.bib to cited keys."""
import re
from pathlib import Path

# Compile in md-number order so prose cross-references (Section 4 = Discussion,
# Section 5 = Pilot) match the compiled numbering.
ORDER = ["01_Introduction.md", "02_Related_Work.md", "03_Methodology.md",
         "04_Discussion.md", "05_Pilot_Study.md", "06_Conclusion.md"]

# Numeric md cross-references -> IEEE roman section labels
XREFS = [("Section 3.6", r"Section~III-F"), ("Section 2", r"Section~II"),
         ("Section 3", r"Section~III"), ("Section 4", r"Section~IV"),
         ("Section 5", r"Section~V")]


def md2tex(text):
    t = text
    t = t.replace('\\', r'\textbackslash{}')
    for ch, rep in [('%', r'\%'), ('&', r'\&'), ('#', r'\#'), ('_', r'\_')]:
        t = t.replace(ch, rep)
    t = t.replace('\u00d7', r'$\times$').replace('\u2265', r'$\geq$').replace('\u2264', r'$\leq$')
    t = t.replace('~', r'\textasciitilde{}')
    # headings: drop manual numbers (IEEEtran numbers automatically); '#' is escaped by now
    t = re.sub(r'^\\\# \d+\.\s*(.+)$', r'\\section{\1}', t, flags=re.M)
    t = re.sub(r'^\\\#\\\# \d+\.\d+\s*(.+)$', r'\\subsection{\1}', t, flags=re.M)
    # bold / italics
    t = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', t, flags=re.S)
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'\\emph{\1}', t)
    # citations [a; b; c] -> \cite{a,b,c}
    def cite(m):
        keys = re.split(r';\s*', m.group(1))
        return r'\cite{' + ','.join(keys) + '}'
    t = re.sub(r'\[([a-z][a-zA-Z0-9]+(?:;\s*[a-z][a-zA-Z0-9]+)*)\]', cite, t)
    # typographic
    t = (t.replace('\u201c', "``").replace('\u201d', "''")
          .replace('\u2019', "'").replace('\u2018', '`')
          .replace('\u2013', '--').replace('\u2014', '---')
          .replace('\u00b7', r'$\cdot$'))
    for src, dst in XREFS:
        t = t.replace(src, dst)
    return t


body_parts, cited = [], set()
for f in ORDER:
    tex = md2tex(Path('paper', f).read_text(encoding='utf-8'))
    cited.update(re.findall(r'\\cite\{([^}]+)\}', tex))
    body_parts.append(tex)
Path('paper/_body_generated.tex').write_text('\n\n'.join(body_parts), encoding='utf-8')

keys = set()
for grp in cited:
    keys.update(k.strip() for k in grp.split(','))
print('cited keys:', len(keys))

bib = Path('02_Research/References.bib').read_text(encoding='utf-8')
entries = re.split(r'(?=^@)', bib, flags=re.M)
kept, found = [], set()
for e in entries:
    m = re.match(r'^@\w+\{([^,]+),', e)
    if m and m.group(1) in keys:
        kept.append(e.strip() + '\n')
        found.add(m.group(1))
missing = keys - found
print('kept entries:', len(kept), '| missing from bib:', sorted(missing) or 'none')
Path('paper/references.bib').write_text(
    '% Trimmed bibliography for the W-category paper '
    '(auto-generated from 02_Research/References.bib)\n\n' + '\n'.join(kept),
    encoding='utf-8')
