import { useState } from 'react'
import { api, useApi } from '../api.js'
import { Chip, Loading } from '../components/shared.jsx'

function OperatingCurve({ curve, threshold }) {
  const X = (m) => 34 + (m - 1) * 48
  const Y = (v) => 150 - v * 130
  const path = (key) => curve.map((r, i) => `${i ? 'L' : 'M'}${X(r.min_signals)} ${Y(r[key])}`).join(' ')
  const last = curve[curve.length - 1]
  return (
    <>
      <svg viewBox="0 0 300 190" width="100%" role="img"
           aria-label="Gate operating curve: pass rate for true and false alerts by required signal count">
        {[0, 0.25, 0.5, 0.75, 1].map((g) => (
          <g key={g}>
            <line x1="34" y1={Y(g)} x2="278" y2={Y(g)} stroke="#eef1f4" />
            <text x="6" y={Y(g) + 3}>{g.toFixed(2)}</text>
          </g>
        ))}
        {curve.map((r) => <text key={r.min_signals} x={X(r.min_signals) - 3} y="168">{r.min_signals}</text>)}
        <text x="110" y="184">required distinct signals</text>
        <rect x={X(threshold) - 10} y="14" width="20" height="146" fill="#0f766e" opacity=".07" />
        <path d={path('pass_rate_true_alerts')} fill="none" stroke="#0d9488" strokeWidth="2" />
        <path d={path('pass_rate_false_alerts')} fill="none" stroke="#b45309" strokeWidth="2" />
        {curve.map((r) => (
          <g key={r.min_signals}>
            <circle cx={X(r.min_signals)} cy={Y(r.pass_rate_true_alerts)} r="3.5"
                    fill="#0d9488" stroke="#fff" strokeWidth="1.5">
              <title>{`true alerts: pass ${(r.pass_rate_true_alerts * 100).toFixed(0)}% at ≥${r.min_signals}`}</title>
            </circle>
            <circle cx={X(r.min_signals)} cy={Y(r.pass_rate_false_alerts)} r="3.5"
                    fill="#b45309" stroke="#fff" strokeWidth="1.5">
              <title>{`false alerts: pass ${(r.pass_rate_false_alerts * 100).toFixed(0)}% at ≥${r.min_signals}`}</title>
            </circle>
          </g>
        ))}
        <text x={X(last.min_signals) - 24} y={Y(last.pass_rate_true_alerts) - 8}
              fill="#0d9488" fontWeight="600">true</text>
        <text x={X(last.min_signals) - 26} y={Y(last.pass_rate_false_alerts) + 14}
              fill="#b45309" fontWeight="600">false</text>
      </svg>
      <div className="legend">
        <span><i style={{ background: '#0d9488' }} />True alerts (died)</span>
        <span><i style={{ background: '#b45309' }} />False alerts (survived)</span>
      </div>
    </>
  )
}

export default function AlertsGate({ go }) {
  const { data, error } = useApi(api.alerts)
  const [tab, setTab] = useState('verified')
  if (!data) return <Loading error={error} />

  return (
    <>
      <div className="tabs">
        <button className={tab === 'verified' ? 'on' : ''} onClick={() => setTab('verified')}>
          Verified — awaiting review ({data.verified.length})
        </button>
        <button className={tab === 'blocked' ? 'on' : ''} onClick={() => setTab('blocked')}>
          Blocked by gate ({data.blocked.length})
        </button>
      </div>
      <div className="gate-grid">
        <div className="card">
          {tab === 'verified' ? (
            <table>
              <thead><tr><th>Time</th><th>Patient</th><th>Risk</th><th>Type</th><th>Signals</th><th></th></tr></thead>
              <tbody>
                {data.verified.map((a) => (
                  <tr key={a.patient}>
                    <td className="mono">{a.time}</td>
                    <td><b>{a.patient}</b> · Bed {a.bed}</td>
                    <td className="mono">{a.risk.toFixed(2)}</td>
                    <td>{a.type}</td>
                    <td><Chip kind="good">{a.signals} / {a.required} required</Chip></td>
                    <td><button className="btn" onClick={() => go('review', a.patient)}>Review</button></td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <table>
              <thead><tr><th>Time</th><th>Patient</th><th>Risk</th><th>Type</th><th>Block reason</th></tr></thead>
              <tbody>
                {data.blocked.map((a) => (
                  <tr key={a.patient} className="blocked">
                    <td className="mono">{a.time}</td>
                    <td>{a.patient} · Bed {a.bed}</td>
                    <td className="mono">{a.risk.toFixed(2)}</td>
                    <td>{a.type}</td>
                    <td>{a.reason}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
          <p className="note">Blocked alerts are auditable, never deleted — a clinician can open and override any of them.</p>
        </div>
        <aside className="card">
          <h2 style={{ fontSize: 14 }}>Gate operating curve <Chip>admin</Chip></h2>
          <p className="sub" style={{ marginBottom: 4 }}>
            Pilot data (MIMIC-IV demo, n=28 alerts): pass rate as the evidence requirement tightens.
            Current threshold: <b>≥{data.current_threshold} signals</b>.
          </p>
          <OperatingCurve curve={data.operating_curve} threshold={data.current_threshold} />
        </aside>
      </div>
    </>
  )
}
