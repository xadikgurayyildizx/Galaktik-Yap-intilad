# Galaktik-Yap-intilad

## Energy Resonance Mechanic

A Ursina-based Python application featuring an energy resonance system with dynamic visual effects.

### Features

- **Energy System**: Press spacebar to add energy (max 6 units)
- **Natural Decay**: Energy naturally decreases over time (97% per frame)
- **Resonance Movement**: Core entity oscillates vertically based on energy level
- **Breathing Scale**: Core entity pulses with a breathing effect
- **Orthographic Camera**: Clean 2D visualization

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
python energy_resonance.py
```

**Controls:**
- Press `SPACE` to add energy to the system
- Watch the energy value in console output

### Technical Details

- **Time Flow**: Continuous time accumulation for animation
- **Resonance Formula**: `y = sin(time * 2) * (0.5 + energy * 0.2)`
- **Breathing Scale**: `scale = 0.4 + sin(time * 4) * 0.05`
- **Energy Decay**: Multiplicative decay of 0.97 per frame
