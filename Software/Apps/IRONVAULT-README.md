# ⊡ IRONVAULT
### SECURE FIELD OPERATIONS TERMINAL
**v1.0.0 // OFFLINE // ENCRYPTED**

---

## OVERVIEW

IRONVAULT is a single-file, offline digital brain built for preppers, survivalists, and field operators who require **zero-trust data storage** with no server dependency, no network calls, and no third-party services.

Everything runs inside one `.html` file. Open it in any modern browser. All data is encrypted and stored locally. Close the tab — your data stays locked. Lose the file — nothing is exposed. The master key is never stored anywhere.

---

## QUICK START

1. **Download** `ironvault.html`
2. **Open** it in any modern browser (Chrome, Firefox, Edge, Brave — offline capable)
3. **First Run:** Click `[ FIRST RUN — INITIALIZE VAULT ]`
4. Complete the 4-step setup wizard
5. Enter your master key on the lock screen to authenticate

> **No installation. No internet. No account. No dependencies.**

---

## SECURITY ARCHITECTURE

### Encryption
| Property | Value |
|---|---|
| Algorithm | AES-256-GCM |
| Key Derivation | PBKDF2-SHA256 |
| KDF Iterations | 250,000 |
| Salt Length | 256-bit (random, unique per vault) |
| IV | 96-bit (random per encrypt operation) |
| Storage | Browser localStorage (encrypted blob only) |
| Network Access | **NONE** — blocked by Content Security Policy |

The master key is **never stored**. It is derived fresh into memory each session and cleared on lock/close. An attacker with full access to your localStorage has only a PBKDF2-hardened ciphertext blob — brute-forcing a strong passphrase at 250,000 iterations is computationally impractical.

### Hardened Security Features

**Duress / Decoy Vault**
A second optional password opens a completely separate, independent vault. The decoy vault is indistinguishable from the primary — same encryption, separate salt, separate blob. Under coercion, authenticate with the duress key. The attacker sees an empty (or populated with fake data) vault and has no way to determine that a primary vault exists.

**Panic Wipe (Lock Screen)**
On the lock screen, prefix any entry with `WIPE:` to trigger immediate vault destruction. Example: `WIPE:anything`. A single confirmation prompt stands between you and complete data erasure. All localStorage keys are cleared — no recovery possible.

**Failed Attempt Auto-Wipe**
Configurable during setup and in Settings. Set a threshold (e.g., 10 attempts) after which the vault self-destructs automatically and silently. Set to `0` to disable.

**DevTools / Inspector Lock**
If browser developer tools are detected (via window size differential threshold), the vault locks immediately. Reopening requires re-authentication.

**Keyboard Shortcut Blocking**
F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+Shift+C, and Ctrl+U (view-source) are suppressed.

**Right-Click Disabled**
Context menu is suppressed application-wide to prevent casual inspection.

**Clipboard Auto-Scrub**
Any value copied via the app's copy functions is automatically cleared from the system clipboard after a configurable delay (default: 30 seconds).

**Auto-Lock on Inactivity**
Vault locks after configurable inactivity period (default: 5 minutes). Timer resets on any mouse, keyboard, or touch event.

**Session Memory Wipe**
On tab close or navigation away, key material is cleared from JavaScript memory via the `beforeunload` event handler.

**Content Security Policy**
The `<meta>` CSP header blocks all external network requests, inline event injection, and external font/script loading at the browser level.

---

## MODULES

### 📓 FIELD NOTES
Encrypted journal and notes system. Create unlimited notes, each with a title and freeform body. Auto-saves while typing (800ms debounce). Notes sorted by last-modified timestamp. Full delete with confirmation.

### ✅ CHECKLISTS
Build and track operational checklists. Pre-loaded templates included:

| Template | Items |
|---|---|
| 72-Hour Bug-Out Bag | 25 items |
| INCH Bag (I'm Never Coming Home) | 21 items |
| Vehicle Emergency Kit | 15 items |
| Home Defense Readiness | 16 items |

Create custom checklists in any category. Individual item toggle, per-item notes, progress bar, bulk reset, export-safe JSON structure.

### 📦 SUPPLY INVENTORY
Track all supplies across 10 pre-defined categories:
- WATER / FOOD (Long-term) / FOOD (Perishable)
- MEDICAL / COMMUNICATIONS / POWER & LIGHTING
- TOOLS & EQUIPMENT / WEAPONS & DEFENSE
- DOCUMENTS & CASH / MISC

Per item: name, quantity, unit, expiry date, and status (OK / LOW / CRITICAL). Low/critical items display color-coded alerts.

### 📖 FIELD MANUAL — REFERENCE LIBRARY
Pre-loaded offline survival reference content. No internet required. Covers:

| Category | Content |
|---|---|
| WATER | Procurement, purification methods (boiling, chemical, filtration), storage, field improvisation |
| FIRE | Triangle, structures, ignition methods (lighter through bow drill), natural starters, wet conditions |
| SHELTER | Siting rules, debris hut construction, tarp configurations, insulation principles |
| FIRST AID | MARCH protocol (Massive hemorrhage, Airway, Respiration, Circulation, Hypothermia), CPR, burns, fractures |
| NAVIGATION | Compass bearing, MGRS grid format, dead reckoning, pace count, celestial navigation, map reading |
| COMMS | Full NATO phonetic alphabet, complete Morse code table, HAM/GMRS/CB/FRS/MURS frequencies, radio protocols |
| SECURITY | OPSEC 5-step process, digital security, layered physical defense, patrol base setup, cache security |
| SIGNALS | SOS patterns, signal mirror, signal fires, ground-to-air symbol set, whistle codes |
| CBRN | Detection, MOPP levels, improvised protection, decontamination, nuclear fallout survival |
| FOOD | Universal Edibility Test, reliable edible plants, small game trapping, field food preservation |
| KNOTS | Square, Bowline, Clove Hitch, Figure-8, Taut-Line Hitch, Timber Hitch, square/diagonal/shear lashings |

### 🗺 LOCATIONS & WAYPOINTS
Log and retrieve operational locations. Per entry:
- Designation / code name
- Type (Cache, Rally Point, Bug-Out Destination, Water Source, Medical, Comms Site, OP, Safe House, Hazard)
- Lat/Long coordinates
- MGRS grid reference
- Bearing and distance from home
- Approach notes

### 📻 COMMUNICATIONS LOG
Frequency and contact management. Per entry:
- Callsign / contact name
- Radio type (HAM, GMRS, CB, FRS, MURS, Phone, Satellite)
- Frequency / channel
- CTCSS / PL tone
- Group / team assignment
- Comm window times (UTC)
- Alternate frequencies and notes

### 🩺 MEDICAL RECORDS
Five sub-sections:

**Personal Profile** — Name, DOB, blood type, height/weight, organ donor status, insurance, emergency contact, medical conditions.

**Medications** — Name, dosage, frequency, on-hand supply, purpose/notes.

**Allergies** — Allergen, severity (Mild/Moderate/Severe), reaction symptoms, treatment (e.g., epinephrine).

**Medical Contacts** — Provider name, role, phone, address, notes.

**Medical Journal** — Timestamped entries for symptoms, treatments, and observations.

### ⚠ SITREP — SITUATION REPORT
Threat event log with 5-level threat classification:

| Level | Color | Use |
|---|---|---|
| 1 — ROUTINE | Green | Normal observation |
| 2 — ELEVATED | Yellow-Green | Anomalous activity |
| 3 — HIGH | Amber | Confirmed threat nearby |
| 4 — CRITICAL | Orange | Immediate danger |
| 5 — EMERGENCY | Red | Active emergency |

Per event: timestamp, threat level, event type, location (grid ref), 5-line SITREP summary. Dashboard shows total events, high/critical count, and last-24-hour activity count.

### ⚙ SETTINGS
- Adjust auto-lock timer (1–60 minutes)
- Adjust clipboard clear delay (5–300 seconds)
- Set failed-attempt wipe threshold (0 = disabled)
- View vault statistics and encryption details
- Export encrypted backup (`.ivbak` file)
- Import encrypted backup
- Change master key (requires current key verification)
- Wipe all data (requires typed confirmation `CONFIRM WIPE`)

---

## VAULT BACKUP & RESTORE

### Export
Settings → `[ EXPORT ENCRYPTED BACKUP ]`

Produces a `.ivbak` file (JSON wrapper around your encrypted vault blob + salt). The file is **fully encrypted** — it contains no plaintext data. Safe to store on external drives, SD cards, or printed as QR if base64 encoded externally.

### Import
Settings → `[ IMPORT BACKUP ]`

Select your `.ivbak` file. The vault is overwritten, then you re-authenticate with your original master key. Import does not require your current session key — useful for disaster recovery on a new device.

### Restore to New Device
1. Copy `ironvault.html` + your `.ivbak` backup to the new device
2. Open `ironvault.html` in a browser
3. **Do not** click First Run
4. Settings → Import Backup
5. Authenticate with master key

---

## OPERATIONAL SECURITY RECOMMENDATIONS

**Master Key Selection**
Use a passphrase of 4+ unrelated words (e.g., `rifle-canyon-frost-2047`). Minimum 12 characters. Mix uppercase, numbers, and symbols for maximum strength. **Write it down on paper and store separately from the device.**

**Device Security**
- Run on an encrypted device (BitLocker, FileVault, LUKS)
- Use a dedicated offline device if threat model warrants it
- Do not open on shared or untrusted computers
- Consider running on an air-gapped laptop or Raspberry Pi

**Storage of the File**
- Primary: Encrypted USB drive
- Backup: Second encrypted USB at a separate physical location
- Emergency: Printed QR code of the `.ivbak` backup in a waterproof container

**Duress Key Setup**
Configure a duress key during initial setup. The decoy vault can be populated with plausible but non-sensitive data to increase believability under coercion scenarios.

**Backup Cadence**
Export an encrypted backup after every significant update. Store at least 2 backup copies in separate locations.

**Panic Procedures**
- Lock screen rapid wipe: enter `WIPE:` as password prefix
- If vault compromise is suspected and you cannot access the device: the localStorage data is encrypted — without the key, an attacker has only ciphertext

---

## TECHNICAL SPECIFICATIONS

| Property | Value |
|---|---|
| File type | Single `.html` file |
| File size | ~140 KB |
| External dependencies | **None** |
| Network requests | **None** (CSP-blocked) |
| Storage mechanism | Browser `localStorage` |
| Browser compatibility | Chrome 89+, Firefox 85+, Edge 89+, Brave, Safari 15+ |
| JavaScript API used | Web Crypto API (built into all modern browsers) |
| Data format | JSON → AES-256-GCM encrypted → Base64 encoded |
| Offline capable | **Yes — fully** |
| Mobile compatible | Yes (responsive layout) |

---

## BROWSER COMPATIBILITY NOTES

The Web Crypto API (`crypto.subtle`) is used for all encryption. This API is built into every modern browser and requires **no external libraries**. It is available offline.

> ⚠ **Important:** `crypto.subtle` requires either a **secure context** (HTTPS) or `localhost`. If you open the file from your local filesystem (`file:///`), it may not work in all browsers due to this restriction.

**Recommended approach:**
- Open directly from filesystem in **Firefox** (no restriction on `file://`)
- In Chrome/Edge: serve locally via a simple HTTP server:
  ```
  python3 -m http.server 8080
  ```
  Then open `http://localhost:8080/ironvault.html`
- **Alternatively:** Place the file on an encrypted USB and open with Firefox — no server needed

---

## FILE INTEGRITY VERIFICATION

To verify the file has not been tampered with, generate a SHA-256 hash of `ironvault.html` immediately after download and compare against your stored reference hash.

**Linux / macOS:**
```bash
sha256sum ironvault.html
```

**Windows (PowerShell):**
```powershell
Get-FileHash ironvault.html -Algorithm SHA256
```

Store the hash in a separate secure location. Re-verify before any sensitive operation on untrusted hardware.

---

## DATA PRIVACY STATEMENT

IRONVAULT does not:
- Transmit any data over any network
- Connect to any external server, CDN, or API
- Load any external fonts, scripts, or stylesheets
- Set any cookies
- Use any analytics or tracking
- Log any user activity externally
- Contain any identifiers, UUIDs, or telemetry

All data remains on the device that generated it, encrypted at rest, until explicitly exported by the user.

---

## KNOWN LIMITATIONS

- **localStorage limit:** Most browsers cap localStorage at 5–10 MB per origin. For typical prepper use (notes, checklists, inventory) this is ample. If storing large documents, consider linking them externally and keeping references in notes.
- **Browser storage is not permanent:** Clearing browser data/cache/cookies will erase the vault. Always maintain `.ivbak` backups on separate media.
- **`file://` protocol restriction:** See Browser Compatibility Notes above. Firefox recommended for direct file access.
- **No cloud sync:** By design. Sync manually via `.ivbak` export/import.
- **No print function:** Print sensitive data only when operationally necessary, then destroy.

---

## GLOSSARY

| Term | Definition |
|---|---|
| AES-256-GCM | Advanced Encryption Standard, 256-bit key, Galois/Counter Mode — authenticated encryption |
| PBKDF2 | Password-Based Key Derivation Function 2 — slows brute-force attacks via repeated hashing |
| MGRS | Military Grid Reference System — standardized coordinate format used by NATO |
| MARCH | Tactical first aid protocol: Massive hemorrhage, Airway, Respiration, Circulation, Hypothermia |
| SITREP | Situation Report |
| OPSEC | Operations Security — protecting critical information from adversaries |
| CBRN | Chemical, Biological, Radiological, Nuclear |
| MOPP | Mission Oriented Protective Posture |
| BOB | Bug-Out Bag — 72-hour emergency kit |
| INCH | I'm Never Coming Home bag — long-term evacuation kit |
| Duress key | Secondary password that opens a decoy vault under coercion |
| .ivbak | IRONVAULT encrypted backup file format |

---

*IRONVAULT v1.0.0 — Built for offline field operations. No network. No cloud. No traces.*
