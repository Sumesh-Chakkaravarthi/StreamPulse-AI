# StreamPulse AI — Metrological Traceability & ISO Compliance Manual

This document details the regulatory compliance architecture, ASTM / EPA standard alignments, and ISO 17025 metrological traceability implemented in **StreamPulse AI**.

---

## 1. Regulatory Standards Cross-Reference

StreamPulse AI's physics guardrails, automated diagnostic engine, and calibration tracking comply directly with the international testing and calibration standards governing water quality instrumentation:

| Standard Code | Standard Title | Application in StreamPulse AI |
| :--- | :--- | :--- |
| **ASTM D1293-18** | *Standard Test Methods for pH of Water* | Implements the theoretical Nernst temperature compensation equation $S(T)$ and flags asymmetric liquid junction potentials. |
| **EPA Method 180.1** | *Determination of Turbidity by Nephelometry* | Dictates ratio nephelometric scattering checks ($90^\circ$ detection) and aeration microbubble discrimination. |
| **ISO/IEC 17025:2017** | *General requirements for competence of testing and calibration laboratories* | Mandates two-point calibration traceability, slope percentage ($S\%$), and zero-potential offset ($E_0$) tracking. |
| **ISO 9001:2015 §8.5.1** | *Control of Production and Service Provision* | Immutable audit trail for Sustaining Engineering sign-offs and root-cause corrective action logs. |
| **ISO 7888:1985** | *Water quality — Determination of electrical conductivity* | Implements linear temperature compensation ($2.0\% / {}^\circ\text{C}$) to normalize raw conductance to $25.0{}^\circ\text{C}$. |

---

## 2. Standard Operating Procedures (SOP) Knowledge Base

The Autonomous AI Agent queries an embedded domain knowledge base mapped directly to instrumentation failure modes:

### SOP-410: Amperometric Working Electrode Biofouling Remediation
* **Condition:** Potentiostat Faradaic current drops $>35\%$ below Cottrell baseline with unchanged bulk water conductivity.
* **Remediation Steps:**
  1. Trigger automated in-situ cathodic cleaning pulse ($-1.20\text{ V}$ vs. $\text{Ag/AgCl}$ for $15\text{ seconds}$).
  2. If baseline current does not recover to within $10\%$ of initial calibration, isolate flow cell.
  3. Perform manual mechanical polishing using $0.05\ \mu\text{m}$ alumina slurries on microcloth.

### SOP-705: Porous Ceramic Reference Junction Unclogging
* **Condition:** Asymmetric liquid junction potential creates $>15\text{ mV}$ offset error or sluggish response ($t_{90} > 45\text{ s}$).
* **Remediation Steps:**
  1. Inspect for dark silver sulfide ($\text{Ag}_2\text{S}$) precipitate clogging the ceramic frit.
  2. Submerge junction in heated ($50{}^\circ\text{C}$) $1\text{M}$ thiourea in $0.1\text{M}\ \text{HCl}$ for $60\text{ minutes}$.
  3. Replenish saturated $\text{KCl}$ electrolyte reservoir and verify zero potential against standard calomel electrode (SCE).

### SOP-702: ISO 17025 Two-Point Buffer Recalibration Protocol
* **Condition:** Linear baseline slope drifts between $92\%$ and $95\%$ of theoretical Nernstian value ($59.16\text{ mV/pH}$ at $25{}^\circ\text{C}$).
* **Remediation Steps:**
  1. Rinse probe thoroughly with deionized water ($<1\ \mu\text{S/cm}$).
  2. Immerse in NIST-traceable pH 7.00 buffer; adjust zero offset pot/register until reading stabilizes.
  3. Rinse and immerse in NIST-traceable pH 4.01 (or 10.01) buffer; adjust span calibration gain.
  4. Record new slope $S_{\text{new}}$ and timestamp into the probe's Digital Twin profile.

### SOP-102: Catastrophic Transducer Fracture Protocol
* **Condition:** Sudden signal flatline ($\sigma^2 \approx 0$, $\text{SNR} < 5\text{ dB}$, instantaneous potential collapse to $0.0\text{ mV}$).
* **Remediation Steps:**
  1. Immediately de-energize sample intake peristaltic pump.
  2. Issue Emergency Maintenance Work Order with station UUID.
  3. Inspect glass bulb for mechanical cracking, hydrostatic water-hammer shock, or BNC coaxial short.

---

## 3. Metrological Audit Trail & Sustaining Sign-Off

Whenever an anomaly trips:
1. An immutable incident record is generated in the database:
   ```json
   {
     "incident_uuid": "INC-7F89B2A1",
     "node_id": "NODE-WA-01",
     "detected_at": "2026-11-06T18:28:14.236Z",
     "fault_classification": "BIOFOULING_ELECTRODE_SCALING",
     "composite_score": 0.884,
     "confidence": 0.941,
     "astm_sop_code": "ASTM D1293 / SOP-410",
     "status": "OPEN"
   }
   ```
2. When the Sustaining Engineer investigates and resolves the incident via `/api/v1/anomalies/resolve/{incident_uuid}`:
   - The user's name/ID, corrective action taken, and resolution timestamp are cryptographically linked.
   - Status transitions to `RESOLVED`, satisfying ISO 9001 §8.5.1 audit compliance.
