import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import pvlib
from pvlib import pvsystem, modelchain, location
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
import json
import time

class SolarPVCalculator:
    """
    Solar PV Power Yield Calculator with Comprehensive Physics Modeling
    
    Core Physics Equation:
    P = G × A × η × PR
    
    Where:
    - P = Power output (W)
    - G = Solar irradiance on panel plane (W/m²)
    - A = Total array area (m²)
    - η = Module efficiency at current conditions
    - PR = Performance ratio (product of all loss factors)
    
    This implementation models all major physical processes affecting PV output.
    """
    
    def __init__(self, latitude, longitude, altitude=None):
        """
        Initialize calculator with location coordinates
        
        The location determines:
        1. Solar geometry (sun paths, angles)
        2. Air mass (atmospheric thickness)
        3. Typical weather patterns (via TMY data)
        
        Parameters:
        -----------
        latitude : float (-90 to 90)
        longitude : float (-180 to 180)
        altitude : float, optional (meters above sea level)
            - Affects air density and irradiance
            - Higher altitude = less atmosphere = more irradiance
            - Roughly +0.7% irradiance per 1000m elevation
        """
        self.lat = latitude
        self.lon = longitude
        # Altitude affects: 1) Air mass calculation 2) Temperature 3) Irradiance intensity
        self.altitude = altitude if altitude else self.get_elevation()
        self.location = location.Location(latitude, longitude, altitude=self.altitude)
        
    def get_elevation(self):
        """
        Fetch elevation data from open-elevation API
        
        Elevation impacts:
        - Direct irradiance (less atmospheric attenuation)
        - Temperature (typically -6.5°C per 1000m)
        - Air density (affects convective cooling)
        """
        url = "https://api.open-elevation.com/api/v1/lookup"
        params = {'locations': f'{self.lat},{self.lon}'}
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data['results'][0]['elevation']
        except:
            pass
        return 0  # Default to sea level if API fails
    
    def fetch_pvgis_data(self, year=None):
        """
        Fetch TMY (Typical Meteorological Year) data from PVGIS
        
        TMY Data Construction:
        - Selects most "typical" months from 10-20 year dataset
        - Preserves long-term averages while maintaining realistic sequences
        - Includes: GHI, DNI, DHI, temperature, wind speed
        
        Irradiance Components:
        1. GHI (Global Horizontal Irradiance) = DNI × cos(θz) + DHI
           - Total radiation on horizontal surface
           - θz = solar zenith angle
        
        2. DNI (Direct Normal Irradiance)
           - Beam radiation from sun disk
           - Varies with air mass: DNI = DNI₀ × exp(-τ × AM)
           - τ = atmospheric optical depth
        
        3. DHI (Diffuse Horizontal Irradiance)
           - Scattered radiation from sky dome
           - Includes Rayleigh scattering (molecules) + Mie scattering (aerosols)
        """
        base_url = "https://re.jrc.ec.europa.eu/api/v5_2/"
        
        # PVGIS uses satellite data (SARAH, NSRDB, or CMSAF depending on location)
        endpoint = "tmy"
        params = {
            'lat': self.lat,
            'lon': self.lon,
            'outputformat': 'json',
            'browser': 1
        }
        
        url = f"{base_url}{endpoint}"
        
        try:
            response = requests.get(url, params=params, timeout=30)
            if response.status_code == 200:
                data = response.json()
                
                # Extract hourly data
                tmy_data = data['outputs']['tmy_hourly']
                
                # Create DataFrame
                df = pd.DataFrame(tmy_data)
                
                # Parse time - PVGIS uses "MM/DD HH:MM" format
                current_year = datetime.now().year if year is None else year
                df['datetime'] = pd.to_datetime(
                    df['time(UTC)'].apply(lambda x: f"{current_year}/{x}"),
                    format='%Y/%m/%d %H:%M'
                )
                df.set_index('datetime', inplace=True)
                
                # Rename columns to pvlib conventions
                # Each parameter represents hourly averages
                df = df.rename(columns={
                    'G(h)': 'ghi',  # W/m² on horizontal plane
                    'Gb(n)': 'dni',  # W/m² normal to sun
                    'Gd(h)': 'dhi',  # W/m² diffuse on horizontal
                    'T2m': 'temp_air',  # °C at 2m height
                    'WS10m': 'wind_speed'  # m/s at 10m height
                })
                
                return df[['ghi', 'dni', 'dhi', 'temp_air', 'wind_speed']]
            else:
                print(f"PVGIS API error: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching PVGIS data: {e}")
            return None
    
    def fetch_nrel_psm3_data(self, year=2020, api_key=None):
        """
        Fetch data from NREL PSM3 (Physical Solar Model v3)
        
        PSM3 Advantages:
        - 4km spatial resolution
        - 30-minute temporal resolution available
        - Includes aerosol optical depth, precipitable water
        - Better snow cover modeling
        
        Register at: https://developer.nrel.gov/signup/
        """
        if not api_key:
            print("NREL API requires a free key from https://developer.nrel.gov/signup/")
            return None
            
        base_url = 'https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-tmy-download.csv'
        
        params = {
            'api_key': api_key,
            'lat': self.lat,
            'lon': self.lon,
            'attributes': 'ghi,dhi,dni,wind_speed,air_temperature',
            'names': 'tmy',
            'utc': 'true',
            'leap_day': 'false',
            'interval': '60',
            'full_name': 'PV Calculator',
            'email': 'test@example.com'
        }
        
        try:
            response = requests.get(base_url, params=params, timeout=30)
            if response.status_code == 200:
                # NREL returns CSV data
                from io import StringIO
                df = pd.read_csv(StringIO(response.text), skiprows=2)
                
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
                
                return df[['ghi', 'dni', 'dhi', 'temp_air', 'wind_speed']]
            else:
                print(f"NREL API error: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching NREL data: {e}")
            return None
    
    def calculate_pv_output(self, weather_data, system_config=None):
        """
        Calculate PV system output using detailed physical models
        
        Process Overview:
        1. Solar Position → determines angle of incidence (AOI)
        2. Irradiance Transposition → GHI/DNI/DHI to plane-of-array (POA)
        3. Temperature Calculation → cell temp from ambient + irradiance
        4. Power Calculation → accounts for temp, irradiance, and losses
        
        Parameters:
        -----------
        weather_data : DataFrame with hourly weather data
        system_config : dict with system design parameters
        """
        
        # Default system configuration with theoretical basis for each parameter
        if system_config is None:
            system_config = {
                # TILT ANGLE OPTIMIZATION:
                # - Latitude tilt maximizes annual yield
                # - Latitude - 15° favors summer
                # - Latitude + 15° favors winter
                'surface_tilt': self.lat,
                
                # AZIMUTH ANGLE:
                # 180° = South (Northern hemisphere), 0° = North (Southern hemisphere)
                # East (90°) favors morning, West (270°) favors afternoon
                'surface_azimuth': 180,
                
                # MODULE SPECIFICATIONS (typical for 60-cell polycrystalline)
                'module_parameters': {
                    'pdc0': 250,  # Nameplate DC power at STC (1000 W/m², 25°C, AM1.5)
                    'v_mp': 30.5,  # Maximum power voltage - decreases with temperature
                    'i_mp': 8.2,   # Maximum power current - increases with irradiance
                    'v_oc': 37.8,  # Open circuit voltage - temperature sensitive
                    'i_sc': 8.7,   # Short circuit current - proportional to irradiance
                    
                    # TEMPERATURE COEFFICIENTS (typical silicon)
                    'alpha_sc': 0.0045,  # Isc temp coefficient (A/°C) ~+0.05%/°C
                    'beta_oc': -0.11,    # Voc temp coefficient (V/°C) ~-0.3%/°C
                    'gamma_pdc': -0.0041,  # Power temp coefficient (%/°C) ~-0.4%/°C
                    # Power loss: ΔP/P = γ × (T_cell - 25°C)
                    
                    'cells_in_series': 60,  # Determines voltage levels
                    'temp_ref': 25.0  # STC reference temperature
                },
                
                # INVERTER EFFICIENCY MODEL
                # η_inv = η_ref × (P_dc/P_dc0) / (η_nom + (P_dc/P_dc0) × (1 - η_nom))
                'inverter_parameters': {
                    'pdc0': 250,  # DC power for peak efficiency
                    'eta_inv_nom': 0.96,  # Nominal efficiency (typically at 50% load)
                    'eta_inv_ref': 0.9637  # Reference efficiency
                },
                
                # ARRAY CONFIGURATION
                'modules_per_string': 20,  # Determines DC voltage (20 × 37.8V = 756V)
                'strings_per_inverter': 2,  # Parallel strings for current
                
                # THERMAL MODEL SELECTION
                # 'open_rack': Good airflow, lower temperatures
                # 'roof_mount': Restricted airflow, higher temperatures (+2-5°C)
                'racking_model': 'open_rack',
                
                # LOSS FACTORS (industry typical values with physics basis)
                'losses': {
                    # SOILING: Dust/dirt accumulation
                    # Depends on: rainfall, tilt angle, local pollution
                    # Typical: 2-5% (cleaned quarterly)
                    'soiling': 2,
                    
                    # SHADING: Near and far obstructions
                    # Non-linear due to bypass diodes
                    # Requires 3D scene analysis for accuracy
                    'shading': 3,
                    
                    # SNOW: Coverage probability × loss when covered
                    # f(tilt angle, temperature patterns)
                    'snow': 0,
                    
                    # MISMATCH: I-V curve variations between modules
                    # Statistical: ~2% for ±3% power tolerance
                    'mismatch': 2,
                    
                    # DC WIRING: I²R losses
                    # P_loss = I² × R × L / A_conductor
                    'wiring': 2,
                    
                    # CONNECTIONS: Contact resistance
                    'connections': 0.5,
                    
                    # LID: Light-Induced Degradation (first year)
                    # Boron-oxygen defects in p-type silicon
                    'lid': 1.5,
                    
                    # NAMEPLATE: Actual vs rated power
                    'nameplate_rating': 1,
                    
                    # AGE: Long-term degradation
                    # Typical: 0.5-0.8% per year
                    'age': 0,
                    
                    # AVAILABILITY: Downtime for maintenance/faults
                    'availability': 3
                }
            }
        
        # Create PV system object with physical parameters
        module = pvsystem.PVSystem(
            surface_tilt=system_config['surface_tilt'],
            surface_azimuth=system_config['surface_azimuth'],
            module_parameters=system_config['module_parameters'],
            inverter_parameters=system_config['inverter_parameters'],
            modules_per_string=system_config['modules_per_string'],
            strings_per_inverter=system_config['strings_per_inverter'],
            racking_model=system_config['racking_model']
        )
        
        # TEMPERATURE MODEL (Sandia Array Performance Model)
        # T_cell = T_ambient + ΔT
        # ΔT = G_POA × exp(a + b × wind_speed)
        # Where a, b are empirically derived for mounting type
        temp_model_params = TEMPERATURE_MODEL_PARAMETERS['sapm'][system_config['racking_model']]
        
        # Create ModelChain - links all the physics models
        mc = modelchain.ModelChain(
            module, 
            self.location,
            
            # AOI Model: Accounts for reflection losses at glass surface
            # Fresnel equations → reflection increases at high angles
            # 'physical' uses n=1.526 for glass, includes AR coating effects
            aoi_model='physical',
            
            # Spectral Model: Wavelength effects on quantum efficiency
            # Air mass affects spectrum (more red at sunrise/sunset)
            # 'first_solar' or 'sapm' for spectral corrections
            spectral_model='no_loss',  # Simplified for general modules
            
            # Temperature Model: Cell temp from ambient conditions
            temperature_model='sapm',
            temperature_model_parameters=temp_model_params
        )
        
        # RUN THE SIMULATION
        # This executes the following steps for each timestamp:
        # 1. Solar position (zenith, azimuth) via SPA algorithm
        # 2. Air mass = 1/cos(zenith) × pressure correction
        # 3. POA irradiance via transposition model (Perez/Hay-Davies)
        # 4. AOI correction for reflection
        # 5. Cell temperature from SAPM thermal model
        # 6. DC power from single diode model or SAPM
        # 7. AC power from inverter efficiency curve
        mc.run_model(weather_data)
        
        # Calculate total system size for yield metrics
        system_size_dc = (system_config['module_parameters']['pdc0'] * 
                         system_config['modules_per_string'] * 
                         system_config['strings_per_inverter'] / 1000)  # kW
        
        # APPLY ADDITIONAL LOSS FACTORS
        # These are not modeled by pvlib and represent system-level effects
        # Total PR = Π(1 - loss_i/100) for all loss factors
        total_loss_factor = 1.0
        for loss_type, loss_pct in system_config['losses'].items():
            total_loss_factor *= (1 - loss_pct/100)
        
        # Compile results with all intermediate values for analysis
        results = pd.DataFrame({
            'dc_power': mc.results.dc / 1000,  # kW before inverter
            'ac_power': mc.results.ac / 1000 * total_loss_factor,  # kW after all losses
            'cell_temperature': mc.results.cell_temperature,  # °C
            'effective_irradiance': mc.results.effective_irradiance,  # W/m² on cells
            'total_loss_factor': total_loss_factor  # Combined PR
        })
        
        return results, system_size_dc
    
    def calculate_monthly_yield(self, results, system_size_dc):
        """
        Calculate energy production metrics
        
        Key Metrics:
        1. Energy (kWh) = Power (kW) × Time (h)
        2. Specific Yield = Energy / System Size (kWh/kWp)
           - Normalizes for system size
           - Typical: 1000-2000 kWh/kWp depending on location
        
        3. Capacity Factor = Actual Energy / (Nameplate × Hours) × 100%
           - Typical: 15-25% for fixed systems
           - Represents average utilization
        
        4. Performance Ratio = Actual / Theoretical under STC
           - Accounts for all real-world losses
           - Good systems: 75-85%
        """
        # Energy = Power × Time (1 hour intervals)
        results['energy_kwh'] = results['ac_power']
        
        # Monthly aggregation
        monthly = results.groupby(results.index.month).agg({
            'energy_kwh': 'sum',  # Total energy
            'ac_power': 'mean',   # Average power
            'cell_temperature': 'mean',  # Average temperature
            'effective_irradiance': 'mean'  # Average irradiance
        })
        
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly.index = month_names
        
        # Specific yield normalizes by system size
        monthly['specific_yield'] = monthly['energy_kwh'] / system_size_dc
        
        # Annual metrics
        annual_energy = results['energy_kwh'].sum()
        annual_specific_yield = annual_energy / system_size_dc
        
        # Capacity factor: actual vs nameplate continuous operation
        capacity_factor = annual_energy / (system_size_dc * 8760) * 100
        
        return monthly, annual_energy, annual_specific_yield, capacity_factor
    
    def generate_report(self, weather_data, results, monthly, annual_energy, 
                       annual_specific_yield, capacity_factor, system_size_dc):
        """
        Generate comprehensive performance report
        
        Report includes all key metrics for:
        - System sizing decisions
        - Financial analysis (kWh × electricity rate)
        - Performance benchmarking
        - O&M planning (cleaning schedules based on soiling)
        """
        
        report = f"""
SOLAR PV YIELD ASSESSMENT REPORT
================================
Location: {self.lat:.4f}°, {self.lon:.4f}°
Altitude: {self.altitude:.0f} m
System Size: {system_size_dc:.1f} kWp

ANNUAL PERFORMANCE SUMMARY
--------------------------
Total Energy Production: {annual_energy:,.0f} kWh
Specific Yield: {annual_specific_yield:,.0f} kWh/kWp
Capacity Factor: {capacity_factor:.1f}%
Performance Ratio: {results['total_loss_factor'].iloc[0]:.1%}

MONTHLY BREAKDOWN
-----------------
"""
        
        # Monthly details showing seasonal variation
        for month, row in monthly.iterrows():
            report += f"{month}: {row['energy_kwh']:>6,.0f} kWh ({row['specific_yield']:>4.0f} kWh/kWp)\n"
        
        # Climate summary affecting performance
        report += f"""
CLIMATE CONDITIONS
------------------
Annual Solar Radiation: {weather_data['ghi'].sum():,.0f} kWh/m²
Average Temperature: {weather_data['temp_air'].mean():.1f}°C
Average Wind Speed: {weather_data['wind_speed'].mean():.1f} m/s

PEAK PERFORMANCE
----------------
Maximum Power: {results['ac_power'].max():,.1f} kW
Occurred: {results['ac_power'].idxmax().strftime('%Y-%m-%d %H:%M')}

DESIGN CONSIDERATIONS
---------------------
- Tilt angle optimization could yield ±3-5% annually
- East/West orientations reduce output by 15-20%
- Tracking systems could increase yield by 25-35%
- Bifacial modules could add 5-15% with high albedo
- Degradation: expect ~0.5-0.7% annual decrease
"""
        
        return report


# Example usage demonstrating the complete workflow
def main():
    """
    Complete example showing data fetch, simulation, and analysis
    
    Workflow:
    1. Initialize with location
    2. Fetch TMY weather data
    3. Configure PV system
    4. Run physics simulation
    5. Calculate yields
    6. Generate report
    """
    # Example coordinates (San Francisco, CA)
    latitude = 37.7749
    longitude = -122.4194
    
    print("Initializing Solar PV Calculator...")
    calc = SolarPVCalculator(latitude, longitude)
    
    print(f"Location: {latitude:.4f}°, {longitude:.4f}°")
    print(f"Elevation: {calc.altitude:.0f} m\n")
    
    # Fetch weather data (TMY represents long-term average)
    print("Fetching solar resource data from PVGIS...")
    weather_data = calc.fetch_pvgis_data()
    
    if weather_data is None:
        print("Failed to fetch weather data. Check internet connection.")
        return
    
    print(f"Retrieved {len(weather_data)} hours of TMY data\n")
    
    # Custom system configuration
    # This example: residential rooftop with premium modules
    system_config = {
        'surface_tilt': 30,  # Typical residential roof
        'surface_azimuth': 180,  # South facing
        
        # High-efficiency monocrystalline silicon
        'module_parameters': {
            'pdc0': 400,  # Modern 400W panels
            'v_mp': 41.0,
            'i_mp': 9.76,
            'v_oc': 49.2,
            'i_sc': 10.3,
            'alpha_sc': 0.0045,
            'beta_oc': -0.11,
            'gamma_pdc': -0.0035,  # Better temp coefficient
            'cells_in_series': 72,  # Half-cut cells (144 half-cells)
            'temp_ref': 25.0
        },
        
        # String inverter sized for array
        'inverter_parameters': {
            'pdc0': 8000,  # 8kW inverter
            'eta_inv_nom': 0.97,  # High-efficiency model
            'eta_inv_ref': 0.9637
        },
        
        'modules_per_string': 20,
        'strings_per_inverter': 1,
        'racking_model': 'open_rack',  # Good ventilation
        
        # Realistic loss assumptions
        'losses': {
            'soiling': 2,  # Quarterly cleaning
            'shading': 1,  # Minimal shading
            'snow': 0,  # No snow in SF
            'mismatch': 2,
            'wiring': 1.5,
            'connections': 0.5,
            'lid': 1.5,  # First year
            'nameplate_rating': 1,
            'age': 0,  # New system
            'availability': 2  # 98% uptime
        }
    }
    
    # Run simulation with hourly timesteps
    print("Running PV simulation...")
    results, system_size_dc = calc.calculate_pv_output(weather_data, system_config)
    
    # Calculate monthly and annual yields
    monthly, annual_energy, annual_specific_yield, capacity_factor = \
        calc.calculate_monthly_yield(results, system_size_dc)
    
    # Generate comprehensive report
    report = calc.generate_report(weather_data, results, monthly, annual_energy,
                                 annual_specific_yield, capacity_factor, system_size_dc)
    
    print(report)
    
    # Optional: Save for detailed analysis
    # results.to_csv('pv_hourly_output.csv')
    # monthly.to_csv('pv_monthly_summary.csv')
    
    return results, monthly


if __name__ == "__main__":
    # Execute the complete workflow
    results, monthly = main()
    
    # Alternative: Use NREL data for USA locations
    # Provides higher resolution and spectral data
    # calc = SolarPVCalculator(latitude, longitude)
    # weather_data = calc.fetch_nrel_psm3_data(api_key='YOUR_API_KEY')
    
    # For advanced analysis:
    # - Export hourly data for load matching studies
    # - Integrate with battery storage models
    # - Perform financial analysis with time-of-use rates
    # - Monte Carlo simulation for uncertainty bounds
