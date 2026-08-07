import { api, useApi } from '../api.js'
import { Chip, StatusChip, Sparkline, RiskBar, Loading } from '../components/shared.jsx'

export default function UnitOverview({ go }) {
  const { data: beds, error: e1 } = useApi(api.beds)
  const { data: queue, error: e2 } = useApi(api.queue)
  if (!beds || !queue) return <Loading error={e1 || e2} />

  return (
    <div className="unit">
      <div>
        <h2>Beds</h2>
        <p className="sub">Sorted by review priority. Risk score = cross-validated model output with 95% interval; chips reflect verification state, not raw risk.</p>
        <div className="beds">
          {beds.map((b) => (
            <div key={b.bed} className="card bed" title="Open patient timeline"
                 onClick={() => go('patient', b.id)}>
              <div className="top">
                <span className="id">Bed {b.bed} · {b.id}</span>
                <span className="meta">{b.meta}</span>
              </div>
              <StatusChip st={b.st} label={b.label} />
              <Sparkline values={b.hr} label={`${b.id} heart-rate trend`} />
              <RiskBar risk={b.risk} lo={b.lo} hi={b.hi} />
            </div>
          ))}
        </div>
      </div>
      <aside>
        <h2>Awaiting review</h2>
        <p className="sub">Verified alerts only — the gate blocks unsupported alerts (see Alerts &amp; Gate).</p>
        <div className="card queue">
          {queue.map((q) => (
            <div key={q.patient + q.time} className="item">
              <Chip kind={q.severity}>▲ {q.severity === 'crit' ? 'Critical' : 'Warning'}</Chip>{' '}
              <b>Bed {q.bed} · {q.patient}</b>
              <div className="small muted">{q.summary}</div>
              <div className="small mono muted">{q.time} · Verification: {q.verification}</div>
            </div>
          ))}
        </div>
      </aside>
    </div>
  )
}
