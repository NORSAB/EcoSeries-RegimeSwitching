"""
Paleta de colores oficial para la tesis — Familia NORD
https://nordtheme.com

Todos los scripts de generación de gráficos deben importar
este módulo para garantizar consistencia visual.
"""

# ================================================================
#   PALETA NORD — Colores Hexadecimales
# ================================================================

# --- Polar Night (oscuros) ---
NORD_0  = "#2E3440"   # Fondo oscuro / texto principal
NORD_1  = "#3B4252"   # Fondo secundario
NORD_2  = "#434C5E"   # Bordes medios
NORD_3  = "#4C566A"   # Bordes, texto secundario

# --- Snow Storm (claros) ---
NORD_4  = "#D8DEE9"   # Texto suave sobre fondo oscuro
NORD_5  = "#E5E9F0"   # Fondos intermedios
NORD_6  = "#ECEFF4"   # Fondos de bloques / cajas

# --- Frost (azules) ---
NORD_7  = "#8FBCBB"   # Frost 1 — verde-azulado
NORD_8  = "#88C0D0"   # Frost 2 — azul claro
NORD_9  = "#81A1C1"   # Frost 3 — azul medio
NORD_10 = "#5E81AC"   # Frost 4 — azul principal (acentos)

# --- Aurora (semáforo) ---
NORD_11 = "#BF616A"   # Rojo  — régimen de caída / error
NORD_12 = "#D08770"   # Naranja — transición / advertencia
NORD_13 = "#EBCB8B"   # Amarillo — régimen moderado
NORD_14 = "#A3BE8C"   # Verde — régimen estable / éxito
NORD_15 = "#B48EAD"   # Púrpura — extensión / SSRC


# ================================================================
#   MAPEO A CONCEPTOS DE LA TESIS
# ================================================================

# Regímenes económicos (K=4)
REGIMEN_COLORS = {
    "caida":          NORD_11,   # Rojo
    "estabilidad":    NORD_14,   # Verde
    "alza_moderada":  NORD_13,   # Amarillo
    "alza_fuerte":    NORD_10,   # Azul Frost
}
REGIMEN_LIST = [NORD_11, NORD_14, NORD_13, NORD_10]

# Comparación de modelos
MODEL_COLORS = {
    "TCROC_Markov":   NORD_10,   # Azul principal
    "Cuantiles":      NORD_3,    # Gris
    "MS_AR":          NORD_11,   # Rojo
    "Observado":      NORD_14,   # Verde
}

# Series de combustibles
SERIES_COLORS = {
    "Regular":        NORD_10,   # Azul
    "Super":          NORD_9,    # Azul medio
    "Diesel":         NORD_13,   # Amarillo
    "Kerosene":       NORD_12,   # Naranja
}

# Elementos de interfaz
BACKGROUND   = "#FFFFFF"
GRID_COLOR   = NORD_5
TEXT_COLOR    = NORD_0
AXIS_COLOR   = NORD_3
ACCENT       = NORD_10


# ================================================================
#   CONFIGURACIÓN MATPLOTLIB
# ================================================================

def apply_thesis_style():
    """Aplica el estilo visual Nord de la tesis a matplotlib."""
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    plt.rcParams.update({
        "figure.facecolor": BACKGROUND,
        "axes.facecolor": BACKGROUND,
        "axes.edgecolor": AXIS_COLOR,
        "axes.labelcolor": TEXT_COLOR,
        "axes.grid": True,
        "grid.color": GRID_COLOR,
        "grid.alpha": 0.7,
        "text.color": TEXT_COLOR,
        "xtick.color": AXIS_COLOR,
        "ytick.color": AXIS_COLOR,
        "font.family": "serif",
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.1,
    })

    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(
        color=REGIMEN_LIST
    )
