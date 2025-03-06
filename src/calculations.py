import numpy as np
from scipy.stats import linregress
import pandas as pd

def calculate_regression(data: pd.DataFrame, start_year: int = None, end_year: int = None) -> tuple[float, float]:
    """Calculate slope and intercept for a range of years."""
    if start_year and end_year:
        data = data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    return slope, intercept

def generate_projection(slope: float, intercept: float, start_year: int, end_year: int = 2050) -> tuple[np.ndarray, np.ndarray]:
    """Generates annual projections until 2050."""
    years = np.arange(start_year, end_year + 1)
    levels = slope * years + intercept
    return years, levels