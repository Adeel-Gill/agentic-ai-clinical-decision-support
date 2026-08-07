/** Shared presentational pieces (ported from the HTML prototype). */

export function Chip({ kind = 'mut', children }) {
  return <span className={`chip ${kind}`}>{children}</span>
}

const ST_ICON = { crit: '▲', warn: '▲', good: '●' }
export function StatusChip({ st, label }) {
  return <Chip kind={st}>{ST_ICON[st] || '●'} {label}</Chip>
}

/** Single-series sparkline: thin 2px line, endpoint dot, no legend (title names it). */
export function Sparkline({ values, w = 200, h = 36, color = '#0d9488', label = 'trend' }) {
  const mn = Math.min(...values), mx = Math.max(...values), pad = 2
  const x = (i) => pad + (i * (w - 2 * pad)) / (values.length - 1)
  const y = (v) => h - pad - ((v - mn) / (mx - mn || 1)) * (h - 2 * pad)
  const d = values.map((v, i) => `${i ? 'L' : 'M'}${x(i).toFixed(1)} ${y(v).toFixed(1)}`).join(' ')
  return (
    <svg viewBox={`0 0 ${w} ${h}`} width="100%" height={h} aria-label={label}>
      <path d={d} fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" />
      <circle cx={x(values.length - 1)} cy={y(values.at(-1))} r="3.5" fill={color} stroke="#fff" strokeWidth="2" />
    </svg>
  )
}

export function RiskBar({ risk, lo, hi }) {
  return (
    <div className="risk">
      <span className="small muted">risk</span>
      <div className="riskbar"><i style={{ width: `${risk * 100}%` }} /></div>
      <span className="mono">{risk.toFixed(2)}</span>
      <span className="ci">({lo.toFixed(2)}–{hi.toFixed(2)})</span>
    </div>
  )
}

export function Loading({ error }) {
  return <p className="sub">{error ? `Failed to load: ${error.message}` : 'Loading…'}</p>
}
