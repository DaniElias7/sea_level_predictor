from data_handling import load_data
from calculations import calculate_regression, generate_projection
from visualization import setup_plot, plot_historical_data, add_projection_line, finalize_plot

def run_analysis():
    # Carga de datos
    df = load_data()
    
    # Configuración del gráfico
    fig, ax = setup_plot()
    plot_historical_data(ax, df)
    
    # Regresión 1880-2013
    slope_full, intercept_full = calculate_regression(df)
    years_full, levels_full = generate_projection(slope_full, intercept_full, 1880)
    add_projection_line(ax, years_full, levels_full, '#e74c3c', 'Tendencia completa (1880-2013)')
    
    # Regresión 2000-2013
    slope_recent, intercept_recent = calculate_regression(df, 2000, 2013)
    years_recent, levels_recent = generate_projection(slope_recent, intercept_recent, 2000)
    add_projection_line(ax, years_recent, levels_recent, '#27ae60', 'Tendencia reciente (2000-2013)')
    
    # Guardar resultados
    finalize_plot(fig, ax)

if __name__ == '__main__':
    run_analysis()