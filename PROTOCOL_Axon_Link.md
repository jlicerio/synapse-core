# PROTOCOL: Synapse Axon-Link (Axon-Link) v2.3

**Version**: 2.4 (Efficiency-Optimized / Tape Relay)
**System**: Synapse Learning Suite v6.5.2
**Standard**: Universal Indicator Bus (200.PB) & Universal Execution Bus (100.BROTEP)

---

## 1. Universal Indicator Bus (200.PB)
Used by Sub-Hubs to relay categorical consensus to the Master Hub.

### **Base: 200.0**
- **Pulse (Intensity)**: (Output - 200.0) * 10
    - `0`: Neutral
    - `1`: Active (Agree)
    - `2`: Unanimous / Extreme
    - `3/4`: Structural Anticipation (Long/Short)
    - `5`: Hard Wall
    - `6`: Expansion Surge (Positive Alpha)
    - `7`: Volatility Squeeze (Negative Alpha)
    - `8`: Absorption / Tape Active
- **Bias (Directionality)**: (Output - 200.0) * 100 % 10
    - `0`: Neutral
    - `1`: Bullish
    - `2`: Bearish

### **Standard Encoding (Pine Script)**
```pine
float Synapse_bus = 200.0 + (pulse * 0.1) + (bias == 1 ? 1 : bias == -1 ? 2 : 0) * 0.01
```

---

## 2. Universal Execution Bus (100.BROTEP)
Used by the Master Hub to relay final trade decisions to execution guards and auditors.

### **Base: 100.0**
- **Bit 1: Bias** (0, 1, 2)
- **Bit 2: Resonance** (1, 2, 3)
- **Bit 3: Risk/Reward (Adaptive RR)** (1, 2, 3, 4)
- **Bit 4: Entry Type** (1, 2)
- **Bit 5: Trap Mode** (1, 2)
- **Bit 6: Volatility Scalar** (1:Norm, 2:Turbid, 3:Calm, 4:Extreme)
- **Bit 7: Pulse/Atten** (0-5)
- **Bit 8-10: ComboID (Bitmask)**

---

## 3. Sub-Hub Slot Assignments
| Slot | Category | Component | Resolution |
| :--- | :--- | :--- | :--- |
| **A** | Order Flow | Velocity & Imbalance | 5s |
| **B** | Institutional | Zone Brain (HTF Landmarks) | 1m/5m/1h |
| **C** | Ensemble ML | Neural Consensus | 5s |
| **D** | Structural Vitality | Exhaustion & Divergence | 5s (1s Clusters) |
| **E** | Momentum | Categorical Oscillators | 1m/5m/15m |

---

## 4. Ouroboros Feedback (100.PB)
Used for cross-script auditing (Master -> SubHubs).
- **100.1**: Win
- **100.2**: Loss
- **100.3**: Break Even
