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

### Data Sources

- **PVGIS**: European Commission's TMY database
  - Coverage: Global
  - Resolution: 5-10 km
  - Years: 10-20 year averages

- **NREL PSM3**: Physical Solar Model v3
  - Coverage: Americas
  - Resolution: 4 km
  - Years: 1998-present

### Key Equations

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

### Next Steps After Analysis

1. **Get Multiple Quotes**: Compare at least 3 installers
2. **Verify Incentives**: Confirm eligibility with local authorities
3. **Check Warranties**: 25+ years for panels, 10+ for inverters
4. **Plan Monitoring**: Real-time systems recommended
5. **Consider Storage**: Battery costs declining rapidly

## 📄 License

This project is licensed under the BSD 3-Clause License - see the LICENSE file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

- Author: Dragos Ruiu
- Email: dr@secwest.net
- GitHub: [https://github.com/secwest/PV-Generation-Planning](https://github.com/secwest/PV-Generation-Planning)

## 🙏 Acknowledgments

- pvlib python developers for the excellent modeling library
- PVGIS and NREL for providing free weather data
- OpenStreetMap for geocoding services

---

*Disclaimer: This tool provides estimates based on typical conditions. Actual performance may vary. Always consult with professional installers for system design and obtain multiple quotes for accurate pricing.*
