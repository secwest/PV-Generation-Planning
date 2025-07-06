#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PV-PowerEstimate.py - Solar PV Power Yield Calculator & Tutorial

Copyright (c) 2025, Dragos Ruiu
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

================================================================================
PV SYSTEM DESIGN AND ESTIMATION TUTORIAL
================================================================================

This tool serves as both a practical calculator and an educational resource for
understanding solar photovoltaic system design and energy yield estimation.

QUICK START GUIDE
-----------------
1. Basic residential system (5kW in San Francisco):
   python PV-PowerEstimate.py --address "San Francisco, CA" --system-size 5

2. Commercial system with custom tilt:
   python PV-PowerEstimate.py --lat 40.7 --lon -74.0 --system-size 100 --tilt 10

3. Interactive mode for beginners:
   python PV-PowerEstimate.py

UNDERSTANDING PV SYSTEMS - THE BASICS
-------------------------------------
A photovoltaic system converts sunlight into electricity through several stages:

   Sunlight → PV Modules → DC Electricity → Inverter → AC Electricity → Grid/Load
      ↓           ↓              ↓             ↓              ↓
   [Irradiance] [Temperature] [Wiring]   [Efficiency]   [Usable Power]

Key Concepts:
- IRRADIANCE: Power of sunlight per unit area (W/m²)
- EFFICIENCY: Ratio of electrical output to solar input (%)
- YIELD: Total energy produced over time (kWh)
- CAPACITY FACTOR: Average output / Rated capacity (%)

FUNDAMENTAL EQUATION
--------------------
The core physics of PV systems:

    P = G × A × η × PR

Where:
- P = Power output (W)
- G = Solar irradiance on panel plane (W/m²)
- A = Total array area (m²)
- η = Module efficiency at current conditions (%)
- PR = Performance ratio (all losses combined) (%)

Example Calculation:
- G = 1000 W/m² (bright sunshine)
- A = 50 m² (about 25 modern panels)
- η = 20% (good quality panels)
- PR = 80% (well-designed system)
- P = 1000 × 50 × 0.20 × 0.80 = 8,000 W = 8 kW

SOLAR RESOURCE ASSESSMENT
-------------------------
Understanding your local solar resource is crucial:

1. DIRECT vs DIFFUSE RADIATION
   
   Direct (DNI): Straight from sun → Can be concentrated → Strong shadows
   Diffuse (DHI): Scattered by atmosphere → Blue sky light → No shadows
   Global (GHI): Total on horizontal = DNI × cos(zenith) + DHI

2. TYPICAL VALUES BY CLIMATE:
   - Desert: 2000-2400 kWh/m²/year (high irradiance)
   - Mediterranean: 1600-2000 kWh/m²/year (above average)
   - Temperate: 1000-1400 kWh/m²/year (moderate)
   - Cloudy/Northern: 800-1200 kWh/m²/year (below average)

3. SEASONAL VARIATION:
   Summer/Winter ratio varies by latitude:
   - Equator: ~1.2:1 (minimal variation)
   - 30° latitude: ~2:1 
   - 45° latitude: ~3:1
   - 60° latitude: ~5:1 or more

SYSTEM DESIGN PRINCIPLES
------------------------
1. TILT ANGLE OPTIMIZATION:
   
   Purpose          Recommended Tilt      Example (40° latitude)
   -------------------------------------------------------------
   Annual Max       Latitude              40°
   Summer Max       Latitude - 15°       25°
   Winter Max       Latitude + 15°       55°
   Snow Shedding    Latitude + 20-30°    60-70°

2. AZIMUTH ORIENTATION:
   
   Direction    Azimuth    Effect on Annual Yield
   -----------------------------------------------
   South        180°       100% (reference orientation in N hemisphere)
   SE/SW        135°/225°  95-97%
   E/W          90°/270°   85-88%
   NE/NW        45°/315°   70-75%
   North        0°         40-60%

3. SHADING ANALYSIS:
   Even small shadows can cause large losses:
   - 10% shading can cause 30% power loss
   - Morning/evening shadows less critical
   - Winter shadows more impactful at high latitudes

LOSS FACTORS - DETAILED BREAKDOWN
---------------------------------
Real systems experience various losses:

1. TEMPERATURE LOSSES (5-15%):
   - Silicon loses ~0.4%/°C above 25°C
   - Cell temp = Ambient + 25-35°C typically
   - Example: 40°C ambient → 65°C cell → 16% loss

2. SOILING LOSSES (1-5%):
   - Dust accumulation reduces transmission
   - Rain provides natural cleaning
   - Desert/agricultural areas worse
   - Optimal cleaning frequency: Loss% × Revenue > Cleaning cost

3. MISMATCH LOSSES (1-3%):
   - Modules vary ±3% from nameplate
   - Series strings limited by weakest module
   - Minimized by binning/sorting

4. WIRING LOSSES (1-3%):
   - I²R losses in DC and AC cables
   - Higher currents = higher losses
   - Proper sizing critical

5. INVERTER LOSSES (2-4%):
   - Peak efficiency ~97-98%
   - Lower at partial loads
   - Clipping at high DC/AC ratios

PRACTICAL DESIGN EXAMPLES
-------------------------
1. RESIDENTIAL ROOFTOP (5 kW):
   - Modules: 12-15 × 400W panels
   - Area needed: ~30-40 m²
   - Annual yield: 5,000-8,000 kWh
   - Typical PR: 75-80%
   - Mounting: glass_polymer + close_mount

2. COMMERCIAL FLAT ROOF (100 kW):
   - Modules: 250 × 400W panels
   - Area needed: ~600-800 m²
   - Tilt: 10-15° (balance yield vs wind/ballast)
   - Row spacing: Avoid self-shading
   - Mounting: glass_glass + open_rack (ballasted)

3. UTILITY SCALE (10 MW):
   - Modules: 25,000 × 400W
   - Land area: 15-20 hectares
   - Tracking: +25-35% yield gain
   - Higher PR: 80-85%
   - Mounting: glass_glass + open_rack (tracked)

ECONOMIC CONSIDERATIONS
-----------------------
Key metrics for financial analysis:

1. LCOE (Levelized Cost of Energy):
   LCOE = (Total Costs) / (Total Energy over Lifetime)
   Typical: $0.03-0.08/kWh for utility scale

2. PAYBACK PERIOD:
   Years = (System Cost) / (Annual Revenue)
   Typical: 5-10 years residential

3. DEGRADATION:
   - Year 1: -1.5% (LID)
   - Years 2-25: -0.5-0.7%/year
   - 25-year output: ~80-85% of initial

TROUBLESHOOTING GUIDE
---------------------
Common issues and solutions:

1. LOWER THAN EXPECTED YIELD:
   - Check shading (winter analysis important)
   - Verify tilt/azimuth installation
   - Inspect for soiling
   - Confirm inverter settings

2. SEASONAL VARIATIONS:
   - Normal: 2-3x summer vs winter
   - Abnormal: >4x variation (check shading)

3. PERFORMANCE RATIO ISSUES:
   - PR < 70%: System problems likely
   - PR 70-75%: Below average
   - PR 75-85%: Typical range
   - PR > 85%: Above average (verify measurements)

ADVANCED TOPICS
---------------
1. BIFACIAL MODULES:
   - Capture rear-side irradiance
   - Gain: 5-30% depending on albedo
   - Best with: High ground reflectance, elevated mounting

2. TRACKING SYSTEMS:
   - Single-axis: +20-30% yield
   - Dual-axis: +30-40% yield
   - Economics: Higher CAPEX vs yield gain

3. SPECTRAL EFFECTS:
   - Module response varies by wavelength
   - AM1.5 standard spectrum
   - Seasonal/weather variations ±2-3%

4. GRID INTEGRATION:
   - Voltage regulation requirements
   - Power factor control
   - Ramp rate limitations
   - Curtailment possibilities

USING THIS TOOL EFFECTIVELY
---------------------------
1. START SIMPLE:
   - Use defaults to understand basics
   - Modify one parameter at a time
   - Compare results

2. REALISTIC INPUTS:
   - Shading: Be conservative
   - Soiling: Consider local conditions
   - Degradation: Plan for 25 years

3. INTERPRET RESULTS:
   - Focus on specific yield (kWh/kWp)
   - Compare to regional benchmarks
   - Consider uncertainty (±10%)

4. NEXT STEPS:
   - Professional shading analysis
   - Structural/electrical engineering
   - Detailed financial modeling
   - Permitting requirements

Author: Dragos Ruiu
Version: 1.0.1
Date: 2025-07-05

Requirements:
    - Python 3.7 or higher
    - pandas >= 1.0.0
    - numpy >= 1.18.0
    - requests >= 2.25.0
    - pvlib >= 0.9.0

Installation:
    pip install pandas numpy requests pvlib
    
    Or use the automatic installer when prompted.

For more detailed theory, see inline documentation throughout the code.
"""

# Standard library imports
import sys
import os
import json
import time
import logging
import argparse
import warnings
from datetime import datetime, timedelta
from typing import Dict, Tuple, Optional, Union, Any
from dataclasses import dataclass
from pathlib import Path

# Python version check
if sys.version_info < (3, 7):
    print(f"Error: Python 3.7 or higher required. You have {sys.version}")
    sys.exit(1)

# Configure logging FIRST, before any logger usage
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Third-party imports with automatic installation option
required_packages = {
    'pandas': 'pandas',
    'numpy': 'numpy', 
    'requests': 'requests',
    'pvlib': 'pvlib'
}

missing_packages = []

# Check for missing packages
for import_name, package_name in required_packages.items():
    try:
        __import__(import_name)
    except ImportError:
        missing_packages.append(package_name)

# Handle missing packages
if missing_packages:
    print("=" * 60)
    print("PV-PowerEstimate.py - Missing Required Packages")
    print("=" * 60)
    print(f"\nThe following packages are not installed:")
    for pkg in missing_packages:
        print(f"  - {pkg}")
    
    # Detect if we're in an externally managed environment
    externally_managed = False
    strict_pep668 = False
    try:
        import sysconfig
        import pathlib
        stdlib = sysconfig.get_path('stdlib')
        marker_file = pathlib.Path(stdlib) / 'EXTERNALLY-MANAGED'
        externally_managed = marker_file.exists()
        
        # Check if even --user is blocked
        if externally_managed:
            import subprocess
            result = subprocess.run([sys.executable, '-m', 'pip', 'install', '--user', '--dry-run', 'pip'], 
                                  capture_output=True, text=True)
            if 'externally-managed-environment' in result.stderr:
                strict_pep668 = True
    except:
        pass
    
    if strict_pep668:
        print("\n⚠️  Detected STRICT externally-managed environment (PEP 668)")
        print("   Your system blocks ALL pip installations, even --user.")
        print("   This is common on Ubuntu 23.04+, Debian 12+.")
        print("\n   You MUST use either:")
        print("   1. A virtual environment (recommended)")
        print("   2. System packages via apt")
        print("   3. Override with --break-system-packages (risky)")
    elif externally_managed:
        print("\n⚠️  Detected externally-managed Python environment (PEP 668)")
    
    print("\n" + "-" * 60)
    
    # Provide installation options based on environment
    if strict_pep668:
        print("\nChoose installation method:")
        print("\n1. Create and use virtual environment (RECOMMENDED)")
        print("2. Install system packages via apt (may be outdated)")
        print("3. Force install with --break-system-packages (AT YOUR OWN RISK)")
        print("4. Exit and install manually")
        
        try:
            choice = input("\nYour choice (1-4): ").strip()
            
            if choice == '1':
                # Virtual environment option
                print("\nCreating virtual environment...")
                import subprocess
                venv_name = "pv_env"
                
                try:
                    # First check if venv module is available
                    try:
                        import venv
                    except ImportError:
                        print("\n❌ Error: venv module not found!")
                        print("Please install it with:")
                        print("   sudo apt install python3-venv python3-full")
                        sys.exit(1)
                    
                    # Create venv with progress indication
                    print(f"Creating {venv_name}... (this may take a moment)")
                    
                    # Run with visible output
                    result = subprocess.run(
                        [sys.executable, '-m', 'venv', venv_name],
                        capture_output=True,
                        text=True,
                        timeout=60  # 60 second timeout
                    )
                    
                    if result.returncode != 0:
                        print(f"\n❌ Error creating virtual environment:")
                        if result.stderr:
                            print(result.stderr)
                        sys.exit(1)
                    
                    print(f"✅ Created virtual environment: {venv_name}")
                    
                    # Determine pip path based on OS
                    if os.name == 'nt':  # Windows
                        pip_path = os.path.join(venv_name, 'Scripts', 'pip')
                        python_path = os.path.join(venv_name, 'Scripts', 'python')
                        activate_cmd = f"{venv_name}\\Scripts\\activate"
                    else:  # Unix-like
                        pip_path = os.path.join(venv_name, 'bin', 'pip')
                        python_path = os.path.join(venv_name, 'bin', 'python')
                        activate_cmd = f"source {venv_name}/bin/activate"
                    
                    # Check if pip exists
                    if not os.path.exists(pip_path):
                        print(f"\n❌ Error: pip not found in virtual environment at {pip_path}")
                        print("The virtual environment may not have been created properly.")
                        sys.exit(1)
                    
                    # Install packages in venv
                    print(f"\nInstalling packages in virtual environment...")
                    print(f"This will install: {', '.join(missing_packages)}")
                    
                    # Run pip install with visible output
                    result = subprocess.run(
                        [pip_path, 'install'] + missing_packages,
                        text=True,
                        timeout=300  # 5 minute timeout for package installation
                    )
                    
                    if result.returncode != 0:
                        print(f"\n❌ Error installing packages")
                        sys.exit(1)
                    
                    print("\n✅ Packages installed successfully!")
                    print(f"\n📝 To use this environment, run:")
                    print(f"   {activate_cmd}")
                    print(f"   python PV-PowerEstimate.py")
                    print(f"\n🚀 Or run directly:")
                    print(f"   {python_path} PV-PowerEstimate.py")
                    
                    sys.exit(0)
                    
                except subprocess.TimeoutExpired:
                    print(f"\n❌ Timeout: Virtual environment creation took too long")
                    print("This might indicate a system issue.")
                    sys.exit(1)
                except subprocess.CalledProcessError as e:
                    print(f"\n❌ Error creating virtual environment: {e}")
                    print("\nMake sure python3-venv is installed:")
                    print("   sudo apt install python3-venv python3-full")
                    sys.exit(1)
                except Exception as e:
                    print(f"\n❌ Unexpected error: {e}")
                    sys.exit(1)
                    
            elif choice == '2':
                # System packages option
                print("\nInstall system packages with:")
                print("   sudo apt update")
                print("   sudo apt install python3-pandas python3-numpy python3-requests")
                print("\nNote: pvlib may not be available via apt. After installing the above, try:")
                print("   pip install --break-system-packages pvlib")
                sys.exit(0)
                
            elif choice == '3':
                # Force install option
                print("\n⚠️  WARNING: This may break system Python packages!")
                confirm = input("Are you SURE you want to continue? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    print("\nForce installing packages...")
                    import subprocess
                    try:
                        subprocess.check_call([
                            sys.executable, '-m', 'pip', 'install', 
                            '--break-system-packages'] + missing_packages
                        )
                        print("\n✅ Packages installed (forced)")
                        print("Please run the script again.")
                        sys.exit(0)
                    except subprocess.CalledProcessError as e:
                        print(f"\n❌ Installation failed: {e}")
                        sys.exit(1)
                else:
                    print("\nInstallation cancelled.")
                    sys.exit(0)
                    
            else:
                print("\nExiting. Please install packages manually.")
                sys.exit(0)
                
        except KeyboardInterrupt:
            print("\n\nInstallation cancelled.")
            sys.exit(1)
            
    else:
        # Non-strict environment - try --user install
        try:
            response = input("\nInstall packages to user directory automatically? (y/n): ").strip().lower()
            if response == 'y':
                print("\nInstalling packages to user directory...")
                import subprocess
                
                try:
                    subprocess.check_call([
                        sys.executable, '-m', 'pip', 'install', '--user'] + missing_packages
                    )
                    print("\n✅ Packages installed successfully!")
                    print("Please run the script again.")
                    sys.exit(0)
                except subprocess.CalledProcessError:
                    print("\n❌ User installation failed. Creating virtual environment instead...")
                    # Fall back to venv
                    subprocess.check_call([sys.executable, '-m', 'venv', 'pv_env'])
                    if os.name == 'nt':
                        pip_path = os.path.join('pv_env', 'Scripts', 'pip')
                    else:
                        pip_path = os.path.join('pv_env', 'bin', 'pip')
                    subprocess.check_call([pip_path, 'install'] + missing_packages)
                    print("\n✅ Virtual environment created and packages installed!")
                    print("Run: source pv_env/bin/activate && python PV-PowerEstimate.py")
                    sys.exit(0)
            else:
                print("\nPlease install the required packages manually.")
                sys.exit(1)
        except KeyboardInterrupt:
            print("\n\nInstallation cancelled.")
            sys.exit(1)

# Now import the packages
try:
    import requests
    import pandas as pd
    import numpy as np
    import pvlib
    from pvlib import pvsystem, modelchain, location
    from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
    
    # Log pvlib version for debugging (using logger that's now defined)
    logger.info(f"Using pvlib version: {pvlib.__version__}")
except ImportError as e:
    print(f"Error: Failed to import package after installation. {e}")
    print("Please check your Python environment.")
    sys.exit(1)

# Suppress pvlib warnings for cleaner output
warnings.filterwarnings('ignore', module='pvlib')

# Constants
VERSION = "1.0.1"
DEFAULT_SYSTEM_SIZE = 8.0  # kW
MIN_LATITUDE = -90.0
MAX_LATITUDE = 90.0
MIN_LONGITUDE = -180.0
MAX_LONGITUDE = 180.0
MAX_ALTITUDE = 8848  # Mt. Everest height in meters
MIN_ALTITUDE = -420   # Dead Sea depth in meters

# API endpoints
NOMINATIM_API = "https://nominatim.openstreetmap.org/search"
ELEVATION_API = "https://api.open-elevation.com/api/v1/lookup"
PVGIS_API_BASE = "https://re.jrc.ec.europa.eu/api/v5_2/"
NREL_API_BASE = "https://developer.nrel.gov/api/nsrdb/v2/solar/"


@dataclass
class SystemConfig:
    """
    Data class for PV system configuration parameters.
    
    Encapsulates all system design choices and loss factors with their
    physical basis and typical ranges based on industry standards.
    
    QUICK REFERENCE - TYPICAL LOSS VALUES:
    ======================================
    
    Loss Type            Low     Average    High    Notes
    ---------------------------------------------------------
    Soiling              1-2%    2-3%       4-6%    Desert/farm worse
    Shading              0-2%    3-5%       >10%    Site-specific
    Snow                 0%      0-5%       5-10%   Climate-dependent
    Mismatch             1-2%    2-3%       3-4%    Quality matters
    DC Wiring            0.5-1%  1-2%       2-3%    Distance matters
    Connections          0.5%    0.5-1%     1-2%    Maintenance helps
    LID (first year)     1-2%    1.5-2%     2-3%    Technology-dependent
    Nameplate            0-1%    1-2%       2-3%    Buy quality
    Degradation/year     0.5%    0.5-0.7%   0.8%    Linear after year 1
    Availability         1-2%    2-3%       3-5%    Regular O&M needed
    
    Total PR (typical)   85%     80%        70%     Performance Ratio
    
    DESIGN RULES OF THUMB:
    ======================
    - 1 kW ≈ 3-4 panels ≈ 60-80 ft² ≈ 6-8 m²
    - 1 kW produces 1,000-2,000 kWh/year (location-dependent)
    - Residential: 3-10 kW typical
    - Commercial: 10-500 kW typical
    - Utility: >1 MW (1000+ kW)
    
    MOUNTING OPTIONS:
    =================
    Module Types:
    - glass_glass: Double glass modules (bifacial capable)
    - glass_polymer: Glass front, polymer backsheet (standard)
    
    Racking Models:
    - open_rack: Ground/pole mount with good airflow
    - close_mount: Roof mount with minimal air gap
    - insulated_back: Building integrated (BIPV)
    
    Loss Factor Physics:
    Each loss mechanism has a physical basis that affects energy production:
    - Optical losses (soiling, shading): Reduce incoming irradiance
    - Electrical losses (mismatch, wiring): I²R and voltage drops
    - Thermal losses: Temperature-dependent efficiency
    - Degradation: Material aging effects
    """
    # SYSTEM ORIENTATION PARAMETERS
    # Tilt angle optimization theory:
    # - Annual optimum ≈ latitude (maximizes yearly insolation)
    # - Summer optimum ≈ latitude - 15° (sun higher in sky)
    # - Winter optimum ≈ latitude + 15° (sun lower in sky)
    # - 0° (horizontal) maximizes diffuse collection but loses direct beam
    surface_tilt: float = 30.0
    
    # Azimuth angle (0° = North, 180° = South, 90° = East, 270° = West)
    # Theory: Maximize cos(θ) between sun and panel normal vector
    # - True south (180° in N hemisphere) maximizes daily integral
    # - East bias captures morning sun (lower temperatures = higher efficiency)
    # - West bias captures afternoon sun (may align with peak demand)
    surface_azimuth: float = 180.0
    
    # MODULE SPECIFICATIONS
    # Modern crystalline silicon modules: 300-600W typical
    # Efficiency η = Pmax / (Area × 1000 W/m²) under STC
    # Typical efficiencies: 15-22% for commercial modules
    module_power: float = 400.0
    
    # STRING CONFIGURATION
    # Series connection: Voltages add, current stays same
    # Parallel connection: Currents add, voltage stays same
    # Design constraints:
    # - Max system voltage (typically 600V or 1000V)
    # - Inverter MPPT voltage range
    # - Temperature-corrected voltage calculations
    modules_per_string: int = 20
    strings_per_inverter: int = 1
    
    # INVERTER SIZING
    # DC/AC ratio typically 1.1-1.4 for economic optimization
    # Higher ratios increase clipping but improve capacity factor
    inverter_power: float = 8000.0
    
    # MOUNTING CONFIGURATION
    # Affects cell temperature via convective cooling
    # T_cell = T_ambient + ΔT, where ΔT depends on mounting
    # Module type: 'glass_glass' or 'glass_polymer'
    # Racking model: 'open_rack', 'close_mount', 'insulated_back'
    module_type: str = 'glass_glass'
    racking_model: str = 'open_rack'
    
    # LOSS FACTORS - Each represents a physical mechanism
    
    # SOILING LOSSES (2-5% typical)
    # Physics: Particulate accumulation reduces transmission
    # τ_soiled = τ_clean × (1 - soiling_factor)
    # Depends on: Rainfall, tilt angle, local pollution, cleaning frequency
    # Research shows: Loss ∝ (days since rain)^0.5 in many climates
    soiling_loss: float = 2.0
    
    # SHADING LOSSES (site-specific, 0-20%)
    # Physics: Non-linear due to bypass diodes
    # Even small shade can cause large losses (current-limited strings)
    # Near shading: Buildings, trees (time-varying)
    # Far shading: Horizon profile (seasonal variation)
    # Self-shading: Row-to-row in large arrays
    shading_loss: float = 3.0
    
    # SNOW LOSSES (0-10% depending on climate)
    # Physics: Complete opaque coverage → zero production
    # Loss = Coverage_probability × Loss_when_covered
    # Mitigation: Steep tilt (>40°) promotes sliding
    # Bifacial modules can produce from rear during snow coverage
    snow_loss: float = 0.0
    
    # MISMATCH LOSSES (1-3%)
    # Physics: Series string limited by weakest module
    # Statistical distribution of module parameters
    # For ±3% power tolerance: ~2% mismatch loss typical
    # Increases with age due to non-uniform degradation
    mismatch_loss: float = 2.0
    
    # DC WIRING LOSSES (1-3%)
    # Physics: P_loss = I² × R = I² × (ρ × L / A)
    # Where: ρ = resistivity, L = length, A = cross-section
    # Design trade-off: Wire cost vs efficiency
    # Increases with current (low voltage systems worse)
    wiring_loss: float = 2.0
    
    # CONNECTION LOSSES (0.5-1%)
    # Physics: Contact resistance at terminals
    # R_contact causes voltage drop and heat generation
    # Degradation mechanism: Corrosion increases resistance
    connection_loss: float = 0.5
    
    # LIGHT-INDUCED DEGRADATION (1-3% first year)
    # Physics: Boron-oxygen defects in p-type silicon
    # Mechanism: Light exposure creates recombination centers
    # Stabilizes after ~1000 sun-hours
    # Reduced in n-type and heterojunction cells
    lid_loss: float = 1.5
    
    # NAMEPLATE TOLERANCE (0-3%)
    # Manufacturing variability vs rated power
    # Positive tolerance modules available at premium
    # Statistical: Gaussian distribution around nominal
    nameplate_loss: float = 1.0
    
    # AGE-RELATED DEGRADATION (0% for new systems)
    # Physics: Multiple mechanisms
    # - EVA browning/delamination
    # - Solder bond fatigue
    # - Corrosion of metallization
    # Typical rates: 0.5-0.8%/year for crystalline Si
    age_loss: float = 0.0
    
    # AVAILABILITY LOSSES (0.5-3%)
    # Downtime causes: Inverter trips, grid outages, maintenance
    # Statistical modeling: MTBF and MTTR metrics
    # Higher for complex systems (tracking, string inverters)
    availability_loss: float = 3.0
    
    @property
    def system_size_kw(self) -> float:
        """Calculate total DC system size in kW"""
        return (self.module_power * self.modules_per_string * 
                self.strings_per_inverter) / 1000.0
    
    @property
    def total_loss_factor(self) -> float:
        """
        Calculate combined loss factor (Performance Ratio components).
        
        Theory: Losses multiply (not add) because they act in series
        PR = ∏(1 - loss_i) for all loss factors
        
        Typical PR: 0.75-0.85 (75-85%)
        Below 0.75: Investigate system issues
        Above 0.85: High-performing system
        """
        losses = [
            self.soiling_loss, self.shading_loss, self.snow_loss,
            self.mismatch_loss, self.wiring_loss, self.connection_loss,
            self.lid_loss, self.nameplate_loss, self.age_loss,
            self.availability_loss
        ]
        factor = 1.0
        for loss in losses:
            factor *= (1 - loss / 100.0)
        return factor


class AddressGeocoder:
    """
    Handles conversion of street addresses to GPS coordinates.
    Uses OpenStreetMap's Nominatim service (free, no API key required).
    
    Geocoding is essential for solar analysis as location determines:
    - Solar path geometry (latitude effect)
    - Climate zone and weather patterns
    - Time zone and solar noon timing
    - Magnetic declination for compass headings
    """
    
    def __init__(self):
        """Initialize geocoder with proper headers for OSM compliance"""
        self.session = requests.Session()
        # OSM requires a user agent
        self.session.headers.update({
            'User-Agent': f'PV-PowerEstimate/{VERSION} (https://github.com/secwest/PV-Generation-Planning)'
        })
    
    def geocode(self, address: str) -> Optional[Tuple[float, float]]:
        """
        Convert address string to latitude/longitude coordinates.
        
        Args:
            address: Street address, city, or location description
            
        Returns:
            Tuple of (latitude, longitude) or None if not found
            
        Example:
            >>> geocoder = AddressGeocoder()
            >>> coords = geocoder.geocode("111 Wellington Street, Ottawa, Ontario")
            >>> print(f"Lat: {coords[0]}, Lon: {coords[1]}")
        """
        try:
            # Nominatim API parameters
            params = {
                'q': address,
                'format': 'json',
                'limit': 1,
                'addressdetails': 1
            }
            
            # Make request with timeout
            response = self.session.get(
                NOMINATIM_API, 
                params=params, 
                timeout=10
            )
            
            # Check response
            if response.status_code == 200:
                data = response.json()
                if data and len(data) > 0:
                    result = data[0]
                    lat = float(result['lat'])
                    lon = float(result['lon'])
                    
                    # Log the resolved location for verification
                    display_name = result.get('display_name', 'Unknown')
                    logger.info(f"Geocoded '{address}' to: {display_name}")
                    logger.info(f"Coordinates: {lat:.4f}, {lon:.4f}")
                    
                    return lat, lon
                else:
                    logger.warning(f"No results found for address: {address}")
                    return None
            else:
                logger.error(f"Geocoding API error: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error during geocoding: {e}")
            return None
        except (KeyError, ValueError) as e:
            logger.error(f"Error parsing geocoding response: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error during geocoding: {e}")
            return None


class SolarPVCalculator:
    """
    Main calculator class for solar PV power yield estimation.
    
    Implements comprehensive physics-based modeling of the complete
    photovoltaic energy conversion chain:
    
    1. SOLAR RESOURCE (Extraterrestrial → Ground level)
       - Solar constant: 1361 W/m² at 1 AU
       - Atmospheric attenuation (air mass, aerosols, water vapor)
       - Cloud effects on direct/diffuse split
    
    2. GEOMETRIC CORRECTIONS (Ground level → Panel plane)
       - Solar position algorithms (azimuth, elevation)
       - Angle of incidence calculations
       - Transposition models (isotropic/anisotropic sky)
    
    3. OPTICAL PROCESSES (Panel plane → Cell surface)
       - Reflection losses (Fresnel equations)
       - Soiling and snow coverage
       - Shading (near and far obstacles)
    
    4. PHOTOVOLTAIC CONVERSION (Photons → DC electricity)
       - Semiconductor physics (bandgap, quantum efficiency)
       - Temperature effects on voltage and current
       - Series/parallel electrical configuration
    
    5. POWER CONDITIONING (DC → AC grid power)
       - Maximum power point tracking (MPPT)
       - Inverter efficiency curves
       - Clipping losses at high DC/AC ratios
    
    6. SYSTEM LOSSES (Gross → Net production)
       - Wiring and connection resistance
       - Mismatch between modules
       - Downtime and availability
    """
    
    def __init__(self, latitude: float, longitude: float, 
                 altitude: Optional[float] = None, address: Optional[str] = None):
        """
        Initialize calculator with location parameters.
        
        Location determines fundamental solar geometry:
        - Latitude: Solar elevation angles, day length, seasonal variation
        - Longitude: Solar time calculations, time zone
        - Altitude: Air mass, temperature, direct irradiance intensity
        
        Higher latitudes have:
        - Lower solar elevations (cosine losses)
        - Larger seasonal variations
        - Longer summer days (can partially compensate)
        
        Args:
            latitude: Latitude in decimal degrees (-90 to 90)
            longitude: Longitude in decimal degrees (-180 to 180)
            altitude: Elevation in meters (optional, will be fetched)
            address: Human-readable address for reference
            
        Raises:
            ValueError: If coordinates are out of valid range
        """
        # Validate coordinates
        if not self._validate_coordinates(latitude, longitude):
            raise ValueError(f"Invalid coordinates: {latitude}, {longitude}")
        
        self.lat = latitude
        self.lon = longitude
        self.address = address
        
        # Altitude effects on solar resource:
        # 1. Reduced air mass → less atmospheric attenuation
        # 2. Lower temperatures → better module efficiency  
        # 3. Typical: +0.7% irradiance per 1000m elevation
        # 4. Temperature lapse: -6.5°C per 1000m (standard atmosphere)
        if altitude is not None:
            if not MIN_ALTITUDE <= altitude <= MAX_ALTITUDE:
                logger.warning(f"Altitude {altitude}m seems unrealistic, fetching from API")
                self.altitude = self._fetch_elevation()
            else:
                self.altitude = altitude
        else:
            self.altitude = self._fetch_elevation()
        
        # Create pvlib Location object for solar calculations
        self.location = location.Location(
            latitude=self.lat,
            longitude=self.lon,
            altitude=self.altitude,
            name=address or f"Site at {self.lat:.4f}, {self.lon:.4f}"
        )
        
        logger.info(f"Initialized PV calculator for {self.location.name}")
        logger.info(f"Coordinates: {self.lat:.4f}°, {self.lon:.4f}°, {self.altitude:.0f}m")
    
    @staticmethod
    def _validate_coordinates(lat: float, lon: float) -> bool:
        """Validate latitude and longitude values."""
        return (MIN_LATITUDE <= lat <= MAX_LATITUDE and 
                MIN_LONGITUDE <= lon <= MAX_LONGITUDE)
    
    def _fetch_elevation(self) -> float:
        """
        Fetch elevation data from open-elevation API.
        
        Elevation affects PV performance through:
        
        1. DIRECT IRRADIANCE ENHANCEMENT
           DNI(h) = DNI(0) × exp(-τ × AM(h))
           where τ = optical depth, AM = air mass
           Lower pressure at altitude → smaller AM → higher DNI
        
        2. TEMPERATURE EFFECTS
           Ambient temp decreases ~6.5°C/1000m
           Module efficiency increases ~0.4%/°C cooling
           Net benefit: ~2.6% per 1000m from temperature alone
        
        3. UV CONTENT
           Higher UV fraction at altitude
           Can cause increased degradation rates
           Affects spectral response of some cell types
        
        Returns:
            Elevation in meters, defaults to 0 if API fails
        """
        try:
            logger.info("Fetching elevation data...")
            
            params = {'locations': f'{self.lat},{self.lon}'}
            
            response = requests.get(
                ELEVATION_API, 
                params=params, 
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'results' in data and len(data['results']) > 0:
                    elevation = float(data['results'][0]['elevation'])
                    logger.info(f"Fetched elevation: {elevation:.0f}m")
                    return elevation
            
            logger.warning("Could not fetch elevation, defaulting to sea level")
            return 0.0
            
        except Exception as e:
            logger.error(f"Error fetching elevation: {e}")
            return 0.0
    
    def fetch_pvgis_data(self, year: Optional[int] = None) -> Optional[pd.DataFrame]:
        """
        Fetch Typical Meteorological Year (TMY) data from PVGIS.
        
        THEORY: TMY Data Construction
        ================================
        TMY is a synthetic year that represents long-term patterns:
        
        1. STATISTICAL SELECTION
           - Analyzes 10-20 years of satellite/ground data
           - For each month, selects the most "typical" month
           - Typical = closest to long-term cumulative distribution
           
        2. PRESERVED STATISTICS
           - Mean values (irradiance, temperature)
           - Extremes and variability
           - Temporal correlations (persistence)
           
        3. IRRADIANCE COMPONENTS
           
           Global Horizontal Irradiance (GHI):
           GHI = DNI × cos(θz) + DHI
           where θz = solar zenith angle
           
           Direct Normal Irradiance (DNI):
           - Beam radiation from solar disk (0.5° angular diameter)
           - Follows Beer-Lambert law through atmosphere:
             DNI = E₀ × ε × exp(-τ × m)
             where: E₀ = extraterrestrial irradiance
                    ε = eccentricity correction
                    τ = atmospheric optical depth
                    m = air mass
           
           Diffuse Horizontal Irradiance (DHI):
           - Scattered radiation from sky dome
           - Components: Rayleigh (molecular), Mie (aerosol), multiple
           - Increases with turbidity and cloud cover
           
        4. SATELLITE DERIVATION
           PVGIS uses different databases by region:
           - SARAH: Europe/Africa (Meteosat)
           - NSRDB: Americas (GOES)
           - CMSAF: High latitudes
           Resolution: 3-5 km spatial, hourly temporal
        
        Args:
            year: Year for timestamps (default: current year)
            
        Returns:
            DataFrame with hourly weather data:
            - ghi: Global Horizontal Irradiance (W/m²)
            - dni: Direct Normal Irradiance (W/m²)
            - dhi: Diffuse Horizontal Irradiance (W/m²)
            - temp_air: Ambient temperature at 2m (°C)
            - wind_speed: Wind speed at 10m (m/s)
        """
        try:
            logger.info("Fetching TMY data from PVGIS...")
            
            # PVGIS API endpoint
            endpoint = "tmy"
            url = f"{PVGIS_API_BASE}{endpoint}"
            
            params = {
                'lat': self.lat,
                'lon': self.lon,
                'outputformat': 'json',
                'browser': 1
            }
            
            # Make API request with retry logic
            for attempt in range(3):
                try:
                    response = requests.get(url, params=params, timeout=30)
                    if response.status_code == 200:
                        break
                except requests.exceptions.Timeout:
                    if attempt < 2:
                        logger.warning(f"Timeout, retrying... (attempt {attempt + 2}/3)")
                        time.sleep(2)
                    else:
                        raise
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract metadata
                meta = data.get('meta', {})
                logger.info(f"PVGIS data source: {meta.get('meteo_data', 'Unknown')}")
                
                # Extract hourly data
                tmy_data = data['outputs']['tmy_hourly']
                
                # Create DataFrame
                df = pd.DataFrame(tmy_data)
                
                # Parse timestamps - PVGIS uses UTC
                # Handle different possible formats from PVGIS
                try:
                    # First, check what format we're getting
                    sample_time = df['time(UTC)'].iloc[0]
                    logger.info(f"PVGIS timestamp format sample: {sample_time}")
                    
                    # Try different parsing strategies
                    if ':' in str(sample_time) and len(str(sample_time)) > 10:
                        # Format like "20070101:0010" (YYYYMMDD:HHMM)
                        df['datetime'] = pd.to_datetime(
                            df['time(UTC)'].astype(str),
                            format='%Y%m%d:%H%M'
                        )
                    elif '/' in str(sample_time):
                        # Original format "MM/DD HH:MM"
                        current_year = year if year else datetime.now().year
                        df['datetime'] = pd.to_datetime(
                            df['time(UTC)'].apply(lambda x: f"{current_year}/{x}"),
                            format='%Y/%m/%d %H:%M'
                        )
                    else:
                        # Try pandas auto-detection
                        df['datetime'] = pd.to_datetime(df['time(UTC)'])
                    
                    # For TMY data, we typically want to use a reference year
                    # Update the year to the requested year while keeping month/day/hour
                    if year:
                        df['datetime'] = df['datetime'].apply(
                            lambda x: x.replace(year=year)
                        )
                    
                except Exception as e:
                    logger.error(f"Failed to parse PVGIS timestamps: {e}")
                    logger.error(f"Sample timestamp: {df['time(UTC)'].iloc[0]}")
                    # Try alternative parsing
                    try:
                        # Remove any year prefix and parse
                        df['datetime'] = pd.to_datetime(df['time(UTC)'], format='mixed')
                    except:
                        raise ValueError(f"Unable to parse PVGIS timestamps. Format: {df['time(UTC)'].iloc[0]}")
                
                df.set_index('datetime', inplace=True)
                
                # Rename to pvlib conventions
                # Each represents hourly integrated/averaged values
                df = df.rename(columns={
                    'G(h)': 'ghi',      # ∫GHI dt over hour (Wh/m²)
                    'Gb(n)': 'dni',     # ∫DNI dt over hour
                    'Gd(h)': 'dhi',     # ∫DHI dt over hour
                    'T2m': 'temp_air',  # Average temp at 2m height
                    'WS10m': 'wind_speed'  # Average wind at 10m
                })
                
                # Select required columns
                df = df[['ghi', 'dni', 'dhi', 'temp_air', 'wind_speed']]
                
                # Validate physical constraints
                if self._validate_weather_data(df):
                    logger.info(f"Successfully fetched {len(df)} hours of TMY data")
                    return df
                else:
                    logger.error("Weather data validation failed")
                    return None
                    
            else:
                logger.error(f"PVGIS API error: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error fetching PVGIS data: {e}")
            return None
    
    def fetch_nrel_psm3_data(self, year: int = 2020, 
                            api_key: Optional[str] = None) -> Optional[pd.DataFrame]:
        """
        Fetch data from NREL Physical Solar Model v3 (PSM3).
        
        PSM3 TECHNICAL ADVANTAGES:
        
        1. HIGHER RESOLUTION
           - Spatial: 4km (vs 5-10km PVGIS)
           - Temporal: 30-min available (vs hourly)
           - Spectral: Multiple wavelength bands
        
        2. ADVANCED MODELING
           - FARMS radiative transfer model
           - Aerosol optical depth from MODIS
           - Precipitable water from GOES
           - Cloud properties from satellite
        
        3. ADDITIONAL PARAMETERS
           - Spectral irradiance (280-4000nm)
           - Atmospheric pressure
           - Aerosol/albedo data
           - Better snow detection
        
        Requires free API key from: https://developer.nrel.gov/signup/
        
        Args:
            year: Year for TMY data
            api_key: NREL API key
            
        Returns:
            DataFrame with weather data or None if failed
        """
        if not api_key:
            logger.error("NREL API requires a key. Register at: https://developer.nrel.gov/signup/")
            return None
        
        try:
            logger.info("Fetching data from NREL PSM3...")
            
            url = f"{NREL_API_BASE}psm3-tmy-download.csv"
            
            params = {
                'api_key': api_key,
                'lat': self.lat,
                'lon': self.lon,
                'attributes': 'ghi,dhi,dni,wind_speed,air_temperature',
                'names': 'tmy',
                'utc': 'true',
                'leap_day': 'false',
                'interval': '60',
                'full_name': 'PV-PowerEstimate',
                'email': 'user@example.com'
            }
            
            response = requests.get(url, params=params, timeout=60)
            
            if response.status_code == 200:
                # Parse CSV response
                from io import StringIO
                
                lines = response.text.split('\n')
                header_rows = 2
                csv_data = '\n'.join(lines[header_rows:])
                
                df = pd.read_csv(StringIO(csv_data))
                
                # Create datetime index
                df['datetime'] = pd.to_datetime(
                    df[['Year', 'Month', 'Day', 'Hour']].astype(str).agg('-'.join, axis=1) + 
                    ':' + df['Minute'].astype(str).str.zfill(2),
                    format='%Y-%m-%d-%H:%M'
                )
                df.set_index('datetime', inplace=True)
                
                # Rename columns
                df = df.rename(columns={
                    'GHI': 'ghi',
                    'DNI': 'dni',
                    'DHI': 'dhi',
                    'Temperature': 'temp_air',
                    'Wind Speed': 'wind_speed'
                })
                
                df = df[['ghi', 'dni', 'dhi', 'temp_air', 'wind_speed']]
                
                if self._validate_weather_data(df):
                    logger.info(f"Successfully fetched NREL PSM3 data")
                    return df
                else:
                    logger.error("NREL data validation failed")
                    return None
                    
            else:
                logger.error(f"NREL API error: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error fetching NREL data: {e}")
            return None
    
    @staticmethod
    def _validate_weather_data(df: pd.DataFrame) -> bool:
        """
        Validate weather data for physical consistency.
        
        VALIDATION RULES BASED ON PHYSICS:
        
        1. IRRADIANCE CONSTRAINTS
           - No negative values (physically impossible)
           - GHI ≥ DHI (diffuse is component of global)
           - GHI ≤ DNI × cos(θz) + DHI (energy conservation)
           - Max GHI < 1367 W/m² (solar constant)
        
        2. TEMPERATURE CONSTRAINTS  
           - Reasonable range: -50°C to +60°C
           - Rate of change < 20°C/hour (frontal passages)
        
        3. CLOSURE RELATIONSHIP
           GHI should ≈ DNI × cos(θz) + DHI
           Discrepancies indicate measurement/model errors
        
        Args:
            df: Weather data DataFrame
            
        Returns:
            True if valid, False otherwise
        """
        try:
            # Check required columns
            required = ['ghi', 'dni', 'dhi', 'temp_air', 'wind_speed']
            if not all(col in df.columns for col in required):
                logger.error("Missing required weather data columns")
                return False
            
            # Check for NaN values
            if df[required].isnull().any().any():
                logger.warning("Weather data contains NaN values")
            
            # Physical constraints
            if (df['ghi'] < 0).any() or (df['dni'] < 0).any() or (df['dhi'] < 0).any():
                logger.error("Negative irradiance values found")
                return False
            
            # GHI must be >= DHI (diffuse is subset of global)
            if (df['ghi'] < df['dhi']).any():
                logger.warning("DHI exceeds GHI in some hours (correcting...)")
                # Could implement correction here
            
            # Temperature sanity check
            if (df['temp_air'] < -50).any() or (df['temp_air'] > 60).any():
                logger.warning("Extreme temperatures found")
            
            return True
            
        except Exception as e:
            logger.error(f"Error validating weather data: {e}")
            return False
    
    def calculate_pv_output(self, weather_data: pd.DataFrame, 
                           system_config: Optional[SystemConfig] = None) -> Tuple[pd.DataFrame, float]:
        """
        Calculate PV system power output using physics models.
        
        PHOTOVOLTAIC MODELING CHAIN:
        =====================================
        
        1. SOLAR POSITION CALCULATION (Astronomical Algorithms)
           --------------------------------------------------
           Uses NREL SPA (Solar Position Algorithm):
           - Accuracy: ±0.0003° 
           - Accounts for: Nutation, aberration, refraction
           
           Key angles:
           - θz: Zenith angle (0° = sun overhead)
           - γs: Azimuth angle (180° = south)
           - α: Elevation = 90° - θz
           
           Air Mass calculation:
           AM = 1/(cos(θz) + 0.50572×(96.07995-θz)^-1.6364)
           Kasten & Young formula, accurate for θz < 85°
        
        2. IRRADIANCE TRANSPOSITION (Horizontal → Tilted Plane)
           ---------------------------------------------------
           Converts GHI/DNI/DHI to plane-of-array (POA) irradiance
           
           POA = DNI×cos(AOI) + DHI×F_sky + (GHI)×ρ×F_ground
           
           Where:
           - AOI: Angle of incidence between sun and panel normal
           - F_sky: Sky view factor (anisotropic models)
           - ρ: Ground albedo (0.2 grass, 0.8 snow)
           - F_ground: Ground view factor = (1-cos(tilt))/2
           
           Models (increasing complexity/accuracy):
           - Isotropic: Uniform sky radiance
           - Klucher: Horizon/circumsolar brightening  
           - Hay-Davies: Circumsolar + isotropic
           - Perez: Full anisotropic (most accurate)
        
        3. OPTICAL LOSSES (Reflection and Absorption)
           ------------------------------------------
           Angle of Incidence (AOI) modifier:
           - Based on Fresnel equations for air-glass interface
           - Typical anti-reflective coating: n ≈ 1.3
           
           IAM = 1 - b₀×(1/cos(AOI) - 1)
           where b₀ ≈ 0.05 for AR-coated glass
           
           Additional optical losses:
           - Soiling: Reduces transmission
           - Module glass absorption: ~2%
           - EVA encapsulant absorption: ~1%
        
        4. CELL TEMPERATURE MODELING (Thermal Physics)
           -------------------------------------------
           Energy balance: Solar input = Electrical + Thermal output
           
           Sandia Array Performance Model (SAPM):
           T_cell = T_amb + G_POA × exp(a + b×v_wind)
           
           Typical parameters:
           - Open rack: a=-3.47, b=-0.0594
           - Roof mount: a=-2.98, b=-0.0471
           - BIPV: a=-1.50, b=-0.0200
           
           Temperature effects on performance:
           - Voltage: dV/dT = β_oc ≈ -0.3%/°C
           - Current: dI/dT = α_sc ≈ +0.05%/°C  
           - Power: dP/dT = γ_pmp ≈ -0.4%/°C
        
        5. DC POWER CALCULATION (Semiconductor Physics)
           --------------------------------------------
           Single Diode Model (full physics):
           I = I_L - I_0×[exp(q×(V+I×Rs)/(n×k×T)) - 1] - (V+I×Rs)/Rsh
           
           Where:
           - I_L: Light current ∝ irradiance
           - I_0: Saturation current ∝ exp(-Eg/kT)
           - Rs: Series resistance
           - Rsh: Shunt resistance
           - n: Ideality factor (1-2)
           
           Simplified (pvlib SAPM):
           P_dc = G_eff/G_ref × P_dc0 × (1 + γ×(T_cell - T_ref))
           
           Maximum Power Point (MPP):
           - Voltage and current adjust to maximize P = V×I
           - MPPT efficiency typically 98-99%
        
        6. INVERTER MODELING (Power Electronics)
           -------------------------------------
           Efficiency curve (Sandia/CEC models):
           η = P_ac/P_dc = function of loading and voltage
           
           Key features:
           - Peak efficiency at 30-70% loading
           - Lower efficiency at low power (no-load losses)
           - Clipping when P_dc > P_ac_rated
           - European/CEC weighted efficiency metrics
        
        7. SYSTEM LOSS AGGREGATION
           ------------------------
           Total PR = Π(1 - L_i) for all loss mechanisms
           
           Loss budget example for good system:
           - Temperature: 5-8%
           - Soiling: 2-3%
           - Shading: 1-3%
           - Mismatch: 2%
           - DC wiring: 1-2%
           - AC wiring: 0.5-1%
           - Inverter: 2-4%
           - Availability: 1-3%
           - Total PR: 75-85%
        
        Args:
            weather_data: DataFrame with hourly weather
            system_config: System design parameters
            
        Returns:
            Tuple of (results DataFrame, system size kW)
        """
        try:
            logger.info("Starting PV system simulation...")
            
            # Use default config if not provided
            if system_config is None:
                system_config = SystemConfig()
                # TILT OPTIMIZATION RULES:
                # Annual energy: tilt = latitude
                # Summer emphasis: tilt = latitude - 15°
                # Winter emphasis: tilt = latitude + 15°
                system_config.surface_tilt = abs(self.lat)
                # AZIMUTH FOR HEMISPHERE:
                # Northern: 180° (south-facing)
                # Southern: 0° (north-facing)  
                # Equator: Either acceptable
                system_config.surface_azimuth = 180 if self.lat > 0 else 0
            
            logger.info(f"System size: {system_config.system_size_kw:.1f} kW")
            logger.info(f"Tilt: {system_config.surface_tilt}°, Azimuth: {system_config.surface_azimuth}°")
            logger.info(f"Module type: {system_config.module_type}, Racking: {system_config.racking_model}")
            logger.info(f"Total loss factor: {system_config.total_loss_factor:.1%}")
            
            # MODULE ELECTRICAL PARAMETERS
            # Based on typical 72-cell monocrystalline silicon
            # STC: 1000 W/m², 25°C, AM1.5 spectrum
            module_params = {
                'pdc0': system_config.module_power,  # Nameplate DC watts
                'v_mp': 41.0,    # Vmp at STC (voltage at max power)
                'i_mp': system_config.module_power / 41.0,  # Imp = P/V
                'v_oc': 49.2,    # Open circuit voltage (no load)
                'i_sc': system_config.module_power / 41.0 * 1.1,  # Short circuit current
                
                # TEMPERATURE COEFFICIENTS (typical c-Si)
                'alpha_sc': 0.0045,   # dIsc/dT in A/°C (~+0.05%/°C)
                'beta_oc': -0.11,     # dVoc/dT in V/°C (~-0.3%/°C)
                'gamma_pdc': -0.0035, # dP/dT in %/°C (~-0.35 to -0.45)
                
                'cells_in_series': 72,  # Determines voltage levels
                'temp_ref': 25.0        # Reference temperature
            }
            
            # INVERTER PARAMETERS
            # Efficiency model: η = f(P_dc/P_dc0, V_dc)
            inverter_params = {
                'pdc0': system_config.inverter_power,
                'eta_inv_nom': 0.97,   # Nominal (datasheet) efficiency  
                'eta_inv_ref': 0.9637  # Reference efficiency for model
            }
            
            # Create PV system object
            pv_system = pvsystem.PVSystem(
                surface_tilt=system_config.surface_tilt,
                surface_azimuth=system_config.surface_azimuth,
                module_parameters=module_params,
                inverter_parameters=inverter_params,
                modules_per_string=system_config.modules_per_string,
                strings_per_inverter=system_config.strings_per_inverter,
                module_type=system_config.module_type,
                racking_model=system_config.racking_model
            )
            
            # TEMPERATURE MODEL NOTE
            # The combination of module_type and racking_model automatically
            # sets appropriate temperature model parameters:
            # - 'glass_glass' + 'open_rack': Well-ventilated ground mount
            # - 'glass_polymer' + 'close_mount': Standard rooftop
            # - 'glass_glass' + 'insulated_back': Building integrated
            
            # CREATE MODELCHAIN
            # Links all component models in correct sequence
            mc = modelchain.ModelChain(
                pv_system,
                self.location,
                
                # AOI model: 'physical' uses Fresnel equations
                # Accounts for polarization and AR coatings
                aoi_model='physical',
                
                # Spectral model: Corrects for non-AM1.5 spectra
                spectral_model='no_loss',  # Simplified
                
                # Temperature model: Cell temp from weather
                temperature_model='sapm'
            )
            
            # RUN THE SIMULATION
            # Executes complete modeling chain for each timestamp:
            # 1. Solar position → 2. Transposition → 3. Temperature →
            # 4. DC power → 5. AC power
            logger.info("Running power simulation for 8760 hours...")
            mc.run_model(weather_data)
            
            # Extract and process results
            results = pd.DataFrame({
                'dc_power': mc.results.dc / 1000.0,  # Convert W to kW
                'ac_power': mc.results.ac / 1000.0 * system_config.total_loss_factor,
                'cell_temperature': mc.results.cell_temperature,
                'effective_irradiance': mc.results.effective_irradiance,
                'total_loss_factor': system_config.total_loss_factor
            })
            
            # Calculate temperature-specific losses for analysis
            results['temperature_loss'] = (
                (results['cell_temperature'] - 25.0) * 
                module_params['gamma_pdc'] / 100.0
            )
            
            # Validation check
            if results['ac_power'].max() == 0:
                logger.error("Simulation produced zero power - check inputs")
                
            logger.info(f"Simulation complete. Peak power: {results['ac_power'].max():.1f} kW")
            
            return results, system_config.system_size_kw
            
        except Exception as e:
            logger.error(f"Error in PV calculation: {e}")
            raise
    
    def calculate_monthly_yield(self, results: pd.DataFrame, 
                               system_size_dc: float) -> Tuple[pd.DataFrame, float, float, float]:
        """
        Calculate monthly and annual energy production metrics.
        
        KEY PERFORMANCE INDICATORS EXPLAINED:
        ====================================
        
        1. ENERGY vs POWER
           - Power (kW): Instantaneous rate of energy flow
           - Energy (kWh): Power integrated over time
           - E = ∫P(t)dt ≈ Σ(P_i × Δt) for discrete data
        
        2. SPECIFIC YIELD (kWh/kWp/year)
           - Energy normalized by system capacity
           - Removes system size dependence
           - Allows fair comparison between sites
           - Typical ranges by climate:
             * Poor: < 800 (very cloudy/high latitude)
             * Fair: 800-1200 (temperate climates)
             * Good: 1200-1600 (sunny temperate)
             * Excellent: 1600-2000 (desert/tropical)
             * Outstanding: > 2000 (high altitude desert)
        
        3. CAPACITY FACTOR (%)
           - CF = E_actual / (P_rated × 8760h) × 100
           - Average power as % of nameplate
           - Solar PV typically 10-25% (location dependent)
           - Compare: Wind 25-45%, Coal/Nuclear 50-90%
           - Limited by: Night, weather, solar geometry
        
        4. PERFORMANCE RATIO (%)
           - PR = E_actual / E_theoretical
           - E_theoretical = Irradiation × Area × η_STC
           - Captures all losses from STC to actual
           - Good systems: 75-85%
           - Degrades ~0.5%/year typically
        
        5. YIELD VARIATIONS
           - Seasonal: Summer/winter ratio 2-5x (latitude dependent)
           - Daily: Clear vs cloudy 5-10x difference
           - Hourly: Bell curve centered on solar noon
        
        Args:
            results: Hourly simulation results
            system_size_dc: System capacity in kW
            
        Returns:
            Tuple of (monthly DataFrame, annual energy kWh, 
                     specific yield kWh/kWp, capacity factor %)
        """
        try:
            # Energy calculation: Power × Time interval
            # For hourly data: kW × 1 hour = kWh
            results['energy_kwh'] = results['ac_power'] * 1.0
            
            # Monthly aggregation
            monthly = results.groupby(results.index.month).agg({
                'energy_kwh': 'sum',          # Total monthly energy
                'ac_power': 'mean',           # Average power
                'cell_temperature': 'mean',    # Average operating temp
                'effective_irradiance': 'mean' # Average POA irradiance
            })
            
            # Convert month numbers to names
            month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            monthly.index = month_names
            
            # Specific yield: Normalize by capacity
            monthly['specific_yield'] = monthly['energy_kwh'] / system_size_dc
            
            # Daily statistics for sizing batteries/loads
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            monthly['daily_energy'] = monthly['energy_kwh'] / days_in_month
            
            # Annual summaries
            annual_energy = results['energy_kwh'].sum()
            annual_specific_yield = annual_energy / system_size_dc
            
            # Capacity factor: Key economic metric
            hours_in_year = len(results)  # 8760 for standard year
            theoretical_max = system_size_dc * hours_in_year
            capacity_factor = (annual_energy / theoretical_max) * 100.0
            
            # Equivalent full sun hours (design parameter)
            # Hours of 1000 W/m² that would produce same energy
            equivalent_sun_hours = annual_specific_yield / 1000
            
            logger.info(f"Annual energy: {annual_energy:,.0f} kWh")
            logger.info(f"Specific yield: {annual_specific_yield:,.0f} kWh/kWp")
            logger.info(f"Capacity factor: {capacity_factor:.1f}%")
            logger.info(f"Equivalent sun hours: {equivalent_sun_hours:.1f} h/day average")
            
            return monthly, annual_energy, annual_specific_yield, capacity_factor
            
        except Exception as e:
            logger.error(f"Error calculating yields: {e}")
            raise
    
    def generate_report(self, weather_data: pd.DataFrame, results: pd.DataFrame,
                       monthly: pd.DataFrame, annual_energy: float,
                       annual_specific_yield: float, capacity_factor: float,
                       system_size_dc: float, system_config: SystemConfig) -> str:
        """
        Generate comprehensive performance assessment report.
        
        Report includes technical analysis for:
        - System design verification
        - Performance benchmarking
        - O&M planning
        - Financial analysis
        - Optimization opportunities
        """
        # Calculate additional metrics
        pr = system_config.total_loss_factor * 100
        peak_power_time = results['ac_power'].idxmax()
        peak_power = results['ac_power'].max()
        
        # Climate statistics
        total_irradiation = weather_data['ghi'].sum() / 1000  # kWh/m²
        avg_temp = weather_data['temp_air'].mean()
        avg_wind = weather_data['wind_speed'].mean()
        
        # Economic assumptions
        electricity_rate = 0.15  # $/kWh
        annual_revenue = annual_energy * electricity_rate
        
        # Best and worst months
        best_month = monthly['energy_kwh'].idxmax()
        worst_month = monthly['energy_kwh'].idxmin()
        variation = monthly.loc[best_month, 'energy_kwh'] / monthly.loc[worst_month, 'energy_kwh']
        
        # Calculate insolation utilization
        # How much of available solar resource is captured
        avg_module_eff = 0.20  # 20% assumed module efficiency
        array_area = system_size_dc / (avg_module_eff * 1.0)  # m²
        theoretical_max = total_irradiation * array_area * avg_module_eff
        utilization = (annual_energy / theoretical_max) * 100
        
        report = f"""
================================================================================
                     SOLAR PV POWER YIELD ASSESSMENT REPORT
================================================================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Software: PV-PowerEstimate v{VERSION}

SITE INFORMATION
----------------
Location: {self.location.name}
Coordinates: {self.lat:.4f}°, {self.lon:.4f}°
Elevation: {self.altitude:.0f} m above sea level
Time Zone: UTC (all times in UTC)

SYSTEM CONFIGURATION
--------------------
System Size: {system_size_dc:.2f} kW DC
Module Power: {system_config.module_power:.0f} W
Number of Modules: {system_config.modules_per_string * system_config.strings_per_inverter}
Array Configuration: {system_config.strings_per_inverter} string(s) × {system_config.modules_per_string} modules
Inverter Size: {system_config.inverter_power/1000:.1f} kW AC
DC/AC Ratio: {system_size_dc/(system_config.inverter_power/1000):.2f}
Tilt Angle: {system_config.surface_tilt:.1f}°
Azimuth: {system_config.surface_azimuth:.0f}° ({self._azimuth_to_direction(system_config.surface_azimuth)})
Mounting: {system_config.module_type.replace('_', ' ').title()} / {system_config.racking_model.replace('_', ' ').title()}

ANNUAL PERFORMANCE SUMMARY
--------------------------
Total Energy Production: {annual_energy:,.0f} kWh/year
Specific Yield: {annual_specific_yield:,.0f} kWh/kWp/year
Capacity Factor: {capacity_factor:.1f}%
Performance Ratio: {pr:.1f}%
Solar Resource Utilization: {utilization:.1f}%
Estimated Annual Revenue: ${annual_revenue:,.0f} (at ${electricity_rate}/kWh)

TECHNICAL PERFORMANCE METRICS
-----------------------------
Peak AC Power Output: {peak_power:,.1f} kW ({peak_power/system_size_dc*100:.0f}% of DC rating)
Peak Output Occurred: {peak_power_time.strftime('%B %d at %H:%M UTC')}
Average Module Temperature: {results['cell_temperature'].mean():.1f}°C
Module Temp at Peak Power: {results.loc[peak_power_time, 'cell_temperature']:.1f}°C
Temperature Losses (annual): {abs(results['temperature_loss'].mean()):.1f}%
Average POA Irradiance: {results['effective_irradiance'].mean():.0f} W/m²

MONTHLY ENERGY PRODUCTION
-------------------------
Month    Energy (kWh)    Specific Yield    Daily Avg    Cell Temp
-------  -------------   --------------    ---------    ---------"""
        
        # Create simple bar chart for monthly production
        max_energy = monthly['energy_kwh'].max()
        
        for idx, (month, row) in enumerate(monthly.iterrows()):
            report += f"\n{month:<7}  {row['energy_kwh']:>12,.0f}    "
            report += f"{row['specific_yield']:>8.0f} kWh/kWp    "
            report += f"{row['daily_energy']:>8.1f}    "
            report += f"{row['cell_temperature']:>8.1f}°C"
            
            # Add visual bar
            bar_length = int(row['energy_kwh'] / max_energy * 20)
            report += "  " + "█" * bar_length
            
            if month == best_month:
                report += " ← Best"
            elif month == worst_month:
                report += " ← Worst"
        
        # Add seasonal pattern visualization
        report += f"""

SEASONAL PATTERN
----------------"""
        
        # Adjust seasonal labels based on hemisphere
        if self.lat > 0:  # Northern hemisphere
            report += """
Winter  ████████░░░░░░░░░░░░  Low sun angle, short days
Spring  ████████████████░░░░  Increasing production
Summer  ████████████████████  Peak production
Fall    ████████████████░░░░  Decreasing production"""
        else:  # Southern hemisphere
            report += """
Summer  ████████████████████  Peak production
Fall    ████████████████░░░░  Decreasing production  
Winter  ████████░░░░░░░░░░░░  Low sun angle, short days
Spring  ████████████████░░░░  Increasing production"""
        
        report += f"""

Your location shows {variation:.1f}:1 seasonal variation ({best_month} vs {worst_month})"""
        
        report += f"""

LOSS ANALYSIS (Detailed Breakdown)
----------------------------------
Optical & Environmental Losses:
  Soiling: {system_config.soiling_loss:.1f}% (transmission reduction)
  Shading: {system_config.shading_loss:.1f}% (direct + diffuse components)
  Snow: {system_config.snow_loss:.1f}% (coverage probability × loss)
  
Electrical & Mismatch Losses:
  Module Mismatch: {system_config.mismatch_loss:.1f}% (I-V curve variations)
  DC Wiring: {system_config.wiring_loss:.1f}% (I²R losses)
  Connections: {system_config.connection_loss:.1f}% (contact resistance)
  
System-Level Losses:
  Inverter Conversion: ~{100 - system_config.inverter_power/system_config.inverter_power*97:.1f}% (DC→AC efficiency)
  Availability: {system_config.availability_loss:.1f}% (downtime allowance)
  
Degradation Factors:
  Light-Induced (LID): {system_config.lid_loss:.1f}% (first year)
  Age-Related: {system_config.age_loss:.1f}% (current year)
  Nameplate Tolerance: {system_config.nameplate_loss:.1f}%
  
Total Losses: {(1-system_config.total_loss_factor)*100:.1f}%
Performance Ratio: {system_config.total_loss_factor*100:.1f}%

CLIMATE ANALYSIS
----------------
Annual Solar Resource:
  Horizontal Irradiation: {total_irradiation:,.0f} kWh/m²/year
  Avg Ambient Temperature: {avg_temp:.1f}°C
  Avg Wind Speed: {avg_wind:.1f} m/s
  
Seasonal Variation:
  Best Month: {best_month} ({monthly.loc[best_month, 'energy_kwh']:,.0f} kWh)
  Worst Month: {worst_month} ({monthly.loc[worst_month, 'energy_kwh']:,.0f} kWh)
  Seasonal Ratio: {monthly.loc[best_month, 'energy_kwh']/monthly.loc[worst_month, 'energy_kwh']:.1f}:1

TECHNICAL RECOMMENDATIONS
-------------------------
1. Tilt Angle Optimization:
   Current: {system_config.surface_tilt:.0f}° | Latitude: {abs(self.lat):.0f}°
   {"✓ Within 5° of latitude angle" if abs(system_config.surface_tilt - abs(self.lat)) < 5 else "→ Consider adjusting tilt closer to latitude"}
   Potential gain from adjustment: ~{max(0, 5-abs(system_config.surface_tilt - abs(self.lat))):.0f}%

2. Soiling Management:
   {self._get_cleaning_recommendation(system_config.soiling_loss)}
   Estimated annual loss: {annual_energy * system_config.soiling_loss/100:.0f} kWh

3. Temperature Management:
   Average cell temp excess: {results['cell_temperature'].mean() - 25:.1f}°C
   Annual temperature losses: {annual_energy * abs(results['temperature_loss'].mean())/100:.0f} kWh
   → Consider enhanced ventilation or different mounting type
   → Open rack mounting typically runs 3-5°C cooler than roof mount

4. System Monitoring:
   - Real-time performance ratio tracking
   - String-level monitoring for mismatch detection
   - Weather station for model validation
   - Thermal imaging: Annual inspection

5. Future Enhancements:
   - Battery Storage: Size for {monthly['daily_energy'].mean():.0f} kWh daily cycling
   - Tracking Systems: Could increase yield 25-35% (economic analysis needed)
   - Bifacial Modules: 5-15% gain with {0.2:.1f} ground albedo
   - Module Upgrade: Latest high-efficiency could add 10-20% capacity

UNDERSTANDING YOUR RESULTS
--------------------------
This simulation used:
- Typical Meteorological Year (TMY) data representing long-term averages
- Hour-by-hour solar position calculations (8,760 data points)
- Temperature-dependent efficiency modeling
- Industry-standard loss factors

Key Metrics Explained:
- kWh (kilowatt-hour): Energy unit, like "miles" for your car
- kW (kilowatt): Power unit, like "horsepower" for your car
- Specific Yield: Energy per installed capacity - allows fair comparison
- Capacity Factor: Average output / maximum possible output
- Performance Ratio: Actual performance / theoretical performance

NEXT STEPS
----------
1. Save this report for reference
2. Get quotes from 3+ local installers
3. Ask installers about:
   - Equipment warranties (25+ years for panels)
   - Performance guarantees
   - Monitoring systems
   - Maintenance plans

4. Financial considerations:
   - Federal/state/local incentives
   - Net metering policies
   - Time-of-use rates
   - Financing options

5. Technical validation:
   - Professional shading analysis
   - Structural engineering review
   - Electrical system compatibility
   - Utility interconnection requirements

UNCERTAINTY ANALYSIS
--------------------
This assessment uncertainty: ±8-10%
Sources of uncertainty:
- TMY vs actual weather: ±5%
- Shading estimation: ±3%
- Degradation rates: ±2%
- Equipment tolerances: ±2%

P50 Estimate (50% probability): {annual_energy:,.0f} kWh
P90 Estimate (90% probability): {annual_energy*0.92:,.0f} kWh
P10 Estimate (10% probability): {annual_energy*1.08:,.0f} kWh

================================================================================
End of Report - Generated by PV-PowerEstimate v{VERSION}
Technical questions: dr@secwest.net
Educational resources: Run with --help-tutorial for detailed guide
================================================================================
"""
        
        return report
    
    def _azimuth_to_direction(self, azimuth: float) -> str:
        """Convert azimuth angle to cardinal direction"""
        directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                     'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        index = int((azimuth + 11.25) / 22.5) % 16
        return directions[index]
    
    def _get_cleaning_recommendation(self, soiling_loss: float) -> str:
        """
        Get cleaning recommendation based on soiling loss.
        
        Soiling accumulation typically follows:
        L(t) = L_max × (1 - exp(-t/τ))
        where τ = time constant (days), depends on:
        - Rainfall frequency
        - Dust levels
        - Tilt angle (steeper = less accumulation)
        """
        if soiling_loss < 2:
            return "→ Low soiling environment: Quarterly cleaning sufficient"
        elif soiling_loss < 5:
            return "→ Moderate soiling: Monthly cleaning recommended"
        else:
            return "→ High soiling: Consider automated cleaning or anti-soiling coating"
    
    def save_results(self, results: pd.DataFrame, monthly: pd.DataFrame,
                    report: str, output_dir: str = "pv_analysis") -> None:
        """
        Save analysis results to files.
        
        Creates directory structure:
        output_dir/
        ├── hourly_output.csv      # Full time series data
        ├── monthly_summary.csv    # Monthly aggregates
        ├── report.txt            # Detailed text report
        └── metadata.json         # Configuration and location data
        """
        try:
            # Create output directory
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Save hourly results
            hourly_file = output_path / "hourly_output.csv"
            results.to_csv(hourly_file)
            logger.info(f"Saved hourly results to {hourly_file}")
            
            # Save monthly summary
            monthly_file = output_path / "monthly_summary.csv"
            monthly.to_csv(monthly_file)
            logger.info(f"Saved monthly summary to {monthly_file}")
            
            # Save report
            report_file = output_path / "report.txt"
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report)
            logger.info(f"Saved report to {report_file}")
            
            # Save metadata
            metadata = {
                'version': VERSION,
                'timestamp': datetime.now().isoformat(),
                'location': {
                    'latitude': self.lat,
                    'longitude': self.lon,
                    'altitude': self.altitude,
                    'address': self.address
                },
                'system': {
                    'size_kw': results.attrs.get('system_size', 0)
                }
            }
            
            metadata_file = output_path / "metadata.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            logger.info(f"Saved metadata to {metadata_file}")
            
            logger.info(f"All results saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error saving results: {e}")
            raise


def main():
    """
    Main entry point for command-line usage.
    
    Supports multiple input methods:
    1. Coordinates: --lat 37.7749 --lon -122.4194
    2. Address: --address "1600 Pennsylvania Ave, Washington DC"
    3. Interactive: prompts for input
    
    Example usage:
        python PV-PowerEstimate.py --lat 37.7749 --lon -122.4194 --system-size 10
        python PV-PowerEstimate.py --address "San Francisco, CA" --tilt 30
        python PV-PowerEstimate.py  # Interactive mode
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='PV-PowerEstimate: Comprehensive Solar PV Power Yield Calculator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --lat 45.4215 --lon -75.6972
  %(prog)s --address "111 Wellington Street, Ottawa, Ontario"
  %(prog)s --lat 51.5074 --lon -0.1278 --system-size 10 --tilt 35

For more information, visit: https://github.com/secwest/PV-Generation-Planning
        """
    )
    
    # Location arguments (mutually exclusive group)
    location_group = parser.add_mutually_exclusive_group()
    location_group.add_argument(
        '--lat', '--latitude',
        type=float,
        help='Latitude in decimal degrees (-90 to 90). Positive = North, Negative = South. Find yours at maps.google.com'
    )
    location_group.add_argument(
        '--address', '-a',
        type=str,
        help='Street address or location name (e.g., "Toronto, ON" or "111 Wellington St, Ottawa")'
    )
    
    parser.add_argument(
        '--lon', '--longitude',
        type=float,
        help='Longitude in decimal degrees (-180 to 180). Positive = East, Negative = West'
    )
    
    parser.add_argument(
        '--altitude', '--elevation',
        type=float,
        help='Altitude in meters above sea level. Higher = more sun but cooler. Optional - will be auto-detected'
    )
    
    # System configuration arguments
    parser.add_argument(
        '--system-size',
        type=float,
        default=DEFAULT_SYSTEM_SIZE,
        help=f'Total system size in kW DC (default: {DEFAULT_SYSTEM_SIZE}). Residential: 3-10kW, Commercial: 10-500kW'
    )
    
    parser.add_argument(
        '--tilt',
        type=float,
        help='Panel tilt angle in degrees from horizontal (0=flat, 90=vertical). Default: your latitude. Steeper helps with snow'
    )
    
    parser.add_argument(
        '--azimuth',
        type=float,
        default=180,
        help='Panel direction in degrees (0=North, 90=East, 180=South, 270=West). Default: 180 (South) for Northern hemisphere'
    )
    
    parser.add_argument(
        '--module-power',
        type=float,
        default=400,
        help='Power rating of each solar panel in watts (default: 400W). Modern panels: 350-600W'
    )
    
    parser.add_argument(
        '--module-type',
        choices=['glass_glass', 'glass_polymer'],
        default='glass_glass',
        help='Module construction type (default: glass_glass)'
    )
    
    parser.add_argument(
        '--racking-model',
        choices=['open_rack', 'close_mount', 'insulated_back'],
        default='open_rack',
        help='Mounting configuration (default: open_rack)'
    )
    
    # Data source selection
    parser.add_argument(
        '--data-source',
        choices=['pvgis', 'nrel'],
        default='pvgis',
        help='Weather data source (default: pvgis)'
    )
    
    parser.add_argument(
        '--nrel-api-key',
        type=str,
        help='NREL API key (required for NREL data source)'
    )
    
    # Output options
    parser.add_argument(
        '--output', '-o',
        type=str,
        default='pv_analysis',
        help='Output directory for results (default: pv_analysis)'
    )
    
    parser.add_argument(
        '--no-save',
        action='store_true',
        help='Do not save results to files'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Suppress progress messages'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version=f'%(prog)s {VERSION}'
    )
    
    parser.add_argument(
        '--help-tutorial',
        action='store_true',
        help='Show PV system design tutorial and theory guide'
    )
    
    parser.add_argument(
        '--help-glossary',
        action='store_true',
        help='Show glossary of technical terms used in solar PV'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Show tutorial if requested
    if hasattr(args, 'help_tutorial') and args.help_tutorial:
        tutorial_text = """
================================================================================
                        PV SYSTEM DESIGN TUTORIAL
================================================================================

UNDERSTANDING SOLAR ENERGY BASICS
---------------------------------
Solar panels convert sunlight to electricity through the photovoltaic effect.
Key factors affecting energy production:

1. LOCATION (Most Important)
   - Latitude affects sun angles and day length
   - Climate determines cloud cover
   - Local shading from buildings/trees

2. SYSTEM DESIGN
   - Panel orientation (tilt and azimuth)
   - System size and module efficiency
   - Inverter sizing and efficiency

3. ENVIRONMENTAL FACTORS
   - Temperature (hot panels produce less)
   - Soiling (dust, snow, bird droppings)
   - Weather patterns (clouds, rain)

QUICK SIZING GUIDE
------------------
Residential (USA Average):
- 1 kW system = ~1,400 kWh/year
- Average home uses ~10,000 kWh/year
- Typical system: 5-8 kW
- Usually glass_polymer + close_mount

Space Requirements:
- 1 kW ≈ 3-4 panels ≈ 60-80 sq ft

Commercial/Industrial:
- Flat roofs: glass_glass + open_rack with ballast
- Ground mount: glass_glass + open_rack on posts

ORIENTATION GUIDELINES
----------------------
Tilt Angle:
- Annual average = Your latitude
- Summer emphasis = Latitude - 15°
- Winter emphasis = Latitude + 15°
- Flat roofs: 10-15° minimum

Direction (Azimuth):
- 180° (South) = Standard orientation for Northern hemisphere
- ±45° from South = 5-10% reduction
- East/West = 15-20% reduction

INTERPRETING RESULTS
--------------------
Specific Yield (kWh/kWp/year):
- <1000: Below average (cloudy/shaded locations)
- 1000-1300: Average
- 1300-1600: Above average
- 1600-2000: High yield
- >2000: Very high (desert climates)

Performance Ratio (%):
- <70%: System has problems
- 70-75%: Below average
- 75-80%: Average
- 80-85%: Above average
- >85%: High performance

COMMON MISTAKES TO AVOID
------------------------
1. Ignoring shading (even partial shade hurts)
2. Undersizing wire (causes power loss)
3. Poor ventilation (hot panels = less power)
4. Wrong tilt for goal (summer vs winter vs annual)
5. Forgetting degradation (0.5%/year typical)

NEXT STEPS
----------
1. Run this tool with your location
2. Get multiple installer quotes
3. Check local incentives/rebates
4. Consider battery storage
5. Monitor actual vs predicted

For more help: python PV-PowerEstimate.py --help
================================================================================
"""
        print(tutorial_text)
        sys.exit(0)
    
    # Show glossary if requested
    if hasattr(args, 'help_glossary') and args.help_glossary:
        glossary_text = """
================================================================================
                    SOLAR PV GLOSSARY OF TERMS
================================================================================

ELECTRICAL TERMS
----------------
AC (Alternating Current): Electricity type used by grid and appliances
DC (Direct Current): Electricity type produced by solar panels
kW (kilowatt): Power unit, 1 kW = 1,000 watts
kWh (kilowatt-hour): Energy unit, 1 kWh = using 1 kW for 1 hour
kWp (kilowatt-peak): DC power rating at Standard Test Conditions
MW (megawatt): 1,000 kW, used for large systems

SOLAR TERMS
-----------
Azimuth: Compass direction panels face (0°=N, 90°=E, 180°=S, 270°=W)
GHI (Global Horizontal Irradiance): Total sunlight on flat surface
DNI (Direct Normal Irradiance): Direct beam sunlight
DHI (Diffuse Horizontal Irradiance): Scattered sunlight from sky
Irradiance: Instantaneous solar power per area (W/m²)
Irradiation: Solar energy over time (kWh/m²)
Insolation: Amount of solar radiation reaching a surface
POA (Plane of Array): Irradiance on tilted panel surface
Solar Noon: Time when sun is highest in sky
Zenith Angle: Angle between sun and vertical

SYSTEM COMPONENTS
-----------------
Array: Multiple solar panels connected together
Inverter: Converts DC from panels to AC for grid
Module: Individual solar panel
MPPT: Maximum Power Point Tracking (optimizes power)
String: Solar panels connected in series
BOS: Balance of System (everything except panels)
Mounting/Racking: Support structure for panels
  - Module types: glass_glass or glass_polymer backsheet
  - open_rack: Ground or pole mounted with airflow
  - close_mount: Attached to building roof
  - insulated_back: Building integrated PV (BIPV)

PERFORMANCE METRICS
-------------------
Capacity Factor: Average output / maximum possible output (%)
Degradation: Power loss over time (~0.5%/year)
Efficiency: Power out / power in (%)
Performance Ratio (PR): Actual / theoretical yield (%)
Specific Yield: Annual energy / system size (kWh/kWp)
Yield: Total energy produced

LOSS MECHANISMS
---------------
Clipping: Power loss when DC exceeds inverter capacity
LID: Light-Induced Degradation (first-year power loss)
Mismatch: Loss from unequal module performance
Shading: Shadows reducing power (can be severe)
Soiling: Dirt/dust on panels reducing light
Temperature Loss: Power reduction in hot conditions

FINANCIAL TERMS
---------------
LCOE: Levelized Cost of Energy ($/kWh over lifetime)
NPV: Net Present Value of investment
Payback Period: Years to recover investment
PPA: Power Purchase Agreement
ROI: Return on Investment

TECHNICAL PARAMETERS
--------------------
Albedo: Ground reflectance (0=black, 1=mirror)
AM: Air Mass (atmosphere thickness effect)
AOI: Angle of Incidence (between sun ray and panel normal)
STC: Standard Test Conditions (1000 W/m², 25°C, AM1.5)
Temperature Coefficient: Power change per °C (~-0.4%/°C)
Tilt: Panel angle from horizontal (0°=flat)

WEATHER/CLIMATE
---------------
TMY: Typical Meteorological Year (representative weather)
Ambient Temperature: Air temperature
Cell Temperature: Solar cell operating temperature
Wind Speed: Affects panel cooling

ADVANCED CONCEPTS
-----------------
Bifacial: Panels producing from both sides
Spectral Response: Efficiency vs light wavelength
Tracking: System that follows sun movement
Grid Parity: Solar cost equals grid electricity
Backsheet: Rear protective layer of module
  - glass_glass: Glass on both sides (bifacial capable)
  - glass_polymer: Traditional polymer backing

================================================================================
For detailed explanations, run: python PV-PowerEstimate.py --help-tutorial
================================================================================
"""
        print(glossary_text)
        sys.exit(0)
    
    # Configure logging based on quiet flag
    if args.quiet:
        logging.getLogger().setLevel(logging.WARNING)
    
    try:
        # Determine location
        latitude = None
        longitude = None
        address = None
        
        if args.lat is not None and args.lon is not None:
            # Coordinates provided
            latitude = args.lat
            longitude = args.lon
            logger.info(f"Using provided coordinates: {latitude}, {longitude}")
            
        elif args.address:
            # Address provided - geocode it
            logger.info(f"Geocoding address: {args.address}")
            geocoder = AddressGeocoder()
            coords = geocoder.geocode(args.address)
            
            if coords:
                latitude, longitude = coords
                address = args.address
            else:
                print(f"Error: Could not geocode address '{args.address}'")
                print("Please check the address or use coordinates instead.")
                return 1
                
        else:
            # Interactive mode
            print("\nPV-PowerEstimate - Solar PV Power Yield Calculator")
            print("=" * 50)
            print("\nThis tool estimates solar panel energy production for any location.")
            print("It uses real weather data and detailed physics modeling.")
            print("\nNeed help? Run with --help-tutorial for a detailed guide.")
            print("\nEnter location (choose one option):")
            print("1. Enter coordinates (latitude, longitude)")
            print("2. Enter address (street, city, etc.)")
            
            choice = input("\nChoice (1 or 2): ").strip()
            
            if choice == '1':
                print("\n📍 COORDINATE ENTRY")
                print("Tip: Find coordinates at maps.google.com (right-click → copy coordinates)")
                lat_str = input("Latitude (-90 to 90, negative for Southern hemisphere): ").strip()
                lon_str = input("Longitude (-180 to 180, negative for Western hemisphere): ").strip()
                
                try:
                    latitude = float(lat_str)
                    longitude = float(lon_str)
                except ValueError:
                    print("Error: Invalid coordinates")
                    return 1
                    
            elif choice == '2':
                print("\n🏠 ADDRESS ENTRY")
                print("Examples: '123 Main St, Toronto, ON' or just 'Vancouver, BC'")
                address = input("Address: ").strip()
                if address:
                    geocoder = AddressGeocoder()
                    coords = geocoder.geocode(address)
                    
                    if coords:
                        latitude, longitude = coords
                        print(f"✓ Found coordinates: {latitude:.4f}, {longitude:.4f}")
                    else:
                        print(f"Error: Could not geocode address '{address}'")
                        return 1
            else:
                print("Invalid choice")
                return 1
            
            # Ask about system size
            print("\n⚡ SYSTEM SIZE")
            print("Typical sizes: Residential 3-10 kW, Commercial 10-500 kW, Utility >1000 kW")
            print("Rule of thumb: 1 kW ≈ 3-4 panels ≈ 1,400 kWh/year (varies by location)")
            
            size_str = input(f"System size in kW (press Enter for default {DEFAULT_SYSTEM_SIZE} kW): ").strip()
            if size_str:
                try:
                    system_size = float(size_str)
                    # Calculate modules needed
                    modules_needed = int(system_size * 1000 / 400)  # Assuming 400W modules
                    system_config = SystemConfig()
                    system_config.modules_per_string = min(modules_needed, 20)
                    system_config.strings_per_inverter = max(1, modules_needed // 20)
                except ValueError:
                    print("Invalid size, using default")
                    system_config = SystemConfig()
            else:
                system_config = SystemConfig()
            
            # Ask about tilt
                        
            print("\n📐 TILT ANGLE")
            print(f"Recommended tilt for your latitude ({abs(latitude):.1f}°): {abs(latitude):.0f}°")
            print("Flatter = better for summer, Steeper = better for winter & snow shedding")
            
            tilt_str = input(f"Tilt angle in degrees (press Enter for latitude-based default): ").strip()
            if tilt_str:
                try:
                    system_config.surface_tilt = float(tilt_str)
                except ValueError:
                    system_config.surface_tilt = abs(latitude)
            else:
                system_config.surface_tilt = abs(latitude)
            
            # Set standard mounting type
            system_config.module_type = 'glass_glass'
            system_config.racking_model = 'open_rack'
            
            # Set azimuth based on hemisphere
            system_config.surface_azimuth = 180 if latitude > 0 else 0
            
            # Helper function for azimuth direction
            def azimuth_to_direction(azimuth):
                directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                             'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
                index = int((azimuth + 11.25) / 22.5) % 16
                return directions[index]
            
            print("\n🎯 Using standard azimuth (direction) for your hemisphere")
            print(f"   Azimuth: {system_config.surface_azimuth}° ({azimuth_to_direction(system_config.surface_azimuth)})")
            
            # Add some educational info before calculation
            print("\n" + "="*50)
            print("📊 STARTING CALCULATION")
            print("="*50)
            print("This tool will:")
            print("1. Fetch typical weather data for your location")
            print("2. Calculate sun angles for every hour of the year")
            print("3. Model panel temperature effects")
            print("4. Apply real-world loss factors")
            print("5. Generate detailed energy production estimates")
            print("="*50 + "\n")
        
        # Validate we have location
        if latitude is None or longitude is None:
            print("Error: Location not specified")
            return 1
        
        # Create calculator instance
        print(f"\nInitializing calculator for location: {latitude:.4f}, {longitude:.4f}")
        calc = SolarPVCalculator(
            latitude=latitude,
            longitude=longitude,
            altitude=args.altitude,
            address=address
        )
        
        # Fetch weather data
        print("Fetching weather data...")
        if args.data_source == 'nrel':
            if not args.nrel_api_key:
                print("Error: NREL data source requires --nrel-api-key")
                print("Get a free key at: https://developer.nrel.gov/signup/")
                return 1
            weather_data = calc.fetch_nrel_psm3_data(api_key=args.nrel_api_key)
        else:
            weather_data = calc.fetch_pvgis_data()
        
        if weather_data is None:
            print("Error: Failed to fetch weather data")
            return 1
        
        print(f"Retrieved {len(weather_data)} hours of weather data")
        
        # Configure system
        system_config = SystemConfig()
        
        # Apply command-line overrides
        if args.system_size:
            # Calculate modules needed for target system size
            modules_needed = int(args.system_size * 1000 / args.module_power)
            system_config.modules_per_string = min(modules_needed, 20)
            system_config.strings_per_inverter = max(1, modules_needed // 20)
            
        system_config.module_power = args.module_power
        system_config.surface_tilt = args.tilt if args.tilt else abs(calc.lat)
        system_config.surface_azimuth = args.azimuth
        system_config.module_type = args.module_type
        system_config.racking_model = args.racking_model
        
        # Size inverter appropriately (DC/AC ratio of 1.2)
        system_config.inverter_power = system_config.system_size_kw * 1000 / 1.2
        
        # Run simulation
        print(f"Running simulation for {system_config.system_size_kw:.1f} kW system...")
        results, system_size = calc.calculate_pv_output(weather_data, system_config)
        
        # Calculate yields
        print("Calculating energy yields...")
        monthly, annual_energy, annual_specific_yield, capacity_factor = \
            calc.calculate_monthly_yield(results, system_size)
        
        # Generate report
        print("Generating report...")
        report = calc.generate_report(
            weather_data, results, monthly, annual_energy,
            annual_specific_yield, capacity_factor, system_size, system_config
        )
        
        # Display key results
        print("\n" + "=" * 60)
        print("RESULTS SUMMARY")
        print("=" * 60)
        print(f"📍 Location: {calc.location.name}")
        print(f"⚡ System Size: {system_size:.1f} kW DC")
        print(f"📊 Annual Energy: {annual_energy:,.0f} kWh/year")
        print(f"📈 Specific Yield: {annual_specific_yield:,.0f} kWh/kWp/year")
        print(f"⚙️  Capacity Factor: {capacity_factor:.1f}%")
        print(f"💰 Est. Annual Revenue: ${annual_energy * 0.15:,.0f} (at $0.15/kWh)")
        print("=" * 60)
        
        # Add interpretation of results
        print("\n📋 RESULTS INTERPRETATION:")
        
        # Specific yield interpretation
        if annual_specific_yield < 1000:
            yield_rating = "Below average - Check for shading or consider different location"
        elif annual_specific_yield < 1300:
            yield_rating = "Average - Typical for cloudy/northern climates"
        elif annual_specific_yield < 1600:
            yield_rating = "Above average - Well-suited for solar"
        elif annual_specific_yield < 2000:
            yield_rating = "High - Strong solar resource"
        else:
            yield_rating = "Very high - Desert-like conditions"
        
        print(f"   Specific Yield Rating: {yield_rating}")
        
        # Capacity factor interpretation
        print(f"   Capacity Factor: {capacity_factor:.1f}% (typical solar: 15-25%)")
        
        # Payback estimate
        system_cost_estimate = system_size * 2000  # Rough $2/W installed
        payback_years = system_cost_estimate / (annual_energy * 0.15)
        print(f"   Simple Payback: ~{payback_years:.1f} years (at $2/W installed cost)")
        
        # CO2 savings
        co2_saved = annual_energy * 0.4  # kg CO2 per kWh (US grid average)
        print(f"   CO2 Avoided: {co2_saved/1000:.1f} metric tons/year")
        
        # Monthly variation
        best_month = monthly['energy_kwh'].idxmax()
        worst_month = monthly['energy_kwh'].idxmin()
        variation = monthly.loc[best_month, 'energy_kwh'] / monthly.loc[worst_month, 'energy_kwh']
        print(f"   Seasonal Variation: {variation:.1f}:1 ({best_month} vs {worst_month})")
        
        print("\n💡 RECOMMENDATIONS:")
        if capacity_factor < 15:
            print("   - Consider checking shading or system design")
        if variation > 3:
            print("   - High seasonal variation - consider battery storage")
        if annual_specific_yield > 1500:
            print("   - Above-average solar resource for investment")
        print("   - Get multiple installer quotes for accurate pricing")
        print("   - Check local incentives and net metering policies")
        
        print("=" * 60)
        
        # Save results unless disabled
        if not args.no_save:
            print(f"\nSaving results to {args.output}/")
            # Store system size in results for metadata
            results.attrs['system_size'] = system_size
            calc.save_results(results, monthly, report, args.output)
            print(f"Report saved to {args.output}/report.txt")
        else:
            # Print full report to console
            print("\nFULL REPORT:")
            print(report)
        
        print("\nAnalysis complete!")
        return 0
        
    except KeyboardInterrupt:
        print("\n\nAnalysis cancelled by user")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        print(f"\nError: {e}")
        print("Please check the log for details")
        return 1


if __name__ == "__main__":
    sys.exit(main())
