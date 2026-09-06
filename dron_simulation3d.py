import numpy as np
import matplotlib.pyplot as plt
from vpython import sphere, vector, color, rate, label, box, curve

# Fase 1: Altitud y Velocidad Instantánea
def h(t):
    "Función de Altitud"
    return -0.1 * t**4 + 1.6 * t**3 - 7.2 * t**2 + 10 * t + 5

def v(t):
    "Velocidad Instantánea "
    return -0.4 * t**3 + 4.8 * t**2 - 14.4 * t + 10

def a(t):
    "Segunda Derivada h''(t)"
    return -1.2 * t**2 + 9.6 * t - 14.4

# Fase 3: Consumo de Datos
def D(t):
    "Tasa de Transferencia de Datos en MB/s"
    return 3 * t**2 + 2 * t + 5

def F_D(t):
    "Antiderivada de D(t)"
    return t**3 + t**2 + 5 * t



# Suelo en la Animación
ground = box(pos=vector(0, 0, 0), size=vector(30, 0.2, 10), color=color.green)

# Dron en la Animación
dron = sphere(pos=vector(-12, h(0), 0), radius=0.6, color=color.cyan, make_trail=True, trail_color=color.yellow)

# Telemetría en la Animación
hud = label(
    pos=vector(0, 22, 0),
    text="",
    xoffset=0, yoffset=0,
    space=30, height=15, border=10,
    font='Times New Roman', color=color.white, box=True, opacity=0.8
)


# Animación
t_start = 0.0 #Tiempo Inicial
t_end = 10.0 #Tiempo Final
dt = 0.05  # Paso del tiempo de la animación

t_curr = t_start
acumulado_datos = 0.0

# Vectores para almacenamiento de datos en la gráfica posterior
t_vec = []
h_vec = []
v_vec = []
D_vec = []

while t_curr <= t_end:
    rate(20)  # Limita la animación a 20 FPS 
    
    # Evalua funciones analíticas
    altitud = h(t_curr)
    velocidad = v(t_curr)
    tasa_datos = D(t_curr)
    
    # Acumulación continua mediante integración numérica 
    if t_curr > 0:
        acumulado_datos += 0.5 * (D(t_curr - dt) + tasa_datos) * dt
    
    # Mapeo de las coordenadas 
    x_pos = -12 + (t_curr / 10.0) * 24
    dron.pos = vector(x_pos, altitud, 0)
    
    # Datos en el HUD
    hud.text = f"--- TELEMETRÍA EN TIEMPO REAL ---\n" \
               f"Tiempo: {t_curr:.2f} s\n" \
               f"Altitud: {altitud:.2f} m\n" \
               f"Velocidad Instantánea: {velocidad:.2f} m/s\n" \
               f"Datos Acumulados: {acumulado_datos:.2f} MB"
    
    # Registro de datos
    t_vec.append(t_curr)
    h_vec.append(altitud)
    v_vec.append(velocidad)
    D_vec.append(tasa_datos)
    
    t_curr += dt

#Gráficas

t_arr = np.array(t_vec)
h_arr = np.array(h_vec)
v_arr = np.array(v_vec)

# Punto máx de la tangente
idx_max = np.argmax(h_arr)
t_max = t_arr[idx_max]
h_max = h_arr[idx_max]
v_max = v_arr[idx_max]  # Debería ser cercano a 0

fig, axs = plt.subplots(3, 1, figsize=(9, 11))
fig.suptitle("REPORTE DE TELEMETRÍA Y CÁLCULO", fontsize=14, fontweight='bold')

#Posición / Altitud h(t)
axs[0].plot(t_arr, h_arr, color='blue', linewidth=2, label=r'$h(t) = -0.1t^4 + 1.6t^3 - 7.2t^2 + 10t + 5$')
axs[0].scatter([t_max], [h_max], color='red', zorder=5, label=f'Altura Máx ({t_max:.2f}s, {h_max:.2f}m)')
axs[0].set_title("1. Trayectoria de Altitud h(t)", fontsize=11)
axs[0].set_xlabel("Tiempo (s)")
axs[0].set_ylabel("Altitud (m)")
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend()

#Velocidad Instantánea v(t) y Recta Tangente en el Máximo
axs[1].plot(t_arr, v_arr, color='green', linewidth=2, label=r'$v(t) = h^{\prime}(t) = -0.4t^3 + 4.8t^2 - 14.4t + 10$')
axs[1].axhline(0, color='black', linestyle=':', alpha=0.7)

# Recta Tangente en el máx
a_at_max = a(t_max)
t_tang = np.linspace(max(0, t_max - 2), min(10, t_max + 2), 50)
v_tang = a_at_max * (t_tang - t_max) + v_max
axs[1].plot(t_tang, v_tang, color='red', linestyle='--', linewidth=1.5, label=f'Recta Tangente en $t_{{máx}}={t_max:.2f}s$')

axs[1].scatter([t_max], [v_max], color='red', zorder=5)
axs[1].set_title("2. Velocidad Instantánea v(t) con Tangente en Punto Máximo", fontsize=11)
axs[1].set_xlabel("Tiempo (s)")
axs[1].set_ylabel("Velocidad (m/s)")
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend()

#Transferencia de Datos y Área Bajo la Curva
D_arr = D(t_arr)
axs[2].plot(t_arr, D_arr, color='purple', linewidth=2, label=r'$D(t) = 3t^2 + 2t + 5$')

# Sombreado para el área bajo la curva
t_fill = np.linspace(1, 4, 100)
D_fill = D(t_fill)
area_exacta = F_D(4) - F_D(1)  # TFC: F(4) - F(1)

#Textos adicionales de la ventana
axs[2].fill_between(t_fill, D_fill, color='purple', alpha=0.3, label=f'Área Acumulada: {area_exacta:.1f} MB')
axs[2].set_title("3. Transferencia de Datos D(t) y Acumulación Integral", fontsize=11)
axs[2].set_xlabel("Tiempo (s)")
axs[2].set_ylabel("Ancho de Banda (MB/s)")
axs[2].grid(True, linestyle='--', alpha=0.6)
axs[2].legend()

plt.tight_layout()
plt.show()