import { useState } from 'react'
import { api, useApi } from '../api.js'
import { Chip, Loading } from '../components/shared.jsx'

const W = 720, H = 46
const xScale = (t) => 40 + (Math.max(0, t + 8) / 40) * (W - 60)

function Lane({ lane, tmax }) {
  const x = xScale
  let content = null
  if (lane.type === 'line') {
    const vs = lane.pts.filter((p) => p.t <= tmax)
    const all = lane.pts.map((p) => p.v)
    const mn = Math.min(...all), mx = Math.max(...all)
    const y = (v) => H - 14 - ((v - mn) / (mx - mn || 1)) * (H - 22)
    content = (
      <>
        {vs.length > 0 && (
          <path d={vs.map((p, i) => `${i ? 'L' : 'M'}${x(p.t)} ${y(p.v)}`).join(' ')}
                fill="none" stroke="#0d9488" strokeWidth="2" />
        )}
        {vs.map((p) => (
          <circle key={p.t} cx={x(p.t)} cy={y(p.v)} r={p.abn ? 4 : 2.5}
                  fill={p.abn ? '#b91c1c' : '#0d9488'} stroke="#fff" strokeWidth="1.5">
            <title>{`${lane.name} = ${p.v} ${lane.unit} · t=+${p.t}h · icu/chartevents`}</title>
          </circle>
        ))}
      </>
    )
  } else if (lane.type === 'dot') {
    content = lane.pts.filter((p) => p.t <= tmax).map((p) => (
      <circle key={p.t} cx={x(p.t)} cy={H - 24} r="5"
              fill={p.abn ? '#b91c1c' : '#5a6472'} stroke="#fff" strokeWidth="1.5">
        <title>{`${p.label} · t=${p.t < 0 ? p.t + ' (prior)' : '+' + p.t + 'h'}`}</title>
      </circle>
    ))
  } else {
    content = lane.pts.filter((p) => p.t0 <= tmax).map((p) => (
      <rect key={p.label} x={x(p.t0)} y={H - 30}
            width={Math.max(6, x(Math.min(p.t1, tmax)) - x(p.t0))} height="10" rx="4"
            fill="#0d9488" opacity=".55">
        <title>{`${p.label} · +${p.t0}h → +${Math.min(p.t1, tmax)}h · hosp/prescriptions`}</title>
      </rect>
    ))
  }
  return (
    <div className="lane">
      <div className="lbl">{lane.name}</div>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%">
        <line x1="40" y1={H - 12} x2={W - 20} y2={H - 12} stroke="#e3e8ee" />
        {content}
        <line x1={x(tmax)} y1="4" x2={x(tmax)} y2={H - 8}
              stroke="#b45309" strokeWidth="1.5" strokeDasharray="3 3" />
      </svg>
    </div>
  )
}

export default function PatientTimeline({ pid, go }) {
  const { data, error } = useApi(() => api.timeline(pid), [pid])
  const [tmax, setTmax] = useState(null)
  const [hl, setHl] = useState({})
  if (!data) return <Loading error={error} />
  const h = data.header
  const t = tmax ?? h.tmax

  return (
    <>
      <div className="pt-head card" style={{ padding: '12px 16px' }}>
        <div className="kv">Patient<b>{h.patient} <span className="muted small">(synthetic)</span></b></div>
        <div className="kv">Bed<b>{h.bed}</b></div>
        <div className="kv">Adm. diagnosis<b>{h.diagnosis}</b></div>
        <div className="kv">Day of stay<b>{h.day}</b></div>
        <div className="kv">Prior admissions<b>{h.prior_admissions} in timeline</b></div>
        <div className="spacer" />
        <div className="kv">Current risk<b>{h.risk.toFixed(2)} <span className="ci">({h.lo.toFixed(2)}–{h.hi.toFixed(2)})</span> <Chip kind="crit">▲ review</Chip></b></div>
      </div>
      <div className="tlgrid" style={{ marginTop: 14 }}>
        <div className="card">
          <div className="nowrow">
            <span>Replay “what was knowable”</span>
            <input type="range" min="0" max={h.tmax} value={t}
                   onChange={(e) => setTmax(+e.target.value)} />
            <span className="mono">t = admission + {t} h{t === h.tmax ? ' (now)' : ''}</span>
          </div>
          <div>{data.lanes.map((l) => <Lane key={l.name} lane={l} tmax={t} />)}</div>
          <p className="note">Timeline lanes are small multiples — one measure per lane, one axis each. Hover any point for value + provenance. Events after the cursor are hidden, mirroring the framework’s timestamp-aware retrieval.</p>
        </div>
        <aside>
          <div className="card">
            <h2 style={{ fontSize: 14 }}>Retrieved evidence <Chip>k = {data.evidence.length} · t = now</Chip></h2>
            <p className="sub" style={{ marginBottom: 8 }}>What the agents actually saw. Click a chip to mark it.</p>
            <div className="evtray">
              {data.evidence.map((e, i) => (
                <span key={i} className={`ev ${hl[i] ? 'hl' : ''}`}
                      onClick={() => setHl((s) => ({ ...s, [i]: !s[i] }))}>
                  <b>{e.t}</b> {e.label}{e.abn ? ' ⚠' : ''}
                </span>
              ))}
            </div>
          </div>
          <div className="card" style={{ marginTop: 14 }}>
            <h2 style={{ fontSize: 14 }}>Current recommendation</h2>
            <p className="small" style={{ margin: '6px 0' }}>
              Obtain blood cultures and reassess fluid status; consider early sepsis bundle.{' '}
              <Chip kind="good">✓ verified</Chip>
            </p>
            <div className="small muted">Confidence {h.risk.toFixed(2)} ({h.lo.toFixed(2)}–{h.hi.toFixed(2)}) · 4 concordant signals</div>
            <button className="btn primary" style={{ marginTop: 10 }} onClick={() => go('review')}>
              Open full review →
            </button>
          </div>
        </aside>
      </div>
    </>
  )
}
