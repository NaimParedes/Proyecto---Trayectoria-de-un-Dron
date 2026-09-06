# Proyecto---Trayectoria-de-un-Dron
Proyecto destinado a explicar mediante la telemetría, el cálculo y el modelado la trayectoria, velocidad, altura y ancho de banda de un dron.

A continuación, demostraciones del proyecto realizado:

Modelado 3D, HUD y Trayectoria:

![Imágen de VPython](https://github.com/NaimParedes/Proyecto---Trayectoria-de-un-Dron/blob/main/Modelado%20del%20Dron,%20HUD%20y%20Trayectoria.png?raw=true)

Reporte de Telemetría y Cálculo:

![Imágen de MatPlotLib](https://github.com/NaimParedes/Proyecto---Trayectoria-de-un-Dron/blob/main/Reporte%20de%20Telemetr%C3%ADa%20y%20C%C3%A1lculo%20.png?raw=true)

Fórmulas Utilizadas:
Velocidad Instantánea: 
v(t) = \frac{d}{dt}h(t) = -0.4t^3 + 4.8t^2 - 14.4t + 10
Segunda Derivada: a(t) = \frac{d^2}{dt^2}h(t) = -1.2t^2 + 9.6t - 14.4
Recta Tangente: y - v(t_{\text{máx}}) = a(t_{\text{máx}}) \cdot (t - t_{\text{máx}})
Tasa Instantánea de Calentamiento: T'(t) = 0.6t^2 - 2t + 4 \quad [\text{°C/s}]
Integral Indefinida: T(t) = \int (0.6t^2 - 2t + 4) \, dt = 0.2t^3 - t^2 + 4t + C
Tasa de Transferencia de Datos: D(t) = 3t^2 + 2t + 5 \quad [\text{MB/s}]
Función Antiderivada de Datos: F_D(t) = \int (3t^2 + 2t + 5) \, dt = t^3 + t^2 + 5t
Integración Numérica en Tiempo Real del HUD: \text{Acumulado}(t_k) \approx \text{Acumulado}(t_{k-1}) + \left( \frac{D(t_{k-1}) + D(t_k)}{2} \right) \Delta t

Librerías utilizadas: VPython y MatPlotLib
