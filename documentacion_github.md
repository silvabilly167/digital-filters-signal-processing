# Implementación y Evaluación de Filtros Digitales en Python

Repositorio correspondiente a la **Actividad Formativa 3**, enfocado en el diseño, implementación y análisis de filtros digitales (pasa bajos, pasa altos y pasa bandas) para la eliminación de ruido en señales compuestas.

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3.x**
* **NumPy:** Procesamiento numérico y generación de vectores temporales.
* **SciPy (`scipy.signal`):** Diseño de filtros IIR (Butterworth) y aplicación mediante ecuaciones de diferencias.
* **Matplotlib:** Visualización gráfica de señales en el dominio del tiempo.

## 📂 Estructura del Repositorio
* `filter_design.py`: Script principal que contiene la generación de la señal con ruido, el diseño de los filtros y la visualización de las gráficas.
* `requirements.txt`: Lista de dependencias del proyecto.
* `README.md`: Documentación del proyecto.

## 🚀 Instrucciones de Ejecución
1. Asegúrate de tener Python instalado junto con las librerías necesarias. Puedes instalarlas ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el script principal:
   ```bash
   python filter_design.py
   ```

## 📊 Resultados y Análisis
* **Filtro Pasa Bajos ($f_c = 20\text{ Hz}$):** Atenúa eficazmente el ruido blanco y las componentes de alta frecuencia (como el armónico de 100 Hz), aislando la señal senoidal útil de baja frecuencia.
* **Filtro Pasa Bandas ($2\text{ Hz} - 10\text{ Hz}$):** Aísla con gran precisión la frecuencia central de interés, bloqueando tanto el ruido superior como el inferior.

## 👤 Autor
* **Estudiante:** Billy Rolando Silva Vargas