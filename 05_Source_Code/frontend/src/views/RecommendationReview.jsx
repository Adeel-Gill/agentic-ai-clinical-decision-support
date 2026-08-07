import { useState } from 'react'
import { api, useApi } from '../api.js'
import { Chip, Loading } from '../components/shared.jsx'

export default function RecommendationReview({ pid }) {
  const { data: rec, error } = useApi(() => api.recommendation(pid), [pid])
  const [activeEv, setActiveEv] = useState([])
  const [reason, setReason] = useState('')
  const [result, setResult] = useState(null)
  const [busy, setBusy] = useState(false)
  if (!rec) return <Loading error={error} />

  const decide = async (decision) => {
    setBusy(true); setResult(null)
    try {
      const r = await api.review(rec.id, { decision, reason })
      setResult({ ok: true, msg: `Recorded: ${decision} (audit ${r.audit_entry.ts})` })
    } catch (e) {
      setResult({ ok: false, msg: e.message })
    } finally { setBusy(false) }
  }

  const conf = rec.confidence
  return (
    <div className="review">
      <div className="card">
        <div className="crumbs">Agent chain:{' '}
          {rec.chain.map((c, i) => (
            <span key={c} className={i === rec.chain.length - 1 ? 'ok' : ''}>
              {c}{i === rec.chain.length - 1 ? ' ✓' : ''}
            </span>
          ))}
        </div>
        <h2 style={{ margin: '12px 0 6px' }}>Recommendation for {rec.patient} · Bed {rec.bed}</h2>
        <p style={{ fontSize: 14.5 }}>
          {rec.claims.map((c, i) => (
            <span key={i}>
              <span className={`claim ${activeEv === c.evidence ? 'on' : ''}`}
                    onClick={() => setActiveEv(c.evidence)}>{c.text}</span>
              {i < rec.claims.length - 1 ? '; ' : '. '}
            </span>
          ))}
          {rec.narrative}
        </p>
        <div className="conf">
          <span className="small muted">Calibrated confidence</span>
          <div className="confbar">
            <i className="rng" style={{ left: `${conf.lo * 100}%`, width: `${(conf.hi - conf.lo) * 100}%` }} />
            <i className="pt" style={{ left: `${conf.point * 100}%` }} />
          </div>
          <span className="mono">{conf.point.toFixed(2)} ({conf.lo.toFixed(2)}–{conf.hi.toFixed(2)})</span>
        </div>
        <div className="verif">
          <div className="tick">✓</div>
          <div>
            <b>Verification: {rec.verification.status}</b> — {rec.verification.signals} distinct concordant
            signals within the last 6 h (threshold: ≥{rec.verification.required}).
            <details className="small" style={{ marginTop: 4 }}>
              <summary style={{ cursor: 'pointer', color: 'var(--brand)' }}>Show gate detail</summary>
              {rec.verification.detail}
            </details>
          </div>
        </div>
      </div>

      <div className="evcols">
        <div className="card">
          <h2 style={{ fontSize: 14 }}>Patient evidence <Chip>timeline RAG</Chip></h2>
          <table>
            <thead><tr><th>t</th><th>Item</th><th>Value</th></tr></thead>
            <tbody>
              {rec.patient_evidence.map((e) => (
                <tr key={e.id} style={{ background: activeEv.includes(e.id) ? 'var(--brand-soft)' : '' }}>
                  <td className="mono">{e.t}</td><td>{e.item}</td>
                  <td><b>{e.value}</b> <Chip kind={e.severity}>abn</Chip></td>
                </tr>
              ))}
            </tbody>
          </table>
          <p className="note">Every row carries provenance (source table + row id) into the audit trail. Click a claim above to highlight its evidence.</p>
        </div>
        <div className="card">
          <h2 style={{ fontSize: 14 }}>Knowledge evidence <Chip>guideline RAG</Chip></h2>
          {rec.knowledge_evidence.map((k) => (
            <p key={k.source} className="small" style={{ margin: '8px 0' }}>
              <b>{k.source}:</b> “{k.excerpt}”
            </p>
          ))}
          <p className="note">Sources are named and versioned; excerpts are retrieved, never generated.</p>
        </div>
      </div>

      <div className="card">
        <div className="actions">
          <button className="btn primary" disabled={busy} onClick={() => decide('approve')}>✓ Approve</button>
          <button className="btn" disabled={busy} onClick={() => decide('modify')}>✎ Modify</button>
          <button className="btn danger" disabled={busy} onClick={() => decide('reject')}>✕ Reject</button>
          <textarea placeholder="Reason (required for Modify / Reject) — recorded to audit trail"
                    value={reason} onChange={(e) => setReason(e.target.value)} />
        </div>
        {result && (
          <p className="small" style={{ marginTop: 8, color: result.ok ? 'var(--good)' : 'var(--crit)' }}>
            {result.msg}{result.ok ? ' — see Audit Trail.' : ''}
          </p>
        )}
        <p className="note">Nothing executes automatically. Your decision and reason are written to the audit trail and fed back to the monitoring loop as a supervision signal.</p>
      </div>
    </div>
  )
}
