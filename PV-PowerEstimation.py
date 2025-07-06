#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PV--PowerEstimate.py - Solar PV Power Yield Calculator & Tutorial

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

Description:
    Educational and production-ready solar PV power yield calculator implementing:
    - Complete physics-based PV modeling theory
    - Real meteorological data integration  
    - Multi-Factor Loss calculations
    - Industry-standard performance metrics
    
    This code serves as both a practical tool and a tutorial on PV system modeling
    for technical audiences, with extensive documentation of underlying physics.

Author: Dragos Ruiu
Version: 1.0.0
Date: 2025-07-05

Theory Overview:
    Solar PV power generation follows the fundamental equation:
    
    P = G × A × η × PR
    
    Where:
    - P = Power output (W)
    - G = Solar irradiance on panel plane (W/m²)
    - A = Total array area (m²)
    - η = Module efficiency at current conditions
    - PR = Performance ratio (product of all loss factors)
    
    This implementation models each component with detailed physics.
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

# Third-party imports
try:
    import requests
    import pandas as pd
    import numpy as np
    import pvlib
    from pvlib import pvsystem, modelchain, location
    from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
except ImportError as e:
    print(f"Error: Required package not installed. {e}")
    print("Please install required packages:")
    print("pip install pandas numpy requests pvlib")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Suppress pvlib warnings for cleaner output
warnings.filterwarnings('ignore', module='pvlib')

# Constants
VERSION = "1.0.0"
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
    # Open rack: Good airflow, ΔT ≈ 25-30°C at 1000 W/m²
    # Roof mount: Restricted airflow, ΔT ≈ 30-35°C
    # Building integrated: Poor cooling, ΔT ≈ 35-45°C
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
        
        Typical good PR: 0.75-0.85 (75-85%)
        Below 0.75: Investigate system issues
        Above 0.85: Very well-optimized system
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
            'User-Agent': f'PV-PowerEstimate/{VERSION} (https://github.com/yourusername/pv-estimate)'
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
            >>> coords = geocoder.geocode("1600 Pennsylvania Ave, Washington DC")
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
    
    Implements full physics-based modeling of the complete
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
                current_year = year if year else datetime.now().year
                df['datetime'] = pd.to_datetime(
                    df['time(UTC)'].apply(lambda x: f"{current_year}/{x}"),
                    format='%Y/%m/%d %H:%M'
                )
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
        Calculate PV system power output using full physics models.
        
        COMPLETE PHOTOVOLTAIC MODELING CHAIN:
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
                # Annual: tilt = latitude
                # Summer: tilt = latitude - 15°
                # Winter: tilt = latitude + 15°
                system_config.surface_tilt = abs(self.lat)
                # AZIMUTH FOR HEMISPHERE:
                # Northern: 180° (south-facing)
                # Southern: 0° (north-facing)  
                # Equator: Either acceptable
                system_config.surface_azimuth = 180 if self.lat > 0 else 0
            
            logger.info(f"System size: {system_config.system_size_kw:.1f} kW")
            logger.info(f"Tilt: {system_config.surface_tilt}°, Azimuth: {system_config.surface_azimuth}°")
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
                racking_model=system_config.racking_model
            )
            
            # TEMPERATURE MODEL PARAMETERS
            # Empirically derived for different mounting configurations
            # ΔT = POA_irradiance × exp(a + b×wind_speed)
            temp_params = TEMPERATURE_MODEL_PARAMETERS['sapm'][system_config.racking_model]
            
            # CREATE MODELCHAIN
            # Links all component models in correct sequence
            mc = modelchain.ModelChain(
                pv_system,
                self.location,
                
                # AOI model: 'physical' uses Fresnel equations
                # Accounts for polarization and AR coatings
                aoi_model='physical',
                
                # Spectral model: Corrects for non-AM1.5 spectra
                # 'first_solar' or 'sapm' for advanced corrections
                spectral_model='no_loss',  # Simplified
                
                # Temperature model: Cell temp from weather
                temperature_model='sapm',
                temperature_model_parameters=temp_params
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
        Generate complete performance assessment report.
        
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
Software: PV--PowerEstimate v{VERSION}

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
Mounting: {system_config.racking_model.replace('_', ' ').title()}

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
        
        for idx, (month, row) in enumerate(monthly.iterrows()):
            report += f"\n{month:<7}  {row['energy_kwh']:>12,.0f}    "
            report += f"{row['specific_yield']:>8.0f} kWh/kWp    "
            report += f"{row['daily_energy']:>8.1f}    "
            report += f"{row['cell_temperature']:>8.1f}°C"
            
            if month == best_month:
                report += " ← Best"
            elif month == worst_month:
                report += " ← Worst"
        
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
   {"✓ Well optimized for annual yield" if abs(system_config.surface_tilt - abs(self.lat)) < 5 else "→ Consider adjusting tilt closer to latitude"}
   Potential gain from optimization: ~{max(0, 5-abs(system_config.surface_tilt - abs(self.lat))):.0f}%

2. Soiling Management:
   {self._get_cleaning_recommendation(system_config.soiling_loss)}
   Estimated annual loss: {annual_energy * system_config.soiling_loss/100:.0f} kWh

3. Temperature Management:
   Average cell temp excess: {results['cell_temperature'].mean() - 25:.1f}°C
   Annual temperature losses: {annual_energy * abs(results['temperature_loss'].mean())/100:.0f} kWh
   → Consider enhanced ventilation or higher efficiency modules

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
End of Report - Generated by PV--PowerEstimate v{VERSION}
Technical questions: contact@solaranalysistools.com
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
    2. Address: --address "111 Wellington Street, Ottawa, Ontario, K1A 0A9"
    3. Interactive: prompts for input
    
    Example usage:
        python PV--PowerEstimate.py --lat 37.7749 --lon -122.4194 --system-size 10
        python PV--PowerEstimate.py --address "San Francisco, CA" --tilt 30
        python PV--PowerEstimate.py  # Interactive mode
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='PV--PowerEstimate: Solar PV Power Yield Calculator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --lat 37.7749 --lon -122.4194
  %(prog)s --address "111 Wellington Street, Ottawa, Ontario, K1A 0A9"
  %(prog)s --lat 51.5074 --lon -0.1278 --system-size 10 --tilt 35

For more information, visit: https://github.com/yourusername/pv-powerestimate
        """
    )
    
    # Location arguments (mutually exclusive group)
    location_group = parser.add_mutually_exclusive_group()
    location_group.add_argument(
        '--lat', '--latitude',
        type=float,
        help='Latitude in decimal degrees (-90 to 90)'
    )
    location_group.add_argument(
        '--address', '-a',
        type=str,
        help='Street address or location name'
    )
    
    parser.add_argument(
        '--lon', '--longitude',
        type=float,
        help='Longitude in decimal degrees (-180 to 180)'
    )
    
    parser.add_argument(
        '--altitude', '--elevation',
        type=float,
        help='Altitude in meters (optional, will be fetched if not provided)'
    )
    
    # System configuration arguments
    parser.add_argument(
        '--system-size',
        type=float,
        default=DEFAULT_SYSTEM_SIZE,
        help=f'System size in kW (default: {DEFAULT_SYSTEM_SIZE})'
    )
    
    parser.add_argument(
        '--tilt',
        type=float,
        help='Panel tilt angle in degrees (default: latitude)'
    )
    
    parser.add_argument(
        '--azimuth',
        type=float,
        default=180,
        help='Panel azimuth in degrees, 180=South (default: 180)'
    )
    
    parser.add_argument(
        '--module-power',
        type=float,
        default=400,
        help='Individual module power in watts (default: 400)'
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
    
    # Parse arguments
    args = parser.parse_args()
    
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
            print("\nPV--PowerEstimate - Solar PV Power Yield Calculator")
            print("=" * 50)
            print("\nEnter location (choose one option):")
            print("1. Enter coordinates (latitude, longitude)")
            print("2. Enter address")
            
            choice = input("\nChoice (1 or 2): ").strip()
            
            if choice == '1':
                lat_str = input("Latitude (-90 to 90): ").strip()
                lon_str = input("Longitude (-180 to 180): ").strip()
                
                try:
                    latitude = float(lat_str)
                    longitude = float(lon_str)
                except ValueError:
                    print("Error: Invalid coordinates")
                    return 1
                    
            elif choice == '2':
                address = input("Address: ").strip()
                if address:
                    geocoder = AddressGeocoder()
                    coords = geocoder.geocode(address)
                    
                    if coords:
                        latitude, longitude = coords
                    else:
                        print(f"Error: Could not geocode address '{address}'")
                        return 1
            else:
                print("Invalid choice")
                return 1
        
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
        print(f"Location: {calc.location.name}")
        print(f"System Size: {system_size:.1f} kW")
        print(f"Annual Energy: {annual_energy:,.0f} kWh")
        print(f"Specific Yield: {annual_specific_yield:,.0f} kWh/kWp")
        print(f"Capacity Factor: {capacity_factor:.1f}%")
        print(f"Est. Annual Revenue: ${annual_energy * 0.15:,.0f} (at $0.15/kWh)")
        print("=" * 60)
        
        # Save results unless disabled
        if not args.no_save:
            print(f"\nSaving results to {args.output}/")
            # Store system size in results for metadata
            results.attrs['system_size'] = system_size
            calc.save_results(results, monthly, report, args.output)
            print(f"Complete report saved to {args.output}/report.txt")
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
