import { useState } from 'react'
import UnitOverview from './views/UnitOverview.jsx'
import PatientTimeline from './views/PatientTimeline.jsx'
import RecommendationReview from './views/RecommendationReview.jsx'
import AlertsGate from './views/AlertsGate.jsx'
import AuditTrail from './views/AuditTrail.jsx'
import AgentMonitor from './views/AgentMonitor.jsx'

const VIEWS = [
  { key: 'unit', icon: '▦', label: 'Unit Overview', title: 'Unit Overview — MICU A' },
  { key: 'patient', icon: '∿', label: 'Patient Timeline', title: 'Patient Timeline — P-1043' },
  { key: 'review', icon: '✓', label: 'Recommendation Review', title: 'Recommendation Review — P-1043' },
  { key: 'alerts', icon: '⚑', label: 'Alerts & Gate', title: 'Alerts & Verification Gate' },
  { key: 'audit', icon: '≡', label: 'Audit Trail', title: 'Audit Trail' },
  { key: 'agents', icon: '◎', label: 'Agent Monitor', title: 'Agent Orchestration Monitor' },
]

export default function App() {
  const [view, setView] = useState('unit')
  const [patient, setPatient] = useState('P-1043')
  const go = (v, pid) => { if (pid) setPatient(pid); setView(v) }

  const Body = {
    unit: <UnitOverview go={go} />,
    patient: <PatientTimeline pid={patient} go={go} />,
    review: <RecommendationReview pid={patient} go={go} />,
    alerts: <AlertsGate go={go} />,
    audit: <AuditTrail />,
    agents: <AgentMonitor />,
  }[view]

  return (
    <>
      <nav>
        <div className="logo">ACDSS<small>Agentic Clinical Decision Support — prototype</small></div>
        {VIEWS.map((v) => (
          <a key={v.key} href="#" className={view === v.key ? 'active' : ''}
             onClick={(e) => { e.preventDefault(); go(v.key) }}>
            {v.icon} <span className="txt">{v.label}</span>
          </a>
        ))}
        <div className="foot">All data is <b>synthetic</b> (MIMIC-IV demo–shaped). Research prototype — not for clinical use.</div>
      </nav>
      <main>
        <header>
          <h1>{VIEWS.find((v) => v.key === view).title}</h1>
          <div className="spacer" />
          <span className="chip crit">▲ 2 verified alerts <span className="badge">2</span></span>
          <span className="who">Dr. A. Rehman · Day shift</span>
        </header>
        <section className="view on">{Body}</section>
      </main>
    </>
  )
}
