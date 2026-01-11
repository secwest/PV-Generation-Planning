# PV-PowerEstimation: Solar PV Power Yield Calculator

(c) 2025-07-06 Dragos Ruiu

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A comprehensive solar photovoltaic (PV) power yield calculator with global coverage, real weather data, and detailed economic analysis including regional incentives.

## 🌟 Features

- **Global Coverage**: Works for any location worldwide with automatic electricity rate detection
- **Real Weather Data**: Uses Typical Meteorological Year (TMY) data from PVGIS or NREL
- **Physics-Based Modeling**: Hour-by-hour simulation of solar position, temperature effects, and system losses
- **Economic Analysis**: Includes regional electricity rates and applicable solar incentives
- **Educational Tool**: Extensive documentation and tutorials for understanding solar PV systems
- **Multiple Input Methods**: Coordinates, addresses, or interactive mode

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage Examples](#-usage-examples)
- [Understanding PV Systems](#-understanding-pv-systems)
- [System Design Guide](#-system-design-guide)
- [Economic Analysis](#-economic-analysis)
- [Regional Electricity Rates](#-regional-electricity-rates)
- [Solar Incentives by Region](#-solar-incentives-by-region)
- [Technical Details](#-technical-details)
- [Troubleshooting](#-troubleshooting)

## 🚀 Quick Start

```bash
# Install dependencies
pip install pandas numpy requests pvlib

# Run with coordinates
python PV-PowerEstimate.py --lat 37.7749 --lon -122.4194

# Run with address
python PV-PowerEstimate.py --address "San Francisco, CA"

# Interactive mode
python PV-PowerEstimate.py
```

## 💻 Installation

### Requirements
- Python 3.7 or higher
- Required packages: pandas, numpy, requests, pvlib

### Automatic Installation
The script will prompt to install missing packages automatically, or you can install manually:

```bash
pip install pandas numpy requests pvlib
```

### For Debian/Ubuntu Users (Python 3.11+)
If you encounter PEP 668 "externally managed environment" errors:

```bash
# Option 1: Use virtual environment (recommended)
python3 -m venv pv_env
source pv_env/bin/activate
pip install pandas numpy requests pvlib

# Option 2: Install system packages
sudo apt install python3-pandas python3-numpy python3-requests
pip install --user pvlib
```

## 📖 Usage Examples

### Basic Usage

```bash
# Residential system in Toronto
python PV-PowerEstimate.py --address "Toronto, ON" --system-size 8

# Commercial system with custom tilt
python PV-PowerEstimate.py --lat 40.7 --lon -74.0 --system-size 100 --tilt 10

# Detailed analysis with cost assumptions
python PV-PowerEstimate.py --address "Berlin, Germany" --system-size 5 --cost-per-watt 2.50
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--lat`, `--latitude` | Latitude in decimal degrees | - |
| `--lon`, `--longitude` | Longitude in decimal degrees | - |
| `--address` | Street address or location name | - |
| `--system-size` | System size in kW DC | 8.0 |
| `--tilt` | Panel tilt angle in degrees | Latitude |
| `--azimuth` | Panel direction (180=South) | 180 |
| `--module-power` | Individual panel wattage | 400W |
| `--cost-per-watt` | Installed cost per watt DC | Auto |
| `--electricity-rate` | Local electricity rate $/kWh | Auto-detected |

## 🌞 Understanding PV Systems

### How Solar Panels Work

Solar PV systems convert sunlight into electricity through several stages:

```
Sunlight → PV Modules → DC Electricity → Inverter → AC Electricity → Grid/Load
   ↓           ↓              ↓             ↓              ↓
[Irradiance] [Temperature] [Wiring]   [Efficiency]   [Usable Power]
```

### Key Concepts

| Term | Definition | Typical Values |
|------|------------|----------------|
| **Irradiance** | Power of sunlight per unit area | 0-1000 W/m² |
| **Efficiency** | Ratio of electrical output to solar input | 15-22% |
| **Specific Yield** | Annual energy per kW installed | 800-2000 kWh/kWp |
| **Capacity Factor** | Average output / Rated capacity | 10-25% |
| **Performance Ratio** | Actual / Theoretical yield | 75-85% |

### Fundamental Equation

The core physics of PV systems:

**P = G × A × η × PR**

Where:
- P = Power output (W)
- G = Solar irradiance on panel plane (W/m²)
- A = Total array area (m²)
- η = Module efficiency (%)
- PR = Performance ratio (all losses combined) (%)

## 🔧 System Design Guide

### Optimal Tilt Angles

| Purpose | Recommended Tilt | Example (40° latitude) |
|---------|-----------------|------------------------|
| Annual Maximum | Latitude | 40° |
| Summer Maximum | Latitude - 15° | 25° |
| Winter Maximum | Latitude + 15° | 55° |
| Snow Shedding | Latitude + 20-30° | 60-70° |

### Azimuth Orientation Impact

| Direction | Azimuth | Annual Yield |
|-----------|---------|--------------|
| South | 180° | 100% (reference) |
| SE/SW | 135°/225° | 95-97% |
| E/W | 90°/270° | 85-88% |
| NE/NW | 45°/315° | 70-75% |
| North | 0° | 40-60% |

### System Sizing Guidelines

| Application | Typical Size | Space Required | Key Considerations |
|-------------|--------------|----------------|-------------------|
| Residential | 3-10 kW | 200-600 ft² | Roof space, shading |
| Small Commercial | 10-100 kW | 600-6,000 ft² | Demand charges |
| Large Commercial | 100-1000 kW | 0.5-5 acres | Interconnection |
| Utility Scale | >1 MW | 5+ acres/MW | Transmission access |

### Loss Factors Breakdown

| Loss Type | Typical Range | Mitigation Strategy |
|-----------|---------------|---------------------|
| Temperature | 5-15% | Good ventilation, elevated mounting |
| Soiling | 1-5% | Regular cleaning, anti-soiling coating |
| Shading | 0-20% | Careful site selection, trimming |
| Mismatch | 1-3% | Quality modules, power optimizers |
| Wiring | 1-3% | Proper cable sizing, short runs |
| Inverter | 2-4% | Quality inverter, proper sizing |
| Snow | 0-10% | Steep tilt angle, manual clearing |
| Availability | 1-3% | Regular maintenance, monitoring |

## 💰 Economic Analysis

### Current Market Costs (2024-2025)

| System Type | Installed Cost | Notes |
|-------------|----------------|-------|
| Residential (≤10kW) | $2.50-3.00/W | Includes permits, labor |
| Small Commercial (10-100kW) | $1.75-2.25/W | Economies of scale |
| Large Commercial (100kW-1MW) | $1.25-1.75/W | Bulk purchasing |
| Utility Scale (>1MW) | $0.80-1.20/W | Lowest cost/watt |

*Note: Costs have declined ~70% since 2010*

### Key Financial Metrics

| Metric | Description | Typical Values |
|--------|-------------|----------------|
| **Payback Period** | Years to recover investment | 4-10 years |
| **LCOE** | Levelized cost of energy | $0.03-0.10/kWh |
| **ROI** | Return on investment | 10-20% annually |
| **NPV** | Net present value over 25 years | 2-3x initial cost |

## 🌍 Regional Electricity Rates

### North America (2024-2025)

| Region | Rate ($/kWh) | Notes |
|--------|--------------|-------|
| **US Average** | $0.154 | Varies significantly by state |
| Hawaii | $0.447 | Highest in US |
| California | $0.287 | High rates, good solar incentives |
| Texas | $0.143 | Moderate rates, growing solar |
| New York | $0.216 | High rates, strong incentives |
| Washington | $0.103 | Low rates (hydropower) |
| **Canada Average** | $0.140 | CAD 0.20/kWh |
| Ontario | $0.158 | Time-of-use pricing available |
| Quebec | $0.073 | Lowest in North America |
| British Columbia | $0.133 | Tiered residential rates |

### Europe (2024-2025)

| Country | Rate ($/kWh) | Local Currency/kWh |
|---------|--------------|-------------------|
| Germany | $0.397 | €0.378 |
| Denmark | $0.356 | DKK 2.65 |
| Belgium | $0.337 | €0.321 |
| Spain | $0.247 | €0.235 |
| France | $0.231 | €0.220 |
| UK | $0.228 | £0.180 |
| Poland | $0.173 | PLN 0.71 |
| Norway | $0.116 | NOK 1.30 |

### Asia-Pacific (2024-2025)

| Country/Region | Rate ($/kWh) | Local Currency/kWh |
|----------------|--------------|-------------------|
| Japan | $0.228 | ¥31.0 |
| Australia Average | $0.294 | AUD 0.474 |
| South Korea | $0.085 | ₩123.7 |
| China (Beijing) | $0.073 | ¥0.53 |
| India (Delhi) | $0.078 | ₹6.50 |
| Singapore | $0.226 | SGD 0.308 |

## 🎁 Solar Incentives by Region

### United States Federal Incentive

| Program | Type | Value | Expires | Notes |
|---------|------|-------|---------|-------|
| Federal ITC | Tax Credit | 30% | 2032 | Reduces to 26% in 2033, 22% in 2034 |

### US State Incentives (Selected)

| State | Program | Type | Value | Notes |
|-------|---------|------|-------|-------|
| **California** | SGIP | Rebate | $0.20/Wh | For battery storage |
| | DAC-SASH | Rebate | $3.00/W | Low-income communities |
| **New York** | NY-Sun | Rebate | $0.20/W | Declining block |
| | State Tax Credit | Tax Credit | 25% (max $5,000) | Stackable with federal |
| **Massachusetts** | SMART | Performance | $0.15/kWh for 20 years | Production-based |
| **Arizona** | State Tax Credit | Tax Credit | 25% (max $1,000) | Residential only |
| **New Jersey** | SuSI | Performance | $90/MWh for 15 years | Successor program |

### Canada Incentives

| Province | Program | Type | Value | Notes |
|----------|---------|------|-------|-------|
| **Federal** | Greener Homes | Grant | $5,000 max | Plus 0% loan up to $40k |
| **Alberta** | Solar Rebate | Rebate | $0.90/W | Max $10,000 |
| **Ontario** | Net Metering | Credit | 1:1 | Full retail credit |
| **Nova Scotia** | SolarHomes | Rebate | $0.60/W | Max $6,000 |
| **PEI** | Solar Electric | Rebate | $1.00/W | Max $10,000 |

### Europe Incentives

| Country | Program | Type | Value | Notes |
|---------|---------|------|-------|-------|
| **Germany** | Feed-in Tariff | FiT | €0.082/kWh | 20 years, <10kW |
| | VAT Exemption | Tax | 0% VAT | Residential solar |
| **France** | Self-consumption | Premium | €0.38/W | For <3kW |
| **Italy** | Superbonus | Tax Credit | 110% | Through 2025 |
| **Spain** | EU Recovery | Rebate | €0.60/W | Max €3,000 |
| **Netherlands** | Net Metering | Credit | 1:1 | Until 2027 |

### Australia Incentives

| Program | Type | Value | Notes |
|---------|------|-------|-------|
| Federal STC | Rebate | ~$0.45/W | Small-scale certificates |
| Victoria Solar Homes | Rebate | $1,400 | Plus interest-free loan |
| NSW Empowering Homes | Loan | $14,000 | 0% interest |
| Queensland Battery | Rebate | $3,000 | For battery systems |

## 📊 Performance Benchmarks

### Specific Yield by Climate

| Climate Type | Annual Yield | Locations |
|--------------|--------------|-----------|
| Desert | 1,800-2,200 kWh/kWp | Phoenix, Dubai, Atacama |
| Mediterranean | 1,400-1,800 kWh/kWp | California, Spain, Australia |
| Temperate | 1,000-1,400 kWh/kWp | Germany, UK, Canada |
| Tropical | 1,300-1,600 kWh/kWp | Singapore, Hawaii, India |
| High Latitude | 800-1,200 kWh/kWp | Alaska, Norway, Scotland |

### System Performance Indicators

| Metric | Poor | Fair | Good | Excellent |
|--------|------|------|------|-----------|
| Performance Ratio | <70% | 70-75% | 75-82% | >82% |
| Capacity Factor | <12% | 12-17% | 17-22% | >22% |
| Availability | <95% | 95-97% | 97-99% | >99% |
| Degradation Rate | >0.8%/yr | 0.6-0.8%/yr | 0.4-0.6%/yr | <0.4%/yr |

## 🔬 Technical Details

### Modeling Approach

The calculator uses a comprehensive physics-based approach:

1. **Solar Position**: NREL SPA algorithm (±0.0003° accuracy)
2. **Irradiance Transposition**: Perez anisotropic sky model
3. **Temperature Modeling**: Sandia Array Performance Model (SAPM)
4. **DC Power**: Single diode equivalent circuit model
5. **AC Conversion**: Sandia/CEC inverter efficiency curves

### Solar Position Algorithms

**NREL Solar Position Algorithm (SPA)**
- Accuracy: ±0.0003° for years -2000 to 6000
- Accounts for: Nutation, aberration, atmospheric refraction
- Key angles calculated:
  - θz: Zenith angle (0° = sun overhead)
  - γs: Azimuth angle (180° = south)
  - α: Elevation = 90° - θz

**Air Mass Calculation (Kasten & Young):**
```
AM = 1/(cos(θz) + 0.50572×(96.07995-θz)^-1.6364)
```
Valid for θz < 85°, accounts for Earth's curvature

### Irradiance Decomposition and Transposition

**Global Horizontal Irradiance Components:**
```
GHI = DNI × cos(θz) + DHI
```

**Plane of Array (POA) Irradiance:**
```
POA = DNI×cos(AOI) + DHI×F_sky + (GHI)×ρ×F_ground
```

Where:
- AOI: Angle of incidence = arccos(cos(θz)×cos(β) + sin(θz)×sin(β)×cos(γs-γ))
- β: Panel tilt angle
- γ: Panel azimuth angle

**Sky View Factors:**
- Isotropic: F_sky = (1 + cos(β))/2
- Circumsolar: F_cs = max(0, cos(AOI))/cos(θz)
- Horizon brightening: F_hb = sqrt(sin(β))

**Perez Model Coefficients:**
The model uses empirical coefficients based on:
- Clearness index: ε = ((DHI + DNI)/DHI + κ×θz³)/(1 + κ×θz³)
- Brightness index: Δ = DHI × AM / E₀
- Sky clearness bins: 8 categories from overcast to clear

### Temperature Modeling Details

**Sandia Array Performance Model (SAPM):**
```
T_cell = T_amb + G_POA × exp(a + b×v_wind) / 1000
```

**Temperature Model Parameters:**

| Module Type | Racking | a | b | ΔT at 1000 W/m², 0 m/s |
|-------------|---------|---|---|------------------------|
| glass_glass | open_rack | -3.47 | -0.0594 | 30°C |
| glass_glass | close_mount | -2.98 | -0.0471 | 35°C |
| glass_polymer | open_rack | -3.56 | -0.0750 | 29°C |
| glass_polymer | close_mount | -2.81 | -0.0455 | 36°C |
| glass_polymer | insulated_back | -2.00 | -0.0300 | 45°C |

### DC Power Modeling

**Single Diode Equation:**
```
I = I_L - I_0×[exp(q×(V+I×Rs)/(n×k×T×Ns)) - 1] - (V+I×Rs)/Rsh
```

Where:
- I_L = Light current = G/G_ref × (I_L,ref + α_sc×(T_c - T_ref))
- I_0 = Saturation current = I_0,ref × (T_c/T_ref)³ × exp((q×E_g)/(n×k) × (1/T_ref - 1/T_c))
- Rs = Series resistance (Ω)
- Rsh = Shunt resistance (Ω)
- n = Ideality factor (1.0-1.5)
- Ns = Cells in series

**Temperature Coefficients (Typical c-Si):**
- α_sc: +0.045%/°C (current temperature coefficient)
- β_oc: -0.30%/°C (voltage temperature coefficient)
- γ_pmp: -0.40%/°C (power temperature coefficient)

**Simplified SAPM DC Power:**
```
P_dc = G_eff/G_ref × P_dc0 × (1 + γ_pmp×(T_cell - T_ref))
```

### Optical Losses and IAM

**Angle of Incidence Modifier (Physical Model):**
```
IAM = 1 - b₀×(1/cos(AOI) - 1) - b₁×((1/cos(AOI) - 1)²)
```

Typical values:
- b₀ = 0.05 (AR-coated glass)
- b₁ = 0.002

**Spectral Corrections:**
```
M = a₀ + a₁×AM + a₂×PWV + a₃×AM^1.5 + a₄×PWV^0.5
```

Where PWV = Precipitable Water Vapor (cm)

### Inverter Modeling

**Sandia Inverter Model:**
```
P_ac = [(P_dc0 - C₁×(P_dc - P_dc0))/(1 + C₂×(P_dc - P_dc0))] × 
       (P_dc/(P_dc0 + C₃×P_dc0))
```

**CEC Inverter Model:**
```
η = P_ac0/P_dc0 × [(1 - P_night/P_dc) / (1 - P_night/P_dc0)]
```

Where:
- P_ac0: Max AC power at reference conditions
- P_dc0: DC power at which P_ac0 is achieved
- P_night: Night tare loss (self-consumption)

### Data Sources

- **PVGIS**: European Commission's TMY database
  - Coverage: Global
  - Resolution: 5-10 km
  - Years: 10-20 year averages
  - Databases: SARAH (Europe/Africa), NSRDB (Americas), CMSAF (High latitudes)

- **NREL PSM3**: Physical Solar Model v3
  - Coverage: Americas
  - Resolution: 4 km
  - Years: 1998-present
  - Spectral data: 280-4000nm bands
  - Update frequency: Annually

### Key Equations Summary

**Cell Temperature:**
```
T_cell = T_ambient + G_POA × exp(a + b×v_wind)
```

**DC Power:**
```
P_dc = G_eff/G_ref × P_dc0 × (1 + γ×(T_cell - T_ref))
```

**Performance Ratio:**
```
PR = E_actual / (G_POA × P_rated / G_STC)
```

**Energy Yield:**
```
E = ∑(P_ac,i × Δt) = ∫P_ac(t)dt
```

## 🔬 Advanced Technical Topics

### Loss Mechanisms - Detailed Physics

#### Temperature Losses
**Physical Basis:** Semiconductor bandgap narrowing with temperature
```
V_oc(T) = V_oc(T_ref) + β_oc × (T - T_ref)
I_sc(T) = I_sc(T_ref) × (1 + α_sc × (T - T_ref))
FF(T) = FF(T_ref) × (1 + δ_FF × (T - T_ref))
```

**Power Loss:**
```
P_loss,temp = P_STC × γ_pmp × (T_cell - 25°C)
```

Typical γ_pmp values:
- Crystalline Si: -0.35 to -0.45%/°C
- CdTe: -0.25 to -0.35%/°C
- CIGS: -0.30 to -0.40%/°C
- Amorphous Si: -0.15 to -0.25%/°C

#### Soiling Loss Mechanisms
**Accumulation Model (Kimber):**
```
L_soiling(t) = L_max × (1 - exp(-t/τ))
```
Where:
- τ = time constant (20-60 days typical)
- L_max = maximum soiling loss (location dependent)

**Factors affecting τ:**
- Rainfall frequency/intensity
- Particle size distribution
- Panel tilt angle: τ ∝ 1/sin(β)
- Surface properties (anti-soiling coatings)

#### Shading Loss Analysis
**String-Level Impact:**
```
P_shaded = P_unshaded × (1 - F_shade)^n
```
Where n > 1 due to bypass diode effects

**Shading Factor Calculation:**
- Near obstacles: Ray tracing with sun path
- Horizon profile: Elevation angles vs azimuth
- Diffuse shading: View factor integration

**Self-Shading (Row-to-Row):**
```
d_min = h × [cos(β) + sin(β)/tan(α_crit)]
```
Where:
- d_min = minimum row spacing
- h = array height
- α_crit = critical sun elevation (typically winter solstice)

#### Mismatch Loss Analysis
**Statistical Distribution:**
```
σ_mismatch = sqrt(σ_Pmax² + σ_FF² + σ_Isc² + σ_Voc²)
L_mismatch ≈ σ_mismatch²/2
```

**Mitigation Strategies:**
- Module binning (±2% power tolerance)
- String-level MPPT
- DC optimizers (reduce to <0.5%)

### Degradation Mechanisms

#### Light-Induced Degradation (LID)
**Physical Process:** Boron-oxygen complex formation
```
P(t) = P_0 × (1 - LID_∞ × (1 - exp(-t/τ_LID)))
```
Where:
- LID_∞ = 1-3% (stabilized loss)
- τ_LID = 100-1000 hours

**Mitigation:**
- n-type wafers (no boron)
- Gallium doping
- Light soaking pre-treatment

#### Long-Term Degradation Modes

| Mechanism | Rate (%/year) | Observable Signs |
|-----------|---------------|------------------|
| EVA browning | 0.1-0.3 | Yellowing, reduced transmission |
| Solder bond fatigue | 0.05-0.2 | Increased Rs, hot spots |
| Backsheet cracking | 0.1-0.3 | Moisture ingress, ground faults |
| Metallization corrosion | 0.05-0.15 | Grid line thinning |
| AR coating degradation | 0.05-0.1 | Increased reflection |
| Encapsulant delamination | 0.1-0.5 | Bubbles, moisture paths |

**Arrhenius Model for Thermal Degradation:**
```
R_deg = A × exp(-E_a/(k×T))
```
Where E_a = activation energy (0.5-1.5 eV typical)

### Advanced Irradiance Modeling

#### Spectral Effects
**Average Photon Energy (APE):**
```
APE = ∫E(λ)×λ dλ / ∫E(λ) dλ
```

**Module Spectral Response Correction:**
```
G_eff = G × M_spectral × M_AOI × (1 - L_soiling)
```

#### Transposition Model Comparison

| Model | Accuracy | Computation | Best Use Case |
|-------|----------|------------|---------------|
| Isotropic | ±10% | Fast | Overcast climates |
| Klucher | ±5-7% | Fast | Partly cloudy |
| Hay-Davies | ±4-6% | Medium | General purpose |
| Reindl | ±3-5% | Medium | Enhanced accuracy |
| Perez | ±2-4% | Slow | Research grade |

#### Diffuse Irradiance Models

**Erbs Model:**
```
k_d = {
  1.0 - 0.09×k_t                    for k_t ≤ 0.22
  0.9511 - 0.1604×k_t + 4.388×k_t² - 16.638×k_t³ + 12.336×k_t⁴   for 0.22 < k_t ≤ 0.80
  0.165                             for k_t > 0.80
}
```
Where k_t = clearness index = GHI/E_extraterrestrial

### System Design Optimization

#### DC/AC Ratio Optimization
**Economic Optimum:**
```
ILR_opt = f(C_dc/C_ac, climate, electricity_rate)
```

Typical values:
- Low irradiance: 1.1-1.2
- Moderate irradiance: 1.2-1.3
- High irradiance: 1.3-1.5

**Clipping Loss Estimation:**
```
L_clip = ∫max(0, P_dc - P_inv,rated) dt / ∫P_dc dt
```

#### Wire Sizing Calculations
**DC Wire Losses:**
```
P_loss = I² × R = I² × (ρ × L / A)
V_drop = I × R = I × (ρ × L / A)
```

Design criteria:
- Voltage drop < 2% (DC side)
- Voltage drop < 1% (AC side)
- Temperature derating per NEC

**Optimum Wire Gauge:**
```
A_opt = sqrt(ρ × L × I × C_wire / (V × η × C_energy × t))
```

### Bifacial Module Modeling

**Rear Irradiance Estimation:**
```
G_rear = G_ground_reflected × VF_ground + G_diffuse × VF_sky
```

**Bifacial Gain:**
```
BG = (P_front + φ × P_rear) / P_front_only - 1
```
Where φ = bifaciality factor (0.65-0.90)

**View Factors:**
```
VF_ground = (1 - cos(β))/2
VF_sky = (1 + cos(β))/2
```

### Tracking System Analysis

#### Single-Axis Tracking
**Rotation Angle:**
```
θ_track = arctan(sin(γ_s - γ_axis)/tan(α_s))
```

**Backtracking Algorithm:**
```
θ_max = arccos(GCR × cos(θ_sun))
```
Where GCR = Ground Coverage Ratio

**Energy Gain Estimation:**
- E-W horizontal axis: +15-25%
- N-S horizontal axis: +20-30%
- Tilted axis: +25-35%

#### Dual-Axis Tracking
**Control Equations:**
```
β_track = θ_z (zenith tracking)
γ_track = γ_s (azimuth tracking)
```

Energy gain: +30-40% (climate dependent)

### Uncertainty Analysis

#### Sources of Uncertainty

| Source | Typical Range | Type |
|--------|---------------|------|
| Solar resource | ±4-6% | Epistemic |
| Temperature | ±2-3% | Aleatory |
| Soiling | ±1-3% | Both |
| Degradation | ±0.1-0.2%/yr | Epistemic |
| Shading | ±2-5% | Epistemic |
| Equipment tolerance | ±3% | Aleatory |

#### Uncertainty Propagation
**Monte Carlo Approach:**
```
σ_total = sqrt(Σσ_i²) (uncorrelated)
σ_total = Σσ_i (fully correlated)
```

**P-Values:**
- P50: Median estimate
- P90: 90% probability of exceedance
- P99: 99% probability of exceedance

```
P90 = P50 × (1 - 1.28 × σ_total)
```

### Grid Integration Considerations

#### Power Quality Requirements
**Voltage Regulation:**
```
V_poc = V_grid + I × Z_line
```

**Power Factor Control:**
```
Q = P × tan(arccos(PF_target))
```

#### Ramp Rate Limitations
**Cloud Edge Effects:**
```
dP/dt_max = system_size × 0.7 / t_cloud
```
Where t_cloud = cloud passage time

**Mitigation:**
- Energy storage
- Curtailment
- Forecasting integration

### Monitoring and Validation

#### Key Performance Indicators

**Performance Index:**
```
PI = E_measured / E_expected
```

**Temperature-Corrected PR:**
```
PR_tc = PR_measured / (1 + γ × (T_avg - T_ref))
```

**Availability:**
```
A = uptime / total_time
```

#### Data Quality Checks
- Irradiance: 0 < GHI < 1.2 × E_extraterrestrial
- Temperature: -40°C < T < 60°C
- Power: 0 < P < P_rated × 1.1
- Night values: P = 0 when GHI < 10 W/m²

## 🛠 Troubleshooting

### Common Issues and Solutions

| Issue | Possible Cause | Solution |
|-------|----------------|----------|
| Low yield | Shading, wrong tilt/azimuth | Check for obstacles, verify angles |
| Zero output | Failed data fetch | Check internet connection |
| High temperature losses | Poor ventilation | Consider open rack mounting |
| Unexpected costs | Old market data | Verify local installer quotes |

### Validation Checklist

- [ ] Verify location coordinates are correct
- [ ] Check for shading from nearby objects
- [ ] Confirm system size matches roof space
- [ ] Account for all applicable incentives
- [ ] Consider seasonal variations in output
- [ ] Include maintenance costs in ROI

## 📚 Educational Resources

### Understanding Your Results

- **kWh (kilowatt-hour)**: Energy unit, like "miles" for your car
- **kW (kilowatt)**: Power unit, like "horsepower" for your car  
- **Specific Yield**: Energy per installed capacity - allows fair comparison
- **Capacity Factor**: Average output / maximum possible output
- **Performance Ratio**: Actual performance / theoretical performance

### Weather Data Processing

#### TMY Data Construction
Typical Meteorological Year data represents long-term patterns:

**Statistical Selection Process:**
1. Analyze 10-20 years of historical data
2. For each month, calculate cumulative distribution functions (CDFs)
3. Select month with CDF closest to long-term average
4. Smooth transitions between months

**Preserved Statistics:**
- Mean values (irradiance, temperature)
- Extremes and variability
- Temporal correlations (persistence)
- Diurnal patterns

#### Satellite-Derived Irradiance

**Physical Model Chain:**
```
Satellite Image → Cloud Index → Clear Sky Model → Surface Irradiance
```

**Cloud Index:**
```
n = (ρ_measured - ρ_clear) / (ρ_cloud - ρ_clear)
```

**Heliosat Method:**
```
GHI = GHI_clear × (1 - n × k_cloud)
```

#### Data Validation Rules

**Physical Constraints:**
```
0 ≤ GHI ≤ 1.2 × E_0 × cos(θ_z)
0 ≤ DNI ≤ 0.95 × E_0
0 ≤ DHI ≤ 0.8 × GHI
GHI = DNI × cos(θ_z) + DHI (±5% tolerance)
```

**Quality Control Flags:**
- Extremely rare limits (physical possible)
- Rare limits (statistically rare)
- Common limits (typical ranges)

### Solar Resource Assessment Best Practices

#### Bankable Resource Assessment
1. **Data Sources:**
   - Ground measurements: ±2-3% (highest accuracy)
   - Satellite data: ±4-5% (good coverage)
   - Reanalysis: ±6-8% (long-term trends)

2. **Minimum Requirements:**
   - 10+ years of data
   - Hourly or sub-hourly resolution
   - Site adaptation with ground data
   - Uncertainty quantification

3. **Interannual Variability:**
   ```
   σ_interannual = std(annual_GHI) / mean(annual_GHI)
   ```
   Typical: 3-5% for GHI, 5-10% for DNI

#### Climate Change Considerations
**Projected Changes (2050 vs 2020):**
- Temperature: +1-3°C → -0.4 to -1.2% yield
- Cloud patterns: Regional variations ±5%
- Extreme events: Increased frequency

### Module Technology Comparison

| Technology | Efficiency | Temp Coef | Spectral Response | Cost |
|------------|-----------|-----------|-------------------|------|
| Mono c-Si | 20-22% | -0.35%/°C | Good IR | $ |
| Poly c-Si | 17-19% | -0.40%/°C | Standard | $ |
| PERC | 21-23% | -0.32%/°C | Enhanced IR | $$ |
| HJT | 22-25% | -0.25%/°C | Excellent | $$ |
| TOPCon | 23-25% | -0.30%/°C | Very good | $$ |
| CdTe | 17-19% | -0.25%/°C | Good low light | $ |
| CIGS | 16-18% | -0.35%/°C | Wide spectrum | $ |

### Advanced Modeling Topics

#### Non-Linear Effects
**Module Efficiency vs Irradiance:**
```
η(G) = η_STC × [a × ln(G/G_STC) + b]
```
Low-light performance critical for cloudy climates

**Thermal Transients:**
```
dT/dt = (G × α - U × (T - T_amb)) / (m × c_p)
```
Time constant: 5-15 minutes

#### Snow Modeling
**Coverage Probability:**
```
P_snow = f(snowfall, T_air, wind, tilt)
```

**Sliding Threshold:**
```
Critical angle ≈ 27° + 0.4 × T_surface
```

#### Horizon Profile Impact
**Beam Shading Hours:**
```
t_shade = Σ(max(0, h_horizon(γ) - h_sun(γ,t)))
```

**Annual Loss Estimation:**
```
L_horizon = ∫(DNI × shade_flag) dt / ∫DNI dt
```

### Next Steps After Analysis

1. **Get Multiple Quotes**: Compare at least 3 installers
2. **Verify Incentives**: Confirm eligibility with local authorities
3. **Check Warranties**: 25+ years for panels, 10+ for inverters
4. **Plan Monitoring**: Real-time systems recommended
5. **Consider Storage**: Battery costs declining rapidly
6. **Professional Site Assessment**: Shading analysis, structural evaluation
7. **Interconnection Application**: Utility requirements vary
8. **Financing Options**: Loans, leases, PPAs comparison

### Recommended Reading

**Technical Standards:**
- IEC 61724: PV System Performance Monitoring
- IEC 61853: PV Module Performance Testing
- IEC 62446: Grid Connected PV Systems
- IEC 61730: PV Module Safety Qualification

**Key Research Papers:**
- Perez et al. (1990): "Modeling daylight availability and irradiance components"
- King et al. (2004): "Photovoltaic Array Performance Model" (SAND2004-3535)
- Holmgren et al. (2018): "pvlib python: a python package for modeling solar energy systems"

**Industry Resources:**
- NREL System Advisor Model (SAM) documentation
- PVsyst help files and methodology
- IEA PVPS Task 13: Performance and Reliability
- Sandia PV Performance Modeling Collaborative

## 📄 License

This project is licensed under the BSD 3-Clause License - see the LICENSE file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 💻 API and Programmatic Usage

### Using as a Python Module

```python
from PV_PowerEstimate import SolarPVCalculator, SystemConfig, LocationInfo

# Initialize calculator
calc = SolarPVCalculator(
    latitude=37.7749,
    longitude=-122.4194,
    altitude=52.0
)

# Configure system
config = SystemConfig()
config.surface_tilt = 30.0
config.surface_azimuth = 180.0
config.modules_per_string = 20
config.strings_per_inverter = 2

# Fetch weather data
weather_data = calc.fetch_pvgis_data()

# Run simulation
results, system_size = calc.calculate_pv_output(weather_data, config)

# Calculate yields
monthly, annual_energy, specific_yield, capacity_factor = \
    calc.calculate_monthly_yield(results, system_size)
```

### Custom Loss Scenarios

```python
# High soiling desert environment
config.soiling_loss = 6.0

# Heavy shading urban environment  
config.shading_loss = 15.0

# Aged system (10 years)
config.age_loss = 5.0  # 0.5%/year × 10 years

# Snow-prone location
config.snow_loss = 8.0
config.surface_tilt = 45.0  # Steeper for snow shedding
```

### Batch Processing Multiple Sites

```python
sites = [
    {"name": "Site A", "lat": 37.7749, "lon": -122.4194},
    {"name": "Site B", "lat": 40.7128, "lon": -74.0060},
    {"name": "Site C", "lat": 51.5074, "lon": -0.1278}
]

results_summary = []

for site in sites:
    calc = SolarPVCalculator(site['lat'], site['lon'])
    weather = calc.fetch_pvgis_data()
    results, size = calc.calculate_pv_output(weather)
    _, annual, specific, cf = calc.calculate_monthly_yield(results, size)
    
    results_summary.append({
        'site': site['name'],
        'annual_kwh': annual,
        'specific_yield': specific,
        'capacity_factor': cf
    })
```

### Integration with External APIs

```python
# NREL API integration
calculator = SolarPVCalculator(lat, lon)
weather_data = calculator.fetch_nrel_psm3_data(
    year=2020,
    api_key="your_nrel_api_key"
)

# Custom weather data
import pandas as pd
custom_weather = pd.DataFrame({
    'ghi': ghi_values,
    'dni': dni_values,
    'dhi': dhi_values,
    'temp_air': temperature_values,
    'wind_speed': wind_values
}, index=datetime_index)

results, _ = calculator.calculate_pv_output(custom_weather, config)
```

### Output Data Structure

```python
# Hourly results DataFrame columns
results.columns = [
    'dc_power',           # DC power before inverter (kW)
    'ac_power',           # AC power after losses (kW)
    'cell_temperature',   # Module temperature (°C)
    'effective_irradiance', # POA irradiance after losses (W/m²)
    'temperature_loss'    # Temperature derating factor (%)
]

# Monthly summary DataFrame
monthly.columns = [
    'energy_kwh',      # Total monthly energy
    'specific_yield',  # kWh/kWp for the month
    'daily_energy',    # Average daily energy
    'cell_temperature', # Average cell temperature
    'effective_irradiance' # Average POA irradiance
]
```

## 📧 Contact

- Author: Dragos Ruiu
- Email: dr@secwest.net
- GitHub: [https://github.com/secwest/PV-Generation-Planning](https://github.com/secwest/PV-Generation-Planning)

## 🙏 Acknowledgments

- pvlib python developers for the excellent modeling library
- PVGIS and NREL for providing free weather data
- OpenStreetMap for geocoding services

## 📖 Technical Glossary

### Solar Resource Terms
- **AM (Air Mass)**: Path length of sunlight through atmosphere relative to zenith path. AM1.5 = standard test condition
- **AOI (Angle of Incidence)**: Angle between sun ray and panel normal vector
- **APE (Average Photon Energy)**: Spectral quality metric affecting module performance
- **DHI (Diffuse Horizontal Irradiance)**: Scattered sky radiation on horizontal surface (W/m²)
- **DNI (Direct Normal Irradiance)**: Beam radiation from sun disk on tracking surface (W/m²)
- **GHI (Global Horizontal Irradiance)**: Total radiation on horizontal surface = DNI×cos(θz) + DHI
- **GTI/POA (Global Tilted Irradiance)**: Total radiation on tilted panel surface
- **Clearness Index (kt)**: GHI / Extraterrestrial radiation, indicates sky clarity
- **Linke Turbidity**: Atmospheric opacity measure affecting DNI

### Module Physics Terms
- **Bandgap (Eg)**: Energy difference between valence and conduction bands (~1.1 eV for Si)
- **Fill Factor (FF)**: (Vmp × Imp) / (Voc × Isc), indicates I-V curve quality
- **Ideality Factor (n)**: Diode quality factor, 1 = ideal, >1 = recombination
- **Isc**: Short-circuit current at zero voltage
- **Voc**: Open-circuit voltage at zero current
- **Imp, Vmp**: Current and voltage at maximum power point
- **Series Resistance (Rs)**: Internal resistance reducing voltage
- **Shunt Resistance (Rsh)**: Leakage path reducing current
- **Quantum Efficiency**: Electrons per incident photon vs wavelength
- **Spectral Response**: Amps per watt vs wavelength

### Temperature Coefficients
- **α (alpha)**: Current temperature coefficient (%/°C or A/°C)
- **β (beta)**: Voltage temperature coefficient (%/°C or V/°C)
- **γ (gamma)**: Power temperature coefficient (%/°C)
- **δ (delta)**: Fill factor temperature coefficient (%/°C)

### System Design Terms
- **BOS (Balance of System)**: All non-module components
- **DC/AC Ratio (ILR)**: DC array size / AC inverter size
- **GCR (Ground Coverage Ratio)**: Array area / land area
- **MBB (Multi-Busbar)**: Module interconnection technology
- **MLPE (Module Level Power Electronics)**: Optimizers/microinverters
- **MPPT (Maximum Power Point Tracking)**: Algorithm to optimize power extraction
- **String**: Modules connected in series
- **Combiner Box**: Parallel connection point for strings

### Performance Metrics
- **Availability**: Fraction of time system is operational
- **Capacity Factor (CF)**: Average power / Nameplate power
- **CUF (Capacity Utilization Factor)**: Same as CF
- **Performance Ratio (PR)**: Actual yield / Reference yield
- **Reference Yield (Yr)**: In-plane irradiation / 1000 W/m²
- **Specific Yield (Yf)**: kWh per kWp installed
- **System Efficiency**: AC energy out / Solar energy in

### Loss Mechanisms
- **IAM (Incidence Angle Modifier)**: Optical loss vs angle
- **LID (Light-Induced Degradation)**: Initial power loss from B-O defects
- **PID (Potential-Induced Degradation)**: Voltage stress degradation
- **Clipping**: Power loss when DC exceeds inverter capacity
- **Curtailment**: Intentional power reduction for grid stability
- **Mismatch**: Loss from non-uniform module parameters
- **Soiling Ratio**: Actual output / Clean output

### Advanced Technologies
- **Bifacial Gain**: Additional energy from rear side
- **Half-Cell**: Module design reducing resistive losses
- **HJT (Heterojunction)**: High-efficiency c-Si technology
- **PERC (Passivated Emitter Rear Cell)**: Enhanced c-Si design
- **TOPCon (Tunnel Oxide Passivated Contact)**: Advanced c-Si
- **Shingled Cells**: Overlapping cell interconnection

### Modeling Terms
- **ASHRAE Model**: Clear sky radiation model
- **Bird Model**: Spectral irradiance model
- **Erbs Model**: Diffuse fraction correlation
- **Hay-Davies Model**: Transposition model with circumsolar
- **Isotropic Model**: Uniform sky radiance assumption
- **Kasten-Young**: Air mass formula
- **Perez Model**: Anisotropic sky radiance model
- **SAPM**: Sandia Array Performance Model
- **SPA**: Solar Position Algorithm
- **TMY**: Typical Meteorological Year dataset

### Electrical Terms
- **Anti-Islanding**: Safety feature preventing backfeed
- **Grid Parity**: Solar LCOE equals grid electricity cost
- **Islanding**: Operating disconnected from grid
- **Power Factor**: Real power / Apparent power
- **Reactive Power**: Non-working power for grid stability
- **RMS (Root Mean Square)**: Effective AC value
- **THD (Total Harmonic Distortion)**: Power quality metric

### Economic Terms
- **CAPEX**: Capital expenditure ($/W)
- **Discount Rate**: Time value of money for NPV
- **IRR (Internal Rate of Return)**: Discount rate for NPV = 0
- **LCOE (Levelized Cost of Energy)**: Total cost / Total energy
- **NPV (Net Present Value)**: Present value of cash flows
- **O&M (Operations & Maintenance)**: Ongoing costs
- **OPEX**: Operating expenditure ($/kW-year)
- **PPA (Power Purchase Agreement)**: Long-term energy contract

### Weather Data Terms
- **Albedo**: Ground reflectance (0-1)
- **Precipitable Water**: Atmospheric water vapor (cm)
- **Pressure**: Atmospheric pressure (mbar)
- **Turbidity**: Atmospheric haziness
- **Wind Direction**: Compass bearing of wind origin
- **Wind Speed**: Horizontal wind velocity (m/s)

### Standards and Test Conditions
- **IEC 61215**: Crystalline silicon module qualification
- **IEC 61646**: Thin-film module qualification  
- **IEC 61724**: PV system performance standards
- **IEC 61730**: Module safety qualification
- **IEC 62446**: Grid-connected system testing
- **NOCT**: Nominal Operating Cell Temperature (45±2°C)
- **STC**: Standard Test Conditions (1000 W/m², 25°C, AM1.5)

---

*Disclaimer: This tool provides estimates based on typical conditions. Actual performance may vary. Always consult with professional installers for system design and obtain multiple quotes for accurate pricing.*
