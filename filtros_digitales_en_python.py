import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# ==========================================
# 1. DEFINICIÓN DE LA SEÑAL DE ENTRADA Y RUIDO
# ==========================================
fs = 1000.0  # Frecuencia de muestreo (1000 Hz)
t = np.linspace(0, 1.0, int(fs), endpoint=False)  # Vector de tiempo de 1 segundo

# Señal útil de baja frecuencia (5 Hz) + componente armónica alta (100 Hz)
signal_clean = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 100 * t)

# Adición de ruido blanco gaussiano para simular condiciones reales
np.random.seed(42)
noise = 0.5 * np.random.normal(size=t.shape)
signal_noisy = signal_clean + noise  # Señal compuesta final

# ==========================================
# 2. DISEÑO Y APLICACIÓN DE FILTROS DIGITALES
# ==========================================
def butter_filter(cutoff, fs, btype, order=4):
    """Diseña un filtro IIR Butterworth (low, high, band)"""
    nyq = 0.5 * fs
    if btype == 'band':
        normal_cutoff = [c / nyq for c in cutoff]
    else:
        normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype=btype, analog=False)
    return b, a

def apply_filter(data, cutoff, fs, btype, order=4):
    """Aplica el filtro diseñado a la señal de entrada"""
    b, a = butter_filter(cutoff, fs, btype, order=order)
    y = lfilter(b, a, data)
    return y

# A. Filtro Pasa Bajos (Corte a 20 Hz): Elimina el ruido y el armónico de 100 Hz
signal_lowpass = apply_filter(signal_noisy, 20.0, fs, 'low', order=4)

# B. Filtro Pasa Altos (Corte a 50 Hz): Aísla las componentes de alta frecuencia
signal_highpass = apply_filter(signal_noisy, 50.0, fs, 'high', order=4)

# C. Filtro Pasa Bandas (Entre 2 Hz y 10 Hz): Aísla estrictamente la señal de 5 Hz
signal_bandpass = apply_filter(signal_noisy, [2.0, 10.0], fs, 'band', order=4)

# ==========================================
# 3. VISUALIZACIÓN DE RESULTADOS (GRÁFICAS)
# ==========================================
plt.figure(figsize=(12, 10))

# Gráfica 1: Señal original vs Señal ruidosa
plt.subplot(4, 1, 1)
plt.plot(t, signal_noisy, color='gray', label='Señal con Ruido (Entrada)')
plt.plot(t, signal_clean, color='blue', linestyle='--', label='Señal Pura Teórica')
plt.title('1. Señal Original vs Señal Ruidosa')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend(loc='upper right')
plt.grid(True)

# Gráfica 2: Filtro Pasa Bajos
plt.subplot(4, 1, 2)
plt.plot(t, signal_lowpass, color='red', label='Filtrada (Pasa Bajos - 20 Hz)')
plt.title('2. Efecto del Filtro Pasa Bajos (Atenúa altas frecuencias y ruido)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend(loc='upper right')
plt.grid(True)

# Gráfica 3: Filtro Pasa Altos
plt.subplot(4, 1, 3)
plt.plot(t, signal_highpass, color='green', label='Filtrada (Pasa Altos - 50 Hz)')
plt.title('3. Efecto del Filtro Pasa Altos (Extrae ruido y frecuencias rápidas)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend(loc='upper right')
plt.grid(True)

# Gráfica 4: Filtro Pasa Bandas
plt.subplot(4, 1, 4)
plt.plot(t, signal_bandpass, color='purple', label='Filtrada (Pasa Bandas - 2 a 10 Hz)')
plt.title('4. Efecto del Filtro Pasa Bandas (Aísla la frecuencia de interés de 5 Hz)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend(loc='upper right')
plt.grid(True)

plt.tight_layout()
plt.show()