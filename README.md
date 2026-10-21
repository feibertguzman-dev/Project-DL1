# Clasificador Neuronal Convolucional: Piedra, Papel o Tijera

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow 2.x](https://img.shields.io/badge/TensorFlow-2.x-FF6F00.svg?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-D00000.svg?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![UCN Deep Learning](https://img.shields.io/badge/UCN-Deep_Learning_2026-005696.svg?style=for-the-badge)](https://www.ucn.cl/)
[![License MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

---
| N.º | Entregable | Enlace |
|---:|---|---|
| 1 | Landing Page del proyecto | [Ver Landing Page](https://feibertguzman-dev.github.io/Project-DL1/) |
| 2 | Documento escrito del proyecto Deep Learning | [Ver documento escrito](https://github.com/feibertguzman-dev/Project-DL1/blob/main/Plantilla_Profesional_Proyecto_Deep_Learning_2026.docx) |
| 3 | Aplicación desplegada en Streamlit | [Acceder a la aplicación](https://project-dl1.streamlit.app/) |
---

## 1. Descripción del Proyecto

Proyecto de investigación aplicada para la asignatura de **Deep Learning (2026)** de la **Universidad Católica del Norte (UCN)**, desarrollado por **Feibert Alirio Guzmán Pérez**.

El sistema implementa un modelo de **Visión por Computadora** basado en redes neuronales convolucionales profundas (CNN) capaz de realizar inferencia en tiempo real sobre el flujo de una cámara web, clasificando la morfología manual en tres clases canónicas:
- **Piedra (Clase 0)**: Puño cerrado, neutraliza a Tijera.
- **Papel (Clase 1)**: Palma abierta en plano frontal, neutraliza a Piedra.
- **Tijera (Clase 2)**: Dígitos índice y medio extendidos en bifurcación, neutraliza a Papel.

La solución integra un motor de reglas desacoplado que enfrenta al usuario contra un agente algorítmico en una serie competitiva estructurada al primer participante en registrar **3 victorias**.

---

## 2. Arquitectura de Software por Capas (Clean Architecture)

El repositorio está organizado desacoplando la inferencia matemática, la lógica del juego y la presentación de usuario:

```text
Project-DL1/
|
|-- .agents/
|   `-- skills/
|       `-- dl-project-docs/
|           `-- SKILL.md             # Guía técnica de documentación formal
|
|-- converted_keras (Piedra-Papel-Tijera)/
|   |-- keras_model.h5               # Pesos sinápticos serializados en HDF5
|   `-- labels.txt                   # Mapeo de índices a clases textuales
|
|-- src/
|   |-- __init__.py
|   |-- model/
|   |   |-- __init__.py
|   |   `-- classifier.py            # Preprocesamiento tensorial e inferencia Keras
|   |-- game/
|   |   |-- __init__.py
|   |   `-- engine.py                # Motor formal de reglas y estado de competencia
|   `-- ui/
|       |-- __init__.py
|       |-- svg_icons.py             # Generador de gráficos vectoriales SVG escalables
|       `-- components.py            # Componentes visuales glassmorphism y métricas
|
|-- assets/
|   |-- css/
|   |   `-- style.css                # Estilos modernos para la landing page
|   |-- js/
|   |   `-- main.js                  # Lógica del simulador in-browser y Web Audio API
|   `-- images/
|       `-- svg/                     # Activos vectoriales SVG independientes
|
|-- index.html                       # Landing Page moderna en la raíz
|-- app.py                           # Aplicación interactiva en Streamlit (WebCam)
|-- requirements.txt                 # Especificación de dependencias
|-- Plantilla_Profesional_Proyecto_Deep_Learning_2026.docx  # Documento técnico maestro
|-- .gitignore                       # Filtros de exclusión para Git
`-- README.md                        # Documentación general del repositorio
```

---

## 3. Especificaciones del Modelo de Deep Learning

| Parámetro | Valor / Especificación |
| :--- | :--- |
| **Framework Base** | TensorFlow 2.x / Keras (`tf_keras` / `tensorflow.keras`) |
| **Tensor de Entrada** | Formato 4D: `(Batch_Size, 224, 224, 3)` |
| **Canales de Color** | RGB |
| **Interpolación Espacial** | Algoritmo Lanczos con recorte y ajuste de aspecto centrado |
| **Ecuación de Normalización** | $X_{	ext{norm}} = rac{X}{127.5} - 1.0 \quad \in [-1.0, 1.0]$ |
| **Capa de Salida** | Función de densidad Softmax sobre 3 clases mutuamente excluyentes |
| **Serialización** | Archivo jerárquico HDF5 (`.h5`) |

---

## 4. Instalación y Ejecución Local

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/feibertguzman-dev/Project-DL1.git
cd Project-DL1
```

### Paso 2: Crear el Entorno Virtual
En Windows (PowerShell):
```powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Paso 4: Ejecutar la Aplicación Streamlit
```bash
streamlit run app.py
```
La aplicación se abrirá en `http://localhost:8501`.

### Paso 5: Visualizar la Landing Page
Abre directamente `index.html` en el navegador o ejecuta un servidor estático:
```bash
python -m http.server 8000
```
Y accede a `http://localhost:8000`.

---

## 5. Despliegue en Streamlit Community Cloud

1. Realizar push del repositorio a GitHub:
   ```bash
   git add .
   git commit -m "feat: release version 1.0 with clean architecture and svg vectors"
   git push origin main
   ```
2. Acceder a [share.streamlit.io](https://share.streamlit.io/).
3. Configurar nueva aplicación:
   - **Repository**: `feibertguzman-dev/Project-DL1`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Desplegar. Streamlit Cloud provee certificado SSL/HTTPS indispensable para habilitar los permisos del sensor de cámara web del navegador.

---

## 6. Módulos de la Aplicación

- **Partida vs Máquina**: Captura en tiempo real mediante WebCam, inferencia feedforward, respuesta aleatoria del agente de la máquina, marcador visual y resolución automática de serie a 3 victorias.
- **Inspector de Inferencia**: Evaluación analítica de imágenes estáticas o capturadas con inspección detallada del vector de probabilidades.
- **Arquitectura & Documentación**: Resumen metodológico de las capas del sistema y fórmulas matemáticas asociadas.

---

## 7. Autoría y Créditos

- **Investigador / Desarrollador**: Feibert Alirio Guzmán Pérez
- **Institución**: Universidad Católica del Norte (UCN)
- **Materia**: Deep Learning
- **Año**: 2026
- **Repositorio Oficial**: [https://github.com/feibertguzman-dev/Project-DL1.git](https://github.com/feibertguzman-dev/Project-DL1.git)
