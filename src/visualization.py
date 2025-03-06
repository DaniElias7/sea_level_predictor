import os 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def setup_plot() -> tuple[plt.Figure, plt.Axes]:
    """Set the matplotlib figure and axes."""
    fig, ax = plt.subplots(figsize=(12, 6))
    return fig, ax

def plot_historical_data(ax: plt.Axes, data: pd.DataFrame) -> None:
    """Plot historical data as points."""
    ax.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='#2c3e50', alpha=0.6, label='Datos históricos')

def add_projection_line(ax: plt.Axes, years: np.ndarray, levels: np.ndarray, color: str, label: str) -> None:
    """Adds a projection line to the chart."""
    ax.plot(years, levels, color=color, linewidth=2.5, label=label)

def finalize_plot(fig: plt.Figure, ax: plt.Axes) -> None:
    """Aplica formato final y guarda el gráfico."""
    # Crear directorio si no existe
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)  # Crea la carpeta automáticamente
    
    output_path = os.path.join(output_dir, 'sea_level_projections.png')  # Ruta compatible con OS
    ax.set_xlabel('Año', fontsize=12, labelpad=10)
    ax.set_ylabel('Nivel del Mar (pulgadas)', fontsize=12, labelpad=10)
    ax.set_title('Proyección del Nivel del Mar hasta 2050', fontsize=14, pad=20)
    ax.legend(frameon=True, loc='upper left')
    ax.grid(True, linestyle='--', alpha=0.4)
    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)