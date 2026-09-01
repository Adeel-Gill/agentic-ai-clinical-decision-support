<#
.SYNOPSIS
    Selective MIMIC-IV download - only the tables listed in Data_Dictionary.md.

.DESCRIPTION
    Why selective: the full release is far larger than this project reads. Every
    file below is justified by a row in 03_Dataset/Data_Dictionary.md, keeping the
    credentialed-data footprint minimal (DUA clause 4: reasonable and prudent
    security).

    Password handling: prompted as a SecureString, written to a per-user temp
    netrc that is ACL-restricted and deleted on exit. It is never passed as a
    command-line argument (visible to other processes) and never stored in this
    repository.

    Resumable: re-running skips complete files and resumes partial ones.

.PARAMETER Dest
    Download root. Must be OUTSIDE the git repository (.ai/RULES.md R8).
    Defaults to $env:MIMIC_DEST, else C:\data\mimic-iv.

.EXAMPLE
    .\download_mimic_subset.ps1

.NOTES
    Requires: curl.exe (Windows 10+ ships it), a credentialed PhysioNet account,
    and BOTH signed DUAs (MIMIC-IV and MIMIC-IV-Note). Files return HTTP 403
    until the CITI training submission shows Active on your PhysioNet account.
#>
param(
    [string]$Dest = $(if ($env:MIMIC_DEST) { $env:MIMIC_DEST } else { 'C:\data\mimic-iv' })
)

$CoreVer = '3.1'
$NoteVer = '2.2'
$Base    = 'https://physionet.org/files'

$HospTables = @('patients', 'admissions', 'labevents', 'd_labitems',
                'diagnoses_icd', 'procedures_icd', 'prescriptions', 'microbiologyevents')
$IcuTables  = @('icustays', 'chartevents', 'inputevents', 'outputevents', 'd_items')
$NoteTables = @('discharge', 'radiology')

if ($Dest -like '*agentic-ai-clinical-decision-support*') {
    Write-Host 'REFUSING: destination is inside the git repository (R8).' -ForegroundColor Red
    exit 1
}
if (-not (Get-Command curl.exe -ErrorAction SilentlyContinue)) {
    Write-Host 'curl.exe not found; install curl or use the .sh version in Git Bash.' -ForegroundColor Red
    exit 1
}

$user   = Read-Host 'PhysioNet username'
$secure = Read-Host 'PhysioNet password' -AsSecureString
$bstr   = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
$pass   = [Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)
[Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)

$netrc         = Join-Path $env:TEMP ('physionet_{0}.netrc' -f [guid]::NewGuid().ToString('N'))
$script:failed = 0
$script:got    = 0

function Get-MimicFile {
    param([string]$Url, [string]$Dir)

    if (-not (Test-Path $Dir)) { New-Item -ItemType Directory -Force -Path $Dir | Out-Null }
    $name = Split-Path $Url -Leaf
    $out  = Join-Path $Dir $name
    Write-Host ('  {0,-26} ' -f $name) -NoNewline

    & curl.exe -sSfL --netrc-file $netrc -C - -o $out $Url
    $code = $LASTEXITCODE

    if ($code -eq 0) {
        $mb = [math]::Round((Get-Item $out).Length / 1MB, 1)
        Write-Host ('ok ({0} MB)' -f $mb) -ForegroundColor Green
        $script:got++
    }
    elseif (($code -eq 33 -or $code -eq 36) -and (Test-Path $out)) {
        Write-Host 'already complete' -ForegroundColor DarkGray
        $script:got++
    }
    else {
        Write-Host ('FAILED (curl exit {0})' -f $code) -ForegroundColor Red
        $script:failed++
    }
}

try {
    "machine physionet.org login $user password $pass" |
        Out-File -FilePath $netrc -Encoding ascii
    $pass = $null
    & icacls $netrc /inheritance:r /grant:r "$($env:USERNAME):(R,W)" | Out-Null

    Write-Host ''
    Write-Host "Destination: $Dest" -ForegroundColor Cyan
    Write-Host ''
    Write-Host "== MIMIC-IV v$CoreVer : hosp module ==" -ForegroundColor Cyan
    foreach ($t in $HospTables) {
        Get-MimicFile "$Base/mimiciv/$CoreVer/hosp/$t.csv.gz" (Join-Path $Dest "mimiciv-$CoreVer\hosp")
    }

    Write-Host "== MIMIC-IV v$CoreVer : icu module ==" -ForegroundColor Cyan
    foreach ($t in $IcuTables) {
        Get-MimicFile "$Base/mimiciv/$CoreVer/icu/$t.csv.gz" (Join-Path $Dest "mimiciv-$CoreVer\icu")
    }

    Write-Host "== MIMIC-IV-Note v$NoteVer ==" -ForegroundColor Cyan
    foreach ($t in $NoteTables) {
        Get-MimicFile "$Base/mimic-iv-note/$NoteVer/note/$t.csv.gz" (Join-Path $Dest "mimic-iv-note-$NoteVer\note")
    }

    Write-Host '== checksums (provenance) ==' -ForegroundColor Cyan
    Get-MimicFile "$Base/mimiciv/$CoreVer/SHA256SUMS.txt"        (Join-Path $Dest "mimiciv-$CoreVer")
    Get-MimicFile "$Base/mimic-iv-note/$NoteVer/SHA256SUMS.txt"  (Join-Path $Dest "mimic-iv-note-$NoteVer")
}
finally {
    Remove-Item $netrc -Force -ErrorAction SilentlyContinue
}

Write-Host ''
if (Test-Path $Dest) {
    $bytes = (Get-ChildItem $Dest -Recurse -File | Measure-Object -Property Length -Sum).Sum
    Write-Host ('Downloaded {0} file(s), {1} failed. Total on disk: {2} GB' -f `
        $script:got, $script:failed, [math]::Round($bytes / 1GB, 2))
}
if ($script:failed -gt 0) {
    Write-Host ''
    Write-Host 'If every file failed with HTTP 403, your CITI training submission is not yet' -ForegroundColor Yellow
    Write-Host 'Active. Check https://physionet.org/settings/certification/ and re-run later -' -ForegroundColor Yellow
    Write-Host 'this script resumes and skips what is already complete.' -ForegroundColor Yellow
}
else {
    Write-Host ''
    Write-Host 'Next: point the code at this root (never copy data into the repo):' -ForegroundColor Cyan
    Write-Host ('  $env:ACDSS_MIMIC_ROOT = "{0}"' -f $Dest)
}
