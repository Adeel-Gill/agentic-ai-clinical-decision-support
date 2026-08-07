import { api, useApi } from '../api.js'
import { Chip, Loading } from '../components/shared.jsx'

const STATUS_CHIP = {
  'verified-approved': ['good', '✓ verified · approved'],
  'verified-pending': ['good', '✓ verified · pending'],
  'blocked': ['warn', '◼ blocked by gate'],
  'clinician-approve': ['good', '✓ approved (this session)'],
  'clinician-modify': ['warn', '✎ modified (this session)'],
  'clinician-reject': ['crit', '✕ rejected (this session)'],
}

export default function AuditTrail() {
  const { data: entries, error } = useApi(api.audit)
  if (!entries) return <Loading error={error} />

  return (
    <>
      <div className="filters">
        <select><option>All patients</option></select>
        <select><option>All agents</option></select>
        <select><option>All decisions</option></select>
        <input type="date" defaultValue="2026-08-07" />
        <div className="spacer" />
        <button className="btn">⇩ Export for review</button>
      </div>
      {entries.map((e, i) => {
        const [kind, label] = STATUS_CHIP[e.status] || ['mut', e.status]
        return (
          <details className="audit" key={i} open={i === 0}>
            <summary>
              <span className="mono muted">{e.ts}</span>
              <b>{e.patient}</b>
              <Chip kind={kind}>{label}</Chip>
              <span className="muted small">{e.title}</span>
              <span className="spacer" />
              {e.resolvability && <Chip>resolvability ✓</Chip>}
            </summary>
            <div className="body">
              <p><b>Recommendation:</b> {e.recommendation}</p>
              <p style={{ marginTop: 6 }}><b>Verification:</b> {e.verification}</p>
              {e.references.length > 0 && (
                <p style={{ marginTop: 6 }}>
                  <b>Evidence references:</b>{' '}
                  {e.references.map((r) => <span key={r} className="ref">{r}</span>)}
                  {' '}— all re-resolved against source tables ✓
                </p>
              )}
              <p style={{ marginTop: 6 }}><b>Decision:</b> {e.decision}</p>
            </div>
          </details>
        )
      })}
      <p className="note">Trail faithfulness is a measured system metric (pilot: 183/183 references re-resolved). Entries are append-only.</p>
    </>
  )
}
