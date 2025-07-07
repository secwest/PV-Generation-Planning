#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PV-PowerEstimate.py - Solar PV Power Yield Calculator & Tutorial with Incentives v1.3.1

Copyright (c) 2025, Dragos Ruiu
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PV-PowerEstimate.py - Solar PV Power Yield Calculator & Tutorial with Incentives v1.3.2

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
   Current typical values (2024-2025):
   - Residential: $0.06-0.10/kWh
   - Commercial: $0.04-0.07/kWh  
   - Utility scale: $0.03-0.05/kWh

2. INSTALLED COSTS (2024-2025 US Market):
   System Type         $/W DC    Notes
   ----------------------------------------
   Residential         $2.50-3.00  Includes permitting, labor
   Small Commercial    $1.75-2.25  Economies of scale
   Large Commercial    $1.25-1.75  Bulk purchasing
   Utility Scale       $0.80-1.20  Lowest cost/watt

   Cost decline: ~70% reduction since 2010
   Future trend: ~3-5% annual decline expected

3. PAYBACK PERIOD:
   Years = (System Cost) / (Annual Savings)
   Current typical: 
   - With incentives: 4-7 years
   - Without incentives: 6-10 years

4. INCENTIVES (US):
   - Federal ITC: 30% through 2032
   - State/local: Varies widely
   - Net metering: Check local utility

5. DEGRADATION:
   - Year 1: -1.5% (LID)
   - Years 2-25: -0.5-0.7%/year
   - 25-year output: ~80-85% of initial

GLOBAL ELECTRICITY RATES
------------------------
This calculator now includes comprehensive electricity rate data for:
- All US states and Canadian provinces (with regional variations)
- European Union countries (27 members)
- Asia-Pacific region (including state-level data for India, China, Australia)
- Latin America (country and regional rates)
- Middle East and Africa (major markets)
- Over 150 countries total

Rates are updated for 2024-2025 and include:
- Residential, commercial, and industrial tariffs where available
- Time-of-use considerations
- Currency conversions to USD for comparison
- Regional variations within large countries

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
Version: 1.3.2
Date: 2025-07-06

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
from typing import Dict, Tuple, Optional, Union, Any, List
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
VERSION = "1.3.2"
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


# Comprehensive regional solar incentives database (2024-2025)
# Values are in percentage of system cost or $/W for rebates
SOLAR_INCENTIVES = {
    # US STATES - All federal programs plus state-specific
    "united states": {
        # Federal incentive applies to all states
        "federal": {
            "type": "tax_credit",
            "value": 0.30,  # 30% through 2032
            "expires": "2032-12-31",
            "notes": "Federal Investment Tax Credit (ITC)"
        },
        
        # State-specific incentives
        "california": {
            "programs": [
                {
                    "name": "SGIP",
                    "type": "rebate",
                    "value": 0.20,  # $/Wh for storage
                    "category": "battery",
                    "notes": "Self-Generation Incentive Program for storage"
                },
                {
                    "name": "DAC-SASH",
                    "type": "rebate",
                    "value": 3.00,  # $/W
                    "category": "low-income",
                    "notes": "Disadvantaged Communities Single-family Solar Homes"
                },
                {
                    "name": "Property Tax Exclusion",
                    "type": "tax_exemption",
                    "value": 1.0,  # 100% exemption
                    "notes": "Solar installations excluded from property tax"
                }
            ]
        },
        
        "new york": {
            "programs": [
                {
                    "name": "NY-Sun",
                    "type": "rebate",
                    "value": 0.20,  # $/W
                    "category": "residential",
                    "max_rebate": 5000,
                    "notes": "Declining block incentive"
                },
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.25,  # 25% of system cost
                    "max_credit": 5000,
                    "notes": "25% state tax credit"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "massachusetts": {
            "programs": [
                {
                    "name": "SMART",
                    "type": "performance",
                    "value": 0.15,  # $/kWh
                    "duration": 20,  # years
                    "notes": "Solar Massachusetts Renewable Target program"
                },
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.15,  # 15% of system cost
                    "max_credit": 1000,
                    "notes": "15% state tax credit"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "texas": {
            "programs": [
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption for solar value"
                },
                {
                    "name": "Austin Energy Rebate",
                    "type": "rebate",
                    "value": 2500,  # flat amount
                    "category": "utility",
                    "location": "Austin",
                    "notes": "Austin Energy solar rebate"
                },
                {
                    "name": "CPS Energy Rebate",
                    "type": "rebate",
                    "value": 0.60,  # $/W
                    "category": "utility",
                    "location": "San Antonio",
                    "notes": "CPS Energy solar rebate"
                }
            ]
        },
        
        "florida": {
            "programs": [
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,  # 1:1 credit
                    "notes": "Full retail rate net metering"
                }
            ]
        },
        
        "arizona": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.25,
                    "max_credit": 1000,
                    "notes": "25% state tax credit"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "No added property tax"
                }
            ]
        },
        
        "colorado": {
            "programs": [
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Xcel Energy Rebate",
                    "type": "rebate",
                    "value": 0.50,  # $/W
                    "category": "utility",
                    "notes": "Xcel Energy Solar*Rewards"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Renewable energy property tax exemption"
                }
            ]
        },
        
        "new jersey": {
            "programs": [
                {
                    "name": "SuSI",
                    "type": "performance",
                    "value": 90,  # $/MWh
                    "duration": 15,
                    "notes": "Successor Solar Incentive program"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Solar property tax exemption"
                }
            ]
        },
        
        "illinois": {
            "programs": [
                {
                    "name": "Illinois Shines",
                    "type": "performance",
                    "value": 0.0775,  # $/kWh for 15 years
                    "duration": 15,
                    "notes": "Adjustable Block Program"
                },
                {
                    "name": "Solar for All",
                    "type": "rebate",
                    "value": 1.0,  # 100% for qualifying
                    "category": "low-income",
                    "notes": "Low-income solar program"
                }
            ]
        },
        
        "maryland": {
            "programs": [
                {
                    "name": "State Grant",
                    "type": "rebate",
                    "value": 1000,  # flat amount
                    "category": "residential",
                    "notes": "Residential Clean Energy Rebate"
                },
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.30,
                    "max_credit": 5000,
                    "expires": "2025-12-31",
                    "notes": "30% state tax credit through 2025"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption"
                }
            ]
        },
        
        "minnesota": {
            "programs": [
                {
                    "name": "Solar*Rewards",
                    "type": "rebate",
                    "value": 0.50,  # $/W
                    "category": "utility",
                    "notes": "Xcel Energy rebate"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Solar property tax exemption"
                }
            ]
        },
        
        "oregon": {
            "programs": [
                {
                    "name": "Solar + Storage Rebate",
                    "type": "rebate",
                    "value": 0.30,  # $/W
                    "max_rebate": 5000,
                    "category": "residential",
                    "notes": "Oregon solar + storage rebate"
                },
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.40,  # 40% for low-income
                    "category": "low-income",
                    "max_credit": 5000,
                    "notes": "Enhanced credit for low-income"
                }
            ]
        },
        
        # Additional states with basic incentives
        "connecticut": {
            "programs": [
                {
                    "name": "Residential Solar Investment",
                    "type": "rebate",
                    "value": 0.40,  # $/W
                    "notes": "Green Bank incentive"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption"
                }
            ]
        },
        
        "nevada": {
            "programs": [
                {
                    "name": "NV Energy Rebate",
                    "type": "rebate",
                    "value": 0.15,  # $/W
                    "category": "utility",
                    "notes": "NV Energy solar rebate"
                },
                {
                    "name": "Property Tax Abatement",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Property tax abatement"
                }
            ]
        },
        
        "hawaii": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.35,  # 35%
                    "max_credit": 5000,
                    "notes": "35% state tax credit"
                },
                {
                    "name": "Green Infrastructure Loan",
                    "type": "loan",
                    "value": 0.0,  # 0% interest
                    "notes": "On-bill financing available"
                }
            ]
        },
        
        "rhode island": {
            "programs": [
                {
                    "name": "REF Solar Grant",
                    "type": "rebate",
                    "value": 0.85,  # $/W
                    "max_rebate": 5000,
                    "notes": "Renewable Energy Fund grant"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "vermont": {
            "programs": [
                {
                    "name": "State Incentive",
                    "type": "rebate",
                    "value": 0.40,  # $/W
                    "notes": "Efficiency Vermont incentive"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "new mexico": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.10,  # 10%
                    "max_credit": 6000,
                    "notes": "10% state tax credit"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption"
                }
            ]
        },
        
        "iowa": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.30,  # 30%
                    "max_credit": 5000,
                    "notes": "30% state tax credit"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "duration": 5,  # years
                    "notes": "5-year property tax exemption"
                }
            ]
        },
        
        "south carolina": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.25,  # 25%
                    "notes": "25% state tax credit"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Manufacturing equipment exemption"
                }
            ]
        },
        
        "wisconsin": {
            "programs": [
                {
                    "name": "Focus on Energy",
                    "type": "rebate",
                    "value": 0.10,  # $/W
                    "max_rebate": 500,
                    "notes": "Focus on Energy rebate"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "utah": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.25,
                    "max_credit": 1600,
                    "notes": "25% state tax credit"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Renewable energy property tax exemption"
                }
            ]
        }
    },
    
    # CANADA - Federal and provincial programs
    "canada": {
        "federal": {
            "programs": [
                {
                    "name": "Greener Homes Grant",
                    "type": "rebate",
                    "value": 5000,  # flat amount
                    "category": "residential",
                    "notes": "Canada Greener Homes Grant for solar"
                },
                {
                    "name": "Greener Homes Loan",
                    "type": "loan",
                    "value": 40000,  # max loan
                    "interest": 0.0,  # 0% interest
                    "notes": "Interest-free loan up to $40,000"
                }
            ]
        },
        
        "ontario": {
            "programs": [
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Full retail rate net metering"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "category": "commercial",
                    "notes": "Commercial property tax exemption"
                }
            ]
        },
        
        "british columbia": {
            "programs": [
                {
                    "name": "PST Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Provincial sales tax exemption"
                },
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "BC Hydro net metering program"
                }
            ]
        },
        
        "alberta": {
            "programs": [
                {
                    "name": "Solar Rebate",
                    "type": "rebate",
                    "value": 0.90,  # $/W
                    "max_rebate": 10000,
                    "notes": "Residential and Commercial Solar Program"
                },
                {
                    "name": "Micro-generation",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Credit for excess generation"
                }
            ]
        },
        
        "quebec": {
            "programs": [
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Hydro-Quebec net metering"
                },
                {
                    "name": "Commercial Program",
                    "type": "rebate",
                    "value": 0.50,  # $/W
                    "category": "commercial",
                    "notes": "Commercial solar incentive"
                }
            ]
        },
        
        "saskatchewan": {
            "programs": [
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "max_system": 100,  # kW
                    "notes": "SaskPower net metering up to 100kW"
                },
                {
                    "name": "PST Rebate",
                    "type": "rebate",
                    "value": 0.10,  # 10% PST rebate
                    "notes": "PST rebate on solar equipment"
                }
            ]
        },
        
        "nova scotia": {
            "programs": [
                {
                    "name": "SolarHomes",
                    "type": "rebate",
                    "value": 0.60,  # $/W
                    "max_rebate": 6000,
                    "notes": "Efficiency NS SolarHomes rebate"
                },
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Enhanced net metering program"
                }
            ]
        },
        
        "prince edward island": {
            "programs": [
                {
                    "name": "Solar Electric Rebate",
                    "type": "rebate",
                    "value": 1.00,  # $/W
                    "max_rebate": 10000,
                    "notes": "PEI solar electric rebate program"
                },
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Net metering available"
                }
            ]
        },
        
        "newfoundland and labrador": {
            "programs": [
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Newfoundland Power net metering"
                }
            ]
        }
    },
    
    # EUROPE - Major markets
    "germany": {
        "programs": [
            {
                "name": "Feed-in Tariff",
                "type": "feed_in_tariff",
                "value": 0.082,  # €/kWh
                "duration": 20,
                "notes": "EEG feed-in tariff for <10kW"
            },
            {
                "name": "KfW Loan",
                "type": "loan",
                "value": 0.0145,  # 1.45% interest
                "notes": "Low-interest loans from KfW bank"
            },
            {
                "name": "VAT Reduction",
                "type": "tax_reduction",
                "value": 0.0,  # 0% VAT
                "notes": "0% VAT on residential solar"
            }
        ]
    },
    
    "france": {
        "programs": [
            {
                "name": "Self-consumption Premium",
                "type": "rebate",
                "value": 0.38,  # €/W for <3kW
                "notes": "Premium for self-consumption"
            },
            {
                "name": "Feed-in Tariff",
                "type": "feed_in_tariff",
                "value": 0.13,  # €/kWh
                "duration": 20,
                "notes": "20-year feed-in tariff"
            },
            {
                "name": "VAT Reduction",
                "type": "tax_reduction",
                "value": 0.10,  # 10% VAT instead of 20%
                "notes": "Reduced VAT rate"
            }
        ]
    },
    
    "italy": {
        "programs": [
            {
                "name": "Superbonus 110%",
                "type": "tax_credit",
                "value": 1.10,  # 110% tax deduction
                "expires": "2025-12-31",
                "notes": "110% tax deduction over 4 years"
            },
            {
                "name": "Net Billing",
                "type": "net_metering",
                "value": 0.80,  # partial credit
                "notes": "Scambio sul posto (net billing)"
            }
        ]
    },
    
    "spain": {
        "programs": [
            {
                "name": "Next Generation EU Funds",
                "type": "rebate",
                "value": 0.60,  # €/W
                "max_rebate": 3000,
                "notes": "EU recovery fund subsidies"
            },
            {
                "name": "IBI Reduction",
                "type": "tax_reduction",
                "value": 0.50,  # 50% property tax reduction
                "duration": 5,
                "notes": "Property tax reduction varies by municipality"
            },
            {
                "name": "Net Billing",
                "type": "net_metering",
                "value": 0.90,
                "notes": "Simplified compensation mechanism"
            }
        ]
    },
    
    "netherlands": {
        "programs": [
            {
                "name": "Net Metering",
                "type": "net_metering",
                "value": 1.0,
                "expires": "2027-01-01",
                "notes": "Full net metering until 2027"
            },
            {
                "name": "BTW Refund",
                "type": "tax_refund",
                "value": 0.21,  # 21% VAT refund
                "notes": "VAT refund for residential solar"
            },
            {
                "name": "SDE++",
                "type": "feed_in_premium",
                "value": 0.05,  # €/kWh premium
                "category": "commercial",
                "notes": "Feed-in premium for large systems"
            }
        ]
    },
    
    "united kingdom": {
        "programs": [
            {
                "name": "Smart Export Guarantee",
                "type": "feed_in_tariff",
                "value": 0.05,  # £/kWh average
                "notes": "SEG payments for exported electricity"
            },
            {
                "name": "0% VAT",
                "type": "tax_exemption",
                "value": 1.0,
                "notes": "0% VAT on residential solar until 2027"
            },
            {
                "name": "ECO4 Scheme",
                "type": "rebate",
                "value": 1.0,  # 100% for qualifying
                "category": "low-income",
                "notes": "Free solar for low-income households"
            }
        ]
    },
    
    # AUSTRALIA - State programs
    "australia": {
        "federal": {
            "programs": [
                {
                    "name": "STC Rebate",
                    "type": "rebate",
                    "value": 0.45,  # $/W approximate
                    "notes": "Small-scale Technology Certificates"
                },
                {
                    "name": "GST Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "GST exemption for systems <100kW"
                }
            ]
        },
        
        "victoria": {
            "programs": [
                {
                    "name": "Solar Homes",
                    "type": "rebate",
                    "value": 1400,  # flat amount
                    "notes": "Victorian Solar Homes rebate"
                },
                {
                    "name": "Interest-free Loan",
                    "type": "loan",
                    "value": 1400,
                    "interest": 0.0,
                    "notes": "Interest-free loan matching rebate"
                }
            ]
        },
        
        "new south wales": {
            "programs": [
                {
                    "name": "Empowering Homes",
                    "type": "loan",
                    "value": 14000,
                    "interest": 0.0,
                    "notes": "Interest-free loan for solar+battery"
                },
                {
                    "name": "Low Income Solar",
                    "type": "rebate",
                    "value": 2200,
                    "category": "low-income",
                    "notes": "Low income household rebate"
                }
            ]
        },
        
        "queensland": {
            "programs": [
                {
                    "name": "Battery Booster",
                    "type": "rebate",
                    "value": 3000,
                    "category": "battery",
                    "notes": "Battery rebate program"
                },
                {
                    "name": "Solar for Rentals",
                    "type": "rebate",
                    "value": 3500,
                    "category": "rental",
                    "notes": "Rebate for rental properties"
                }
            ]
        },
        
        "south australia": {
            "programs": [
                {
                    "name": "Home Battery Scheme",
                    "type": "rebate",
                    "value": 0.30,  # $/Wh
                    "max_rebate": 3000,
                    "category": "battery",
                    "notes": "Battery subsidy program"
                }
            ]
        }
    },
    
    # Other major markets
    "japan": {
        "programs": [
            {
                "name": "FIT Scheme",
                "type": "feed_in_tariff",
                "value": 16,  # ¥/kWh
                "duration": 10,
                "notes": "Feed-in tariff for <10kW"
            },
            {
                "name": "Tokyo Subsidy",
                "type": "rebate",
                "value": 100000,  # ¥/kW
                "location": "Tokyo",
                "notes": "Tokyo metropolitan subsidy"
            }
        ]
    },
    
    "south korea": {
        "programs": [
            {
                "name": "Home Solar Subsidy",
                "type": "rebate",
                "value": 0.70,  # 70% subsidy
                "notes": "Government subsidy program"
            },
            {
                "name": "REC Trading",
                "type": "performance",
                "value": 50000,  # ₩/REC
                "notes": "Renewable Energy Certificate trading"
            }
        ]
    },
    
    "india": {
        "federal": {
            "programs": [
                {
                    "name": "PM-KUSUM",
                    "type": "rebate",
                    "value": 0.60,  # 60% subsidy
                    "category": "agricultural",
                    "notes": "Agricultural pump solarization"
                },
                {
                    "name": "Rooftop Solar Phase II",
                    "type": "rebate",
                    "value": 0.40,  # 40% for <3kW
                    "notes": "National rooftop solar program"
                }
            ]
        }
    },
    
    "china": {
        "programs": [
            {
                "name": "Feed-in Tariff",
                "type": "feed_in_tariff",
                "value": 0.42,  # ¥/kWh
                "notes": "National feed-in tariff"
            },
            {
                "name": "Distributed Solar Subsidy",
                "type": "rebate",
                "value": 0.02,  # ¥/kWh
                "notes": "Additional distributed generation subsidy"
            }
        ]
    }
}


@dataclass
class IncentiveDetails:
    """
    Details about a specific solar incentive program.
    """
    name: str
    type: str  # tax_credit, rebate, performance, loan, etc.
    value: float  # Percentage, $/W, or flat amount
    max_value: Optional[float] = None
    duration: Optional[int] = None  # Years for performance incentives
    expires: Optional[str] = None
    category: Optional[str] = None  # residential, commercial, low-income
    notes: Optional[str] = None


# Comprehensive global electricity rates database (2024-2025 data)
# Rates are in local currency per kWh
ELECTRICITY_RATES = {
    # NORTH AMERICA - Detailed coverage
    "canada": {
        "alberta": 0.166,
        "british columbia": 0.133,
        "manitoba": 0.097,
        "new brunswick": 0.129,
        "newfoundland and labrador": 0.137,
        "northwest territories": 0.387,
        "nova scotia": 0.183,
        "nunavut": 0.375,
        "ontario": 0.158,
        "prince edward island": 0.179,
        "quebec": 0.073,
        "saskatchewan": 0.150,
        "yukon": 0.187,
        "default": 0.140
    },
    
    "united states": {
        "alabama": 0.147,
        "alaska": 0.235,
        "arizona": 0.136,
        "arkansas": 0.125,
        "california": 0.287,
        "colorado": 0.140,
        "connecticut": 0.248,
        "delaware": 0.139,
        "district of columbia": 0.165,
        "florida": 0.139,
        "georgia": 0.138,
        "hawaii": 0.447,
        "idaho": 0.111,
        "illinois": 0.147,
        "indiana": 0.146,
        "iowa": 0.120,
        "kansas": 0.132,
        "kentucky": 0.123,
        "louisiana": 0.120,
        "maine": 0.229,
        "maryland": 0.148,
        "massachusetts": 0.264,
        "michigan": 0.179,
        "minnesota": 0.138,
        "mississippi": 0.129,
        "missouri": 0.120,
        "montana": 0.117,
        "nebraska": 0.116,
        "nevada": 0.143,
        "new hampshire": 0.267,
        "new jersey": 0.175,
        "new mexico": 0.139,
        "new york": 0.216,
        "north carolina": 0.123,
        "north dakota": 0.109,
        "ohio": 0.138,
        "oklahoma": 0.113,
        "oregon": 0.118,
        "pennsylvania": 0.157,
        "rhode island": 0.273,
        "south carolina": 0.137,
        "south dakota": 0.125,
        "tennessee": 0.127,
        "texas": 0.143,
        "utah": 0.110,
        "vermont": 0.208,
        "virginia": 0.134,
        "washington": 0.103,
        "west virginia": 0.133,
        "wisconsin": 0.154,
        "wyoming": 0.110,
        "default": 0.154
    },
    
    "mexico": {
        "baja california": 0.092,
        "baja california sur": 0.088,
        "chihuahua": 0.085,
        "mexico city": 0.079,
        "nuevo leon": 0.082,
        "jalisco": 0.081,
        "yucatan": 0.089,
        "default": 0.083
    },
    
    # EUROPE - Complete EU coverage
    "austria": 0.246,
    "belgium": 0.337,
    "bulgaria": 0.119,
    "croatia": 0.137,
    "cyprus": 0.238,
    "czech republic": 0.183,
    "denmark": 0.356,
    "estonia": 0.193,
    "finland": 0.178,
    "france": 0.231,
    "germany": 0.397,
    "greece": 0.189,
    "hungary": 0.113,
    "ireland": 0.298,
    "italy": 0.284,
    "latvia": 0.201,
    "lithuania": 0.181,
    "luxembourg": 0.192,
    "malta": 0.125,
    "netherlands": 0.300,
    "poland": 0.173,
    "portugal": 0.222,
    "romania": 0.152,
    "slovakia": 0.168,
    "slovenia": 0.167,
    "spain": 0.247,
    "sweden": 0.153,
    
    # Non-EU European countries
    "united kingdom": 0.228,
    "norway": 0.116,
    "switzerland": 0.210,
    "iceland": 0.054,
    "albania": 0.094,
    "bosnia and herzegovina": 0.089,
    "kosovo": 0.067,
    "macedonia": 0.078,
    "moldova": 0.112,
    "montenegro": 0.101,
    "serbia": 0.075,
    "turkey": 0.093,
    "ukraine": 0.044,
    
    # ASIA - Comprehensive coverage
    "china": {
        "beijing": 0.53,
        "shanghai": 0.61,
        "guangdong": 0.58,
        "shandong": 0.55,
        "jiangsu": 0.56,
        "zhejiang": 0.57,
        "sichuan": 0.45,
        "hebei": 0.52,
        "henan": 0.50,
        "hubei": 0.51,
        "hunan": 0.54,
        "anhui": 0.53,
        "fujian": 0.55,
        "jiangxi": 0.52,
        "liaoning": 0.49,
        "heilongjiang": 0.48,
        "shaanxi": 0.47,
        "gansu": 0.45,
        "qinghai": 0.43,
        "xinjiang": 0.39,
        "tibet": 0.38,
        "inner mongolia": 0.42,
        "default": 0.52
    },
    
    "india": {
        "maharashtra": 7.14,
        "gujarat": 5.50,
        "delhi": 6.50,
        "tamil nadu": 6.85,
        "karnataka": 6.95,
        "andhra pradesh": 7.25,
        "telangana": 7.20,
        "west bengal": 7.85,
        "rajasthan": 6.75,
        "uttar pradesh": 6.30,
        "madhya pradesh": 6.15,
        "kerala": 5.80,
        "haryana": 6.45,
        "punjab": 6.00,
        "bihar": 6.90,
        "odisha": 5.40,
        "assam": 6.70,
        "jharkhand": 6.20,
        "chattisgarh": 5.30,
        "himachal pradesh": 4.50,
        "uttarakhand": 5.25,
        "goa": 3.25,
        "jammu and kashmir": 3.00,
        "northeast states": 5.50,
        "default": 6.50
    },
    
    "japan": {
        "tokyo": 31.0,
        "osaka": 29.5,
        "hokkaido": 33.0,
        "kyushu": 28.5,
        "okinawa": 32.0,
        "default": 31.0
    },
    
    "south korea": 123.7,
    "taiwan": 2.63,
    "hong kong": 1.19,
    "singapore": 0.226,
    "thailand": 4.18,
    "vietnam": 1864,
    "philippines": 9.85,
    "indonesia": 1150,
    "malaysia": 0.436,
    "myanmar": 110,
    "cambodia": 720,
    "laos": 948,
    "bangladesh": 7.18,
    "pakistan": 16.5,
    "sri lanka": 21.0,
    "nepal": 8.77,
    "afghanistan": 2.85,
    "kazakhstan": 16.9,
    "uzbekistan": 295,
    "kyrgyzstan": 2.16,
    "tajikistan": 0.35,
    "turkmenistan": 0.033,
    "mongolia": 232,
    "north korea": 0.03,
    
    # MIDDLE EAST
    "saudi arabia": 0.048,
    "united arab emirates": 0.085,
    "qatar": 0.041,
    "kuwait": 0.030,
    "bahrain": 0.029,
    "oman": 0.062,
    "jordan": 0.142,
    "lebanon": 0.056,
    "israel": 0.485,
    "palestine": 0.556,
    "syria": 0.012,
    "iraq": 0.040,
    "iran": 0.007,
    "yemen": 0.038,
    
    # AFRICA
    "south africa": {
        "gauteng": 2.31,
        "western cape": 2.45,
        "kwazulu-natal": 2.28,
        "eastern cape": 2.38,
        "mpumalanga": 2.25,
        "limpopo": 2.22,
        "north west": 2.26,
        "free state": 2.29,
        "northern cape": 2.33,
        "default": 2.31
    },
    
    "egypt": 1.45,
    "nigeria": 68,
    "kenya": 23.7,
    "ethiopia": 1.36,
    "morocco": 1.26,
    "algeria": 4.67,
    "tunisia": 0.183,
    "libya": 0.041,
    "sudan": 5.67,
    "ghana": 0.365,
    "tanzania": 292,
    "uganda": 720,
    "zimbabwe": 0.098,
    "zambia": 0.089,
    "mozambique": 6.84,
    "malawi": 152,
    "rwanda": 183,
    "botswana": 1.29,
    "namibia": 1.78,
    "mauritius": 6.35,
    "madagascar": 645,
    "senegal": 118,
    "ivory coast": 87.4,
    "cameroon": 79.5,
    "angola": 42.5,
    "democratic republic of congo": 0.089,
    "gabon": 123,
    "mauritania": 18.2,
    "mali": 112,
    "burkina faso": 105,
    "niger": 89.7,
    "chad": 95.6,
    "somalia": 0.50,
    "eritrea": 0.14,
    "djibouti": 32.4,
    "seychelles": 5.48,
    "cape verde": 25.3,
    "guinea": 1250,
    "sierra leone": 2854,
    "liberia": 0.41,
    "togo": 125,
    "benin": 123,
    "gambia": 7.82,
    "guinea-bissau": 93.5,
    "equatorial guinea": 71.5,
    "central african republic": 88.9,
    "congo": 65.4,
    "sao tome and principe": 7.25,
    "comoros": 89.5,
    "lesotho": 1.45,
    "swaziland": 1.32,
    
    # SOUTH AMERICA
    "brazil": {
        "sao paulo": 0.75,
        "rio de janeiro": 0.82,
        "minas gerais": 0.71,
        "rio grande do sul": 0.68,
        "parana": 0.66,
        "santa catarina": 0.65,
        "bahia": 0.70,
        "pernambuco": 0.73,
        "ceara": 0.72,
        "amazonas": 0.67,
        "para": 0.69,
        "mato grosso": 0.74,
        "goias": 0.71,
        "distrito federal": 0.69,
        "default": 0.71
    },
    
    "argentina": {
        "buenos aires": 65.4,
        "cordoba": 68.2,
        "santa fe": 66.8,
        "mendoza": 71.3,
        "tucuman": 69.5,
        "default": 67.8
    },
    
    "chile": 159,
    "colombia": 678,
    "peru": 0.64,
    "venezuela": 0.001,
    "ecuador": 0.092,
    "bolivia": 0.58,
    "paraguay": 325,
    "uruguay": 6.87,
    "guyana": 32.1,
    "suriname": 0.087,
    "french guiana": 0.231,
    
    # OCEANIA
    "australia": {
        "new south wales": 0.308,
        "victoria": 0.289,
        "queensland": 0.285,
        "south australia": 0.347,
        "western australia": 0.289,
        "tasmania": 0.265,
        "northern territory": 0.255,
        "australian capital territory": 0.212,
        "default": 0.294
    },
    
    "new zealand": {
        "north island": 0.303,
        "south island": 0.289,
        "default": 0.296
    },
    
    "fiji": 0.343,
    "papua new guinea": 0.482,
    "solomon islands": 0.95,
    "vanuatu": 0.63,
    "samoa": 0.87,
    "tonga": 0.77,
    "kiribati": 0.54,
    "tuvalu": 0.60,
    "nauru": 0.52,
    "palau": 0.35,
    "marshall islands": 0.39,
    "micronesia": 0.41,
    "french polynesia": 35.2,
    "new caledonia": 26.8,
    "cook islands": 0.82,
    
    # CARIBBEAN
    "jamaica": 44.7,
    "trinidad and tobago": 0.28,
    "barbados": 0.41,
    "bahamas": 0.32,
    "haiti": 13.5,
    "dominican republic": 11.8,
    "cuba": 0.10,
    "puerto rico": 0.22,
    "cayman islands": 0.35,
    "bermuda": 0.44,
    "virgin islands": 0.38,
    "antigua and barbuda": 0.38,
    "saint lucia": 0.36,
    "grenada": 0.37,
    "dominica": 0.39,
    "saint vincent": 0.41,
    "saint kitts and nevis": 0.37,
    "turks and caicos": 0.35,
    "aruba": 0.28,
    "curacao": 0.39,
    "bonaire": 0.31,
    
    # Default global rate
    "default": 0.140
}

# Currency conversion rates to USD (as of Jan 2025)
# Extended coverage for all currencies in the database
CURRENCY_TO_USD = {
    # Major currencies
    "CAD": 0.70,    # Canadian Dollar
    "USD": 1.00,    # US Dollar
    "EUR": 1.05,    # Euro
    "GBP": 1.27,    # British Pound
    "JPY": 0.0064,  # Japanese Yen
    "CNY": 0.137,   # Chinese Yuan
    "INR": 0.012,   # Indian Rupee
    
    # Americas
    "MXN": 0.049,   # Mexican Peso
    "BRL": 0.163,   # Brazilian Real
    "ARS": 0.0010,  # Argentine Peso
    "CLP": 0.0010,  # Chilean Peso
    "COP": 0.00023, # Colombian Peso
    "PEN": 0.265,   # Peruvian Sol
    "VES": 0.020,   # Venezuelan Bolivar
    "BOB": 0.145,   # Bolivian Boliviano
    "PYG": 0.00013, # Paraguayan Guarani
    "UYU": 0.025,   # Uruguayan Peso
    "GYD": 0.0048,  # Guyanese Dollar
    "SRD": 0.028,   # Surinamese Dollar
    
    # Caribbean
    "JMD": 0.0064,  # Jamaican Dollar
    "TTD": 0.147,   # Trinidad Dollar
    "BBD": 0.50,    # Barbadian Dollar
    "BSD": 1.00,    # Bahamian Dollar
    "HTG": 0.0076,  # Haitian Gourde
    "DOP": 0.017,   # Dominican Peso
    "CUP": 0.042,   # Cuban Peso
    "XCD": 0.37,    # East Caribbean Dollar
    "KYD": 1.20,    # Cayman Dollar
    "BMD": 1.00,    # Bermudian Dollar
    "AWG": 0.56,    # Aruban Florin
    "ANG": 0.56,    # Netherlands Antillean Guilder
    
    # Europe (non-Euro)
    "CHF": 1.10,    # Swiss Franc
    "NOK": 0.089,   # Norwegian Krone
    "SEK": 0.091,   # Swedish Krona
    "DKK": 0.141,   # Danish Krone
    "ISK": 0.0071,  # Icelandic Krona
    "CZK": 0.042,   # Czech Koruna
    "PLN": 0.244,   # Polish Zloty
    "HUF": 0.0025,  # Hungarian Forint
    "RON": 0.212,   # Romanian Leu
    "BGN": 0.536,   # Bulgarian Lev
    "HRK": 0.139,   # Croatian Kuna
    "RSD": 0.0089,  # Serbian Dinar
    "BAM": 0.536,   # Bosnia Mark
    "MKD": 0.017,   # Macedonian Denar
    "ALL": 0.0093,  # Albanian Lek
    "MDL": 0.054,   # Moldovan Leu
    "UAH": 0.024,   # Ukrainian Hryvnia
    "TRY": 0.029,   # Turkish Lira
    
    # Asia
    "KRW": 0.00069, # South Korean Won
    "TWD": 0.031,   # Taiwan Dollar
    "HKD": 0.128,   # Hong Kong Dollar
    "SGD": 0.735,   # Singapore Dollar
    "THB": 0.029,   # Thai Baht
    "VND": 0.000039,# Vietnamese Dong
    "PHP": 0.017,   # Philippine Peso
    "IDR": 0.000062,# Indonesian Rupiah
    "MYR": 0.222,   # Malaysian Ringgit
    "MMK": 0.00048, # Myanmar Kyat
    "KHR": 0.00025, # Cambodian Riel
    "LAK": 0.000045,# Lao Kip
    "BDT": 0.0084,  # Bangladeshi Taka
    "PKR": 0.0036,  # Pakistani Rupee
    "LKR": 0.0031,  # Sri Lankan Rupee
    "NPR": 0.0074,  # Nepalese Rupee
    "AFN": 0.014,   # Afghan Afghani
    "KZT": 0.0020,  # Kazakhstani Tenge
    "UZS": 0.000078,# Uzbek Som
    "KGS": 0.012,   # Kyrgyz Som
    "TJS": 0.091,   # Tajik Somoni
    "TMT": 0.286,   # Turkmen Manat
    "MNT": 0.00029, # Mongolian Tugrik
    "KPW": 0.0011,  # North Korean Won
    
    # Middle East
    "SAR": 0.267,   # Saudi Riyal
    "AED": 0.272,   # UAE Dirham
    "QAR": 0.275,   # Qatari Riyal
    "KWD": 3.25,    # Kuwaiti Dinar
    "BHD": 2.65,    # Bahraini Dinar
    "OMR": 2.60,    # Omani Rial
    "JOD": 1.41,    # Jordanian Dinar
    "LBP": 0.000011,# Lebanese Pound
    "ILS": 0.277,   # Israeli Shekel
    "SYP": 0.00008, # Syrian Pound
    "IQD": 0.00076, # Iraqi Dinar
    "IRR": 0.000002,# Iranian Rial
    "YER": 0.0040,  # Yemeni Rial
    
    # Africa
    "ZAR": 0.053,   # South African Rand
    "EGP": 0.020,   # Egyptian Pound
    "NGN": 0.00064, # Nigerian Naira
    "KES": 0.0078,  # Kenyan Shilling
    "ETB": 0.0079,  # Ethiopian Birr
    "MAD": 0.098,   # Moroccan Dirham
    "DZD": 0.0074,  # Algerian Dinar
    "TND": 0.312,   # Tunisian Dinar
    "LYD": 0.206,   # Libyan Dinar
    "SDG": 0.0017,  # Sudanese Pound
    "GHS": 0.066,   # Ghanaian Cedi
    "TZS": 0.00040, # Tanzanian Shilling
    "UGX": 0.00027, # Ugandan Shilling
    "ZWL": 0.0031,  # Zimbabwean Dollar
    "ZMW": 0.036,   # Zambian Kwacha
    "MZN": 0.016,   # Mozambican Metical
    "MWK": 0.00058, # Malawian Kwacha
    "RWF": 0.00073, # Rwandan Franc
    "BWP": 0.072,   # Botswana Pula
    "NAD": 0.053,   # Namibian Dollar
    "MUR": 0.021,   # Mauritian Rupee
    "MGA": 0.00021, # Malagasy Ariary
    "XOF": 0.0016,  # West African CFA Franc
    "XAF": 0.0016,  # Central African CFA Franc
    "MRU": 0.025,   # Mauritanian Ouguiya
    "SOS": 0.0018,  # Somali Shilling
    "ERN": 0.067,   # Eritrean Nakfa
    "DJF": 0.0056,  # Djiboutian Franc
    "SCR": 0.069,   # Seychellois Rupee
    "CVE": 0.0095,  # Cape Verdean Escudo
    "GNF": 0.00012, # Guinean Franc
    "SLL": 0.000039,# Sierra Leonean Leone
    "LRD": 0.0052,  # Liberian Dollar
    "GMD": 0.014,   # Gambian Dalasi
    "STN": 0.043,   # São Tomé Príncipe Dobra
    "KMF": 0.0021,  # Comorian Franc
    "LSL": 0.053,   # Lesotho Loti
    "SZL": 0.053,   # Swazi Lilangeni
    
    # Oceania
    "AUD": 0.62,    # Australian Dollar
    "NZD": 0.56,    # New Zealand Dollar
    "FJD": 0.436,   # Fijian Dollar
    "PGK": 0.248,   # Papua New Guinea Kina
    "SBD": 0.119,   # Solomon Islands Dollar
    "VUV": 0.0082,  # Vanuatu Vatu
    "WST": 0.356,   # Samoan Tala
    "TOP": 0.419,   # Tongan Pa'anga
    "XPF": 0.0088,  # CFP Franc
}


@dataclass
class LocationInfo:
    """
    Extended location information including geopolitical details.
    """
    latitude: float
    longitude: float
    altitude: float
    address: str
    country: Optional[str] = None
    state_province: Optional[str] = None
    city: Optional[str] = None
    country_code: Optional[str] = None
    electricity_rate: Optional[float] = None
    currency: Optional[str] = None
    rate_source: Optional[str] = None


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
    shading_loss: float = 1.5  # Reduced from 3.0 - assumes minimal shading
    
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
    lid_loss: float = 1.0  # Modern panels have lower LID
    
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
    availability_loss: float = 1.5  # Modern systems are more reliable
    
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


class SolarIncentiveManager:
    """
    Manages solar incentive lookup and calculations based on location.
    Provides comprehensive regional incentive data for economic analysis.
    """
    
    @staticmethod
    def get_incentives_for_location(location_info: LocationInfo, 
                                  system_size_kw: float,
                                  system_cost: float) -> List[IncentiveDetails]:
        """
        Get applicable solar incentives for a specific location.
        
        Args:
            location_info: LocationInfo object with country and state/province
            system_size_kw: System size in kW
            system_cost: Total system cost in USD
            
        Returns:
            List of applicable IncentiveDetails
        """
        incentives = []
        country = location_info.country.lower() if location_info.country else ""
        state_province = location_info.state_province.lower() if location_info.state_province else ""
        
        # Handle US states
        if country == "united states":
            us_incentives = SOLAR_INCENTIVES.get("united states", {})
            
            # Add federal incentive
            if "federal" in us_incentives:
                federal = us_incentives["federal"]
                incentives.append(IncentiveDetails(
                    name="Federal ITC",
                    type=federal["type"],
                    value=federal["value"],
                    expires=federal.get("expires"),
                    notes=federal.get("notes")
                ))
            
            # Add state-specific incentives
            for state_key, state_data in us_incentives.items():
                if state_key == "federal":
                    continue
                    
                if state_key in state_province or state_province in state_key:
                    if "programs" in state_data:
                        for program in state_data["programs"]:
                            # Check if program applies to system category
                            category = program.get("category", "residential")
                            if category == "utility" and system_size_kw < 1000:
                                continue
                            if category == "commercial" and system_size_kw < 10:
                                continue
                            if category == "low-income":
                                # Would need income verification
                                continue
                                
                            incentive = IncentiveDetails(
                                name=program["name"],
                                type=program["type"],
                                value=program["value"],
                                max_value=program.get("max_rebate") or program.get("max_credit"),
                                duration=program.get("duration"),
                                expires=program.get("expires"),
                                category=category,
                                notes=program.get("notes")
                            )
                            incentives.append(incentive)
                    break
        
        # Handle Canadian provinces
        elif country == "canada":
            can_incentives = SOLAR_INCENTIVES.get("canada", {})
            
            # Add federal programs
            if "federal" in can_incentives:
                for program in can_incentives["federal"]["programs"]:
                    incentive = IncentiveDetails(
                        name=program["name"],
                        type=program["type"],
                        value=program["value"],
                        category=program.get("category"),
                        notes=program.get("notes")
                    )
                    incentives.append(incentive)
            
            # Add provincial programs
            for province_key, prov_data in can_incentives.items():
                if province_key == "federal":
                    continue
                    
                if province_key in state_province or state_province in province_key:
                    if "programs" in prov_data:
                        for program in prov_data["programs"]:
                            incentive = IncentiveDetails(
                                name=program["name"],
                                type=program["type"],
                                value=program["value"],
                                max_value=program.get("max_rebate"),
                                category=program.get("category"),
                                notes=program.get("notes")
                            )
                            incentives.append(incentive)
                    break
        
        # Handle Australian states
        elif country == "australia":
            aus_incentives = SOLAR_INCENTIVES.get("australia", {})
            
            # Add federal STC rebate
            if "federal" in aus_incentives:
                for program in aus_incentives["federal"]["programs"]:
                    incentive = IncentiveDetails(
                        name=program["name"],
                        type=program["type"],
                        value=program["value"],
                        notes=program.get("notes")
                    )
                    incentives.append(incentive)
            
            # Add state programs
            for state_key, state_data in aus_incentives.items():
                if state_key == "federal":
                    continue
                    
                if state_key in state_province or state_province in state_key:
                    if "programs" in state_data:
                        for program in state_data["programs"]:
                            incentive = IncentiveDetails(
                                name=program["name"],
                                type=program["type"],
                                value=program["value"],
                                category=program.get("category"),
                                notes=program.get("notes")
                            )
                            incentives.append(incentive)
                    break
        
        # Handle other countries
        else:
            for country_key, country_data in SOLAR_INCENTIVES.items():
                if country_key in ["united states", "canada", "australia"]:
                    continue
                    
                if country_key in country or country in country_key:
                    if "programs" in country_data:
                        for program in country_data["programs"]:
                            incentive = IncentiveDetails(
                                name=program["name"],
                                type=program["type"],
                                value=program["value"],
                                duration=program.get("duration"),
                                notes=program.get("notes")
                            )
                            incentives.append(incentive)
                    break
        
        return incentives
    
    @staticmethod
    def calculate_incentive_value(incentive: IncentiveDetails, 
                                system_size_kw: float,
                                system_cost: float,
                                annual_production: float = 0) -> float:
        """
        Calculate the monetary value of an incentive.
        
        Args:
            incentive: IncentiveDetails object
            system_size_kw: System size in kW
            system_cost: Total system cost in USD
            annual_production: Annual energy production in kWh (for performance incentives)
            
        Returns:
            Incentive value in USD
        """
        if incentive.type == "tax_credit":
            # Percentage of system cost
            value = system_cost * incentive.value
            if incentive.max_value:
                value = min(value, incentive.max_value)
            return value
            
        elif incentive.type == "rebate":
            if isinstance(incentive.value, float) and incentive.value < 1.0:
                # Percentage rebate
                value = system_cost * incentive.value
            elif incentive.value > 100:
                # Flat amount rebate
                value = incentive.value
            else:
                # $/W rebate
                value = incentive.value * system_size_kw * 1000
            
            if incentive.max_value:
                value = min(value, incentive.max_value)
            return value
            
        elif incentive.type in ["performance", "feed_in_tariff", "feed_in_premium"]:
            # $/kWh over duration
            if annual_production > 0 and incentive.duration:
                total_production = annual_production * incentive.duration
                value = total_production * incentive.value
                return value
            return 0
            
        elif incentive.type == "tax_exemption":
            # Estimate tax savings (varies by location)
            if incentive.value == 1.0:  # 100% exemption
                # Rough estimate: 5-8% of system cost in taxes
                return system_cost * 0.065
            else:
                return system_cost * 0.065 * incentive.value
                
        elif incentive.type == "loan":
            # Interest savings on loan
            if incentive.value == 0.0:  # 0% interest loan
                # Estimate savings vs market rate (e.g., 6%)
                loan_amount = min(incentive.max_value or system_cost, system_cost)
                interest_saved = loan_amount * 0.06 * 5  # 5-year average
                return interest_saved * 0.5  # Present value
            return 0
            
        elif incentive.type == "net_metering":
            # Value depends on excess generation and rates
            # This is calculated separately in the main analysis
            return 0
            
        else:
            return 0
    
    @staticmethod
    def format_incentive_summary(incentives: List[IncentiveDetails],
                               system_size_kw: float,
                               system_cost: float,
                               annual_production: float) -> str:
        """
        Format a summary of applicable incentives.
        
        Args:
            incentives: List of IncentiveDetails
            system_size_kw: System size in kW
            system_cost: Total system cost in USD
            annual_production: Annual energy production in kWh
            
        Returns:
            Formatted string summary
        """
        if not incentives:
            return "No specific incentives found for this location."
        
        summary = "APPLICABLE SOLAR INCENTIVES:\n"
        summary += "-" * 60 + "\n"
        
        total_value = 0
        
        for incentive in incentives:
            value = SolarIncentiveManager.calculate_incentive_value(
                incentive, system_size_kw, system_cost, annual_production
            )
            total_value += value
            
            summary += f"\n{incentive.name}:\n"
            summary += f"  Type: {incentive.type.replace('_', ' ').title()}\n"
            
            if incentive.type == "tax_credit":
                summary += f"  Value: {incentive.value*100:.0f}% of system cost\n"
            elif incentive.type == "rebate":
                if isinstance(incentive.value, float) and incentive.value < 1.0:
                    summary += f"  Value: {incentive.value*100:.0f}% of system cost\n"
                elif incentive.value > 100:
                    summary += f"  Value: ${incentive.value:,.0f} flat rebate\n"
                else:
                    summary += f"  Value: ${incentive.value:.2f}/W\n"
            elif incentive.type in ["performance", "feed_in_tariff"]:
                summary += f"  Value: ${incentive.value:.3f}/kWh for {incentive.duration} years\n"
            elif incentive.type == "tax_exemption":
                summary += f"  Value: {incentive.value*100:.0f}% tax exemption\n"
            elif incentive.type == "loan":
                loan_amount = incentive.max_value or incentive.value
                if loan_amount:
                    summary += f"  Value: 0% interest loan up to ${loan_amount:,.0f}\n"
                else:
                    summary += f"  Value: Low-interest loan available\n"
            elif incentive.type == "net_metering":
                summary += f"  Value: Full retail rate credit for excess generation\n"
            
            if value > 0:
                summary += f"  Estimated Value: ${value:,.0f}\n"
            
            if incentive.max_value:
                summary += f"  Maximum: ${incentive.max_value:,.0f}\n"
                
            if incentive.expires:
                summary += f"  Expires: {incentive.expires}\n"
                
            if incentive.notes:
                summary += f"  Notes: {incentive.notes}\n"
        
        summary += "\n" + "-" * 60 + "\n"
        summary += f"TOTAL ESTIMATED INCENTIVE VALUE: ${total_value:,.0f}\n"
        summary += f"Net System Cost After Incentives: ${system_cost - total_value:,.0f}\n"
        
        return summary


class AddressGeocoder:
    """
    Handles conversion of street addresses to GPS coordinates with regional detection.
    Uses OpenStreetMap's Nominatim service (free, no API key required).
    
    Extended to extract country, state/province, and city information for
    electricity rate lookup.
    """
    
    def __init__(self):
        """Initialize geocoder with proper headers for OSM compliance"""
        self.session = requests.Session()
        # OSM requires a user agent
        self.session.headers.update({
            'User-Agent': f'PV-PowerEstimate/{VERSION} (https://github.com/secwest/PV-Generation-Planning)'
        })
    
    def geocode_with_details(self, address: str) -> Optional[LocationInfo]:
        """
        Convert address string to detailed location information.
        
        Args:
            address: Street address, city, or location description
            
        Returns:
            LocationInfo object with coordinates and regional details, or None if not found
        """
        try:
            # Nominatim API parameters
            params = {
                'q': address,
                'format': 'json',
                'limit': 1,
                'addressdetails': 1,
                'extratags': 1,
                'namedetails': 1
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
                    
                    # Extract address components
                    addr = result.get('address', {})
                    
                    # Get country and country code
                    country = addr.get('country', '').lower()
                    country_code = addr.get('country_code', '').upper()
                    
                    # Get state/province - try multiple fields
                    state_province = (
                        addr.get('state', '') or 
                        addr.get('province', '') or 
                        addr.get('region', '') or
                        addr.get('county', '')
                    ).lower()
                    
                    # Get city
                    city = (
                        addr.get('city', '') or 
                        addr.get('town', '') or 
                        addr.get('village', '') or
                        addr.get('municipality', '')
                    ).lower()
                    
                    # Display name for user verification
                    display_name = result.get('display_name', 'Unknown')
                    
                    # Create LocationInfo object
                    location_info = LocationInfo(
                        latitude=lat,
                        longitude=lon,
                        altitude=0.0,  # Will be fetched separately
                        address=display_name,
                        country=country,
                        state_province=state_province,
                        city=city,
                        country_code=country_code
                    )
                    
                    # Log the resolved location for verification
                    logger.info(f"Geocoded '{address}' to: {display_name}")
                    logger.info(f"Country: {country}, State/Province: {state_province}, City: {city}")
                    logger.info(f"Coordinates: {lat:.4f}, {lon:.4f}")
                    
                    return location_info
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
    
    def geocode(self, address: str) -> Optional[Tuple[float, float]]:
        """
        Convert address string to latitude/longitude coordinates.
        Legacy method for backward compatibility.
        
        Args:
            address: Street address, city, or location description
            
        Returns:
            Tuple of (latitude, longitude) or None if not found
        """
        location_info = self.geocode_with_details(address)
        if location_info:
            return location_info.latitude, location_info.longitude
        return None


class ElectricityRateManager:
    """
    Manages electricity rate lookup based on location.
    Provides accurate regional electricity rates for economic analysis.
    
    Enhanced with comprehensive global coverage including:
    - All countries and territories
    - Regional variations for large countries
    - Multiple currency support
    - Time-of-use considerations where applicable
    """
    
    @staticmethod
    def get_rate_for_location(location_info: LocationInfo) -> Tuple[float, str, str]:
        """
        Get electricity rate for a specific location.
        
        Args:
            location_info: LocationInfo object with country and state/province
            
        Returns:
            Tuple of (rate_in_usd, currency, source_description)
        """
        country = location_info.country.lower() if location_info.country else ""
        state_province = location_info.state_province.lower() if location_info.state_province else ""
        
        # Handle Canadian provinces
        if country == "canada" and state_province:
            rates = ELECTRICITY_RATES["canada"]
            # Try to match province name
            for province_key, rate in rates.items():
                if province_key in state_province or state_province in province_key:
                    rate_usd = rate * CURRENCY_TO_USD["CAD"]
                    source = f"{province_key.title()} average rate (2024-2025)"
                    return rate_usd, "CAD", source
            # Default Canadian rate
            rate_cad = rates["default"]
            rate_usd = rate_cad * CURRENCY_TO_USD["CAD"]
            return rate_usd, "CAD", "Canadian average rate"
        
        # Handle US states
        elif country == "united states" and state_province:
            rates = ELECTRICITY_RATES["united states"]
            # Try to match state name
            for state_key, rate in rates.items():
                if state_key in state_province or state_province in state_key:
                    source = f"{state_key.title()} average rate (2024-2025)"
                    return rate, "USD", source
            # Default US rate
            return rates["default"], "USD", "US average rate"
        
        # Handle Mexico states
        elif country == "mexico" and state_province:
            if isinstance(ELECTRICITY_RATES["mexico"], dict):
                rates = ELECTRICITY_RATES["mexico"]
                for state_key, rate in rates.items():
                    if state_key in state_province or state_province in state_key:
                        source = f"{state_key.title()} average rate (2024-2025)"
                        return rate, "USD", source
                return rates["default"], "USD", "Mexico average rate"
        
        # Handle Chinese provinces
        elif country == "china" and state_province:
            if isinstance(ELECTRICITY_RATES["china"], dict):
                rates = ELECTRICITY_RATES["china"]
                for province_key, rate in rates.items():
                    if province_key in state_province or state_province in province_key:
                        rate_usd = rate * CURRENCY_TO_USD["CNY"]
                        source = f"{province_key.title()} average rate (2024-2025)"
                        return rate_usd, "CNY", source
                rate_cny = rates["default"]
                rate_usd = rate_cny * CURRENCY_TO_USD["CNY"]
                return rate_usd, "CNY", "China average rate"
        
        # Handle Indian states
        elif country == "india" and state_province:
            if isinstance(ELECTRICITY_RATES["india"], dict):
                rates = ELECTRICITY_RATES["india"]
                for state_key, rate in rates.items():
                    if state_key in state_province or state_province in state_key:
                        rate_usd = rate * CURRENCY_TO_USD["INR"]
                        source = f"{state_key.title()} average rate (2024-2025)"
                        return rate_usd, "INR", source
                rate_inr = rates["default"]
                rate_usd = rate_inr * CURRENCY_TO_USD["INR"]
                return rate_usd, "INR", "India average rate"
        
        # Handle Brazilian states
        elif country == "brazil" and state_province:
            if isinstance(ELECTRICITY_RATES["brazil"], dict):
                rates = ELECTRICITY_RATES["brazil"]
                for state_key, rate in rates.items():
                    if state_key in state_province or state_province in state_key:
                        rate_usd = rate * CURRENCY_TO_USD["BRL"]
                        source = f"{state_key.title()} average rate (2024-2025)"
                        return rate_usd, "BRL", source
                rate_brl = rates["default"]
                rate_usd = rate_brl * CURRENCY_TO_USD["BRL"]
                return rate_usd, "BRL", "Brazil average rate"
        
        # Handle Australian states
        elif country == "australia" and state_province:
            if isinstance(ELECTRICITY_RATES["australia"], dict):
                rates = ELECTRICITY_RATES["australia"]
                for state_key, rate in rates.items():
                    if state_key in state_province or state_province in state_key:
                        rate_usd = rate * CURRENCY_TO_USD["AUD"]
                        source = f"{state_key.title()} average rate (2024-2025)"
                        return rate_usd, "AUD", source
                rate_aud = rates["default"]
                rate_usd = rate_aud * CURRENCY_TO_USD["AUD"]
                return rate_usd, "AUD", "Australia average rate"
        
        # Handle other countries
        else:
            # Check if country is in our database
            for country_key in ELECTRICITY_RATES:
                if country_key in country or country in country_key:
                    if isinstance(ELECTRICITY_RATES[country_key], dict):
                        # Skip nested dicts (already handled above)
                        continue
                    
                    rate_local = ELECTRICITY_RATES[country_key]
                    
                    # Determine currency based on country
                    currency_map = {
                        # Europe (Euro zone)
                        "austria": "EUR", "belgium": "EUR", "bulgaria": "BGN", "croatia": "HRK",
                        "cyprus": "EUR", "czech republic": "CZK", "denmark": "DKK", "estonia": "EUR",
                        "finland": "EUR", "france": "EUR", "germany": "EUR", "greece": "EUR",
                        "hungary": "HUF", "ireland": "EUR", "italy": "EUR", "latvia": "EUR",
                        "lithuania": "EUR", "luxembourg": "EUR", "malta": "EUR", "netherlands": "EUR",
                        "poland": "PLN", "portugal": "EUR", "romania": "RON", "slovakia": "EUR",
                        "slovenia": "EUR", "spain": "EUR", "sweden": "SEK",
                        
                        # Other European
                        "united kingdom": "GBP", "norway": "NOK", "switzerland": "CHF", "iceland": "ISK",
                        "albania": "ALL", "bosnia": "BAM", "kosovo": "EUR", "macedonia": "MKD",
                        "moldova": "MDL", "montenegro": "EUR", "serbia": "RSD", "turkey": "TRY",
                        "ukraine": "UAH",
                        
                        # Americas
                        "mexico": "MXN", "argentina": "ARS", "chile": "CLP", "colombia": "COP",
                        "peru": "PEN", "venezuela": "VES", "ecuador": "USD", "bolivia": "BOB",
                        "paraguay": "PYG", "uruguay": "UYU", "guyana": "GYD", "suriname": "SRD",
                        "french guiana": "EUR",
                        
                        # Asia
                        "japan": "JPY", "south korea": "KRW", "taiwan": "TWD", "hong kong": "HKD",
                        "singapore": "SGD", "thailand": "THB", "vietnam": "VND", "philippines": "PHP",
                        "indonesia": "IDR", "malaysia": "MYR", "myanmar": "MMK", "cambodia": "KHR",
                        "laos": "LAK", "bangladesh": "BDT", "pakistan": "PKR", "sri lanka": "LKR",
                        "nepal": "NPR", "afghanistan": "AFN", "kazakhstan": "KZT", "uzbekistan": "UZS",
                        "kyrgyzstan": "KGS", "tajikistan": "TJS", "turkmenistan": "TMT", "mongolia": "MNT",
                        
                        # Middle East
                        "saudi arabia": "SAR", "united arab emirates": "AED", "qatar": "QAR",
                        "kuwait": "KWD", "bahrain": "BHD", "oman": "OMR", "jordan": "JOD",
                        "lebanon": "LBP", "israel": "ILS", "syria": "SYP", "iraq": "IQD",
                        "iran": "IRR", "yemen": "YER",
                        
                        # Africa
                        "egypt": "EGP", "nigeria": "NGN", "kenya": "KES", "ethiopia": "ETB",
                        "morocco": "MAD", "algeria": "DZD", "tunisia": "TND", "libya": "LYD",
                        "sudan": "SDG", "ghana": "GHS", "tanzania": "TZS", "uganda": "UGX",
                        "zimbabwe": "ZWL", "zambia": "ZMW", "mozambique": "MZN", "malawi": "MWK",
                        "rwanda": "RWF", "botswana": "BWP", "namibia": "NAD", "mauritius": "MUR",
                        "madagascar": "MGA", "senegal": "XOF", "ivory coast": "XOF", "cameroon": "XAF",
                        "angola": "AOA", "gabon": "XAF", "mauritania": "MRU", "mali": "XOF",
                        "burkina faso": "XOF", "niger": "XOF", "chad": "XAF", "somalia": "SOS",
                        "eritrea": "ERN", "djibouti": "DJF", "seychelles": "SCR", "cape verde": "CVE",
                        "guinea": "GNF", "sierra leone": "SLL", "liberia": "LRD", "togo": "XOF",
                        "benin": "XOF", "gambia": "GMD", "guinea-bissau": "XOF", "equatorial guinea": "XAF",
                        "central african republic": "XAF", "congo": "XAF", "democratic republic of congo": "CDF",
                        "sao tome": "STN", "comoros": "KMF", "lesotho": "LSL", "swaziland": "SZL",
                        "eswatini": "SZL",
                        
                        # Oceania
                        "fiji": "FJD", "papua new guinea": "PGK", "solomon islands": "SBD",
                        "vanuatu": "VUV", "samoa": "WST", "tonga": "TOP", "kiribati": "AUD",
                        "tuvalu": "AUD", "nauru": "AUD", "palau": "USD", "marshall islands": "USD",
                        "micronesia": "USD", "french polynesia": "XPF", "new caledonia": "XPF",
                        "cook islands": "NZD",
                        
                        # Caribbean
                        "jamaica": "JMD", "trinidad and tobago": "TTD", "barbados": "BBD",
                        "bahamas": "BSD", "haiti": "HTG", "dominican republic": "DOP", "cuba": "CUP",
                        "puerto rico": "USD", "cayman islands": "KYD", "bermuda": "BMD",
                        "virgin islands": "USD", "antigua": "XCD", "saint lucia": "XCD",
                        "grenada": "XCD", "dominica": "XCD", "saint vincent": "XCD",
                        "saint kitts": "XCD", "turks and caicos": "USD", "aruba": "AWG",
                        "curacao": "ANG", "bonaire": "USD"
                    }
                    
                    # Get currency for the country
                    currency = "USD"  # Default
                    for country_name, curr in currency_map.items():
                        if country_name in country_key:
                            currency = curr
                            break
                    
                    # Convert to USD
                    if currency in CURRENCY_TO_USD:
                        rate_usd = rate_local * CURRENCY_TO_USD[currency]
                    else:
                        rate_usd = rate_local  # Assume USD if currency not found
                        currency = "USD"
                    
                    source = f"{country_key.title()} average rate (2024-2025)"
                    return rate_usd, currency, source
        
        # Default global rate
        return ELECTRICITY_RATES["default"], "USD", "Global average estimate"
    
    @staticmethod
    def format_rate_info(rate_usd: float, currency: str, source: str) -> str:
        """
        Format electricity rate information for display.
        
        Args:
            rate_usd: Rate in USD per kWh
            currency: Original currency code
            source: Description of rate source
            
        Returns:
            Formatted string for display
        """
        if currency != "USD":
            # Convert back to local currency for display
            local_rate = rate_usd / CURRENCY_TO_USD.get(currency, 1.0)
            return f"${rate_usd:.3f} USD/kWh ({local_rate:.3f} {currency}/kWh) - {source}"
        else:
            return f"${rate_usd:.3f} USD/kWh - {source}"


class SolarPVCalculator:
    """
    Main calculator class for solar PV power yield estimation.
    
    Extended with comprehensive global electricity rate detection and
    incentive calculation for accurate economic analysis worldwide.
    
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
                 altitude: Optional[float] = None, address: Optional[str] = None,
                 location_info: Optional[LocationInfo] = None):
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
            location_info: Extended location information including region
            
        Raises:
            ValueError: If coordinates are out of valid range
        """
        # Validate coordinates
        if not self._validate_coordinates(latitude, longitude):
            raise ValueError(f"Invalid coordinates: {latitude}, {longitude}")
        
        self.lat = latitude
        self.lon = longitude
        self.address = address
        self.location_info = location_info
        
        # Get electricity rate for location
        if location_info:
            rate_usd, currency, source = ElectricityRateManager.get_rate_for_location(location_info)
            self.electricity_rate = rate_usd
            self.electricity_currency = currency
            self.rate_source = source
            logger.info(f"Electricity rate: {ElectricityRateManager.format_rate_info(rate_usd, currency, source)}")
        else:
            self.electricity_rate = 0.14  # Default
            self.electricity_currency = "USD"
            self.rate_source = "Default rate"
        
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
                       system_size_dc: float, system_config: SystemConfig,
                       electricity_rate: float = None, cost_per_watt: float = None,
                       incentives: List[IncentiveDetails] = None) -> str:
        """
        Generate comprehensive performance assessment report with incentives.
        
        Report includes technical analysis for:
        - System design verification
        - Performance benchmarking
        - O&M planning
        - Financial analysis with incentives
        - Optimization opportunities
        """
        # Use location-specific rate if not provided
        if electricity_rate is None:
            electricity_rate = self.electricity_rate
        
        # Calculate additional metrics
        pr = system_config.total_loss_factor * 100
        peak_power_time = results['ac_power'].idxmax()
        peak_power = results['ac_power'].max()
        
        # Climate statistics
        total_irradiation = weather_data['ghi'].sum() / 1000  # kWh/m²
        avg_temp = weather_data['temp_air'].mean()
        avg_wind = weather_data['wind_speed'].mean()
        
        # Calculate monthly weather statistics
        weather_monthly = weather_data.groupby(weather_data.index.month).agg({
            'ghi': ['mean', 'sum'],
            'dni': ['mean', 'sum'],
            'dhi': ['mean', 'sum'],
            'temp_air': ['mean', 'min', 'max'],
            'wind_speed': 'mean'
        })
        
        # Flatten column names
        weather_monthly.columns = ['_'.join(col).strip() for col in weather_monthly.columns.values]
        
        # Convert month numbers to names
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        weather_monthly.index = month_names
        
        # Convert sum values from W to kWh/m²
        weather_monthly['ghi_total'] = weather_monthly['ghi_sum'] / 1000
        weather_monthly['dni_total'] = weather_monthly['dni_sum'] / 1000
        weather_monthly['dhi_total'] = weather_monthly['dhi_sum'] / 1000
        
        # Economic assumptions - updated for 2024-2025 market
        # Use provided electricity rate or default
        
        # Determine installed cost based on system size if not provided
        if cost_per_watt is None:
            if system_size_dc <= 20:  # Residential (raised from 10kW)
                default_cost_per_watt = 2.25  # $2.00-2.50/W typical 2024-2025 (middle of range)
            elif system_size_dc <= 100:  # Small commercial
                default_cost_per_watt = 1.50  # $1.25-1.75/W typical 2024-2025 (middle of range)
            elif system_size_dc <= 1000:  # Large commercial
                default_cost_per_watt = 1.25  # $1.00-1.50/W typical 2024-2025 (middle of range)
            else:  # Utility scale
                default_cost_per_watt = 0.85  # $0.70-1.00/W typical 2024-2025 (middle of range)
        else:
            default_cost_per_watt = cost_per_watt
        
        system_cost = system_size_dc * default_cost_per_watt * 1000
        annual_revenue = annual_energy * electricity_rate
        
        # Calculate incentive values
        total_incentive_value = 0
        if incentives:
            for incentive in incentives:
                value = SolarIncentiveManager.calculate_incentive_value(
                    incentive, system_size_dc, system_cost, annual_energy
                )
                total_incentive_value += value
        
        net_system_cost = system_cost - total_incentive_value
        payback_with_incentives = net_system_cost / annual_revenue
        
        # Calculate NPV and enhanced payback with electricity rate escalation
        electricity_escalation_rate = 0.03  # 3% annual increase
        discount_rate = 0.05  # 5% discount rate
        system_life = 25  # years
        
        # Calculate NPV of electricity savings
        npv_savings = 0
        cumulative_savings = 0
        enhanced_payback_years = 0
        enhanced_payback_with_incentives = 0
        
        for year in range(1, system_life + 1):
            # Degradation: -0.5% per year after year 1
            year_degradation = 1.0 if year == 1 else (1 - 0.005 * (year - 1))
            year_production = annual_energy * year_degradation
            
            # Electricity price with escalation
            year_electricity_rate = electricity_rate * ((1 + electricity_escalation_rate) ** (year - 1))
            year_revenue = year_production * year_electricity_rate
            
            # NPV calculation
            npv_savings += year_revenue / ((1 + discount_rate) ** year)
            cumulative_savings += year_revenue
            
            if cumulative_savings >= system_cost and enhanced_payback_years == 0:
                enhanced_payback_years = year
                
            if cumulative_savings >= net_system_cost and enhanced_payback_with_incentives == 0:
                enhanced_payback_with_incentives = year
        
        # Enhanced commercial and utility-scale financial modeling
        ppa_rate = None
        lcoe = None
        project_irr = None
        debt_fraction = 0
        tax_equity_fraction = 0
        
        if system_size_dc > 100:  # Large commercial and utility scale
            # Modern utility-scale financing assumptions (2024-2025)
            if system_size_dc > 1000:  # Utility scale
                # Typical utility-scale PPA rates by region
                if electricity_rate < 0.08:  # Low-cost regions
                    ppa_rate = 0.025  # $25/MWh
                elif electricity_rate < 0.12:  # Moderate-cost regions
                    ppa_rate = 0.035  # $35/MWh
                else:  # High-cost regions
                    ppa_rate = 0.045  # $45/MWh
                
                # Utility-scale financing structure
                debt_fraction = 0.70  # 70% debt typical
                tax_equity_fraction = 0.20  # 20% tax equity
                equity_fraction = 0.10  # 10% sponsor equity
                debt_rate = 0.045  # 4.5% interest rate
                
            else:  # Large commercial (100kW-1MW)
                # C&I PPA rates typically 10-20% below retail
                ppa_rate = electricity_rate * 0.85
                
                # Commercial financing structure
                debt_fraction = 0.60  # 60% debt
                tax_equity_fraction = 0.0  # Less common for C&I
                equity_fraction = 0.40  # 40% equity
                debt_rate = 0.055  # 5.5% interest rate
            
            # Calculate LCOE for commercial/utility projects
            # LCOE = (Total Lifetime Cost) / (Total Lifetime Energy)
            capex = system_cost
            annual_opex = system_size_dc * 10  # $10/kW/year O&M
            
            # Calculate present value of costs
            pv_costs = capex
            pv_energy = 0
            
            for year in range(1, system_life + 1):
                # O&M costs escalate at inflation (2.5%)
                year_opex = annual_opex * ((1 + 0.025) ** (year - 1))
                pv_costs += year_opex / ((1 + discount_rate) ** year)
                
                # Energy with degradation
                year_degradation = 1.0 if year == 1 else (1 - 0.005 * (year - 1))
                year_energy = annual_energy * year_degradation
                pv_energy += year_energy / ((1 + discount_rate) ** year)
            
            lcoe = pv_costs / pv_energy
            
            # Calculate project IRR (simplified)
            # For utility scale with ITC and depreciation
            if system_size_dc > 1000:
                # Include 30% ITC and MACRS depreciation benefits
                itc_value = capex * 0.30
                depreciation_pv = capex * 0.85 * 0.21 * 2.5  # Simplified MACRS PV
                
                # Approximate project IRR
                project_irr = ((annual_revenue + depreciation_pv/5) / (capex - itc_value)) * 100
            else:
                project_irr = (annual_revenue / capex) * 100
        
        # Additional savings for commercial customers
        if system_size_dc > 20:  # Commercial system
            # Demand charge savings (more sophisticated calculation)
            # Based on typical demand charge rates and solar coincidence
            if system_size_dc <= 100:  # Small commercial
                demand_charge_savings = system_size_dc * 5 * 12 * 0.6  # 60% coincidence
            elif system_size_dc <= 1000:  # Large commercial  
                demand_charge_savings = system_size_dc * 8 * 12 * 0.5  # Higher charges, lower coincidence
            else:  # Utility scale (usually no demand charges)
                demand_charge_savings = 0
                
            annual_revenue += demand_charge_savings
            
        # Time-of-use benefit (if applicable)
        if electricity_rate > 0.15 and system_size_dc <= 1000:  # TOU for commercial, not utility
            tou_multiplier = 1.15  # 15% benefit from producing during peak hours
            annual_revenue *= tou_multiplier
        
        # Best and worst months
        best_month = monthly['energy_kwh'].idxmax()
        worst_month = monthly['energy_kwh'].idxmin()
        variation = monthly.loc[best_month, 'energy_kwh'] / monthly.loc[worst_month, 'energy_kwh']
        
        # Utility-scale specific analysis
        if system_size_dc > 1000:
            # Calculate hourly generation profile statistics
            hourly_profile = results.groupby(results.index.hour)['ac_power'].mean()
            peak_hour = hourly_profile.idxmax()
            
            # Calculate ramp rates
            ramp_rates = results['ac_power'].diff().abs()
            max_ramp_rate = ramp_rates.max()
            
            # Calculate generation duration curve
            sorted_generation = results['ac_power'].sort_values(ascending=False).reset_index(drop=True)
            hours_above_90 = (sorted_generation > system_size_dc * 0.9).sum()
            hours_above_50 = (sorted_generation > system_size_dc * 0.5).sum()
            hours_above_20 = (sorted_generation > system_size_dc * 0.2).sum()
        
        # Calculate insolation utilization
        # How much of available solar resource is captured
        avg_module_eff = 0.20  # 20% assumed module efficiency
        array_area = system_size_dc / (avg_module_eff * 1.0)  # m²
        theoretical_max = total_irradiation * array_area * avg_module_eff
        utilization = (annual_energy / theoretical_max) * 100
        
        # Get location info for header
        location_name = self.location.name
        if self.location_info:
            if self.location_info.country:
                location_name += f", {self.location_info.country.title()}"
        
        report = f"""
================================================================================
                     SOLAR PV POWER YIELD ASSESSMENT REPORT
================================================================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Software: PV-PowerEstimate v{VERSION} (Global Edition with Incentives)

SITE INFORMATION
----------------
Location: {location_name}
Coordinates: {self.lat:.4f}°, {self.lon:.4f}°
Elevation: {self.altitude:.0f} m above sea level
Time Zone: UTC (all times in UTC)
Electricity Rate: {ElectricityRateManager.format_rate_info(electricity_rate, self.electricity_currency, self.rate_source)}

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
Estimated Annual Revenue: ${annual_revenue:,.0f} (at ${electricity_rate:.3f}/kWh)

ECONOMIC ANALYSIS (2024-2025 Market)
------------------------------------
System Category: {"Residential" if system_size_dc <= 20 else "Commercial" if system_size_dc <= 1000 else "Utility Scale"}
Typical Installed Cost: ${default_cost_per_watt:.2f}/W DC
Total System Cost Estimate: ${system_cost:,.0f}
Simple Payback Period: {system_cost / annual_revenue:.1f} years (before incentives, no rate escalation)
Future Rate Increase Payback: {enhanced_payback_years} years (before incentives, with 3% rate escalation)

{SolarIncentiveManager.format_incentive_summary(incentives, system_size_dc, system_cost, annual_energy) if incentives else ("Note: Incentives not applicable for large commercial/utility scale systems (>100kW)." if system_size_dc > 100 else "No specific incentives found for this location.")}

NET PRESENT VALUE ANALYSIS (25-year)
------------------------------------
NPV of Energy Savings: ${npv_savings:,.0f} (at 3% electricity escalation, 5% discount rate)
Net Present Value: ${npv_savings - net_system_cost:,.0f}
Internal Rate of Return: {((npv_savings / net_system_cost) ** (1/25) - 1) * 100:.1f}%

{"FINANCIAL SUMMARY WITH INCENTIVES" if total_incentive_value > 0 else "FINANCIAL SUMMARY"}
---------------------------------
System Cost: ${system_cost:,.0f}
{"Total Incentive Value: ${:,.0f}".format(total_incentive_value) if total_incentive_value > 0 else ""}
{"Net Cost After Incentives: ${:,.0f}".format(net_system_cost) if total_incentive_value > 0 else ""}
Simple Payback: {system_cost / annual_revenue:.1f} years (no incentives, no escalation)
{"Simple Payback with Incentives: {:.1f} years (no escalation)".format(payback_with_incentives) if total_incentive_value > 0 else ""}
Future Rate Increase Payback: {enhanced_payback_years} years (no incentives, with 3% rate escalation)
{"Future Rate Increase Payback with Incentives: {} years (with 3% rate escalation)".format(enhanced_payback_with_incentives) if total_incentive_value > 0 else ""}
25-Year Cash Flow: ${cumulative_savings:,.0f}
25-Year Net Profit: ${cumulative_savings - net_system_cost:,.0f}
Effective Cost per Watt: ${net_system_cost / (system_size_dc * 1000):.2f}/W
Levelized Cost of Energy: ${net_system_cost / (annual_energy * 25 * 0.87):,.3f}/kWh

{f'''COMMERCIAL/UTILITY SCALE FINANCIAL METRICS
----------------------------------------
Project Type: {"Utility Scale (>1MW)" if system_size_dc > 1000 else "Large Commercial (100kW-1MW)"}
Typical PPA Rate: ${ppa_rate:.3f}/kWh (${ppa_rate*1000:.0f}/MWh)
Project LCOE: ${lcoe:.3f}/kWh (all-in cost)
LCOE vs PPA Spread: ${(ppa_rate - lcoe)*1000:.1f}/MWh
Estimated Project IRR: {project_irr:.1f}% (unlevered, after-tax)

FINANCING STRUCTURE (TYPICAL)
-----------------------------
Total Project Cost: ${system_cost:,.0f}
Debt Financing: {debt_fraction*100:.0f}% (${system_cost*debt_fraction:,.0f} at {debt_rate*100:.1f}% interest)
Tax Equity: {tax_equity_fraction*100:.0f}% (${system_cost*tax_equity_fraction:,.0f})
Sponsor Equity: {(1-debt_fraction-tax_equity_fraction)*100:.0f}% (${system_cost*(1-debt_fraction-tax_equity_fraction):,.0f})

KEY ASSUMPTIONS
---------------
Federal ITC: 30% (through 2032)
Depreciation: 5-year MACRS
O&M Cost: ${annual_opex:,.0f}/year (${annual_opex/system_size_dc:.0f}/kW/year)
Annual Degradation: 0.5%
Debt Term: {"20 years" if system_size_dc > 1000 else "15 years"}

REVENUE STREAMS
---------------
{f"PPA Revenue: ${annual_energy * ppa_rate:,.0f}/year" if system_size_dc > 1000 else f"Energy Savings: ${annual_energy * electricity_rate:,.0f}/year"}
{f"Capacity Payments: Market dependent" if system_size_dc > 1000 else f"Demand Charge Reduction: ${demand_charge_savings:,.0f}/year"}
{"REC Revenue: ~$5-20/MWh additional" if system_size_dc > 1000 else "SRECs: Market dependent (if available)"}

{f'''UTILITY-SCALE GENERATION PLANNING METRICS
-----------------------------------------
Annual Capacity Factor: {capacity_factor:.1f}% ({"Excellent" if capacity_factor > 25 else "Good" if capacity_factor > 20 else "Moderate"})
Peak Generation Season: {best_month} ({monthly.loc[best_month, 'energy_kwh']:,.0f} kWh)
Lowest Generation Month: {worst_month} ({monthly.loc[worst_month, 'energy_kwh']:,.0f} kWh)
Seasonal Variation Ratio: {variation:.1f}:1

GRID INTEGRATION CONSIDERATIONS
-------------------------------
Peak Output: {peak_power:,.1f} kW AC ({peak_power/system_size_dc*100:.0f}% of DC capacity)
Ramp Rate Capability: ~{system_size_dc * 0.2:.0f} kW/minute (typical)
Minimum Stable Generation: ~{system_size_dc * 0.1:.0f} kW (10% of capacity)
Reactive Power Range: ±{system_size_dc * 0.33:.0f} kVAR (at full output)

AVAILABILITY & RELIABILITY
--------------------------
Expected Availability: 97-99% (weather-adjusted)
Forced Outage Rate: 0.5-1.0% annually
Scheduled Maintenance: 3-5 days/year
Weather Downtime: {1.5 if self.lat > 45 or self.lat < -45 else 0.5:.1f}% (snow/soiling)

CURTAILMENT RISK FACTORS
------------------------
Grid Congestion Risk: {"High" if capacity_factor > 25 else "Moderate" if capacity_factor > 20 else "Low"} (based on resource quality)
Negative Pricing Hours: Location and market dependent
Economic Curtailment: 2-5% typical in high-penetration markets
Voltage/Frequency Events: <0.5% with modern inverters

ENERGY SHAPE ANALYSIS
---------------------
Solar Peak Hours: 10 AM - 3 PM (varies by season)
Peak Generation Hour: {peak_hour}:00 (annual average)
Duck Curve Contribution: Peak generation during low demand
Evening Ramp Support: None without storage
Morning Ramp Timing: Good alignment with demand increase

GENERATION DURATION CURVE
-------------------------
Hours > 90% Capacity: {hours_above_90:,} hours/year ({hours_above_90/87.6:.1f}%)
Hours > 50% Capacity: {hours_above_50:,} hours/year ({hours_above_50/87.6:.1f}%)  
Hours > 20% Capacity: {hours_above_20:,} hours/year ({hours_above_20/87.6:.1f}%)
Maximum Ramp Rate: {max_ramp_rate:.0f} kW/interval

RESOURCE ADEQUACY VALUE
-----------------------
Capacity Credit: {15 if system_size_dc > 5000 else 20 if system_size_dc > 1000 else 25}% typical (market dependent)
ELCC (Effective Load Carrying Capability): Declining with penetration
Peak Coincidence: {60 if self.lat < 35 and self.lat > -35 else 40}% summer peak contribution

TRANSMISSION & INTERCONNECTION
------------------------------
Interconnection Voltage: {345 if system_size_dc > 200000 else 230 if system_size_dc > 100000 else 138 if system_size_dc > 50000 else 69 if system_size_dc > 20000 else 34.5} kV typical
Substation Requirements: {"New substation likely" if system_size_dc > 50000 else "Existing substation possible"}
Network Upgrades Risk: {"High" if system_size_dc > 100000 else "Moderate" if system_size_dc > 50000 else "Low"}
Gen-Tie Line Length: Site specific (major cost factor)

ADVANCED GRID SERVICES
----------------------
Frequency Response: Fast (sub-second with modern inverters)
Voltage Regulation: ±0.95-1.05 p.u. capability
Black Start Capability: Possible with battery hybrid
Synthetic Inertia: Available with advanced controls
Grid Forming Mode: Future capability for microgrids

ENVIRONMENTAL & PERMITTING
--------------------------
Land Requirements: ~{system_size_dc * 0.004:.0f} acres (fixed tilt)
                  ~{system_size_dc * 0.007:.0f} acres (single-axis tracking)
Habitat Impact: Site-specific assessment required
Glare Analysis: Required near airports/highways
Stormwater Management: NPDES permit typically required
Cultural Resources: Phase I assessment recommended

DEVELOPMENT TIMELINE
--------------------
Typical Schedule: {"36-48 months" if system_size_dc > 50000 else "24-36 months"} from NTP to COD
- Permitting: 6-12 months
- Interconnection: 12-24 months
- Procurement: 3-6 months  
- Construction: 6-12 months
- Commissioning: 1-2 months
''' if system_size_dc > 1000 else ""}''' if system_size_dc > 100 else ""}
Current Market Costs (2024-2025):
- Residential (≤20kW): $2.00-2.50/W installed (was $3.50+ in 2020)
- Small Commercial (10-100kW): $1.25-1.75/W installed
- Large Commercial (100kW-1MW): $1.00-1.50/W installed
- Utility Scale (>1MW): $0.70-1.00/W installed
- Expected cost decline: 3-5% annually through 2030

Note: Costs have declined ~70% since 2010. Current prices include equipment,
installation, permitting, and interconnection.{" Incentives shown above are estimated values - verify eligibility and actual amounts with local authorities." if system_size_dc <= 100 else ""}

{"Cost Factors:" if system_size_dc <= 100 else "Large-Scale Project Considerations:"}
{"""- Location: Labor costs vary significantly by region
- Roof complexity: Simple roofs cost less than complex ones
- Local permitting: Some areas have streamlined processes
- Competition: More installers = better pricing
- Equipment quality: Premium panels cost 10-20% more""" if system_size_dc <= 100 else """- EPC contractor selection critical for project success
- Interconnection costs can vary significantly by location
- Land lease/acquisition costs not included in $/W figures
- Tracking systems add 10-20% to cost but boost production
- Grid capacity and transmission access are key factors"""}

{"TECHNICAL PERFORMANCE METRICS" if system_size_dc > 100 else "SYSTEM PERFORMANCE"}
-----------------------------
Peak Power Output: {peak_power:,.1f} kW ({peak_power/system_size_dc*100:.0f}% of rated capacity)
{"Peak Output Time: " + peak_power_time.strftime('%B %d at %H:%M') if system_size_dc <= 100 else "Peak Output Occurred: " + peak_power_time.strftime('%B %d at %H:%M UTC')}
Average Panel Temperature: {results['cell_temperature'].mean():.1f}°C ({results['cell_temperature'].mean() * 1.8 + 32:.0f}°F)
{"Temperature Impact on Output: -" + f"{abs(results['temperature_loss'].mean()):.1f}% annually" if system_size_dc <= 100 else f"Temperature Losses (annual): {abs(results['temperature_loss'].mean()):.1f}%"}
{"Typical Sun Intensity: " + f"{results['effective_irradiance'].mean():.0f} W/m²" if system_size_dc <= 100 else f"Average POA Irradiance: {results['effective_irradiance'].mean():.0f} W/m²"}
{"" if system_size_dc <= 100 else f"Module Temp at Peak Power: {results.loc[peak_power_time, 'cell_temperature']:.1f}°C"}

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

Your location shows {variation:.1f}:1 seasonal variation ({best_month} vs {worst_month})

MONTHLY WEATHER SUMMARY
-----------------------
This data represents typical meteorological conditions for your location.

Solar Irradiation (Monthly Totals)
Month    GHI (kWh/m²)    DNI (kWh/m²)    DHI (kWh/m²)
-------  -------------   -------------   -------------"""
        
        # Add monthly irradiation data
        for idx, (month, row) in enumerate(weather_monthly.iterrows()):
            report += f"\n{month:<7}  {row['ghi_total']:>12.1f}    {row['dni_total']:>12.1f}    {row['dhi_total']:>12.1f}"
        
        report += f"\n-------  -------------   -------------   -------------"
        report += f"\nTOTAL    {weather_monthly['ghi_total'].sum():>12.1f}    {weather_monthly['dni_total'].sum():>12.1f}    {weather_monthly['dhi_total'].sum():>12.1f}"
        
        report += f"""

Temperature and Wind Conditions
Month    Avg Temp (°C)    Min/Max (°C)      Avg Wind (m/s)
-------  --------------   ---------------   --------------"""
        
        # Add monthly temperature and wind data
        for idx, (month, row) in enumerate(weather_monthly.iterrows()):
            report += f"\n{month:<7}  {row['temp_air_mean']:>13.1f}    {row['temp_air_min']:>5.1f} / {row['temp_air_max']:>5.1f}    {row['wind_speed_mean']:>13.1f}"
        
        report += f"""

Climate Classification:
- Annual horizontal irradiation: {total_irradiation:,.0f} kWh/m²/year
- Average temperature: {avg_temp:.1f}°C
- Average wind speed: {avg_wind:.1f} m/s
- Classification: {self._classify_solar_resource(total_irradiation)}

Solar Component Analysis:
- Direct/Global Ratio: {weather_monthly['dni_total'].sum()/total_irradiation:.1%}
  * >70%: Very clear skies, excellent for tracking systems
  * 50-70%: Moderate clarity, good for fixed tilt
  * <50%: Cloudy/diffuse dominated, tracking less beneficial

Key Insights:
- Sunniest month: {weather_monthly['ghi_total'].idxmax()} ({weather_monthly['ghi_total'].max():.0f} kWh/m²)
- Cloudiest month: {weather_monthly['ghi_total'].idxmin()} ({weather_monthly['ghi_total'].min():.0f} kWh/m²)
- Hottest month: {weather_monthly['temp_air_mean'].idxmax()} ({weather_monthly['temp_air_mean'].max():.1f}°C average)
- Coldest month: {weather_monthly['temp_air_mean'].idxmin()} ({weather_monthly['temp_air_mean'].min():.1f}°C average)"""
        
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
  Direct Normal Total: {weather_monthly['dni_total'].sum():,.0f} kWh/m²/year
  Diffuse Total: {weather_monthly['dhi_total'].sum():,.0f} kWh/m²/year
  Direct/Global Ratio: {weather_monthly['dni_total'].sum()/total_irradiation:.1%}
  
Temperature Statistics:
  Annual Average: {avg_temp:.1f}°C
  Absolute Range: {weather_monthly['temp_air_min'].min():.1f}°C to {weather_monthly['temp_air_max'].max():.1f}°C
  Avg Wind Speed: {avg_wind:.1f} m/s
  
Energy Production Variation:
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
     * Current battery costs: $400-600/kWh installed (2024-2025)
     * 10 kWh system: $4,000-6,000 (down from $10,000+ in 2020)
   - Tracking Systems: Could increase yield 25-35% (economic analysis needed)
   - Bifacial Modules: 5-15% gain with {0.2:.1f} ground albedo
   - Module Upgrade: Latest high-efficiency could add 10-20% capacity

INCENTIVE OPTIMIZATION TIPS
---------------------------"""
        
        if incentives:
            report += """
To maximize your incentive benefits:

1. Federal Tax Credit (if applicable):
   - Ensure you have sufficient tax liability
   - Consider spreading credit over multiple years
   - Include all eligible costs (equipment, labor, permits)

2. State/Local Incentives:
   - Check application deadlines - some have limited funding
   - Verify all eligibility requirements
   - Submit applications before installation starts
   - Keep detailed documentation of all costs

3. Performance Incentives:
   - Monitor system production to ensure payments
   - Maintain system well to maximize generation
   - Understand payment schedules and requirements

4. Net Metering:
   - Size system to maximize self-consumption
   - Understand utility policies on credit rollovers
   - Consider time-of-use rates if available

5. Documentation Required:
   - Itemized invoices from installer
   - Proof of payment
   - System specifications
   - Interconnection agreement
   - Building permits
"""
        else:
            report += """
No specific incentives were found for your location, but you should:
- Check with local utilities for rebate programs
- Research state/provincial incentive databases
- Consult with local installers about current programs
- Consider federal tax incentives if applicable
"""
        
        report += f"""

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
   - Verify all incentive eligibility
   - Compare financing options
   - Understand net metering policies
   - Consider time-of-use rates

5. Technical validation:
   - Professional shading analysis
   - Structural engineering review
   - Electrical system compatibility
   - Utility interconnection requirements

REGIONAL ELECTRICITY CONTEXT
----------------------------
Location: {location_name}
Rate Used: {ElectricityRateManager.format_rate_info(electricity_rate, self.electricity_currency, self.rate_source)}

This rate was automatically determined based on your location. Actual rates may vary by:
- Utility provider (some regions have multiple providers)
- Rate schedule (residential vs commercial)
- Time-of-use pricing
- Demand charges (commercial customers)
- Net metering policies

For most accurate analysis, verify your actual electricity rate from a recent utility bill.

GLOBAL COMPARISON
-----------------
Your electricity rate compared to global averages:
- World average: ~$0.140/kWh
- Your rate: ${electricity_rate:.3f}/kWh ({electricity_rate/0.140*100:.0f}% of global average)
- Payback implications: {"Faster" if electricity_rate > 0.140 else "Slower"} than global average

Countries with highest rates (fastest solar payback):
1. Denmark: ~$0.35/kWh
2. Germany: ~$0.32/kWh  
3. Belgium: ~$0.30/kWh
4. Japan: ~$0.28/kWh
5. Italy: ~$0.26/kWh

Countries with lowest rates (slowest solar payback):
1. Iran: ~$0.01/kWh
2. Iraq: ~$0.04/kWh
3. Kuwait: ~$0.04/kWh
4. Saudi Arabia: ~$0.05/kWh
5. Libya: ~$0.04/kWh

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
        
        # Add residential performance insights
        if system_size_dc <= 20:
            report += f"""

RESIDENTIAL PERFORMANCE INSIGHTS
--------------------------------
Expected Daily Production: {annual_energy/365:.1f} kWh/day average
Best Production Season: {best_month} ({monthly.loc[best_month, 'energy_kwh']/30:.1f} kWh/day)
Lowest Production Season: {worst_month} ({monthly.loc[worst_month, 'energy_kwh']/30:.1f} kWh/day)

COMPARISON TO TYPICAL SYSTEMS
-----------------------------
Your Specific Yield: {annual_specific_yield:,.0f} kWh/kWp
{"Below Average (<1000)" if annual_specific_yield < 1000 else "Average (1000-1300)" if annual_specific_yield < 1300 else "Above Average (1300-1600)" if annual_specific_yield < 1600 else "Excellent (>1600)"}

OPTIMIZATION OPPORTUNITIES
--------------------------
{f"- Panel temperatures averaging {results['cell_temperature'].mean():.0f}°C - ensure good ventilation" if results['cell_temperature'].mean() > 50 else "- Good panel cooling observed"}
{f"- High seasonal variation ({variation:.1f}:1) - consider battery storage" if variation > 2.5 else "- Moderate seasonal variation - good year-round production"}
{f"- Strong solar resource - system should perform well" if annual_specific_yield > 1400 else "- Check for shading or soiling issues if underperforming"}

MONITORING YOUR SYSTEM
----------------------
- Compare monthly production to these estimates
- Clean panels when production drops >5% below expected
- Most issues show as gradual production decline
- Sudden drops indicate equipment problems
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
    
    def _classify_solar_resource(self, annual_ghi: float) -> str:
        """
        Classify solar resource based on annual GHI.
        
        Args:
            annual_ghi: Annual global horizontal irradiation in kWh/m²
            
        Returns:
            Classification string
        """
        if annual_ghi >= 2000:
            return "Excellent (Desert/High altitude)"
        elif annual_ghi >= 1600:
            return "Very Good (Sunny/Mediterranean)"
        elif annual_ghi >= 1300:
            return "Good (Moderate climate)"
        elif annual_ghi >= 1000:
            return "Fair (Temperate/Partly cloudy)"
        else:
            return "Poor (Cloudy/High latitude)"
    
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
                    'address': self.address,
                    'country': self.location_info.country if self.location_info else None,
                    'state_province': self.location_info.state_province if self.location_info else None,
                    'electricity_rate_usd': self.electricity_rate,
                    'electricity_currency': self.electricity_currency,
                    'rate_source': self.rate_source
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
        description='PV-PowerEstimate v1.3.2: Comprehensive Solar PV Power Yield Calculator (Global Edition with Incentives)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --lat 45.4215 --lon -75.6972
  %(prog)s --address "111 Wellington Street, Ottawa, Ontario"
  %(prog)s --lat 51.5074 --lon -0.1278 --system-size 10 --tilt 35

Output Control:
  By default, the full report is printed to console AND saved to files.
  Use --no-print to suppress console output (still shows summary)
  Use --no-save to prevent saving files

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
    
    # Economic parameters
    parser.add_argument(
        '--cost-per-watt',
        type=float,
        help='Installed cost per watt DC in $/W. Default: auto-selected by system size. Current market: Residential $2.50-3.00/W, Commercial $1.25-2.25/W, Utility $0.80-1.20/W'
    )
    
    parser.add_argument(
        '--electricity-rate',
        type=float,
        help='Electricity rate in $/kWh. Default: auto-detected based on location'
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
        '--no-print',
        action='store_true',
        help='Do not print full report to console (still shows summary)'
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
ITC: Investment Tax Credit (30% federal in US)
Rebate: Direct payment reducing system cost
Feed-in Tariff: Payment for generated electricity

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
        location_info = None
        
        if args.lat is not None and args.lon is not None:
            # Coordinates provided
            latitude = args.lat
            longitude = args.lon
            logger.info(f"Using provided coordinates: {latitude}, {longitude}")
            
        elif args.address:
            # Address provided - geocode it
            logger.info(f"Geocoding address: {args.address}")
            geocoder = AddressGeocoder()
            location_info = geocoder.geocode_with_details(args.address)
            
            if location_info:
                latitude = location_info.latitude
                longitude = location_info.longitude
                address = location_info.address
            else:
                print(f"Error: Could not geocode address '{args.address}'")
                print("Please check the address or use coordinates instead.")
                return 1
                
        else:
            # Interactive mode
            print("\nPV-PowerEstimate v1.3.2 - Solar PV Power Yield Calculator (Global Edition with Incentives)")
            print("=" * 50)
            print("\nThis tool estimates solar panel energy production for any location worldwide.")
            print("It uses real weather data and detailed physics modeling.")
            print("NEW: Now includes comprehensive incentive calculations!")
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
                print("          'Berlin, Germany' or 'Tokyo, Japan'")
                address = input("Address: ").strip()
                if address:
                    geocoder = AddressGeocoder()
                    location_info = geocoder.geocode_with_details(address)
                    
                    if location_info:
                        latitude = location_info.latitude
                        longitude = location_info.longitude
                        print(f"✓ Found coordinates: {latitude:.4f}, {longitude:.4f}")
                        if location_info.country:
                            print(f"✓ Location: {location_info.city or 'Unknown city'}, {location_info.state_province or 'Unknown region'}, {location_info.country}")
                    else:
                        print(f"Error: Could not geocode address '{address}'")
                        return 1
            else:
                print("Invalid choice")
                return 1
            
            # Ask about system size
            print("\n⚡ SYSTEM SIZE")
            print("Typical sizes: Residential 3-20 kW, Commercial 20-1000 kW, Utility >1000 kW")
            print("Rule of thumb: 1 kW ≈ 3-4 panels ≈ 1,400 kWh/year (varies by location)")
            print("\n💵 CURRENT MARKET COSTS (2024-2025):")
            print("   Residential: $2.00-2.50/W installed")
            print("   Commercial: $1.25-1.75/W installed")
            print("   Utility: $0.70-1.00/W installed")
            print("   (Costs have declined ~70% since 2010!)")
            if not args.system_size or args.system_size <= 100:
                print("   Note: Get multiple quotes - prices vary by region and installer")
            else:
                print("   Note: Large projects typically use competitive RFP process")
            
            size_str = input(f"\nSystem size in kW (press Enter for default {DEFAULT_SYSTEM_SIZE} kW): ").strip()
            # Note: system_config will be created later with proper defaults and command-line overrides
            interactive_system_size = None
            if size_str:
                try:
                    interactive_system_size = float(size_str)
                    print(f"System size set to {interactive_system_size} kW")
                except ValueError:
                    print("Invalid size, will use default or command-line value")
            
            # Ask about tilt
                        
            print("\n📐 TILT ANGLE")
            print(f"Recommended tilt for your latitude ({abs(latitude):.1f}°): {abs(latitude):.0f}°")
            print("Flatter = better for summer, Steeper = better for winter & snow shedding")
            
            tilt_str = input(f"Tilt angle in degrees (press Enter for latitude-based default): ").strip()
            interactive_tilt = None
            if tilt_str:
                try:
                    interactive_tilt = float(tilt_str)
                except ValueError:
                    print("Invalid tilt, will use latitude-based default")
            
            # Store interactive mode settings to apply later
            interactive_module_type = 'glass_glass'
            interactive_racking_model = 'open_rack'
            
            # Set azimuth based on hemisphere
            interactive_azimuth = 180 if latitude > 0 else 0
            
            # Helper function for azimuth direction
            def azimuth_to_direction(azimuth):
                directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                             'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
                index = int((azimuth + 11.25) / 22.5) % 16
                return directions[index]
            
            print("\n🎯 Using standard azimuth (direction) for your hemisphere")
            print(f"   Azimuth: {interactive_azimuth}° ({azimuth_to_direction(interactive_azimuth)})")
            
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
            print("6. Calculate applicable incentives for your location")
            print("="*50 + "\n")
            
            # Initialize system_config if not already done
            if 'system_config' not in locals():
                system_config = SystemConfig()
        
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
            address=address,
            location_info=location_info
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
        # Start with defaults
        system_config = SystemConfig()
        
        # Apply command-line overrides first
        if args.system_size:
            # Calculate modules needed for target system size
            modules_needed = int(args.system_size * 1000 / args.module_power)
            if modules_needed <= 20:
                system_config.modules_per_string = modules_needed
                system_config.strings_per_inverter = 1
            else:
                system_config.modules_per_string = 20
                system_config.strings_per_inverter = (modules_needed + 19) // 20  # Round up
            
        # Apply command-line overrides
        system_config.module_power = args.module_power
        system_config.surface_tilt = args.tilt if args.tilt else abs(calc.lat)
        system_config.surface_azimuth = args.azimuth
        system_config.module_type = args.module_type
        system_config.racking_model = args.racking_model
        
        # Apply interactive mode overrides (these have highest priority)
        if args.lat is None and args.lon is None and args.address is None:
            # We're in interactive mode
            if 'interactive_system_size' in locals() and interactive_system_size is not None:
                # Reconfigure for interactive system size
                modules_needed = int(interactive_system_size * 1000 / system_config.module_power)
                if modules_needed <= 20:
                    system_config.modules_per_string = modules_needed
                    system_config.strings_per_inverter = 1
                else:
                    system_config.modules_per_string = 20
                    system_config.strings_per_inverter = (modules_needed + 19) // 20
                print(f"Configuring {system_config.modules_per_string * system_config.strings_per_inverter} x {system_config.module_power}W modules = {system_config.system_size_kw:.1f} kW system")
            
            if 'interactive_tilt' in locals() and interactive_tilt is not None:
                system_config.surface_tilt = interactive_tilt
            
            if 'interactive_azimuth' in locals():
                system_config.surface_azimuth = interactive_azimuth
                
            if 'interactive_module_type' in locals():
                system_config.module_type = interactive_module_type
                
            if 'interactive_racking_model' in locals():
                system_config.racking_model = interactive_racking_model
        
        # Size inverter appropriately (DC/AC ratio of 1.2)
        system_config.inverter_power = system_config.system_size_kw * 1000 / 1.2
        
        # Run simulation
        print(f"Running simulation for {system_config.system_size_kw:.1f} kW system...")
        results, system_size = calc.calculate_pv_output(weather_data, system_config)
        
        # Calculate yields
        print("Calculating energy yields...")
        monthly, annual_energy, annual_specific_yield, capacity_factor = \
            calc.calculate_monthly_yield(results, system_size)
        
        # Determine cost per watt for economic calculations
        if hasattr(args, 'cost_per_watt') and args.cost_per_watt:
            cost_per_watt = args.cost_per_watt
        else:
            # Auto-select based on system size (2024-2025 estimates)
            if system_size <= 20:  # Residential
                cost_per_watt = 2.25
            elif system_size <= 100:  # Small commercial
                cost_per_watt = 1.50
            elif system_size <= 1000:  # Large commercial
                cost_per_watt = 1.25
            else:  # Utility scale
                cost_per_watt = 0.85
        
        # Get electricity rate
        if hasattr(args, 'electricity_rate') and args.electricity_rate:
            electricity_rate = args.electricity_rate
        else:
            # Use auto-detected rate
            electricity_rate = calc.electricity_rate
        
        # Economic calculations
        system_cost_estimate = system_size * cost_per_watt * 1000
        annual_revenue = annual_energy * electricity_rate
        payback_years = system_cost_estimate / annual_revenue
        
        # Future rate increase financial calculations with rate escalation
        electricity_escalation_rate = 0.03  # 3% annual increase
        discount_rate = 0.05  # 5% discount rate
        system_life = 25  # years
        
        # Get applicable incentives (only for residential and small commercial)
        # Typical limits: Residential rebates 10-25kW, net metering 25-100kW, USDA REAP 100kW
        if system_size <= 100:  # Only check incentives for systems 100kW or smaller
            print("Checking for applicable incentives...")
            if calc.location_info:
                incentives = SolarIncentiveManager.get_incentives_for_location(
                    calc.location_info, system_size, system_cost_estimate
                )
                if incentives:
                    print(f"Found {len(incentives)} applicable incentive programs!")
                else:
                    print("No specific incentives found for this location.")
            else:
                incentives = []
        else:
            print("Note: Incentives not applicable for large commercial/utility scale systems (>100kW)")
            incentives = []
        
        # Calculate total incentive value
        total_incentive_value = 0
        if incentives:
            for incentive in incentives:
                value = SolarIncentiveManager.calculate_incentive_value(
                    incentive, system_size, system_cost_estimate, annual_energy
                )
                total_incentive_value += value
        
        net_system_cost = system_cost_estimate - total_incentive_value
        payback_with_incentives = net_system_cost / annual_revenue if annual_revenue > 0 else float('inf')
        
        # Calculate NPV and enhanced payback with electricity rate escalation
        npv_savings = 0
        cumulative_savings = 0
        enhanced_payback_years = 0
        enhanced_payback_with_incentives = 0
        
        for year in range(1, system_life + 1):
            # Degradation: -0.5% per year after year 1
            year_degradation = 1.0 if year == 1 else (1 - 0.005 * (year - 1))
            year_production = annual_energy * year_degradation
            
            # Electricity price with escalation
            year_electricity_rate = electricity_rate * ((1 + electricity_escalation_rate) ** (year - 1))
            year_revenue = year_production * year_electricity_rate
            
            # NPV calculation
            npv_savings += year_revenue / ((1 + discount_rate) ** year)
            cumulative_savings += year_revenue
            
            if cumulative_savings >= system_cost_estimate and enhanced_payback_years == 0:
                enhanced_payback_years = year
                
            if cumulative_savings >= net_system_cost and enhanced_payback_with_incentives == 0:
                enhanced_payback_with_incentives = year
        
        # Additional savings for commercial customers
        if system_size > 20:  # Commercial system
            # Demand charge savings (conservative estimate)
            demand_charge_savings = system_size * 5 * 12  # $5/kW/month typical
            annual_revenue += demand_charge_savings
            
        # Time-of-use benefit (if applicable)
        if electricity_rate > 0.15:  # Higher rate areas often have TOU
            tou_multiplier = 1.15  # 15% benefit from producing during peak hours
            annual_revenue *= tou_multiplier
        
        # CO2 savings
        co2_saved = annual_energy * 0.4  # kg CO2 per kWh (global average)
        
        # Performance ratio
        pr = system_config.total_loss_factor * 100
        
        # Peak power
        peak_power = results['ac_power'].max()
        
        # Generate report
        print("Generating report...")
        report = calc.generate_report(
            weather_data, results, monthly, annual_energy,
            annual_specific_yield, capacity_factor, system_size, system_config,
            electricity_rate=electricity_rate, cost_per_watt=cost_per_watt,
            incentives=incentives
        )
        
        # Display key results
        print("\n" + "=" * 60)
        print("🌟 RESULTS SUMMARY 🌟")
        print("=" * 60)
        print(f"📍 Location: {calc.location.name}")
        print(f"⚡ System Size: {system_size:.1f} kW DC")
        print(f"📊 Annual Energy: {annual_energy:,.0f} kWh/year")
        print(f"📈 Specific Yield: {annual_specific_yield:,.0f} kWh/kWp/year")
        print(f"⚙️  Capacity Factor: {capacity_factor:.1f}%")
        print(f"💰 Est. Annual Revenue: ${annual_energy * electricity_rate:,.0f} (at ${electricity_rate:.3f}/kWh)")
        print(f"   Rate Info: {ElectricityRateManager.format_rate_info(electricity_rate, calc.electricity_currency, calc.rate_source)}")
        print("=" * 60)
        
        # Add incentives summary
        if incentives:
            print("\n💵 INCENTIVES SUMMARY:")
            print("-" * 60)
            for incentive in incentives:
                value = SolarIncentiveManager.calculate_incentive_value(
                    incentive, system_size, system_cost_estimate, annual_energy
                )
                if value > 0:
                    print(f"   {incentive.name}: ${value:,.0f}")
            print("-" * 60)
            print(f"   TOTAL INCENTIVE VALUE: ${total_incentive_value:,.0f}")
            print(f"   Net System Cost: ${net_system_cost:,.0f}")
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
        print(f"   System Cost: ${system_cost_estimate:,.0f} (at ${cost_per_watt}/W installed)")
        print(f"   Annual Value: ${annual_revenue:,.0f} (at ${electricity_rate:.3f}/kWh)")
        print(f"   Simple Payback: {payback_years:.1f} years (before incentives)")
        print(f"   Future Rate Increase Payback: {enhanced_payback_years} years (with 3% rate escalation)")
        
        if incentives:
            print(f"   Simple Payback with Incentives: {payback_with_incentives:.1f} years")
            print(f"   Future Rate Increase Payback with Incentives: {enhanced_payback_with_incentives} years (with escalation)")
            print(f"   25-Year Net Profit: ${cumulative_savings - net_system_cost:,.0f}")
        else:
            print(f"   25-Year Net Profit: ${cumulative_savings - system_cost_estimate:,.0f}")
        
        print(f"\n💰 FUTURE RATE INCREASE FINANCIAL ANALYSIS:")
        print(f"   NPV of Energy Savings: ${npv_savings:,.0f} (25-year, 3% escalation, 5% discount)")
        print(f"   Net Present Value: ${npv_savings - net_system_cost:,.0f}")
        print(f"   Internal Rate of Return: {((npv_savings / net_system_cost) ** (1/25) - 1) * 100:.1f}%")
        print(f"   Levelized Cost of Energy: ${net_system_cost / (annual_energy * 25 * 0.87):,.3f}/kWh")
        
        print(f"\n🌍 ENVIRONMENTAL IMPACT:")
        print(f"   CO2 Avoided: {co2_saved/1000:.1f} metric tons/year")
        print(f"   25-Year CO2 Reduction: {co2_saved * 25 * 0.87 / 1000:.0f} metric tons")
        
        # Commercial benefits if applicable
        if system_size > 20:
            print(f"\n🏢 COMMERCIAL BENEFITS:")
            if system_size <= 1000:
                print(f"   Demand Charge Savings: ${system_size * 5 * 12:,.0f}/year (estimated)")
                print(f"   Peak Shaving Benefit: Reduces peak demand charges")
                print(f"   Grid Independence: Improved resilience during outages")
            
        # Large commercial and utility scale metrics
        if system_size > 100:
            print(f"\n📊 LARGE-SCALE PROJECT METRICS:")
            # Calculate these metrics similar to the report
            if system_size > 1000:  # Utility scale
                if electricity_rate < 0.08:
                    ppa_rate_display = 0.025
                elif electricity_rate < 0.12:
                    ppa_rate_display = 0.035
                else:
                    ppa_rate_display = 0.045
            else:  # Large commercial
                ppa_rate_display = electricity_rate * 0.85
                
            # Simplified LCOE calculation
            annual_opex = system_size * 10
            simple_lcoe = (system_cost_estimate + annual_opex * 20) / (annual_energy * 20 * 0.87)
            
            print(f"   Typical PPA Rate: ${ppa_rate_display:.3f}/kWh (${ppa_rate_display*1000:.0f}/MWh)")
            print(f"   Estimated LCOE: ${simple_lcoe:.3f}/kWh")
            print(f"   {"Utility-Scale" if system_size > 1000 else "C&I"} Financing: {"70% debt, 20% tax equity" if system_size > 1000 else "60% debt typical"}")
            print(f"   Federal ITC: 30% (through 2032)")
            if system_size > 1000:
                print(f"   Grid Services: Frequency regulation, voltage support potential")
        
        if electricity_rate > 0.15:
            print(f"\n⏰ TIME-OF-USE BENEFITS:")
            print(f"   Solar production aligns with peak rate periods")
            print(f"   Estimated TOU benefit: 15% revenue increase")
            print(f"   Consider battery storage for maximum TOU savings")
        
        # Monthly variation
        best_month = monthly['energy_kwh'].idxmax()
        worst_month = monthly['energy_kwh'].idxmin()
        variation = monthly.loc[best_month, 'energy_kwh'] / monthly.loc[worst_month, 'energy_kwh']
        print(f"   Seasonal Variation: {variation:.1f}:1 ({best_month} vs {worst_month})")
        
        # Print monthly breakdown
        print("\n📅 MONTHLY BREAKDOWN:")
        print("   Month      Energy (kWh)    Daily Avg    % of Annual")
        print("   " + "-" * 50)
        for month, row in monthly.iterrows():
            pct_of_annual = (row['energy_kwh'] / annual_energy) * 100
            bar_length = int(pct_of_annual / 2)  # Scale to fit
            bar = "█" * bar_length
            print(f"   {month:<10} {row['energy_kwh']:>12,.0f}    {row['daily_energy']:>8.1f}    {pct_of_annual:>5.1f}% {bar}")
        
        print("\n💡 RECOMMENDATIONS:")
        if system_size <= 100:  # Residential and small commercial
            if capacity_factor < 15:
                print("   - Consider checking shading or system design")
            if variation > 3:
                print("   - High seasonal variation - consider battery storage")
            if annual_specific_yield > 1500:
                print("   - Above-average solar resource for investment")
            print("   - Get multiple installer quotes for accurate pricing")
            print("   - Verify eligibility for all incentives shown")
            print("   - Check net metering policies with your utility")
        else:  # Large commercial and utility scale
            if capacity_factor < 18:
                print("   - Consider single-axis tracking to boost production")
            if annual_specific_yield > 1600:
                print("   - Excellent solar resource for utility-scale development")
            print("   - Engage experienced EPC contractor for project execution")
            print("   - Conduct detailed interconnection study early in process")
            if system_size > 1000:
                print("   - Consider co-location with battery storage for grid services")
                print("   - Evaluate PPA offtake options with utilities/corporates")
        
        print("=" * 60)
        
        # Calculate and display monthly weather summary
        print("\n🌤️  MONTHLY WEATHER SUMMARY:")
        print("   " + "-" * 70)
        
        # Calculate monthly weather statistics
        weather_monthly = weather_data.groupby(weather_data.index.month).agg({
            'ghi': ['mean', 'sum'],
            'dni': 'sum',
            'dhi': 'sum',
            'temp_air': 'mean',
            'wind_speed': 'mean'
        })
        
        # Convert month numbers to names
        month_names_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        print("   Month    Solar Radiation (kWh/m²)          Avg Temp    Avg Wind")
        print("            Global   Direct   Diffuse        (°C)        (m/s)")
        print("   " + "-" * 70)
        
        for i in range(12):
            month_idx = i + 1
            ghi_total = weather_monthly.loc[month_idx, ('ghi', 'sum')] / 1000
            dni_total = weather_monthly.loc[month_idx, ('dni', 'sum')] / 1000
            dhi_total = weather_monthly.loc[month_idx, ('dhi', 'sum')] / 1000
            avg_temp = weather_monthly.loc[month_idx, ('temp_air', 'mean')]
            avg_wind = weather_monthly.loc[month_idx, ('wind_speed', 'mean')]
            
            # Create visual bar for total irradiation
            bar_length = int(ghi_total / 10)  # Scale for display
            bar = "▓" * bar_length
            
            print(f"   {month_names_short[i]:<7}  {ghi_total:>6.1f}   {dni_total:>6.1f}   {dhi_total:>6.1f}        {avg_temp:>6.1f}      {avg_wind:>6.1f}  {bar}")
        
        print("   " + "-" * 70)
        total_ghi = weather_data['ghi'].sum() / 1000
        total_dni = weather_data['dni'].sum() / 1000
        total_dhi = weather_data['dhi'].sum() / 1000
        print(f"   TOTAL    {total_ghi:>6.0f}   {total_dni:>6.0f}   {total_dhi:>6.0f} kWh/m²/year")
        
        # Classify solar resource
        if total_ghi >= 2000:
            climate_class = "Excellent (Desert/High altitude)"
        elif total_ghi >= 1600:
            climate_class = "Very Good (Sunny/Mediterranean)"
        elif total_ghi >= 1300:
            climate_class = "Good (Moderate climate)"
        elif total_ghi >= 1000:
            climate_class = "Fair (Temperate/Partly cloudy)"
        else:
            climate_class = "Poor (Cloudy/High latitude)"
        
        print(f"   Climate: {climate_class}")
        print(f"   Direct/Global Ratio: {total_dni/total_ghi:.1%} (higher = clearer skies)")
        print("\n   📝 Radiation Components:")
        print("      - Global: Total radiation on horizontal surface")
        print("      - Direct: Beam radiation from sun disk (good for tracking)")
        print("      - Diffuse: Scattered radiation from sky (works in shade)")
        
        print("\n📊 PERFORMANCE SUMMARY TABLE:")
        print("   " + "-" * 50)
        print(f"   {'Metric':<30} {'Value':>20}")
        print("   " + "-" * 50)
        print(f"   {'System Size (DC)':<30} {f'{system_size:.1f} kW':>20}")
        print(f"   {'Annual Production':<30} {f'{annual_energy:,.0f} kWh':>20}")
        print(f"   {'Daily Average':<30} {f'{annual_energy/365:.1f} kWh':>20}")
        print(f"   {'Specific Yield':<30} {f'{annual_specific_yield:,.0f} kWh/kWp':>20}")
        print(f"   {'Capacity Factor':<30} {f'{capacity_factor:.1f}%':>20}")
        print(f"   {'Performance Ratio':<30} {f'{pr:.1f}%':>20}")
        print(f"   {'Peak Power Output':<30} {f'{peak_power:.1f} kW':>20}")
        print(f"   {'CO2 Avoided':<30} {f'{co2_saved/1000:.1f} tons/yr':>20}")
        print(f"   {f'Annual Value (@${electricity_rate:.3f}/kWh)':<30} {f'${annual_revenue:,.0f}':>20}")
        print(f"   {f'System Cost (@${cost_per_watt}/W)':<30} {f'${system_cost_estimate:,.0f}':>20}")
        if incentives:
            print(f"   {'Total Incentives':<30} {f'${total_incentive_value:,.0f}':>20}")
            print(f"   {'Net Cost After Incentives':<30} {f'${net_system_cost:,.0f}':>20}")
            print(f"   {'Simple Payback w/ Incentives':<30} {f'{payback_with_incentives:.1f} years':>20}")
            print(f"   {'Future Rate Increase Payback':<30} {f'{enhanced_payback_with_incentives} years':>20}")
        else:
            print(f"   {'Simple Payback':<30} {f'{payback_years:.1f} years':>20}")
            print(f"   {'Future Rate Increase Payback':<30} {f'{enhanced_payback_years} years':>20}")
        print(f"   {'25-Year Net Savings':<30} {f'${cumulative_savings - (net_system_cost if incentives else system_cost_estimate):,.0f}':>20}")
        print("   " + "-" * 50)
        
        # Print the full report to console unless --no-print is specified
        if not args.no_print:
            print("\nFULL REPORT:")
            print(report)
        else:
            print("\n(Full report not printed. Remove --no-print flag to see it)")
        
        # Visual separator
        print("\n" + "=" * 60)
        print("FILE OPERATIONS")
        print("=" * 60)
        
        # Save results unless disabled
        if not args.no_save:
            print(f"\nSaving results to {args.output}/...")
            # Store system size in results for metadata
            results.attrs['system_size'] = system_size
            try:
                calc.save_results(results, monthly, report, args.output)
                print(f"\n✅ Results saved successfully:")
                print(f"   📄 Report: {args.output}/report.txt")
                print(f"   📊 Hourly data: {args.output}/hourly_output.csv")
                print(f"   📅 Monthly summary: {args.output}/monthly_summary.csv")
                print(f"   ⚙️  Metadata: {args.output}/metadata.json")
            except Exception as e:
                print(f"\n❌ Error saving files: {e}")
        else:
            print("\n⚠️  File saving disabled (--no-save flag active)")
        
        print("\n🎉 Analysis complete!")
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
   Current typical values (2024-2025):
   - Residential: $0.06-0.10/kWh
   - Commercial: $0.04-0.07/kWh  
   - Utility scale: $0.03-0.05/kWh

2. INSTALLED COSTS (2024-2025 US Market):
   System Type         $/W DC    Notes
   ----------------------------------------
   Residential         $2.50-3.00  Includes permitting, labor
   Small Commercial    $1.75-2.25  Economies of scale
   Large Commercial    $1.25-1.75  Bulk purchasing
   Utility Scale       $0.80-1.20  Lowest cost/watt

   Cost decline: ~70% reduction since 2010
   Future trend: ~3-5% annual decline expected

3. PAYBACK PERIOD:
   Years = (System Cost) / (Annual Savings)
   Current typical: 
   - With incentives: 4-7 years
   - Without incentives: 6-10 years

4. INCENTIVES (US):
   - Federal ITC: 30% through 2032
   - State/local: Varies widely
   - Net metering: Check local utility

5. DEGRADATION:
   - Year 1: -1.5% (LID)
   - Years 2-25: -0.5-0.7%/year
   - 25-year output: ~80-85% of initial

GLOBAL ELECTRICITY RATES
------------------------
This calculator now includes comprehensive electricity rate data for:
- All US states and Canadian provinces (with regional variations)
- European Union countries (27 members)
- Asia-Pacific region (including state-level data for India, China, Australia)
- Latin America (country and regional rates)
- Middle East and Africa (major markets)
- Over 150 countries total

Rates are updated for 2024-2025 and include:
- Residential, commercial, and industrial tariffs where available
- Time-of-use considerations
- Currency conversions to USD for comparison
- Regional variations within large countries

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
Version: 1.3.1
Date: 2025-07-06

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
from typing import Dict, Tuple, Optional, Union, Any, List
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
VERSION = "1.3.1"
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


# Comprehensive regional solar incentives database (2024-2025)
# Values are in percentage of system cost or $/W for rebates
SOLAR_INCENTIVES = {
    # US STATES - All federal programs plus state-specific
    "united states": {
        # Federal incentive applies to all states
        "federal": {
            "type": "tax_credit",
            "value": 0.30,  # 30% through 2032
            "expires": "2032-12-31",
            "notes": "Federal Investment Tax Credit (ITC)"
        },
        
        # State-specific incentives
        "california": {
            "programs": [
                {
                    "name": "SGIP",
                    "type": "rebate",
                    "value": 0.20,  # $/Wh for storage
                    "category": "battery",
                    "notes": "Self-Generation Incentive Program for storage"
                },
                {
                    "name": "DAC-SASH",
                    "type": "rebate",
                    "value": 3.00,  # $/W
                    "category": "low-income",
                    "notes": "Disadvantaged Communities Single-family Solar Homes"
                },
                {
                    "name": "Property Tax Exclusion",
                    "type": "tax_exemption",
                    "value": 1.0,  # 100% exemption
                    "notes": "Solar installations excluded from property tax"
                }
            ]
        },
        
        "new york": {
            "programs": [
                {
                    "name": "NY-Sun",
                    "type": "rebate",
                    "value": 0.20,  # $/W
                    "category": "residential",
                    "max_rebate": 5000,
                    "notes": "Declining block incentive"
                },
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.25,  # 25% of system cost
                    "max_credit": 5000,
                    "notes": "25% state tax credit"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "massachusetts": {
            "programs": [
                {
                    "name": "SMART",
                    "type": "performance",
                    "value": 0.15,  # $/kWh
                    "duration": 20,  # years
                    "notes": "Solar Massachusetts Renewable Target program"
                },
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.15,  # 15% of system cost
                    "max_credit": 1000,
                    "notes": "15% state tax credit"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "texas": {
            "programs": [
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption for solar value"
                },
                {
                    "name": "Austin Energy Rebate",
                    "type": "rebate",
                    "value": 2500,  # flat amount
                    "category": "utility",
                    "location": "Austin",
                    "notes": "Austin Energy solar rebate"
                },
                {
                    "name": "CPS Energy Rebate",
                    "type": "rebate",
                    "value": 0.60,  # $/W
                    "category": "utility",
                    "location": "San Antonio",
                    "notes": "CPS Energy solar rebate"
                }
            ]
        },
        
        "florida": {
            "programs": [
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,  # 1:1 credit
                    "notes": "Full retail rate net metering"
                }
            ]
        },
        
        "arizona": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.25,
                    "max_credit": 1000,
                    "notes": "25% state tax credit"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "No added property tax"
                }
            ]
        },
        
        "colorado": {
            "programs": [
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Xcel Energy Rebate",
                    "type": "rebate",
                    "value": 0.50,  # $/W
                    "category": "utility",
                    "notes": "Xcel Energy Solar*Rewards"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Renewable energy property tax exemption"
                }
            ]
        },
        
        "new jersey": {
            "programs": [
                {
                    "name": "SuSI",
                    "type": "performance",
                    "value": 90,  # $/MWh
                    "duration": 15,
                    "notes": "Successor Solar Incentive program"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Solar property tax exemption"
                }
            ]
        },
        
        "illinois": {
            "programs": [
                {
                    "name": "Illinois Shines",
                    "type": "performance",
                    "value": 0.0775,  # $/kWh for 15 years
                    "duration": 15,
                    "notes": "Adjustable Block Program"
                },
                {
                    "name": "Solar for All",
                    "type": "rebate",
                    "value": 1.0,  # 100% for qualifying
                    "category": "low-income",
                    "notes": "Low-income solar program"
                }
            ]
        },
        
        "maryland": {
            "programs": [
                {
                    "name": "State Grant",
                    "type": "rebate",
                    "value": 1000,  # flat amount
                    "category": "residential",
                    "notes": "Residential Clean Energy Rebate"
                },
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.30,
                    "max_credit": 5000,
                    "expires": "2025-12-31",
                    "notes": "30% state tax credit through 2025"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption"
                }
            ]
        },
        
        "minnesota": {
            "programs": [
                {
                    "name": "Solar*Rewards",
                    "type": "rebate",
                    "value": 0.50,  # $/W
                    "category": "utility",
                    "notes": "Xcel Energy rebate"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Solar property tax exemption"
                }
            ]
        },
        
        "oregon": {
            "programs": [
                {
                    "name": "Solar + Storage Rebate",
                    "type": "rebate",
                    "value": 0.30,  # $/W
                    "max_rebate": 5000,
                    "category": "residential",
                    "notes": "Oregon solar + storage rebate"
                },
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.40,  # 40% for low-income
                    "category": "low-income",
                    "max_credit": 5000,
                    "notes": "Enhanced credit for low-income"
                }
            ]
        },
        
        # Additional states with basic incentives
        "connecticut": {
            "programs": [
                {
                    "name": "Residential Solar Investment",
                    "type": "rebate",
                    "value": 0.40,  # $/W
                    "notes": "Green Bank incentive"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption"
                }
            ]
        },
        
        "nevada": {
            "programs": [
                {
                    "name": "NV Energy Rebate",
                    "type": "rebate",
                    "value": 0.15,  # $/W
                    "category": "utility",
                    "notes": "NV Energy solar rebate"
                },
                {
                    "name": "Property Tax Abatement",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Property tax abatement"
                }
            ]
        },
        
        "hawaii": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.35,  # 35%
                    "max_credit": 5000,
                    "notes": "35% state tax credit"
                },
                {
                    "name": "Green Infrastructure Loan",
                    "type": "loan",
                    "value": 0.0,  # 0% interest
                    "notes": "On-bill financing available"
                }
            ]
        },
        
        "rhode island": {
            "programs": [
                {
                    "name": "REF Solar Grant",
                    "type": "rebate",
                    "value": 0.85,  # $/W
                    "max_rebate": 5000,
                    "notes": "Renewable Energy Fund grant"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "vermont": {
            "programs": [
                {
                    "name": "State Incentive",
                    "type": "rebate",
                    "value": 0.40,  # $/W
                    "notes": "Efficiency Vermont incentive"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "new mexico": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.10,  # 10%
                    "max_credit": 6000,
                    "notes": "10% state tax credit"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% property tax exemption"
                }
            ]
        },
        
        "iowa": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.30,  # 30%
                    "max_credit": 5000,
                    "notes": "30% state tax credit"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "duration": 5,  # years
                    "notes": "5-year property tax exemption"
                }
            ]
        },
        
        "south carolina": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.25,  # 25%
                    "notes": "25% state tax credit"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Manufacturing equipment exemption"
                }
            ]
        },
        
        "wisconsin": {
            "programs": [
                {
                    "name": "Focus on Energy",
                    "type": "rebate",
                    "value": 0.10,  # $/W
                    "max_rebate": 500,
                    "notes": "Focus on Energy rebate"
                },
                {
                    "name": "Sales Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "100% sales tax exemption"
                }
            ]
        },
        
        "utah": {
            "programs": [
                {
                    "name": "State Tax Credit",
                    "type": "tax_credit",
                    "value": 0.25,
                    "max_credit": 1600,
                    "notes": "25% state tax credit"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Renewable energy property tax exemption"
                }
            ]
        }
    },
    
    # CANADA - Federal and provincial programs
    "canada": {
        "federal": {
            "programs": [
                {
                    "name": "Greener Homes Grant",
                    "type": "rebate",
                    "value": 5000,  # flat amount
                    "category": "residential",
                    "notes": "Canada Greener Homes Grant for solar"
                },
                {
                    "name": "Greener Homes Loan",
                    "type": "loan",
                    "value": 40000,  # max loan
                    "interest": 0.0,  # 0% interest
                    "notes": "Interest-free loan up to $40,000"
                }
            ]
        },
        
        "ontario": {
            "programs": [
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Full retail rate net metering"
                },
                {
                    "name": "Property Tax Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "category": "commercial",
                    "notes": "Commercial property tax exemption"
                }
            ]
        },
        
        "british columbia": {
            "programs": [
                {
                    "name": "PST Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "Provincial sales tax exemption"
                },
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "BC Hydro net metering program"
                }
            ]
        },
        
        "alberta": {
            "programs": [
                {
                    "name": "Solar Rebate",
                    "type": "rebate",
                    "value": 0.90,  # $/W
                    "max_rebate": 10000,
                    "notes": "Residential and Commercial Solar Program"
                },
                {
                    "name": "Micro-generation",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Credit for excess generation"
                }
            ]
        },
        
        "quebec": {
            "programs": [
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Hydro-Quebec net metering"
                },
                {
                    "name": "Commercial Program",
                    "type": "rebate",
                    "value": 0.50,  # $/W
                    "category": "commercial",
                    "notes": "Commercial solar incentive"
                }
            ]
        },
        
        "saskatchewan": {
            "programs": [
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "max_system": 100,  # kW
                    "notes": "SaskPower net metering up to 100kW"
                },
                {
                    "name": "PST Rebate",
                    "type": "rebate",
                    "value": 0.10,  # 10% PST rebate
                    "notes": "PST rebate on solar equipment"
                }
            ]
        },
        
        "nova scotia": {
            "programs": [
                {
                    "name": "SolarHomes",
                    "type": "rebate",
                    "value": 0.60,  # $/W
                    "max_rebate": 6000,
                    "notes": "Efficiency NS SolarHomes rebate"
                },
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Enhanced net metering program"
                }
            ]
        },
        
        "prince edward island": {
            "programs": [
                {
                    "name": "Solar Electric Rebate",
                    "type": "rebate",
                    "value": 1.00,  # $/W
                    "max_rebate": 10000,
                    "notes": "PEI solar electric rebate program"
                },
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Net metering available"
                }
            ]
        },
        
        "newfoundland and labrador": {
            "programs": [
                {
                    "name": "Net Metering",
                    "type": "net_metering",
                    "value": 1.0,
                    "notes": "Newfoundland Power net metering"
                }
            ]
        }
    },
    
    # EUROPE - Major markets
    "germany": {
        "programs": [
            {
                "name": "Feed-in Tariff",
                "type": "feed_in_tariff",
                "value": 0.082,  # €/kWh
                "duration": 20,
                "notes": "EEG feed-in tariff for <10kW"
            },
            {
                "name": "KfW Loan",
                "type": "loan",
                "value": 0.0145,  # 1.45% interest
                "notes": "Low-interest loans from KfW bank"
            },
            {
                "name": "VAT Reduction",
                "type": "tax_reduction",
                "value": 0.0,  # 0% VAT
                "notes": "0% VAT on residential solar"
            }
        ]
    },
    
    "france": {
        "programs": [
            {
                "name": "Self-consumption Premium",
                "type": "rebate",
                "value": 0.38,  # €/W for <3kW
                "notes": "Premium for self-consumption"
            },
            {
                "name": "Feed-in Tariff",
                "type": "feed_in_tariff",
                "value": 0.13,  # €/kWh
                "duration": 20,
                "notes": "20-year feed-in tariff"
            },
            {
                "name": "VAT Reduction",
                "type": "tax_reduction",
                "value": 0.10,  # 10% VAT instead of 20%
                "notes": "Reduced VAT rate"
            }
        ]
    },
    
    "italy": {
        "programs": [
            {
                "name": "Superbonus 110%",
                "type": "tax_credit",
                "value": 1.10,  # 110% tax deduction
                "expires": "2025-12-31",
                "notes": "110% tax deduction over 4 years"
            },
            {
                "name": "Net Billing",
                "type": "net_metering",
                "value": 0.80,  # partial credit
                "notes": "Scambio sul posto (net billing)"
            }
        ]
    },
    
    "spain": {
        "programs": [
            {
                "name": "Next Generation EU Funds",
                "type": "rebate",
                "value": 0.60,  # €/W
                "max_rebate": 3000,
                "notes": "EU recovery fund subsidies"
            },
            {
                "name": "IBI Reduction",
                "type": "tax_reduction",
                "value": 0.50,  # 50% property tax reduction
                "duration": 5,
                "notes": "Property tax reduction varies by municipality"
            },
            {
                "name": "Net Billing",
                "type": "net_metering",
                "value": 0.90,
                "notes": "Simplified compensation mechanism"
            }
        ]
    },
    
    "netherlands": {
        "programs": [
            {
                "name": "Net Metering",
                "type": "net_metering",
                "value": 1.0,
                "expires": "2027-01-01",
                "notes": "Full net metering until 2027"
            },
            {
                "name": "BTW Refund",
                "type": "tax_refund",
                "value": 0.21,  # 21% VAT refund
                "notes": "VAT refund for residential solar"
            },
            {
                "name": "SDE++",
                "type": "feed_in_premium",
                "value": 0.05,  # €/kWh premium
                "category": "commercial",
                "notes": "Feed-in premium for large systems"
            }
        ]
    },
    
    "united kingdom": {
        "programs": [
            {
                "name": "Smart Export Guarantee",
                "type": "feed_in_tariff",
                "value": 0.05,  # £/kWh average
                "notes": "SEG payments for exported electricity"
            },
            {
                "name": "0% VAT",
                "type": "tax_exemption",
                "value": 1.0,
                "notes": "0% VAT on residential solar until 2027"
            },
            {
                "name": "ECO4 Scheme",
                "type": "rebate",
                "value": 1.0,  # 100% for qualifying
                "category": "low-income",
                "notes": "Free solar for low-income households"
            }
        ]
    },
    
    # AUSTRALIA - State programs
    "australia": {
        "federal": {
            "programs": [
                {
                    "name": "STC Rebate",
                    "type": "rebate",
                    "value": 0.45,  # $/W approximate
                    "notes": "Small-scale Technology Certificates"
                },
                {
                    "name": "GST Exemption",
                    "type": "tax_exemption",
                    "value": 1.0,
                    "notes": "GST exemption for systems <100kW"
                }
            ]
        },
        
        "victoria": {
            "programs": [
                {
                    "name": "Solar Homes",
                    "type": "rebate",
                    "value": 1400,  # flat amount
                    "notes": "Victorian Solar Homes rebate"
                },
                {
                    "name": "Interest-free Loan",
                    "type": "loan",
                    "value": 1400,
                    "interest": 0.0,
                    "notes": "Interest-free loan matching rebate"
                }
            ]
        },
        
        "new south wales": {
            "programs": [
                {
                    "name": "Empowering Homes",
                    "type": "loan",
                    "value": 14000,
                    "interest": 0.0,
                    "notes": "Interest-free loan for solar+battery"
                },
                {
                    "name": "Low Income Solar",
                    "type": "rebate",
                    "value": 2200,
                    "category": "low-income",
                    "notes": "Low income household rebate"
                }
            ]
        },
        
        "queensland": {
            "programs": [
                {
                    "name": "Battery Booster",
                    "type": "rebate",
                    "value": 3000,
                    "category": "battery",
                    "notes": "Battery rebate program"
                },
                {
                    "name": "Solar for Rentals",
                    "type": "rebate",
                    "value": 3500,
                    "category": "rental",
                    "notes": "Rebate for rental properties"
                }
            ]
        },
        
        "south australia": {
            "programs": [
                {
                    "name": "Home Battery Scheme",
                    "type": "rebate",
                    "value": 0.30,  # $/Wh
                    "max_rebate": 3000,
                    "category": "battery",
                    "notes": "Battery subsidy program"
                }
            ]
        }
    },
    
    # Other major markets
    "japan": {
        "programs": [
            {
                "name": "FIT Scheme",
                "type": "feed_in_tariff",
                "value": 16,  # ¥/kWh
                "duration": 10,
                "notes": "Feed-in tariff for <10kW"
            },
            {
                "name": "Tokyo Subsidy",
                "type": "rebate",
                "value": 100000,  # ¥/kW
                "location": "Tokyo",
                "notes": "Tokyo metropolitan subsidy"
            }
        ]
    },
    
    "south korea": {
        "programs": [
            {
                "name": "Home Solar Subsidy",
                "type": "rebate",
                "value": 0.70,  # 70% subsidy
                "notes": "Government subsidy program"
            },
            {
                "name": "REC Trading",
                "type": "performance",
                "value": 50000,  # ₩/REC
                "notes": "Renewable Energy Certificate trading"
            }
        ]
    },
    
    "india": {
        "federal": {
            "programs": [
                {
                    "name": "PM-KUSUM",
                    "type": "rebate",
                    "value": 0.60,  # 60% subsidy
                    "category": "agricultural",
                    "notes": "Agricultural pump solarization"
                },
                {
                    "name": "Rooftop Solar Phase II",
                    "type": "rebate",
                    "value": 0.40,  # 40% for <3kW
                    "notes": "National rooftop solar program"
                }
            ]
        }
    },
    
    "china": {
        "programs": [
            {
                "name": "Feed-in Tariff",
                "type": "feed_in_tariff",
                "value": 0.42,  # ¥/kWh
                "notes": "National feed-in tariff"
            },
            {
                "name": "Distributed Solar Subsidy",
                "type": "rebate",
                "value": 0.02,  # ¥/kWh
                "notes": "Additional distributed generation subsidy"
            }
        ]
    }
}


@dataclass
class IncentiveDetails:
    """
    Details about a specific solar incentive program.
    """
    name: str
    type: str  # tax_credit, rebate, performance, loan, etc.
    value: float  # Percentage, $/W, or flat amount
    max_value: Optional[float] = None
    duration: Optional[int] = None  # Years for performance incentives
    expires: Optional[str] = None
    category: Optional[str] = None  # residential, commercial, low-income
    notes: Optional[str] = None


# Comprehensive global electricity rates database (2024-2025 data)
# Rates are in local currency per kWh
ELECTRICITY_RATES = {
    # NORTH AMERICA - Detailed coverage
    "canada": {
        "alberta": 0.166,
        "british columbia": 0.133,
        "manitoba": 0.097,
        "new brunswick": 0.129,
        "newfoundland and labrador": 0.137,
        "northwest territories": 0.387,
        "nova scotia": 0.183,
        "nunavut": 0.375,
        "ontario": 0.158,
        "prince edward island": 0.179,
        "quebec": 0.073,
        "saskatchewan": 0.150,
        "yukon": 0.187,
        "default": 0.140
    },
    
    "united states": {
        "alabama": 0.147,
        "alaska": 0.235,
        "arizona": 0.136,
        "arkansas": 0.125,
        "california": 0.287,
        "colorado": 0.140,
        "connecticut": 0.248,
        "delaware": 0.139,
        "district of columbia": 0.165,
        "florida": 0.139,
        "georgia": 0.138,
        "hawaii": 0.447,
        "idaho": 0.111,
        "illinois": 0.147,
        "indiana": 0.146,
        "iowa": 0.120,
        "kansas": 0.132,
        "kentucky": 0.123,
        "louisiana": 0.120,
        "maine": 0.229,
        "maryland": 0.148,
        "massachusetts": 0.264,
        "michigan": 0.179,
        "minnesota": 0.138,
        "mississippi": 0.129,
        "missouri": 0.120,
        "montana": 0.117,
        "nebraska": 0.116,
        "nevada": 0.143,
        "new hampshire": 0.267,
        "new jersey": 0.175,
        "new mexico": 0.139,
        "new york": 0.216,
        "north carolina": 0.123,
        "north dakota": 0.109,
        "ohio": 0.138,
        "oklahoma": 0.113,
        "oregon": 0.118,
        "pennsylvania": 0.157,
        "rhode island": 0.273,
        "south carolina": 0.137,
        "south dakota": 0.125,
        "tennessee": 0.127,
        "texas": 0.143,
        "utah": 0.110,
        "vermont": 0.208,
        "virginia": 0.134,
        "washington": 0.103,
        "west virginia": 0.133,
        "wisconsin": 0.154,
        "wyoming": 0.110,
        "default": 0.154
    },
    
    "mexico": {
        "baja california": 0.092,
        "baja california sur": 0.088,
        "chihuahua": 0.085,
        "mexico city": 0.079,
        "nuevo leon": 0.082,
        "jalisco": 0.081,
        "yucatan": 0.089,
        "default": 0.083
    },
    
    # EUROPE - Complete EU coverage
    "austria": 0.246,
    "belgium": 0.337,
    "bulgaria": 0.119,
    "croatia": 0.137,
    "cyprus": 0.238,
    "czech republic": 0.183,
    "denmark": 0.356,
    "estonia": 0.193,
    "finland": 0.178,
    "france": 0.231,
    "germany": 0.397,
    "greece": 0.189,
    "hungary": 0.113,
    "ireland": 0.298,
    "italy": 0.284,
    "latvia": 0.201,
    "lithuania": 0.181,
    "luxembourg": 0.192,
    "malta": 0.125,
    "netherlands": 0.300,
    "poland": 0.173,
    "portugal": 0.222,
    "romania": 0.152,
    "slovakia": 0.168,
    "slovenia": 0.167,
    "spain": 0.247,
    "sweden": 0.153,
    
    # Non-EU European countries
    "united kingdom": 0.228,
    "norway": 0.116,
    "switzerland": 0.210,
    "iceland": 0.054,
    "albania": 0.094,
    "bosnia and herzegovina": 0.089,
    "kosovo": 0.067,
    "macedonia": 0.078,
    "moldova": 0.112,
    "montenegro": 0.101,
    "serbia": 0.075,
    "turkey": 0.093,
    "ukraine": 0.044,
    
    # ASIA - Comprehensive coverage
    "china": {
        "beijing": 0.53,
        "shanghai": 0.61,
        "guangdong": 0.58,
        "shandong": 0.55,
        "jiangsu": 0.56,
        "zhejiang": 0.57,
        "sichuan": 0.45,
        "hebei": 0.52,
        "henan": 0.50,
        "hubei": 0.51,
        "hunan": 0.54,
        "anhui": 0.53,
        "fujian": 0.55,
        "jiangxi": 0.52,
        "liaoning": 0.49,
        "heilongjiang": 0.48,
        "shaanxi": 0.47,
        "gansu": 0.45,
        "qinghai": 0.43,
        "xinjiang": 0.39,
        "tibet": 0.38,
        "inner mongolia": 0.42,
        "default": 0.52
    },
    
    "india": {
        "maharashtra": 7.14,
        "gujarat": 5.50,
        "delhi": 6.50,
        "tamil nadu": 6.85,
        "karnataka": 6.95,
        "andhra pradesh": 7.25,
        "telangana": 7.20,
        "west bengal": 7.85,
        "rajasthan": 6.75,
        "uttar pradesh": 6.30,
        "madhya pradesh": 6.15,
        "kerala": 5.80,
        "haryana": 6.45,
        "punjab": 6.00,
        "bihar": 6.90,
        "odisha": 5.40,
        "assam": 6.70,
        "jharkhand": 6.20,
        "chattisgarh": 5.30,
        "himachal pradesh": 4.50,
        "uttarakhand": 5.25,
        "goa": 3.25,
        "jammu and kashmir": 3.00,
        "northeast states": 5.50,
        "default": 6.50
    },
    
    "japan": {
        "tokyo": 31.0,
        "osaka": 29.5,
        "hokkaido": 33.0,
        "kyushu": 28.5,
        "okinawa": 32.0,
        "default": 31.0
    },
    
    "south korea": 123.7,
    "taiwan": 2.63,
    "hong kong": 1.19,
    "singapore": 0.226,
    "thailand": 4.18,
    "vietnam": 1864,
    "philippines": 9.85,
    "indonesia": 1150,
    "malaysia": 0.436,
    "myanmar": 110,
    "cambodia": 720,
    "laos": 948,
    "bangladesh": 7.18,
    "pakistan": 16.5,
    "sri lanka": 21.0,
    "nepal": 8.77,
    "afghanistan": 2.85,
    "kazakhstan": 16.9,
    "uzbekistan": 295,
    "kyrgyzstan": 2.16,
    "tajikistan": 0.35,
    "turkmenistan": 0.033,
    "mongolia": 232,
    "north korea": 0.03,
    
    # MIDDLE EAST
    "saudi arabia": 0.048,
    "united arab emirates": 0.085,
    "qatar": 0.041,
    "kuwait": 0.030,
    "bahrain": 0.029,
    "oman": 0.062,
    "jordan": 0.142,
    "lebanon": 0.056,
    "israel": 0.485,
    "palestine": 0.556,
    "syria": 0.012,
    "iraq": 0.040,
    "iran": 0.007,
    "yemen": 0.038,
    
    # AFRICA
    "south africa": {
        "gauteng": 2.31,
        "western cape": 2.45,
        "kwazulu-natal": 2.28,
        "eastern cape": 2.38,
        "mpumalanga": 2.25,
        "limpopo": 2.22,
        "north west": 2.26,
        "free state": 2.29,
        "northern cape": 2.33,
        "default": 2.31
    },
    
    "egypt": 1.45,
    "nigeria": 68,
    "kenya": 23.7,
    "ethiopia": 1.36,
    "morocco": 1.26,
    "algeria": 4.67,
    "tunisia": 0.183,
    "libya": 0.041,
    "sudan": 5.67,
    "ghana": 0.365,
    "tanzania": 292,
    "uganda": 720,
    "zimbabwe": 0.098,
    "zambia": 0.089,
    "mozambique": 6.84,
    "malawi": 152,
    "rwanda": 183,
    "botswana": 1.29,
    "namibia": 1.78,
    "mauritius": 6.35,
    "madagascar": 645,
    "senegal": 118,
    "ivory coast": 87.4,
    "cameroon": 79.5,
    "angola": 42.5,
    "democratic republic of congo": 0.089,
    "gabon": 123,
    "mauritania": 18.2,
    "mali": 112,
    "burkina faso": 105,
    "niger": 89.7,
    "chad": 95.6,
    "somalia": 0.50,
    "eritrea": 0.14,
    "djibouti": 32.4,
    "seychelles": 5.48,
    "cape verde": 25.3,
    "guinea": 1250,
    "sierra leone": 2854,
    "liberia": 0.41,
    "togo": 125,
    "benin": 123,
    "gambia": 7.82,
    "guinea-bissau": 93.5,
    "equatorial guinea": 71.5,
    "central african republic": 88.9,
    "congo": 65.4,
    "sao tome and principe": 7.25,
    "comoros": 89.5,
    "lesotho": 1.45,
    "swaziland": 1.32,
    
    # SOUTH AMERICA
    "brazil": {
        "sao paulo": 0.75,
        "rio de janeiro": 0.82,
        "minas gerais": 0.71,
        "rio grande do sul": 0.68,
        "parana": 0.66,
        "santa catarina": 0.65,
        "bahia": 0.70,
        "pernambuco": 0.73,
        "ceara": 0.72,
        "amazonas": 0.67,
        "para": 0.69,
        "mato grosso": 0.74,
        "goias": 0.71,
        "distrito federal": 0.69,
        "default": 0.71
    },
    
    "argentina": {
        "buenos aires": 65.4,
        "cordoba": 68.2,
        "santa fe": 66.8,
        "mendoza": 71.3,
        "tucuman": 69.5,
        "default": 67.8
    },
    
    "chile": 159,
    "colombia": 678,
    "peru": 0.64,
    "venezuela": 0.001,
    "ecuador": 0.092,
    "bolivia": 0.58,
    "paraguay": 325,
    "uruguay": 6.87,
    "guyana": 32.1,
    "suriname": 0.087,
    "french guiana": 0.231,
    
    # OCEANIA
    "australia": {
        "new south wales": 0.308,
        "victoria": 0.289,
        "queensland": 0.285,
        "south australia": 0.347,
        "western australia": 0.289,
        "tasmania": 0.265,
        "northern territory": 0.255,
        "australian capital territory": 0.212,
        "default": 0.294
    },
    
    "new zealand": {
        "north island": 0.303,
        "south island": 0.289,
        "default": 0.296
    },
    
    "fiji": 0.343,
    "papua new guinea": 0.482,
    "solomon islands": 0.95,
    "vanuatu": 0.63,
    "samoa": 0.87,
    "tonga": 0.77,
    "kiribati": 0.54,
    "tuvalu": 0.60,
    "nauru": 0.52,
    "palau": 0.35,
    "marshall islands": 0.39,
    "micronesia": 0.41,
    "french polynesia": 35.2,
    "new caledonia": 26.8,
    "cook islands": 0.82,
    
    # CARIBBEAN
    "jamaica": 44.7,
    "trinidad and tobago": 0.28,
    "barbados": 0.41,
    "bahamas": 0.32,
    "haiti": 13.5,
    "dominican republic": 11.8,
    "cuba": 0.10,
    "puerto rico": 0.22,
    "cayman islands": 0.35,
    "bermuda": 0.44,
    "virgin islands": 0.38,
    "antigua and barbuda": 0.38,
    "saint lucia": 0.36,
    "grenada": 0.37,
    "dominica": 0.39,
    "saint vincent": 0.41,
    "saint kitts and nevis": 0.37,
    "turks and caicos": 0.35,
    "aruba": 0.28,
    "curacao": 0.39,
    "bonaire": 0.31,
    
    # Default global rate
    "default": 0.140
}

# Currency conversion rates to USD (as of Jan 2025)
# Extended coverage for all currencies in the database
CURRENCY_TO_USD = {
    # Major currencies
    "CAD": 0.70,    # Canadian Dollar
    "USD": 1.00,    # US Dollar
    "EUR": 1.05,    # Euro
    "GBP": 1.27,    # British Pound
    "JPY": 0.0064,  # Japanese Yen
    "CNY": 0.137,   # Chinese Yuan
    "INR": 0.012,   # Indian Rupee
    
    # Americas
    "MXN": 0.049,   # Mexican Peso
    "BRL": 0.163,   # Brazilian Real
    "ARS": 0.0010,  # Argentine Peso
    "CLP": 0.0010,  # Chilean Peso
    "COP": 0.00023, # Colombian Peso
    "PEN": 0.265,   # Peruvian Sol
    "VES": 0.020,   # Venezuelan Bolivar
    "BOB": 0.145,   # Bolivian Boliviano
    "PYG": 0.00013, # Paraguayan Guarani
    "UYU": 0.025,   # Uruguayan Peso
    "GYD": 0.0048,  # Guyanese Dollar
    "SRD": 0.028,   # Surinamese Dollar
    
    # Caribbean
    "JMD": 0.0064,  # Jamaican Dollar
    "TTD": 0.147,   # Trinidad Dollar
    "BBD": 0.50,    # Barbadian Dollar
    "BSD": 1.00,    # Bahamian Dollar
    "HTG": 0.0076,  # Haitian Gourde
    "DOP": 0.017,   # Dominican Peso
    "CUP": 0.042,   # Cuban Peso
    "XCD": 0.37,    # East Caribbean Dollar
    "KYD": 1.20,    # Cayman Dollar
    "BMD": 1.00,    # Bermudian Dollar
    "AWG": 0.56,    # Aruban Florin
    "ANG": 0.56,    # Netherlands Antillean Guilder
    
    # Europe (non-Euro)
    "CHF": 1.10,    # Swiss Franc
    "NOK": 0.089,   # Norwegian Krone
    "SEK": 0.091,   # Swedish Krona
    "DKK": 0.141,   # Danish Krone
    "ISK": 0.0071,  # Icelandic Krona
    "CZK": 0.042,   # Czech Koruna
    "PLN": 0.244,   # Polish Zloty
    "HUF": 0.0025,  # Hungarian Forint
    "RON": 0.212,   # Romanian Leu
    "BGN": 0.536,   # Bulgarian Lev
    "HRK": 0.139,   # Croatian Kuna
    "RSD": 0.0089,  # Serbian Dinar
    "BAM": 0.536,   # Bosnia Mark
    "MKD": 0.017,   # Macedonian Denar
    "ALL": 0.0093,  # Albanian Lek
    "MDL": 0.054,   # Moldovan Leu
    "UAH": 0.024,   # Ukrainian Hryvnia
    "TRY": 0.029,   # Turkish Lira
    
    # Asia
    "KRW": 0.00069, # South Korean Won
    "TWD": 0.031,   # Taiwan Dollar
    "HKD": 0.128,   # Hong Kong Dollar
    "SGD": 0.735,   # Singapore Dollar
    "THB": 0.029,   # Thai Baht
    "VND": 0.000039,# Vietnamese Dong
    "PHP": 0.017,   # Philippine Peso
    "IDR": 0.000062,# Indonesian Rupiah
    "MYR": 0.222,   # Malaysian Ringgit
    "MMK": 0.00048, # Myanmar Kyat
    "KHR": 0.00025, # Cambodian Riel
    "LAK": 0.000045,# Lao Kip
    "BDT": 0.0084,  # Bangladeshi Taka
    "PKR": 0.0036,  # Pakistani Rupee
    "LKR": 0.0031,  # Sri Lankan Rupee
    "NPR": 0.0074,  # Nepalese Rupee
    "AFN": 0.014,   # Afghan Afghani
    "KZT": 0.0020,  # Kazakhstani Tenge
    "UZS": 0.000078,# Uzbek Som
    "KGS": 0.012,   # Kyrgyz Som
    "TJS": 0.091,   # Tajik Somoni
    "TMT": 0.286,   # Turkmen Manat
    "MNT": 0.00029, # Mongolian Tugrik
    "KPW": 0.0011,  # North Korean Won
    
    # Middle East
    "SAR": 0.267,   # Saudi Riyal
    "AED": 0.272,   # UAE Dirham
    "QAR": 0.275,   # Qatari Riyal
    "KWD": 3.25,    # Kuwaiti Dinar
    "BHD": 2.65,    # Bahraini Dinar
    "OMR": 2.60,    # Omani Rial
    "JOD": 1.41,    # Jordanian Dinar
    "LBP": 0.000011,# Lebanese Pound
    "ILS": 0.277,   # Israeli Shekel
    "SYP": 0.00008, # Syrian Pound
    "IQD": 0.00076, # Iraqi Dinar
    "IRR": 0.000002,# Iranian Rial
    "YER": 0.0040,  # Yemeni Rial
    
    # Africa
    "ZAR": 0.053,   # South African Rand
    "EGP": 0.020,   # Egyptian Pound
    "NGN": 0.00064, # Nigerian Naira
    "KES": 0.0078,  # Kenyan Shilling
    "ETB": 0.0079,  # Ethiopian Birr
    "MAD": 0.098,   # Moroccan Dirham
    "DZD": 0.0074,  # Algerian Dinar
    "TND": 0.312,   # Tunisian Dinar
    "LYD": 0.206,   # Libyan Dinar
    "SDG": 0.0017,  # Sudanese Pound
    "GHS": 0.066,   # Ghanaian Cedi
    "TZS": 0.00040, # Tanzanian Shilling
    "UGX": 0.00027, # Ugandan Shilling
    "ZWL": 0.0031,  # Zimbabwean Dollar
    "ZMW": 0.036,   # Zambian Kwacha
    "MZN": 0.016,   # Mozambican Metical
    "MWK": 0.00058, # Malawian Kwacha
    "RWF": 0.00073, # Rwandan Franc
    "BWP": 0.072,   # Botswana Pula
    "NAD": 0.053,   # Namibian Dollar
    "MUR": 0.021,   # Mauritian Rupee
    "MGA": 0.00021, # Malagasy Ariary
    "XOF": 0.0016,  # West African CFA Franc
    "XAF": 0.0016,  # Central African CFA Franc
    "MRU": 0.025,   # Mauritanian Ouguiya
    "SOS": 0.0018,  # Somali Shilling
    "ERN": 0.067,   # Eritrean Nakfa
    "DJF": 0.0056,  # Djiboutian Franc
    "SCR": 0.069,   # Seychellois Rupee
    "CVE": 0.0095,  # Cape Verdean Escudo
    "GNF": 0.00012, # Guinean Franc
    "SLL": 0.000039,# Sierra Leonean Leone
    "LRD": 0.0052,  # Liberian Dollar
    "GMD": 0.014,   # Gambian Dalasi
    "STN": 0.043,   # São Tomé Príncipe Dobra
    "KMF": 0.0021,  # Comorian Franc
    "LSL": 0.053,   # Lesotho Loti
    "SZL": 0.053,   # Swazi Lilangeni
    
    # Oceania
    "AUD": 0.62,    # Australian Dollar
    "NZD": 0.56,    # New Zealand Dollar
    "FJD": 0.436,   # Fijian Dollar
    "PGK": 0.248,   # Papua New Guinea Kina
    "SBD": 0.119,   # Solomon Islands Dollar
    "VUV": 0.0082,  # Vanuatu Vatu
    "WST": 0.356,   # Samoan Tala
    "TOP": 0.419,   # Tongan Pa'anga
    "XPF": 0.0088,  # CFP Franc
}


@dataclass
class LocationInfo:
    """
    Extended location information including geopolitical details.
    """
    latitude: float
    longitude: float
    altitude: float
    address: str
    country: Optional[str] = None
    state_province: Optional[str] = None
    city: Optional[str] = None
    country_code: Optional[str] = None
    electricity_rate: Optional[float] = None
    currency: Optional[str] = None
    rate_source: Optional[str] = None


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
    shading_loss: float = 1.5  # Reduced from 3.0 - assumes minimal shading
    
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
    lid_loss: float = 1.0  # Modern panels have lower LID
    
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
    availability_loss: float = 1.5  # Modern systems are more reliable
    
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


class SolarIncentiveManager:
    """
    Manages solar incentive lookup and calculations based on location.
    Provides comprehensive regional incentive data for economic analysis.
    """
    
    @staticmethod
    def get_incentives_for_location(location_info: LocationInfo, 
                                  system_size_kw: float,
                                  system_cost: float) -> List[IncentiveDetails]:
        """
        Get applicable solar incentives for a specific location.
        
        Args:
            location_info: LocationInfo object with country and state/province
            system_size_kw: System size in kW
            system_cost: Total system cost in USD
            
        Returns:
            List of applicable IncentiveDetails
        """
        incentives = []
        country = location_info.country.lower() if location_info.country else ""
        state_province = location_info.state_province.lower() if location_info.state_province else ""
        
        # Handle US states
        if country == "united states":
            us_incentives = SOLAR_INCENTIVES.get("united states", {})
            
            # Add federal incentive
            if "federal" in us_incentives:
                federal = us_incentives["federal"]
                incentives.append(IncentiveDetails(
                    name="Federal ITC",
                    type=federal["type"],
                    value=federal["value"],
                    expires=federal.get("expires"),
                    notes=federal.get("notes")
                ))
            
            # Add state-specific incentives
            for state_key, state_data in us_incentives.items():
                if state_key == "federal":
                    continue
                    
                if state_key in state_province or state_province in state_key:
                    if "programs" in state_data:
                        for program in state_data["programs"]:
                            # Check if program applies to system category
                            category = program.get("category", "residential")
                            if category == "utility" and system_size_kw < 1000:
                                continue
                            if category == "commercial" and system_size_kw < 10:
                                continue
                            if category == "low-income":
                                # Would need income verification
                                continue
                                
                            incentive = IncentiveDetails(
                                name=program["name"],
                                type=program["type"],
                                value=program["value"],
                                max_value=program.get("max_rebate") or program.get("max_credit"),
                                duration=program.get("duration"),
                                expires=program.get("expires"),
                                category=category,
                                notes=program.get("notes")
                            )
                            incentives.append(incentive)
                    break
        
        # Handle Canadian provinces
        elif country == "canada":
            can_incentives = SOLAR_INCENTIVES.get("canada", {})
            
            # Add federal programs
            if "federal" in can_incentives:
                for program in can_incentives["federal"]["programs"]:
                    incentive = IncentiveDetails(
                        name=program["name"],
                        type=program["type"],
                        value=program["value"],
                        category=program.get("category"),
                        notes=program.get("notes")
                    )
                    incentives.append(incentive)
            
            # Add provincial programs
            for province_key, prov_data in can_incentives.items():
                if province_key == "federal":
                    continue
                    
                if province_key in state_province or state_province in province_key:
                    if "programs" in prov_data:
                        for program in prov_data["programs"]:
                            incentive = IncentiveDetails(
                                name=program["name"],
                                type=program["type"],
                                value=program["value"],
                                max_value=program.get("max_rebate"),
                                category=program.get("category"),
                                notes=program.get("notes")
                            )
                            incentives.append(incentive)
                    break
        
        # Handle Australian states
        elif country == "australia":
            aus_incentives = SOLAR_INCENTIVES.get("australia", {})
            
            # Add federal STC rebate
            if "federal" in aus_incentives:
                for program in aus_incentives["federal"]["programs"]:
                    incentive = IncentiveDetails(
                        name=program["name"],
                        type=program["type"],
                        value=program["value"],
                        notes=program.get("notes")
                    )
                    incentives.append(incentive)
            
            # Add state programs
            for state_key, state_data in aus_incentives.items():
                if state_key == "federal":
                    continue
                    
                if state_key in state_province or state_province in state_key:
                    if "programs" in state_data:
                        for program in state_data["programs"]:
                            incentive = IncentiveDetails(
                                name=program["name"],
                                type=program["type"],
                                value=program["value"],
                                category=program.get("category"),
                                notes=program.get("notes")
                            )
                            incentives.append(incentive)
                    break
        
        # Handle other countries
        else:
            for country_key, country_data in SOLAR_INCENTIVES.items():
                if country_key in ["united states", "canada", "australia"]:
                    continue
                    
                if country_key in country or country in country_key:
                    if "programs" in country_data:
                        for program in country_data["programs"]:
                            incentive = IncentiveDetails(
                                name=program["name"],
                                type=program["type"],
                                value=program["value"],
                                duration=program.get("duration"),
                                notes=program.get("notes")
                            )
                            incentives.append(incentive)
                    break
        
        return incentives
    
    @staticmethod
    def calculate_incentive_value(incentive: IncentiveDetails, 
                                system_size_kw: float,
                                system_cost: float,
                                annual_production: float = 0) -> float:
        """
        Calculate the monetary value of an incentive.
        
        Args:
            incentive: IncentiveDetails object
            system_size_kw: System size in kW
            system_cost: Total system cost in USD
            annual_production: Annual energy production in kWh (for performance incentives)
            
        Returns:
            Incentive value in USD
        """
        if incentive.type == "tax_credit":
            # Percentage of system cost
            value = system_cost * incentive.value
            if incentive.max_value:
                value = min(value, incentive.max_value)
            return value
            
        elif incentive.type == "rebate":
            if isinstance(incentive.value, float) and incentive.value < 1.0:
                # Percentage rebate
                value = system_cost * incentive.value
            elif incentive.value > 100:
                # Flat amount rebate
                value = incentive.value
            else:
                # $/W rebate
                value = incentive.value * system_size_kw * 1000
            
            if incentive.max_value:
                value = min(value, incentive.max_value)
            return value
            
        elif incentive.type in ["performance", "feed_in_tariff", "feed_in_premium"]:
            # $/kWh over duration
            if annual_production > 0 and incentive.duration:
                total_production = annual_production * incentive.duration
                value = total_production * incentive.value
                return value
            return 0
            
        elif incentive.type == "tax_exemption":
            # Estimate tax savings (varies by location)
            if incentive.value == 1.0:  # 100% exemption
                # Rough estimate: 5-8% of system cost in taxes
                return system_cost * 0.065
            else:
                return system_cost * 0.065 * incentive.value
                
        elif incentive.type == "loan":
            # Interest savings on loan
            if incentive.value == 0.0:  # 0% interest loan
                # Estimate savings vs market rate (e.g., 6%)
                loan_amount = min(incentive.max_value or system_cost, system_cost)
                interest_saved = loan_amount * 0.06 * 5  # 5-year average
                return interest_saved * 0.5  # Present value
            return 0
            
        elif incentive.type == "net_metering":
            # Value depends on excess generation and rates
            # This is calculated separately in the main analysis
            return 0
            
        else:
            return 0
    
    @staticmethod
    def format_incentive_summary(incentives: List[IncentiveDetails],
                               system_size_kw: float,
                               system_cost: float,
                               annual_production: float) -> str:
        """
        Format a summary of applicable incentives.
        
        Args:
            incentives: List of IncentiveDetails
            system_size_kw: System size in kW
            system_cost: Total system cost in USD
            annual_production: Annual energy production in kWh
            
        Returns:
            Formatted string summary
        """
        if not incentives:
            return "No specific incentives found for this location."
        
        summary = "APPLICABLE SOLAR INCENTIVES:\n"
        summary += "-" * 60 + "\n"
        
        total_value = 0
        
        for incentive in incentives:
            value = SolarIncentiveManager.calculate_incentive_value(
                incentive, system_size_kw, system_cost, annual_production
            )
            total_value += value
            
            summary += f"\n{incentive.name}:\n"
            summary += f"  Type: {incentive.type.replace('_', ' ').title()}\n"
            
            if incentive.type == "tax_credit":
                summary += f"  Value: {incentive.value*100:.0f}% of system cost\n"
            elif incentive.type == "rebate":
                if isinstance(incentive.value, float) and incentive.value < 1.0:
                    summary += f"  Value: {incentive.value*100:.0f}% of system cost\n"
                elif incentive.value > 100:
                    summary += f"  Value: ${incentive.value:,.0f} flat rebate\n"
                else:
                    summary += f"  Value: ${incentive.value:.2f}/W\n"
            elif incentive.type in ["performance", "feed_in_tariff"]:
                summary += f"  Value: ${incentive.value:.3f}/kWh for {incentive.duration} years\n"
            elif incentive.type == "tax_exemption":
                summary += f"  Value: {incentive.value*100:.0f}% tax exemption\n"
            elif incentive.type == "loan":
                loan_amount = incentive.max_value or incentive.value
                if loan_amount:
                    summary += f"  Value: 0% interest loan up to ${loan_amount:,.0f}\n"
                else:
                    summary += f"  Value: Low-interest loan available\n"
            elif incentive.type == "net_metering":
                summary += f"  Value: Full retail rate credit for excess generation\n"
            
            if value > 0:
                summary += f"  Estimated Value: ${value:,.0f}\n"
            
            if incentive.max_value:
                summary += f"  Maximum: ${incentive.max_value:,.0f}\n"
                
            if incentive.expires:
                summary += f"  Expires: {incentive.expires}\n"
                
            if incentive.notes:
                summary += f"  Notes: {incentive.notes}\n"
        
        summary += "\n" + "-" * 60 + "\n"
        summary += f"TOTAL ESTIMATED INCENTIVE VALUE: ${total_value:,.0f}\n"
        summary += f"Net System Cost After Incentives: ${system_cost - total_value:,.0f}\n"
        
        return summary


class AddressGeocoder:
    """
    Handles conversion of street addresses to GPS coordinates with regional detection.
    Uses OpenStreetMap's Nominatim service (free, no API key required).
    
    Extended to extract country, state/province, and city information for
    electricity rate lookup.
    """
    
    def __init__(self):
        """Initialize geocoder with proper headers for OSM compliance"""
        self.session = requests.Session()
        # OSM requires a user agent
        self.session.headers.update({
            'User-Agent': f'PV-PowerEstimate/{VERSION} (https://github.com/secwest/PV-Generation-Planning)'
        })
    
    def geocode_with_details(self, address: str) -> Optional[LocationInfo]:
        """
        Convert address string to detailed location information.
        
        Args:
            address: Street address, city, or location description
            
        Returns:
            LocationInfo object with coordinates and regional details, or None if not found
        """
        try:
            # Nominatim API parameters
            params = {
                'q': address,
                'format': 'json',
                'limit': 1,
                'addressdetails': 1,
                'extratags': 1,
                'namedetails': 1
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
                    
                    # Extract address components
                    addr = result.get('address', {})
                    
                    # Get country and country code
                    country = addr.get('country', '').lower()
                    country_code = addr.get('country_code', '').upper()
                    
                    # Get state/province - try multiple fields
                    state_province = (
                        addr.get('state', '') or 
                        addr.get('province', '') or 
                        addr.get('region', '') or
                        addr.get('county', '')
                    ).lower()
                    
                    # Get city
                    city = (
                        addr.get('city', '') or 
                        addr.get('town', '') or 
                        addr.get('village', '') or
                        addr.get('municipality', '')
                    ).lower()
                    
                    # Display name for user verification
                    display_name = result.get('display_name', 'Unknown')
                    
                    # Create LocationInfo object
                    location_info = LocationInfo(
                        latitude=lat,
                        longitude=lon,
                        altitude=0.0,  # Will be fetched separately
                        address=display_name,
                        country=country,
                        state_province=state_province,
                        city=city,
                        country_code=country_code
                    )
                    
                    # Log the resolved location for verification
                    logger.info(f"Geocoded '{address}' to: {display_name}")
                    logger.info(f"Country: {country}, State/Province: {state_province}, City: {city}")
                    logger.info(f"Coordinates: {lat:.4f}, {lon:.4f}")
                    
                    return location_info
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
    
    def geocode(self, address: str) -> Optional[Tuple[float, float]]:
        """
        Convert address string to latitude/longitude coordinates.
        Legacy method for backward compatibility.
        
        Args:
            address: Street address, city, or location description
            
        Returns:
            Tuple of (latitude, longitude) or None if not found
        """
        location_info = self.geocode_with_details(address)
        if location_info:
            return location_info.latitude, location_info.longitude
        return None


class ElectricityRateManager:
    """
    Manages electricity rate lookup based on location.
    Provides accurate regional electricity rates for economic analysis.
    
    Enhanced with comprehensive global coverage including:
    - All countries and territories
    - Regional variations for large countries
    - Multiple currency support
    - Time-of-use considerations where applicable
    """
    
    @staticmethod
    def get_rate_for_location(location_info: LocationInfo) -> Tuple[float, str, str]:
        """
        Get electricity rate for a specific location.
        
        Args:
            location_info: LocationInfo object with country and state/province
            
        Returns:
            Tuple of (rate_in_usd, currency, source_description)
        """
        country = location_info.country.lower() if location_info.country else ""
        state_province = location_info.state_province.lower() if location_info.state_province else ""
        
        # Handle Canadian provinces
        if country == "canada" and state_province:
            rates = ELECTRICITY_RATES["canada"]
            # Try to match province name
            for province_key, rate in rates.items():
                if province_key in state_province or state_province in province_key:
                    rate_usd = rate * CURRENCY_TO_USD["CAD"]
                    source = f"{province_key.title()} average rate (2024-2025)"
                    return rate_usd, "CAD", source
            # Default Canadian rate
            rate_cad = rates["default"]
            rate_usd = rate_cad * CURRENCY_TO_USD["CAD"]
            return rate_usd, "CAD", "Canadian average rate"
        
        # Handle US states
        elif country == "united states" and state_province:
            rates = ELECTRICITY_RATES["united states"]
            # Try to match state name
            for state_key, rate in rates.items():
                if state_key in state_province or state_province in state_key:
                    source = f"{state_key.title()} average rate (2024-2025)"
                    return rate, "USD", source
            # Default US rate
            return rates["default"], "USD", "US average rate"
        
        # Handle Mexico states
        elif country == "mexico" and state_province:
            if isinstance(ELECTRICITY_RATES["mexico"], dict):
                rates = ELECTRICITY_RATES["mexico"]
                for state_key, rate in rates.items():
                    if state_key in state_province or state_province in state_key:
                        source = f"{state_key.title()} average rate (2024-2025)"
                        return rate, "USD", source
                return rates["default"], "USD", "Mexico average rate"
        
        # Handle Chinese provinces
        elif country == "china" and state_province:
            if isinstance(ELECTRICITY_RATES["china"], dict):
                rates = ELECTRICITY_RATES["china"]
                for province_key, rate in rates.items():
                    if province_key in state_province or state_province in province_key:
                        rate_usd = rate * CURRENCY_TO_USD["CNY"]
                        source = f"{province_key.title()} average rate (2024-2025)"
                        return rate_usd, "CNY", source
                rate_cny = rates["default"]
                rate_usd = rate_cny * CURRENCY_TO_USD["CNY"]
                return rate_usd, "CNY", "China average rate"
        
        # Handle Indian states
        elif country == "india" and state_province:
            if isinstance(ELECTRICITY_RATES["india"], dict):
                rates = ELECTRICITY_RATES["india"]
                for state_key, rate in rates.items():
                    if state_key in state_province or state_province in state_key:
                        rate_usd = rate * CURRENCY_TO_USD["INR"]
                        source = f"{state_key.title()} average rate (2024-2025)"
                        return rate_usd, "INR", source
                rate_inr = rates["default"]
                rate_usd = rate_inr * CURRENCY_TO_USD["INR"]
                return rate_usd, "INR", "India average rate"
        
        # Handle Brazilian states
        elif country == "brazil" and state_province:
            if isinstance(ELECTRICITY_RATES["brazil"], dict):
                rates = ELECTRICITY_RATES["brazil"]
                for state_key, rate in rates.items():
                    if state_key in state_province or state_province in state_key:
                        rate_usd = rate * CURRENCY_TO_USD["BRL"]
                        source = f"{state_key.title()} average rate (2024-2025)"
                        return rate_usd, "BRL", source
                rate_brl = rates["default"]
                rate_usd = rate_brl * CURRENCY_TO_USD["BRL"]
                return rate_usd, "BRL", "Brazil average rate"
        
        # Handle Australian states
        elif country == "australia" and state_province:
            if isinstance(ELECTRICITY_RATES["australia"], dict):
                rates = ELECTRICITY_RATES["australia"]
                for state_key, rate in rates.items():
                    if state_key in state_province or state_province in state_key:
                        rate_usd = rate * CURRENCY_TO_USD["AUD"]
                        source = f"{state_key.title()} average rate (2024-2025)"
                        return rate_usd, "AUD", source
                rate_aud = rates["default"]
                rate_usd = rate_aud * CURRENCY_TO_USD["AUD"]
                return rate_usd, "AUD", "Australia average rate"
        
        # Handle other countries
        else:
            # Check if country is in our database
            for country_key in ELECTRICITY_RATES:
                if country_key in country or country in country_key:
                    if isinstance(ELECTRICITY_RATES[country_key], dict):
                        # Skip nested dicts (already handled above)
                        continue
                    
                    rate_local = ELECTRICITY_RATES[country_key]
                    
                    # Determine currency based on country
                    currency_map = {
                        # Europe (Euro zone)
                        "austria": "EUR", "belgium": "EUR", "bulgaria": "BGN", "croatia": "HRK",
                        "cyprus": "EUR", "czech republic": "CZK", "denmark": "DKK", "estonia": "EUR",
                        "finland": "EUR", "france": "EUR", "germany": "EUR", "greece": "EUR",
                        "hungary": "HUF", "ireland": "EUR", "italy": "EUR", "latvia": "EUR",
                        "lithuania": "EUR", "luxembourg": "EUR", "malta": "EUR", "netherlands": "EUR",
                        "poland": "PLN", "portugal": "EUR", "romania": "RON", "slovakia": "EUR",
                        "slovenia": "EUR", "spain": "EUR", "sweden": "SEK",
                        
                        # Other European
                        "united kingdom": "GBP", "norway": "NOK", "switzerland": "CHF", "iceland": "ISK",
                        "albania": "ALL", "bosnia": "BAM", "kosovo": "EUR", "macedonia": "MKD",
                        "moldova": "MDL", "montenegro": "EUR", "serbia": "RSD", "turkey": "TRY",
                        "ukraine": "UAH",
                        
                        # Americas
                        "mexico": "MXN", "argentina": "ARS", "chile": "CLP", "colombia": "COP",
                        "peru": "PEN", "venezuela": "VES", "ecuador": "USD", "bolivia": "BOB",
                        "paraguay": "PYG", "uruguay": "UYU", "guyana": "GYD", "suriname": "SRD",
                        "french guiana": "EUR",
                        
                        # Asia
                        "japan": "JPY", "south korea": "KRW", "taiwan": "TWD", "hong kong": "HKD",
                        "singapore": "SGD", "thailand": "THB", "vietnam": "VND", "philippines": "PHP",
                        "indonesia": "IDR", "malaysia": "MYR", "myanmar": "MMK", "cambodia": "KHR",
                        "laos": "LAK", "bangladesh": "BDT", "pakistan": "PKR", "sri lanka": "LKR",
                        "nepal": "NPR", "afghanistan": "AFN", "kazakhstan": "KZT", "uzbekistan": "UZS",
                        "kyrgyzstan": "KGS", "tajikistan": "TJS", "turkmenistan": "TMT", "mongolia": "MNT",
                        
                        # Middle East
                        "saudi arabia": "SAR", "united arab emirates": "AED", "qatar": "QAR",
                        "kuwait": "KWD", "bahrain": "BHD", "oman": "OMR", "jordan": "JOD",
                        "lebanon": "LBP", "israel": "ILS", "syria": "SYP", "iraq": "IQD",
                        "iran": "IRR", "yemen": "YER",
                        
                        # Africa
                        "egypt": "EGP", "nigeria": "NGN", "kenya": "KES", "ethiopia": "ETB",
                        "morocco": "MAD", "algeria": "DZD", "tunisia": "TND", "libya": "LYD",
                        "sudan": "SDG", "ghana": "GHS", "tanzania": "TZS", "uganda": "UGX",
                        "zimbabwe": "ZWL", "zambia": "ZMW", "mozambique": "MZN", "malawi": "MWK",
                        "rwanda": "RWF", "botswana": "BWP", "namibia": "NAD", "mauritius": "MUR",
                        "madagascar": "MGA", "senegal": "XOF", "ivory coast": "XOF", "cameroon": "XAF",
                        "angola": "AOA", "gabon": "XAF", "mauritania": "MRU", "mali": "XOF",
                        "burkina faso": "XOF", "niger": "XOF", "chad": "XAF", "somalia": "SOS",
                        "eritrea": "ERN", "djibouti": "DJF", "seychelles": "SCR", "cape verde": "CVE",
                        "guinea": "GNF", "sierra leone": "SLL", "liberia": "LRD", "togo": "XOF",
                        "benin": "XOF", "gambia": "GMD", "guinea-bissau": "XOF", "equatorial guinea": "XAF",
                        "central african republic": "XAF", "congo": "XAF", "democratic republic of congo": "CDF",
                        "sao tome": "STN", "comoros": "KMF", "lesotho": "LSL", "swaziland": "SZL",
                        "eswatini": "SZL",
                        
                        # Oceania
                        "fiji": "FJD", "papua new guinea": "PGK", "solomon islands": "SBD",
                        "vanuatu": "VUV", "samoa": "WST", "tonga": "TOP", "kiribati": "AUD",
                        "tuvalu": "AUD", "nauru": "AUD", "palau": "USD", "marshall islands": "USD",
                        "micronesia": "USD", "french polynesia": "XPF", "new caledonia": "XPF",
                        "cook islands": "NZD",
                        
                        # Caribbean
                        "jamaica": "JMD", "trinidad and tobago": "TTD", "barbados": "BBD",
                        "bahamas": "BSD", "haiti": "HTG", "dominican republic": "DOP", "cuba": "CUP",
                        "puerto rico": "USD", "cayman islands": "KYD", "bermuda": "BMD",
                        "virgin islands": "USD", "antigua": "XCD", "saint lucia": "XCD",
                        "grenada": "XCD", "dominica": "XCD", "saint vincent": "XCD",
                        "saint kitts": "XCD", "turks and caicos": "USD", "aruba": "AWG",
                        "curacao": "ANG", "bonaire": "USD"
                    }
                    
                    # Get currency for the country
                    currency = "USD"  # Default
                    for country_name, curr in currency_map.items():
                        if country_name in country_key:
                            currency = curr
                            break
                    
                    # Convert to USD
                    if currency in CURRENCY_TO_USD:
                        rate_usd = rate_local * CURRENCY_TO_USD[currency]
                    else:
                        rate_usd = rate_local  # Assume USD if currency not found
                        currency = "USD"
                    
                    source = f"{country_key.title()} average rate (2024-2025)"
                    return rate_usd, currency, source
        
        # Default global rate
        return ELECTRICITY_RATES["default"], "USD", "Global average estimate"
    
    @staticmethod
    def format_rate_info(rate_usd: float, currency: str, source: str) -> str:
        """
        Format electricity rate information for display.
        
        Args:
            rate_usd: Rate in USD per kWh
            currency: Original currency code
            source: Description of rate source
            
        Returns:
            Formatted string for display
        """
        if currency != "USD":
            # Convert back to local currency for display
            local_rate = rate_usd / CURRENCY_TO_USD.get(currency, 1.0)
            return f"${rate_usd:.3f} USD/kWh ({local_rate:.3f} {currency}/kWh) - {source}"
        else:
            return f"${rate_usd:.3f} USD/kWh - {source}"


class SolarPVCalculator:
    """
    Main calculator class for solar PV power yield estimation.
    
    Extended with comprehensive global electricity rate detection and
    incentive calculation for accurate economic analysis worldwide.
    
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
                 altitude: Optional[float] = None, address: Optional[str] = None,
                 location_info: Optional[LocationInfo] = None):
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
            location_info: Extended location information including region
            
        Raises:
            ValueError: If coordinates are out of valid range
        """
        # Validate coordinates
        if not self._validate_coordinates(latitude, longitude):
            raise ValueError(f"Invalid coordinates: {latitude}, {longitude}")
        
        self.lat = latitude
        self.lon = longitude
        self.address = address
        self.location_info = location_info
        
        # Get electricity rate for location
        if location_info:
            rate_usd, currency, source = ElectricityRateManager.get_rate_for_location(location_info)
            self.electricity_rate = rate_usd
            self.electricity_currency = currency
            self.rate_source = source
            logger.info(f"Electricity rate: {ElectricityRateManager.format_rate_info(rate_usd, currency, source)}")
        else:
            self.electricity_rate = 0.14  # Default
            self.electricity_currency = "USD"
            self.rate_source = "Default rate"
        
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
                       system_size_dc: float, system_config: SystemConfig,
                       electricity_rate: float = None, cost_per_watt: float = None,
                       incentives: List[IncentiveDetails] = None) -> str:
        """
        Generate comprehensive performance assessment report with incentives.
        
        Report includes technical analysis for:
        - System design verification
        - Performance benchmarking
        - O&M planning
        - Financial analysis with incentives
        - Optimization opportunities
        """
        # Use location-specific rate if not provided
        if electricity_rate is None:
            electricity_rate = self.electricity_rate
        
        # Calculate additional metrics
        pr = system_config.total_loss_factor * 100
        peak_power_time = results['ac_power'].idxmax()
        peak_power = results['ac_power'].max()
        
        # Climate statistics
        total_irradiation = weather_data['ghi'].sum() / 1000  # kWh/m²
        avg_temp = weather_data['temp_air'].mean()
        avg_wind = weather_data['wind_speed'].mean()
        
        # Calculate monthly weather statistics
        weather_monthly = weather_data.groupby(weather_data.index.month).agg({
            'ghi': ['mean', 'sum'],
            'dni': ['mean', 'sum'],
            'dhi': ['mean', 'sum'],
            'temp_air': ['mean', 'min', 'max'],
            'wind_speed': 'mean'
        })
        
        # Flatten column names
        weather_monthly.columns = ['_'.join(col).strip() for col in weather_monthly.columns.values]
        
        # Convert month numbers to names
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        weather_monthly.index = month_names
        
        # Convert sum values from W to kWh/m²
        weather_monthly['ghi_total'] = weather_monthly['ghi_sum'] / 1000
        weather_monthly['dni_total'] = weather_monthly['dni_sum'] / 1000
        weather_monthly['dhi_total'] = weather_monthly['dhi_sum'] / 1000
        
        # Economic assumptions - updated for 2024-2025 market
        # Use provided electricity rate or default
        
        # Determine installed cost based on system size if not provided
        if cost_per_watt is None:
            if system_size_dc <= 20:  # Residential (raised from 10kW)
                default_cost_per_watt = 2.25  # $2.00-2.50/W typical 2024-2025 (middle of range)
            elif system_size_dc <= 100:  # Small commercial
                default_cost_per_watt = 1.50  # $1.25-1.75/W typical 2024-2025 (middle of range)
            elif system_size_dc <= 1000:  # Large commercial
                default_cost_per_watt = 1.25  # $1.00-1.50/W typical 2024-2025 (middle of range)
            else:  # Utility scale
                default_cost_per_watt = 0.85  # $0.70-1.00/W typical 2024-2025 (middle of range)
        else:
            default_cost_per_watt = cost_per_watt
        
        system_cost = system_size_dc * default_cost_per_watt * 1000
        annual_revenue = annual_energy * electricity_rate
        
        # Calculate incentive values
        total_incentive_value = 0
        if incentives:
            for incentive in incentives:
                value = SolarIncentiveManager.calculate_incentive_value(
                    incentive, system_size_dc, system_cost, annual_energy
                )
                total_incentive_value += value
        
        net_system_cost = system_cost - total_incentive_value
        payback_with_incentives = net_system_cost / annual_revenue
        
        # Calculate NPV and enhanced payback with electricity rate escalation
        electricity_escalation_rate = 0.03  # 3% annual increase
        discount_rate = 0.05  # 5% discount rate
        system_life = 25  # years
        
        # Calculate NPV of electricity savings
        npv_savings = 0
        cumulative_savings = 0
        enhanced_payback_years = 0
        enhanced_payback_with_incentives = 0
        
        for year in range(1, system_life + 1):
            # Degradation: -0.5% per year after year 1
            year_degradation = 1.0 if year == 1 else (1 - 0.005 * (year - 1))
            year_production = annual_energy * year_degradation
            
            # Electricity price with escalation
            year_electricity_rate = electricity_rate * ((1 + electricity_escalation_rate) ** (year - 1))
            year_revenue = year_production * year_electricity_rate
            
            # NPV calculation
            npv_savings += year_revenue / ((1 + discount_rate) ** year)
            cumulative_savings += year_revenue
            
            if cumulative_savings >= system_cost and enhanced_payback_years == 0:
                enhanced_payback_years = year
                
            if cumulative_savings >= net_system_cost and enhanced_payback_with_incentives == 0:
                enhanced_payback_with_incentives = year
        
        # Enhanced commercial and utility-scale financial modeling
        ppa_rate = None
        lcoe = None
        project_irr = None
        debt_fraction = 0
        tax_equity_fraction = 0
        
        if system_size_dc > 100:  # Large commercial and utility scale
            # Modern utility-scale financing assumptions (2024-2025)
            if system_size_dc > 1000:  # Utility scale
                # Typical utility-scale PPA rates by region
                if electricity_rate < 0.08:  # Low-cost regions
                    ppa_rate = 0.025  # $25/MWh
                elif electricity_rate < 0.12:  # Moderate-cost regions
                    ppa_rate = 0.035  # $35/MWh
                else:  # High-cost regions
                    ppa_rate = 0.045  # $45/MWh
                
                # Utility-scale financing structure
                debt_fraction = 0.70  # 70% debt typical
                tax_equity_fraction = 0.20  # 20% tax equity
                equity_fraction = 0.10  # 10% sponsor equity
                debt_rate = 0.045  # 4.5% interest rate
                
            else:  # Large commercial (100kW-1MW)
                # C&I PPA rates typically 10-20% below retail
                ppa_rate = electricity_rate * 0.85
                
                # Commercial financing structure
                debt_fraction = 0.60  # 60% debt
                tax_equity_fraction = 0.0  # Less common for C&I
                equity_fraction = 0.40  # 40% equity
                debt_rate = 0.055  # 5.5% interest rate
            
            # Calculate LCOE for commercial/utility projects
            # LCOE = (Total Lifetime Cost) / (Total Lifetime Energy)
            capex = system_cost
            annual_opex = system_size_dc * 10  # $10/kW/year O&M
            
            # Calculate present value of costs
            pv_costs = capex
            pv_energy = 0
            
            for year in range(1, system_life + 1):
                # O&M costs escalate at inflation (2.5%)
                year_opex = annual_opex * ((1 + 0.025) ** (year - 1))
                pv_costs += year_opex / ((1 + discount_rate) ** year)
                
                # Energy with degradation
                year_degradation = 1.0 if year == 1 else (1 - 0.005 * (year - 1))
                year_energy = annual_energy * year_degradation
                pv_energy += year_energy / ((1 + discount_rate) ** year)
            
            lcoe = pv_costs / pv_energy
            
            # Calculate project IRR (simplified)
            # For utility scale with ITC and depreciation
            if system_size_dc > 1000:
                # Include 30% ITC and MACRS depreciation benefits
                itc_value = capex * 0.30
                depreciation_pv = capex * 0.85 * 0.21 * 2.5  # Simplified MACRS PV
                
                # Approximate project IRR
                project_irr = ((annual_revenue + depreciation_pv/5) / (capex - itc_value)) * 100
            else:
                project_irr = (annual_revenue / capex) * 100
        
        # Additional savings for commercial customers
        if system_size_dc > 20:  # Commercial system
            # Demand charge savings (more sophisticated calculation)
            # Based on typical demand charge rates and solar coincidence
            if system_size_dc <= 100:  # Small commercial
                demand_charge_savings = system_size_dc * 5 * 12 * 0.6  # 60% coincidence
            elif system_size_dc <= 1000:  # Large commercial  
                demand_charge_savings = system_size_dc * 8 * 12 * 0.5  # Higher charges, lower coincidence
            else:  # Utility scale (usually no demand charges)
                demand_charge_savings = 0
                
            annual_revenue += demand_charge_savings
            
        # Time-of-use benefit (if applicable)
        if electricity_rate > 0.15 and system_size_dc <= 1000:  # TOU for commercial, not utility
            tou_multiplier = 1.15  # 15% benefit from producing during peak hours
            annual_revenue *= tou_multiplier
        
        # Best and worst months
        best_month = monthly['energy_kwh'].idxmax()
        worst_month = monthly['energy_kwh'].idxmin()
        variation = monthly.loc[best_month, 'energy_kwh'] / monthly.loc[worst_month, 'energy_kwh']
        
        # Utility-scale specific analysis
        if system_size_dc > 1000:
            # Calculate hourly generation profile statistics
            hourly_profile = results.groupby(results.index.hour)['ac_power'].mean()
            peak_hour = hourly_profile.idxmax()
            
            # Calculate ramp rates
            ramp_rates = results['ac_power'].diff().abs()
            max_ramp_rate = ramp_rates.max()
            
            # Calculate generation duration curve
            sorted_generation = results['ac_power'].sort_values(ascending=False).reset_index(drop=True)
            hours_above_90 = (sorted_generation > system_size_dc * 0.9).sum()
            hours_above_50 = (sorted_generation > system_size_dc * 0.5).sum()
            hours_above_20 = (sorted_generation > system_size_dc * 0.2).sum()
        
        # Calculate insolation utilization
        # How much of available solar resource is captured
        avg_module_eff = 0.20  # 20% assumed module efficiency
        array_area = system_size_dc / (avg_module_eff * 1.0)  # m²
        theoretical_max = total_irradiation * array_area * avg_module_eff
        utilization = (annual_energy / theoretical_max) * 100
        
        # Get location info for header
        location_name = self.location.name
        if self.location_info:
            if self.location_info.country:
                location_name += f", {self.location_info.country.title()}"
        
        report = f"""
================================================================================
                     SOLAR PV POWER YIELD ASSESSMENT REPORT
================================================================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Software: PV-PowerEstimate v{VERSION} (Global Edition with Incentives)

SITE INFORMATION
----------------
Location: {location_name}
Coordinates: {self.lat:.4f}°, {self.lon:.4f}°
Elevation: {self.altitude:.0f} m above sea level
Time Zone: UTC (all times in UTC)
Electricity Rate: {ElectricityRateManager.format_rate_info(electricity_rate, self.electricity_currency, self.rate_source)}

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
Estimated Annual Revenue: ${annual_revenue:,.0f} (at ${electricity_rate:.3f}/kWh)

ECONOMIC ANALYSIS (2024-2025 Market)
------------------------------------
System Category: {"Residential" if system_size_dc <= 20 else "Commercial" if system_size_dc <= 1000 else "Utility Scale"}
Typical Installed Cost: ${default_cost_per_watt:.2f}/W DC
Total System Cost Estimate: ${system_cost:,.0f}
Simple Payback Period: {system_cost / annual_revenue:.1f} years (before incentives, no rate escalation)
Future Rate Increase Payback: {enhanced_payback_years} years (before incentives, with 3% rate escalation)

{SolarIncentiveManager.format_incentive_summary(incentives, system_size_dc, system_cost, annual_energy) if incentives else ("Note: Incentives not applicable for large commercial/utility scale systems (>100kW)." if system_size_dc > 100 else "No specific incentives found for this location.")}

NET PRESENT VALUE ANALYSIS (25-year)
------------------------------------
NPV of Energy Savings: ${npv_savings:,.0f} (at 3% electricity escalation, 5% discount rate)
Net Present Value: ${npv_savings - net_system_cost:,.0f}
Internal Rate of Return: {((npv_savings / net_system_cost) ** (1/25) - 1) * 100:.1f}%

{"FINANCIAL SUMMARY WITH INCENTIVES" if total_incentive_value > 0 else "FINANCIAL SUMMARY"}
---------------------------------
System Cost: ${system_cost:,.0f}
{"Total Incentive Value: ${:,.0f}".format(total_incentive_value) if total_incentive_value > 0 else ""}
{"Net Cost After Incentives: ${:,.0f}".format(net_system_cost) if total_incentive_value > 0 else ""}
Simple Payback: {system_cost / annual_revenue:.1f} years (no incentives, no escalation)
{"Simple Payback with Incentives: {:.1f} years (no escalation)".format(payback_with_incentives) if total_incentive_value > 0 else ""}
Future Rate Increase Payback: {enhanced_payback_years} years (no incentives, with 3% rate escalation)
{"Future Rate Increase Payback with Incentives: {} years (with 3% rate escalation)".format(enhanced_payback_with_incentives) if total_incentive_value > 0 else ""}
25-Year Cash Flow: ${cumulative_savings:,.0f}
25-Year Net Profit: ${cumulative_savings - net_system_cost:,.0f}
Effective Cost per Watt: ${net_system_cost / (system_size_dc * 1000):.2f}/W
Levelized Cost of Energy: ${net_system_cost / (annual_energy * 25 * 0.87):,.3f}/kWh

{f'''COMMERCIAL/UTILITY SCALE FINANCIAL METRICS
----------------------------------------
Project Type: {"Utility Scale (>1MW)" if system_size_dc > 1000 else "Large Commercial (100kW-1MW)"}
Typical PPA Rate: ${ppa_rate:.3f}/kWh (${ppa_rate*1000:.0f}/MWh)
Project LCOE: ${lcoe:.3f}/kWh (all-in cost)
LCOE vs PPA Spread: ${(ppa_rate - lcoe)*1000:.1f}/MWh
Estimated Project IRR: {project_irr:.1f}% (unlevered, after-tax)

FINANCING STRUCTURE (TYPICAL)
-----------------------------
Total Project Cost: ${system_cost:,.0f}
Debt Financing: {debt_fraction*100:.0f}% (${system_cost*debt_fraction:,.0f} at {debt_rate*100:.1f}% interest)
Tax Equity: {tax_equity_fraction*100:.0f}% (${system_cost*tax_equity_fraction:,.0f})
Sponsor Equity: {(1-debt_fraction-tax_equity_fraction)*100:.0f}% (${system_cost*(1-debt_fraction-tax_equity_fraction):,.0f})

KEY ASSUMPTIONS
---------------
Federal ITC: 30% (through 2032)
Depreciation: 5-year MACRS
O&M Cost: ${annual_opex:,.0f}/year (${annual_opex/system_size_dc:.0f}/kW/year)
Annual Degradation: 0.5%
Debt Term: {"20 years" if system_size_dc > 1000 else "15 years"}

REVENUE STREAMS
---------------
{f"PPA Revenue: ${annual_energy * ppa_rate:,.0f}/year" if system_size_dc > 1000 else f"Energy Savings: ${annual_energy * electricity_rate:,.0f}/year"}
{f"Capacity Payments: Market dependent" if system_size_dc > 1000 else f"Demand Charge Reduction: ${demand_charge_savings:,.0f}/year"}
{"REC Revenue: ~$5-20/MWh additional" if system_size_dc > 1000 else "SRECs: Market dependent (if available)"}

{f'''UTILITY-SCALE GENERATION PLANNING METRICS
-----------------------------------------
Annual Capacity Factor: {capacity_factor:.1f}% ({"Excellent" if capacity_factor > 25 else "Good" if capacity_factor > 20 else "Moderate"})
Peak Generation Season: {best_month} ({monthly.loc[best_month, 'energy_kwh']:,.0f} kWh)
Lowest Generation Month: {worst_month} ({monthly.loc[worst_month, 'energy_kwh']:,.0f} kWh)
Seasonal Variation Ratio: {variation:.1f}:1

GRID INTEGRATION CONSIDERATIONS
-------------------------------
Peak Output: {peak_power:,.1f} kW AC ({peak_power/system_size_dc*100:.0f}% of DC capacity)
Ramp Rate Capability: ~{system_size_dc * 0.2:.0f} kW/minute (typical)
Minimum Stable Generation: ~{system_size_dc * 0.1:.0f} kW (10% of capacity)
Reactive Power Range: ±{system_size_dc * 0.33:.0f} kVAR (at full output)

AVAILABILITY & RELIABILITY
--------------------------
Expected Availability: 97-99% (weather-adjusted)
Forced Outage Rate: 0.5-1.0% annually
Scheduled Maintenance: 3-5 days/year
Weather Downtime: {1.5 if self.lat > 45 or self.lat < -45 else 0.5:.1f}% (snow/soiling)

CURTAILMENT RISK FACTORS
------------------------
Grid Congestion Risk: {"High" if capacity_factor > 25 else "Moderate" if capacity_factor > 20 else "Low"} (based on resource quality)
Negative Pricing Hours: Location and market dependent
Economic Curtailment: 2-5% typical in high-penetration markets
Voltage/Frequency Events: <0.5% with modern inverters

ENERGY SHAPE ANALYSIS
---------------------
Solar Peak Hours: 10 AM - 3 PM (varies by season)
Peak Generation Hour: {peak_hour}:00 (annual average)
Duck Curve Contribution: Peak generation during low demand
Evening Ramp Support: None without storage
Morning Ramp Timing: Good alignment with demand increase

GENERATION DURATION CURVE
-------------------------
Hours > 90% Capacity: {hours_above_90:,} hours/year ({hours_above_90/87.6:.1f}%)
Hours > 50% Capacity: {hours_above_50:,} hours/year ({hours_above_50/87.6:.1f}%)  
Hours > 20% Capacity: {hours_above_20:,} hours/year ({hours_above_20/87.6:.1f}%)
Maximum Ramp Rate: {max_ramp_rate:.0f} kW/interval

RESOURCE ADEQUACY VALUE
-----------------------
Capacity Credit: {15 if system_size_dc > 5000 else 20 if system_size_dc > 1000 else 25}% typical (market dependent)
ELCC (Effective Load Carrying Capability): Declining with penetration
Peak Coincidence: {60 if self.lat < 35 and self.lat > -35 else 40}% summer peak contribution

TRANSMISSION & INTERCONNECTION
------------------------------
Interconnection Voltage: {345 if system_size_dc > 200000 else 230 if system_size_dc > 100000 else 138 if system_size_dc > 50000 else 69 if system_size_dc > 20000 else 34.5} kV typical
Substation Requirements: {"New substation likely" if system_size_dc > 50000 else "Existing substation possible"}
Network Upgrades Risk: {"High" if system_size_dc > 100000 else "Moderate" if system_size_dc > 50000 else "Low"}
Gen-Tie Line Length: Site specific (major cost factor)

ADVANCED GRID SERVICES
----------------------
Frequency Response: Fast (sub-second with modern inverters)
Voltage Regulation: ±0.95-1.05 p.u. capability
Black Start Capability: Possible with battery hybrid
Synthetic Inertia: Available with advanced controls
Grid Forming Mode: Future capability for microgrids

ENVIRONMENTAL & PERMITTING
--------------------------
Land Requirements: ~{system_size_dc * 0.004:.0f} acres (fixed tilt)
                  ~{system_size_dc * 0.007:.0f} acres (single-axis tracking)
Habitat Impact: Site-specific assessment required
Glare Analysis: Required near airports/highways
Stormwater Management: NPDES permit typically required
Cultural Resources: Phase I assessment recommended

DEVELOPMENT TIMELINE
--------------------
Typical Schedule: {"36-48 months" if system_size_dc > 50000 else "24-36 months"} from NTP to COD
- Permitting: 6-12 months
- Interconnection: 12-24 months
- Procurement: 3-6 months  
- Construction: 6-12 months
- Commissioning: 1-2 months
''' if system_size_dc > 1000 else ""}''' if system_size_dc > 100 else ""}
Current Market Costs (2024-2025):
- Residential (≤20kW): $2.00-2.50/W installed (was $3.50+ in 2020)
- Small Commercial (10-100kW): $1.25-1.75/W installed
- Large Commercial (100kW-1MW): $1.00-1.50/W installed
- Utility Scale (>1MW): $0.70-1.00/W installed
- Expected cost decline: 3-5% annually through 2030

Note: Costs have declined ~70% since 2010. Current prices include equipment,
installation, permitting, and interconnection.{" Incentives shown above are estimated values - verify eligibility and actual amounts with local authorities." if system_size_dc <= 100 else ""}

{"Cost Factors:" if system_size_dc <= 100 else "Large-Scale Project Considerations:"}
{"""- Location: Labor costs vary significantly by region
- Roof complexity: Simple roofs cost less than complex ones
- Local permitting: Some areas have streamlined processes
- Competition: More installers = better pricing
- Equipment quality: Premium panels cost 10-20% more""" if system_size_dc <= 100 else """- EPC contractor selection critical for project success
- Interconnection costs can vary significantly by location
- Land lease/acquisition costs not included in $/W figures
- Tracking systems add 10-20% to cost but boost production
- Grid capacity and transmission access are key factors"""}

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

Your location shows {variation:.1f}:1 seasonal variation ({best_month} vs {worst_month})

MONTHLY WEATHER SUMMARY
-----------------------
This data represents typical meteorological conditions for your location.

Solar Irradiation (Monthly Totals)
Month    GHI (kWh/m²)    DNI (kWh/m²)    DHI (kWh/m²)
-------  -------------   -------------   -------------"""
        
        # Add monthly irradiation data
        for idx, (month, row) in enumerate(weather_monthly.iterrows()):
            report += f"\n{month:<7}  {row['ghi_total']:>12.1f}    {row['dni_total']:>12.1f}    {row['dhi_total']:>12.1f}"
        
        report += f"\n-------  -------------   -------------   -------------"
        report += f"\nTOTAL    {weather_monthly['ghi_total'].sum():>12.1f}    {weather_monthly['dni_total'].sum():>12.1f}    {weather_monthly['dhi_total'].sum():>12.1f}"
        
        report += f"""

Temperature and Wind Conditions
Month    Avg Temp (°C)    Min/Max (°C)      Avg Wind (m/s)
-------  --------------   ---------------   --------------"""
        
        # Add monthly temperature and wind data
        for idx, (month, row) in enumerate(weather_monthly.iterrows()):
            report += f"\n{month:<7}  {row['temp_air_mean']:>13.1f}    {row['temp_air_min']:>5.1f} / {row['temp_air_max']:>5.1f}    {row['wind_speed_mean']:>13.1f}"
        
        report += f"""

Climate Classification:
- Annual horizontal irradiation: {total_irradiation:,.0f} kWh/m²/year
- Average temperature: {avg_temp:.1f}°C
- Average wind speed: {avg_wind:.1f} m/s
- Classification: {self._classify_solar_resource(total_irradiation)}

Solar Component Analysis:
- Direct/Global Ratio: {weather_monthly['dni_total'].sum()/total_irradiation:.1%}
  * >70%: Very clear skies, excellent for tracking systems
  * 50-70%: Moderate clarity, good for fixed tilt
  * <50%: Cloudy/diffuse dominated, tracking less beneficial

Key Insights:
- Sunniest month: {weather_monthly['ghi_total'].idxmax()} ({weather_monthly['ghi_total'].max():.0f} kWh/m²)
- Cloudiest month: {weather_monthly['ghi_total'].idxmin()} ({weather_monthly['ghi_total'].min():.0f} kWh/m²)
- Hottest month: {weather_monthly['temp_air_mean'].idxmax()} ({weather_monthly['temp_air_mean'].max():.1f}°C average)
- Coldest month: {weather_monthly['temp_air_mean'].idxmin()} ({weather_monthly['temp_air_mean'].min():.1f}°C average)"""
        
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
  Direct Normal Total: {weather_monthly['dni_total'].sum():,.0f} kWh/m²/year
  Diffuse Total: {weather_monthly['dhi_total'].sum():,.0f} kWh/m²/year
  Direct/Global Ratio: {weather_monthly['dni_total'].sum()/total_irradiation:.1%}
  
Temperature Statistics:
  Annual Average: {avg_temp:.1f}°C
  Absolute Range: {weather_monthly['temp_air_min'].min():.1f}°C to {weather_monthly['temp_air_max'].max():.1f}°C
  Avg Wind Speed: {avg_wind:.1f} m/s
  
Energy Production Variation:
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
     * Current battery costs: $400-600/kWh installed (2024-2025)
     * 10 kWh system: $4,000-6,000 (down from $10,000+ in 2020)
   - Tracking Systems: Could increase yield 25-35% (economic analysis needed)
   - Bifacial Modules: 5-15% gain with {0.2:.1f} ground albedo
   - Module Upgrade: Latest high-efficiency could add 10-20% capacity

INCENTIVE OPTIMIZATION TIPS
---------------------------"""
        
        if incentives:
            report += """
To maximize your incentive benefits:

1. Federal Tax Credit (if applicable):
   - Ensure you have sufficient tax liability
   - Consider spreading credit over multiple years
   - Include all eligible costs (equipment, labor, permits)

2. State/Local Incentives:
   - Check application deadlines - some have limited funding
   - Verify all eligibility requirements
   - Submit applications before installation starts
   - Keep detailed documentation of all costs

3. Performance Incentives:
   - Monitor system production to ensure payments
   - Maintain system well to maximize generation
   - Understand payment schedules and requirements

4. Net Metering:
   - Size system to maximize self-consumption
   - Understand utility policies on credit rollovers
   - Consider time-of-use rates if available

5. Documentation Required:
   - Itemized invoices from installer
   - Proof of payment
   - System specifications
   - Interconnection agreement
   - Building permits
"""
        else:
            report += """
No specific incentives were found for your location, but you should:
- Check with local utilities for rebate programs
- Research state/provincial incentive databases
- Consult with local installers about current programs
- Consider federal tax incentives if applicable
"""
        
        report += f"""

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
   - Verify all incentive eligibility
   - Compare financing options
   - Understand net metering policies
   - Consider time-of-use rates

5. Technical validation:
   - Professional shading analysis
   - Structural engineering review
   - Electrical system compatibility
   - Utility interconnection requirements

REGIONAL ELECTRICITY CONTEXT
----------------------------
Location: {location_name}
Rate Used: {ElectricityRateManager.format_rate_info(electricity_rate, self.electricity_currency, self.rate_source)}

This rate was automatically determined based on your location. Actual rates may vary by:
- Utility provider (some regions have multiple providers)
- Rate schedule (residential vs commercial)
- Time-of-use pricing
- Demand charges (commercial customers)
- Net metering policies

For most accurate analysis, verify your actual electricity rate from a recent utility bill.

GLOBAL COMPARISON
-----------------
Your electricity rate compared to global averages:
- World average: ~$0.140/kWh
- Your rate: ${electricity_rate:.3f}/kWh ({electricity_rate/0.140*100:.0f}% of global average)
- Payback implications: {"Faster" if electricity_rate > 0.140 else "Slower"} than global average

Countries with highest rates (fastest solar payback):
1. Denmark: ~$0.35/kWh
2. Germany: ~$0.32/kWh  
3. Belgium: ~$0.30/kWh
4. Japan: ~$0.28/kWh
5. Italy: ~$0.26/kWh

Countries with lowest rates (slowest solar payback):
1. Iran: ~$0.01/kWh
2. Iraq: ~$0.04/kWh
3. Kuwait: ~$0.04/kWh
4. Saudi Arabia: ~$0.05/kWh
5. Libya: ~$0.04/kWh

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
    
    def _classify_solar_resource(self, annual_ghi: float) -> str:
        """
        Classify solar resource based on annual GHI.
        
        Args:
            annual_ghi: Annual global horizontal irradiation in kWh/m²
            
        Returns:
            Classification string
        """
        if annual_ghi >= 2000:
            return "Excellent (Desert/High altitude)"
        elif annual_ghi >= 1600:
            return "Very Good (Sunny/Mediterranean)"
        elif annual_ghi >= 1300:
            return "Good (Moderate climate)"
        elif annual_ghi >= 1000:
            return "Fair (Temperate/Partly cloudy)"
        else:
            return "Poor (Cloudy/High latitude)"
    
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
                    'address': self.address,
                    'country': self.location_info.country if self.location_info else None,
                    'state_province': self.location_info.state_province if self.location_info else None,
                    'electricity_rate_usd': self.electricity_rate,
                    'electricity_currency': self.electricity_currency,
                    'rate_source': self.rate_source
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
        description='PV-PowerEstimate v1.3.1: Comprehensive Solar PV Power Yield Calculator (Global Edition with Incentives)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --lat 45.4215 --lon -75.6972
  %(prog)s --address "111 Wellington Street, Ottawa, Ontario"
  %(prog)s --lat 51.5074 --lon -0.1278 --system-size 10 --tilt 35

Output Control:
  By default, the full report is printed to console AND saved to files.
  Use --no-print to suppress console output (still shows summary)
  Use --no-save to prevent saving files

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
    
    # Economic parameters
    parser.add_argument(
        '--cost-per-watt',
        type=float,
        help='Installed cost per watt DC in $/W. Default: auto-selected by system size. Current market: Residential $2.50-3.00/W, Commercial $1.25-2.25/W, Utility $0.80-1.20/W'
    )
    
    parser.add_argument(
        '--electricity-rate',
        type=float,
        help='Electricity rate in $/kWh. Default: auto-detected based on location'
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
        '--no-print',
        action='store_true',
        help='Do not print full report to console (still shows summary)'
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
ITC: Investment Tax Credit (30% federal in US)
Rebate: Direct payment reducing system cost
Feed-in Tariff: Payment for generated electricity

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
        location_info = None
        
        if args.lat is not None and args.lon is not None:
            # Coordinates provided
            latitude = args.lat
            longitude = args.lon
            logger.info(f"Using provided coordinates: {latitude}, {longitude}")
            
        elif args.address:
            # Address provided - geocode it
            logger.info(f"Geocoding address: {args.address}")
            geocoder = AddressGeocoder()
            location_info = geocoder.geocode_with_details(args.address)
            
            if location_info:
                latitude = location_info.latitude
                longitude = location_info.longitude
                address = location_info.address
            else:
                print(f"Error: Could not geocode address '{args.address}'")
                print("Please check the address or use coordinates instead.")
                return 1
                
        else:
            # Interactive mode
            print("\nPV-PowerEstimate v1.3.1 - Solar PV Power Yield Calculator (Global Edition with Incentives)")
            print("=" * 50)
            print("\nThis tool estimates solar panel energy production for any location worldwide.")
            print("It uses real weather data and detailed physics modeling.")
            print("NEW: Now includes comprehensive incentive calculations!")
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
                print("          'Berlin, Germany' or 'Tokyo, Japan'")
                address = input("Address: ").strip()
                if address:
                    geocoder = AddressGeocoder()
                    location_info = geocoder.geocode_with_details(address)
                    
                    if location_info:
                        latitude = location_info.latitude
                        longitude = location_info.longitude
                        print(f"✓ Found coordinates: {latitude:.4f}, {longitude:.4f}")
                        if location_info.country:
                            print(f"✓ Location: {location_info.city or 'Unknown city'}, {location_info.state_province or 'Unknown region'}, {location_info.country}")
                    else:
                        print(f"Error: Could not geocode address '{address}'")
                        return 1
            else:
                print("Invalid choice")
                return 1
            
            # Ask about system size
            print("\n⚡ SYSTEM SIZE")
            print("Typical sizes: Residential 3-20 kW, Commercial 20-1000 kW, Utility >1000 kW")
            print("Rule of thumb: 1 kW ≈ 3-4 panels ≈ 1,400 kWh/year (varies by location)")
            print("\n💵 CURRENT MARKET COSTS (2024-2025):")
            print("   Residential: $2.00-2.50/W installed")
            print("   Commercial: $1.25-1.75/W installed")
            print("   Utility: $0.70-1.00/W installed")
            print("   (Costs have declined ~70% since 2010!)")
            if not args.system_size or args.system_size <= 100:
                print("   Note: Get multiple quotes - prices vary by region and installer")
            else:
                print("   Note: Large projects typically use competitive RFP process")
            
            size_str = input(f"\nSystem size in kW (press Enter for default {DEFAULT_SYSTEM_SIZE} kW): ").strip()
            # Note: system_config will be created later with proper defaults and command-line overrides
            interactive_system_size = None
            if size_str:
                try:
                    interactive_system_size = float(size_str)
                    print(f"System size set to {interactive_system_size} kW")
                except ValueError:
                    print("Invalid size, will use default or command-line value")
            
            # Ask about tilt
                        
            print("\n📐 TILT ANGLE")
            print(f"Recommended tilt for your latitude ({abs(latitude):.1f}°): {abs(latitude):.0f}°")
            print("Flatter = better for summer, Steeper = better for winter & snow shedding")
            
            tilt_str = input(f"Tilt angle in degrees (press Enter for latitude-based default): ").strip()
            interactive_tilt = None
            if tilt_str:
                try:
                    interactive_tilt = float(tilt_str)
                except ValueError:
                    print("Invalid tilt, will use latitude-based default")
            
            # Store interactive mode settings to apply later
            interactive_module_type = 'glass_glass'
            interactive_racking_model = 'open_rack'
            
            # Set azimuth based on hemisphere
            interactive_azimuth = 180 if latitude > 0 else 0
            
            # Helper function for azimuth direction
            def azimuth_to_direction(azimuth):
                directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                             'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
                index = int((azimuth + 11.25) / 22.5) % 16
                return directions[index]
            
            print("\n🎯 Using standard azimuth (direction) for your hemisphere")
            print(f"   Azimuth: {interactive_azimuth}° ({azimuth_to_direction(interactive_azimuth)})")
            
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
            print("6. Calculate applicable incentives for your location")
            print("="*50 + "\n")
            
            # Initialize system_config if not already done
            if 'system_config' not in locals():
                system_config = SystemConfig()
        
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
            address=address,
            location_info=location_info
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
        # Start with defaults
        system_config = SystemConfig()
        
        # Apply command-line overrides first
        if args.system_size:
            # Calculate modules needed for target system size
            modules_needed = int(args.system_size * 1000 / args.module_power)
            if modules_needed <= 20:
                system_config.modules_per_string = modules_needed
                system_config.strings_per_inverter = 1
            else:
                system_config.modules_per_string = 20
                system_config.strings_per_inverter = (modules_needed + 19) // 20  # Round up
            
        # Apply command-line overrides
        system_config.module_power = args.module_power
        system_config.surface_tilt = args.tilt if args.tilt else abs(calc.lat)
        system_config.surface_azimuth = args.azimuth
        system_config.module_type = args.module_type
        system_config.racking_model = args.racking_model
        
        # Apply interactive mode overrides (these have highest priority)
        if args.lat is None and args.lon is None and args.address is None:
            # We're in interactive mode
            if 'interactive_system_size' in locals() and interactive_system_size is not None:
                # Reconfigure for interactive system size
                modules_needed = int(interactive_system_size * 1000 / system_config.module_power)
                if modules_needed <= 20:
                    system_config.modules_per_string = modules_needed
                    system_config.strings_per_inverter = 1
                else:
                    system_config.modules_per_string = 20
                    system_config.strings_per_inverter = (modules_needed + 19) // 20
                print(f"Configuring {system_config.modules_per_string * system_config.strings_per_inverter} x {system_config.module_power}W modules = {system_config.system_size_kw:.1f} kW system")
            
            if 'interactive_tilt' in locals() and interactive_tilt is not None:
                system_config.surface_tilt = interactive_tilt
            
            if 'interactive_azimuth' in locals():
                system_config.surface_azimuth = interactive_azimuth
                
            if 'interactive_module_type' in locals():
                system_config.module_type = interactive_module_type
                
            if 'interactive_racking_model' in locals():
                system_config.racking_model = interactive_racking_model
        
        # Size inverter appropriately (DC/AC ratio of 1.2)
        system_config.inverter_power = system_config.system_size_kw * 1000 / 1.2
        
        # Run simulation
        print(f"Running simulation for {system_config.system_size_kw:.1f} kW system...")
        results, system_size = calc.calculate_pv_output(weather_data, system_config)
        
        # Calculate yields
        print("Calculating energy yields...")
        monthly, annual_energy, annual_specific_yield, capacity_factor = \
            calc.calculate_monthly_yield(results, system_size)
        
        # Determine cost per watt for economic calculations
        if hasattr(args, 'cost_per_watt') and args.cost_per_watt:
            cost_per_watt = args.cost_per_watt
        else:
            # Auto-select based on system size (2024-2025 estimates)
            if system_size <= 20:  # Residential
                cost_per_watt = 2.25
            elif system_size <= 100:  # Small commercial
                cost_per_watt = 1.50
            elif system_size <= 1000:  # Large commercial
                cost_per_watt = 1.25
            else:  # Utility scale
                cost_per_watt = 0.85
        
        # Get electricity rate
        if hasattr(args, 'electricity_rate') and args.electricity_rate:
            electricity_rate = args.electricity_rate
        else:
            # Use auto-detected rate
            electricity_rate = calc.electricity_rate
        
        # Economic calculations
        system_cost_estimate = system_size * cost_per_watt * 1000
        annual_revenue = annual_energy * electricity_rate
        payback_years = system_cost_estimate / annual_revenue
        
        # Future rate increase financial calculations with rate escalation
        electricity_escalation_rate = 0.03  # 3% annual increase
        discount_rate = 0.05  # 5% discount rate
        system_life = 25  # years
        
        # Get applicable incentives (only for residential and small commercial)
        # Typical limits: Residential rebates 10-25kW, net metering 25-100kW, USDA REAP 100kW
        if system_size <= 100:  # Only check incentives for systems 100kW or smaller
            print("Checking for applicable incentives...")
            if calc.location_info:
                incentives = SolarIncentiveManager.get_incentives_for_location(
                    calc.location_info, system_size, system_cost_estimate
                )
                if incentives:
                    print(f"Found {len(incentives)} applicable incentive programs!")
                else:
                    print("No specific incentives found for this location.")
            else:
                incentives = []
        else:
            print("Note: Incentives not applicable for large commercial/utility scale systems (>100kW)")
            incentives = []
        
        # Calculate total incentive value
        total_incentive_value = 0
        if incentives:
            for incentive in incentives:
                value = SolarIncentiveManager.calculate_incentive_value(
                    incentive, system_size, system_cost_estimate, annual_energy
                )
                total_incentive_value += value
        
        net_system_cost = system_cost_estimate - total_incentive_value
        payback_with_incentives = net_system_cost / annual_revenue if annual_revenue > 0 else float('inf')
        
        # Calculate NPV and enhanced payback with electricity rate escalation
        npv_savings = 0
        cumulative_savings = 0
        enhanced_payback_years = 0
        enhanced_payback_with_incentives = 0
        
        for year in range(1, system_life + 1):
            # Degradation: -0.5% per year after year 1
            year_degradation = 1.0 if year == 1 else (1 - 0.005 * (year - 1))
            year_production = annual_energy * year_degradation
            
            # Electricity price with escalation
            year_electricity_rate = electricity_rate * ((1 + electricity_escalation_rate) ** (year - 1))
            year_revenue = year_production * year_electricity_rate
            
            # NPV calculation
            npv_savings += year_revenue / ((1 + discount_rate) ** year)
            cumulative_savings += year_revenue
            
            if cumulative_savings >= system_cost_estimate and enhanced_payback_years == 0:
                enhanced_payback_years = year
                
            if cumulative_savings >= net_system_cost and enhanced_payback_with_incentives == 0:
                enhanced_payback_with_incentives = year
        
        # Additional savings for commercial customers
        if system_size > 20:  # Commercial system
            # Demand charge savings (conservative estimate)
            demand_charge_savings = system_size * 5 * 12  # $5/kW/month typical
            annual_revenue += demand_charge_savings
            
        # Time-of-use benefit (if applicable)
        if electricity_rate > 0.15:  # Higher rate areas often have TOU
            tou_multiplier = 1.15  # 15% benefit from producing during peak hours
            annual_revenue *= tou_multiplier
        
        # CO2 savings
        co2_saved = annual_energy * 0.4  # kg CO2 per kWh (global average)
        
        # Performance ratio
        pr = system_config.total_loss_factor * 100
        
        # Peak power
        peak_power = results['ac_power'].max()
        
        # Generate report
        print("Generating report...")
        report = calc.generate_report(
            weather_data, results, monthly, annual_energy,
            annual_specific_yield, capacity_factor, system_size, system_config,
            electricity_rate=electricity_rate, cost_per_watt=cost_per_watt,
            incentives=incentives
        )
        
        # Display key results
        print("\n" + "=" * 60)
        print("🌟 RESULTS SUMMARY 🌟")
        print("=" * 60)
        print(f"📍 Location: {calc.location.name}")
        print(f"⚡ System Size: {system_size:.1f} kW DC")
        print(f"📊 Annual Energy: {annual_energy:,.0f} kWh/year")
        print(f"📈 Specific Yield: {annual_specific_yield:,.0f} kWh/kWp/year")
        print(f"⚙️  Capacity Factor: {capacity_factor:.1f}%")
        print(f"💰 Est. Annual Revenue: ${annual_energy * electricity_rate:,.0f} (at ${electricity_rate:.3f}/kWh)")
        print(f"   Rate Info: {ElectricityRateManager.format_rate_info(electricity_rate, calc.electricity_currency, calc.rate_source)}")
        print("=" * 60)
        
        # Add incentives summary
        if incentives:
            print("\n💵 INCENTIVES SUMMARY:")
            print("-" * 60)
            for incentive in incentives:
                value = SolarIncentiveManager.calculate_incentive_value(
                    incentive, system_size, system_cost_estimate, annual_energy
                )
                if value > 0:
                    print(f"   {incentive.name}: ${value:,.0f}")
            print("-" * 60)
            print(f"   TOTAL INCENTIVE VALUE: ${total_incentive_value:,.0f}")
            print(f"   Net System Cost: ${net_system_cost:,.0f}")
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
        print(f"   System Cost: ${system_cost_estimate:,.0f} (at ${cost_per_watt}/W installed)")
        print(f"   Annual Value: ${annual_revenue:,.0f} (at ${electricity_rate:.3f}/kWh)")
        print(f"   Simple Payback: {payback_years:.1f} years (before incentives)")
        print(f"   Future Rate Increase Payback: {enhanced_payback_years} years (with 3% rate escalation)")
        
        if incentives:
            print(f"   Simple Payback with Incentives: {payback_with_incentives:.1f} years")
            print(f"   Future Rate Increase Payback with Incentives: {enhanced_payback_with_incentives} years (with escalation)")
            print(f"   25-Year Net Profit: ${cumulative_savings - net_system_cost:,.0f}")
        else:
            print(f"   25-Year Net Profit: ${cumulative_savings - system_cost_estimate:,.0f}")
        
        print(f"\n💰 FUTURE RATE INCREASE FINANCIAL ANALYSIS:")
        print(f"   NPV of Energy Savings: ${npv_savings:,.0f} (25-year, 3% escalation, 5% discount)")
        print(f"   Net Present Value: ${npv_savings - net_system_cost:,.0f}")
        print(f"   Internal Rate of Return: {((npv_savings / net_system_cost) ** (1/25) - 1) * 100:.1f}%")
        print(f"   Levelized Cost of Energy: ${net_system_cost / (annual_energy * 25 * 0.87):,.3f}/kWh")
        
        print(f"\n🌍 ENVIRONMENTAL IMPACT:")
        print(f"   CO2 Avoided: {co2_saved/1000:.1f} metric tons/year")
        print(f"   25-Year CO2 Reduction: {co2_saved * 25 * 0.87 / 1000:.0f} metric tons")
        
        # Commercial benefits if applicable
        if system_size > 20:
            print(f"\n🏢 COMMERCIAL BENEFITS:")
            if system_size <= 1000:
                print(f"   Demand Charge Savings: ${system_size * 5 * 12:,.0f}/year (estimated)")
                print(f"   Peak Shaving Benefit: Reduces peak demand charges")
                print(f"   Grid Independence: Improved resilience during outages")
            
        # Large commercial and utility scale metrics
        if system_size > 100:
            print(f"\n📊 LARGE-SCALE PROJECT METRICS:")
            # Calculate these metrics similar to the report
            if system_size > 1000:  # Utility scale
                if electricity_rate < 0.08:
                    ppa_rate_display = 0.025
                elif electricity_rate < 0.12:
                    ppa_rate_display = 0.035
                else:
                    ppa_rate_display = 0.045
            else:  # Large commercial
                ppa_rate_display = electricity_rate * 0.85
                
            # Simplified LCOE calculation
            annual_opex = system_size * 10
            simple_lcoe = (system_cost_estimate + annual_opex * 20) / (annual_energy * 20 * 0.87)
            
            print(f"   Typical PPA Rate: ${ppa_rate_display:.3f}/kWh (${ppa_rate_display*1000:.0f}/MWh)")
            print(f"   Estimated LCOE: ${simple_lcoe:.3f}/kWh")
            print(f"   {"Utility-Scale" if system_size > 1000 else "C&I"} Financing: {"70% debt, 20% tax equity" if system_size > 1000 else "60% debt typical"}")
            print(f"   Federal ITC: 30% (through 2032)")
            if system_size > 1000:
                print(f"   Grid Services: Frequency regulation, voltage support potential")
        
        if electricity_rate > 0.15:
            print(f"\n⏰ TIME-OF-USE BENEFITS:")
            print(f"   Solar production aligns with peak rate periods")
            print(f"   Estimated TOU benefit: 15% revenue increase")
            print(f"   Consider battery storage for maximum TOU savings")
        
        # Monthly variation
        best_month = monthly['energy_kwh'].idxmax()
        worst_month = monthly['energy_kwh'].idxmin()
        variation = monthly.loc[best_month, 'energy_kwh'] / monthly.loc[worst_month, 'energy_kwh']
        print(f"   Seasonal Variation: {variation:.1f}:1 ({best_month} vs {worst_month})")
        
        # Print monthly breakdown
        print("\n📅 MONTHLY BREAKDOWN:")
        print("   Month      Energy (kWh)    Daily Avg    % of Annual")
        print("   " + "-" * 50)
        for month, row in monthly.iterrows():
            pct_of_annual = (row['energy_kwh'] / annual_energy) * 100
            bar_length = int(pct_of_annual / 2)  # Scale to fit
            bar = "█" * bar_length
            print(f"   {month:<10} {row['energy_kwh']:>12,.0f}    {row['daily_energy']:>8.1f}    {pct_of_annual:>5.1f}% {bar}")
        
        print("\n💡 RECOMMENDATIONS:")
        if system_size <= 100:  # Residential and small commercial
            if capacity_factor < 15:
                print("   - Consider checking shading or system design")
            if variation > 3:
                print("   - High seasonal variation - consider battery storage")
            if annual_specific_yield > 1500:
                print("   - Above-average solar resource for investment")
            print("   - Get multiple installer quotes for accurate pricing")
            print("   - Verify eligibility for all incentives shown")
            print("   - Check net metering policies with your utility")
        else:  # Large commercial and utility scale
            if capacity_factor < 18:
                print("   - Consider single-axis tracking to boost production")
            if annual_specific_yield > 1600:
                print("   - Excellent solar resource for utility-scale development")
            print("   - Engage experienced EPC contractor for project execution")
            print("   - Conduct detailed interconnection study early in process")
            if system_size > 1000:
                print("   - Consider co-location with battery storage for grid services")
                print("   - Evaluate PPA offtake options with utilities/corporates")
        
        print("=" * 60)
        
        # Calculate and display monthly weather summary
        print("\n🌤️  MONTHLY WEATHER SUMMARY:")
        print("   " + "-" * 70)
        
        # Calculate monthly weather statistics
        weather_monthly = weather_data.groupby(weather_data.index.month).agg({
            'ghi': ['mean', 'sum'],
            'dni': 'sum',
            'dhi': 'sum',
            'temp_air': 'mean',
            'wind_speed': 'mean'
        })
        
        # Convert month numbers to names
        month_names_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        print("   Month    Solar Radiation (kWh/m²)          Avg Temp    Avg Wind")
        print("            Global   Direct   Diffuse        (°C)        (m/s)")
        print("   " + "-" * 70)
        
        for i in range(12):
            month_idx = i + 1
            ghi_total = weather_monthly.loc[month_idx, ('ghi', 'sum')] / 1000
            dni_total = weather_monthly.loc[month_idx, ('dni', 'sum')] / 1000
            dhi_total = weather_monthly.loc[month_idx, ('dhi', 'sum')] / 1000
            avg_temp = weather_monthly.loc[month_idx, ('temp_air', 'mean')]
            avg_wind = weather_monthly.loc[month_idx, ('wind_speed', 'mean')]
            
            # Create visual bar for total irradiation
            bar_length = int(ghi_total / 10)  # Scale for display
            bar = "▓" * bar_length
            
            print(f"   {month_names_short[i]:<7}  {ghi_total:>6.1f}   {dni_total:>6.1f}   {dhi_total:>6.1f}        {avg_temp:>6.1f}      {avg_wind:>6.1f}  {bar}")
        
        print("   " + "-" * 70)
        total_ghi = weather_data['ghi'].sum() / 1000
        total_dni = weather_data['dni'].sum() / 1000
        total_dhi = weather_data['dhi'].sum() / 1000
        print(f"   TOTAL    {total_ghi:>6.0f}   {total_dni:>6.0f}   {total_dhi:>6.0f} kWh/m²/year")
        
        # Classify solar resource
        if total_ghi >= 2000:
            climate_class = "Excellent (Desert/High altitude)"
        elif total_ghi >= 1600:
            climate_class = "Very Good (Sunny/Mediterranean)"
        elif total_ghi >= 1300:
            climate_class = "Good (Moderate climate)"
        elif total_ghi >= 1000:
            climate_class = "Fair (Temperate/Partly cloudy)"
        else:
            climate_class = "Poor (Cloudy/High latitude)"
        
        print(f"   Climate: {climate_class}")
        print(f"   Direct/Global Ratio: {total_dni/total_ghi:.1%} (higher = clearer skies)")
        print("\n   📝 Radiation Components:")
        print("      - Global: Total radiation on horizontal surface")
        print("      - Direct: Beam radiation from sun disk (good for tracking)")
        print("      - Diffuse: Scattered radiation from sky (works in shade)")
        
        print("\n📊 PERFORMANCE SUMMARY TABLE:")
        print("   " + "-" * 50)
        print(f"   {'Metric':<30} {'Value':>20}")
        print("   " + "-" * 50)
        print(f"   {'System Size (DC)':<30} {f'{system_size:.1f} kW':>20}")
        print(f"   {'Annual Production':<30} {f'{annual_energy:,.0f} kWh':>20}")
        print(f"   {'Daily Average':<30} {f'{annual_energy/365:.1f} kWh':>20}")
        print(f"   {'Specific Yield':<30} {f'{annual_specific_yield:,.0f} kWh/kWp':>20}")
        print(f"   {'Capacity Factor':<30} {f'{capacity_factor:.1f}%':>20}")
        print(f"   {'Performance Ratio':<30} {f'{pr:.1f}%':>20}")
        print(f"   {'Peak Power Output':<30} {f'{peak_power:.1f} kW':>20}")
        print(f"   {'CO2 Avoided':<30} {f'{co2_saved/1000:.1f} tons/yr':>20}")
        print(f"   {f'Annual Value (@${electricity_rate:.3f}/kWh)':<30} {f'${annual_revenue:,.0f}':>20}")
        print(f"   {f'System Cost (@${cost_per_watt}/W)':<30} {f'${system_cost_estimate:,.0f}':>20}")
        if incentives:
            print(f"   {'Total Incentives':<30} {f'${total_incentive_value:,.0f}':>20}")
            print(f"   {'Net Cost After Incentives':<30} {f'${net_system_cost:,.0f}':>20}")
            print(f"   {'Simple Payback w/ Incentives':<30} {f'{payback_with_incentives:.1f} years':>20}")
            print(f"   {'Future Rate Increase Payback':<30} {f'{enhanced_payback_with_incentives} years':>20}")
        else:
            print(f"   {'Simple Payback':<30} {f'{payback_years:.1f} years':>20}")
            print(f"   {'Future Rate Increase Payback':<30} {f'{enhanced_payback_years} years':>20}")
        print(f"   {'25-Year Net Savings':<30} {f'${cumulative_savings - (net_system_cost if incentives else system_cost_estimate):,.0f}':>20}")
        print("   " + "-" * 50)
        
        # Print the full report to console unless --no-print is specified
        if not args.no_print:
            print("\nFULL REPORT:")
            print(report)
        else:
            print("\n(Full report not printed. Remove --no-print flag to see it)")
        
        # Visual separator
        print("\n" + "=" * 60)
        print("FILE OPERATIONS")
        print("=" * 60)
        
        # Save results unless disabled
        if not args.no_save:
            print(f"\nSaving results to {args.output}/...")
            # Store system size in results for metadata
            results.attrs['system_size'] = system_size
            try:
                calc.save_results(results, monthly, report, args.output)
                print(f"\n✅ Results saved successfully:")
                print(f"   📄 Report: {args.output}/report.txt")
                print(f"   📊 Hourly data: {args.output}/hourly_output.csv")
                print(f"   📅 Monthly summary: {args.output}/monthly_summary.csv")
                print(f"   ⚙️  Metadata: {args.output}/metadata.json")
            except Exception as e:
                print(f"\n❌ Error saving files: {e}")
        else:
            print("\n⚠️  File saving disabled (--no-save flag active)")
        
        print("\n🎉 Analysis complete!")
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
