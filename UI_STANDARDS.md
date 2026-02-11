# Synapse UI Standards & HUD Protocols

This document defines the visual and interaction standards for the Synapse Learning Suite to ensure a clean, professional, and non-overlapping user experience across all timeframes (1s - 15m).

## 1. HUD Positioning (Anti-Overlap)

Every script that renders a dashboard table MUST include a `HUD Position` input. To prevent visual clutter, the following default positions are standardized:

| Component | Default Position | Purpose |
| :--- | :--- | :--- |
| Component | Default Position | Purpose |
| :--- | :--- | :--- |
| **Synapse Master Hub** | `position.bottom_right` | Primary Executive Command Center (A-E) |
| **Efficacy Oracle** | `position.top_left` | Performance Auditing & 5-Node Win Rates |
| **Cerebellum Aggregator** | `position.top_right` | Neural Activation & Synaptic Debug |
| **Vitality Hub (Slot D)** | `position.middle_right`| Exhaustion & Divergence Feed |
| **Momentum Hub (Slot E)**| `position.middle_left` | MTF Trend Alignment Diagnostics |
| **ML/OF Sub-Hubs** | `position.bottom_right` | Optimized for Pane 2 (Consensus Overlays) |

### Implementation Pattern (Pine Script v6)
```pine
// Input
table_pos = input.string(position.bottom_right, "HUD Position", 
     options=[position.top_right, position.bottom_right, position.top_left, position.bottom_left, position.middle_right, position.middle_left], 
     group="UI Settings")

// Initialization
var table hud = table.new(table_pos, columns, rows, bgcolor=color.new(color.black, 40), border_width=1)
```

## 2. Color Language

To maintain cognitive speed during fast trading, all HUDs must follow the Synapse Color Identity:

*   **Aqua (`color.aqua`)**: Primary Headers & Bus Outputs.
*   **Lime (`color.lime`)**: High Conviction / Positive Efficacy / Bullish Bias.
*   **Red (`color.red`)**: Low Conviction / Negative Efficacy / Bearish Bias.
*   **Orange (`color.orange`)**: Critical Alerts / Special Modes (Overdrive, Anti-Synapse).
*   **Gray (`color.gray`)**: Passive Metrics / Neutrals.

## 3. Bus Output Formatting

All scripts displaying the `Synapse_bus` value on their table MUST use the following format to avoid the "2200" overflow bug:

```pine
// Correct way to display Axon-Link values
table.cell(hud, col, row, str.tostring(Synapse_bus, "#.##"), text_color=color.aqua)
```

## 4. UI Density Standards

- **Tables**: Use `size.small` for data cells to maximize screen real estate.
- **Backgrounds**: Use `color.new(color.black, 40)` to ensure readability over price action without obscuring the chart.
- **Refresh Rate**: HUD updates should be gated by `barstate.islast` to prevent flickering on lower timeframes (1s/5s).
