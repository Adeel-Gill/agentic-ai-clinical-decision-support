import { api, useApi } from '../api.js'
import { Chip, Loading } from '../components/shared.jsx'

function Hub({ agents }) {
  const cx = 320, cy = 185, R = 135
  return (
    <svg viewBox="0 0 640 380" width="100%" role="img"
         aria-label="Hub and spoke diagram of agents around the coordinator">
      {agents.map((a, i) => {
        const ang = -Math.PI / 2 + (i * 2 * Math.PI) / agents.length
        const x = cx + R * Math.cos(ang), y = cy + R * Math.sin(ang)
        const col = a.status === 'working' ? '#0d9488' : a.status === 'quarantined' ? '#b91c1c' : '#8a94a3'
        return (
          <g key={a.name}>
            <line x1={cx} y1={cy} x2={x} y2={y} stroke="#cfd9df" strokeWidth="1.5" />
            <circle cx={x} cy={y} r="34" fill="#fff" stroke={col} strokeWidth="2">
              <title>{`${a.name} — ${a.status} · all messages via Coordinator`}</title>
            </circle>
            <text x={x} y={y - 2} textAnchor="middle" style={{ fontWeight: 600, fill: '#1a202c' }}>
              {a.name.split(' ')[0]}
            </text>
            <text x={x} y={y + 12} textAnchor="middle">{a.status}</text>
          </g>
        )
      })}
      <circle cx={cx} cy={cy} r="44" fill="#0f766e" />
      <text x={cx} y={cy + 4} textAnchor="middle" style={{ fill: '#fff', fontWeight: 700 }}>Coordinator</text>
    </svg>
  )
}

export default function AgentMonitor() {
  const { data, error } = useApi(api.agents)
  if (!data) return <Loading error={error} />
  const h = data.health

  return (
    <>
      <div className="agents-grid">
        <div className="card">
          <h2 style={{ fontSize: 14 }}>Orchestration topology <Chip>hub-and-spoke</Chip></h2>
          <p className="sub">All inter-agent messages pass through the Coordinator — no side channels. Quarantine isolates an agent whose outputs repeatedly fail verification.</p>
          <Hub agents={data.agents} />
        </div>
        <aside className="card">
          <h2 style={{ fontSize: 14 }}>Agent log — Verification</h2>
          <table>
            <thead><tr><th>t</th><th>Event</th></tr></thead>
            <tbody>
              {data.log.map((l) => (
                <tr key={l.t + l.event}><td className="mono">{l.t}</td><td>{l.event}</td></tr>
              ))}
            </tbody>
          </table>
        </aside>
      </div>
      <div className="health">
        <div className="card"><b>{h.retrieval_latency_ms ?? '—'} ms</b><span>retrieval latency (median, pilot)</span></div>
        <div className="card"><b>{h.gate_pass_rate != null ? `${(h.gate_pass_rate * 100).toFixed(0)} %` : '—'}</b><span>gate pass rate (pilot)</span></div>
        <div className="card"><b>{h.trail_resolvability ?? '—'}</b><span>audit-trail resolvability</span></div>
        <div className="card"><b>{h.quarantined}</b><span>agents quarantined</span></div>
      </div>
      <p className="note">Health metrics source: {h.source}.</p>
    </>
  )
}
