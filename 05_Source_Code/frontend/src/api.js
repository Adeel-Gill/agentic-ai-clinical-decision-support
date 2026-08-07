const BASE = '/api/dashboard'

async function get(path) {
  const r = await fetch(BASE + path)
  if (!r.ok) throw new Error(`${r.status} ${r.statusText} — ${path}`)
  return r.json()
}

export const api = {
  beds: () => get('/beds'),
  queue: () => get('/queue'),
  timeline: (pid) => get(`/patients/${pid}/timeline`),
  recommendation: (pid) => get(`/patients/${pid}/recommendation`),
  alerts: () => get('/alerts'),
  audit: () => get('/audit'),
  agents: () => get('/agents'),
  review: (recId, body) =>
    fetch(`${BASE}/review/${recId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    }).then(async (r) => {
      if (!r.ok) throw new Error((await r.json()).detail || r.statusText)
      return r.json()
    }),
}

/** tiny hook: fetch once, expose {data, error} */
import { useEffect, useState } from 'react'
export function useApi(fn, deps = []) {
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)
  useEffect(() => {
    let live = true
    fn().then((d) => live && setData(d)).catch((e) => live && setError(e))
    return () => { live = false }
  }, deps) // eslint-disable-line
  return { data, error }
}
