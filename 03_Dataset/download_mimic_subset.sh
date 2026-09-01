#!/usr/bin/env bash
# Selective MIMIC-IV download — only the tables in Data_Dictionary.md.
#
# Why selective: the full release is far larger than this project reads. Every
# file below is justified by a row in 03_Dataset/Data_Dictionary.md, which keeps
# the data footprint minimal (DUA clause 4: reasonable and prudent security).
#
# Usage (run from anywhere):
#     bash 03_Dataset/download_mimic_subset.sh
#
# Requirements: curl, a credentialed PhysioNet account, and BOTH signed DUAs
# (MIMIC-IV and MIMIC-IV-Note).
#
# Password handling: prompted once, written to a 0600 temp netrc, and deleted on
# exit. It is never passed as a command-line argument (which would be visible to
# other processes) and never stored in this repository.
#
# Resumable: re-running skips complete files and resumes partial ones (curl -C -).

set -uo pipefail

DEST="${MIMIC_DEST:-/c/data/mimic-iv}"
CORE_VER="3.1"
NOTE_VER="2.2"
BASE="https://physionet.org/files"

HOSP_TABLES=(patients admissions labevents d_labitems diagnoses_icd procedures_icd prescriptions microbiologyevents)
ICU_TABLES=(icustays chartevents inputevents outputevents d_items)
NOTE_TABLES=(discharge radiology)

read -rp "PhysioNet username: " PN_USER
read -rsp "PhysioNet password: " PN_PASS; echo

NETRC="$(mktemp)"; chmod 600 "$NETRC"
trap 'rm -f "$NETRC"' EXIT
printf 'machine physionet.org login %s password %s\n' "$PN_USER" "$PN_PASS" > "$NETRC"
unset PN_PASS

fetch() {  # fetch <url> <out_dir>
    local url="$1" dir="$2" name; name="$(basename "$url")"
    mkdir -p "$dir"
    printf '  %-28s ' "$name"
    if curl -sSfL --netrc-file "$NETRC" -C - -o "$dir/$name" "$url" 2>/tmp/curl_err; then
        printf 'ok (%s)\n' "$(du -h "$dir/$name" | cut -f1)"
    else
        # curl exits 33/36 when the file is already complete and cannot be resumed
        if [[ -s "$dir/$name" ]]; then printf 'already complete\n';
        else printf 'FAILED — %s\n' "$(tail -1 /tmp/curl_err)"; return 1; fi
    fi
}

echo
echo "Destination: $DEST   (must be OUTSIDE the git repository — R8)"
case "$(cd "$(dirname "$DEST")" 2>/dev/null && pwd)" in
  */agentic-ai-clinical-decision-support*) echo "REFUSING: destination is inside the repo."; exit 1;;
esac

echo
echo "== MIMIC-IV v$CORE_VER : hosp module =="
for t in "${HOSP_TABLES[@]}"; do fetch "$BASE/mimiciv/$CORE_VER/hosp/$t.csv.gz" "$DEST/mimiciv-$CORE_VER/hosp"; done

echo "== MIMIC-IV v$CORE_VER : icu module =="
for t in "${ICU_TABLES[@]}"; do fetch "$BASE/mimiciv/$CORE_VER/icu/$t.csv.gz" "$DEST/mimiciv-$CORE_VER/icu"; done

echo "== MIMIC-IV-Note v$NOTE_VER =="
for t in "${NOTE_TABLES[@]}"; do fetch "$BASE/mimic-iv-note/$NOTE_VER/note/$t.csv.gz" "$DEST/mimic-iv-note-$NOTE_VER/note"; done

echo "== checksums (for provenance; verify manually if desired) =="
fetch "$BASE/mimiciv/$CORE_VER/SHA256SUMS.txt" "$DEST/mimiciv-$CORE_VER" || true
fetch "$BASE/mimic-iv-note/$NOTE_VER/SHA256SUMS.txt" "$DEST/mimic-iv-note-$NOTE_VER" || true

echo
echo "Done. Total on disk:"; du -sh "$DEST"
echo
echo "Next: point the code at this root (never copy data into the repo):"
echo "  export ACDSS_MIMIC_ROOT=\"$DEST\""
