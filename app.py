# -*- coding: utf-8 -*-
"""
Aplicación Principal Streamlit - Clasificación Neuronal de Gestos (Deep Learning)
Universidad Católica del Norte (UCN)
Autor: Feibert Alirio Guzmán Pérez
Repositorio: https://github.com/feibertguzman-dev/Project-DL1.git
"""
import os
import sys
import streamlit as st
from PIL import Image

# Agregar directorio raíz al path para importar paquetes internos
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.model.classifier import RPSClassifier
from src.game.engine import RPSEngine
from src.ui.svg_icons import get_svg
from src.ui.components import (
    inject_custom_css,
    render_hero,
    render_scoreboard,
    render_duel_result,
    render_winner_banner,
    render_probabilities,
    render_history_list
)

# Configuración formal de página
st.set_page_config(
    page_title="Deep Learning RPS | UCN",
    page_icon="https://raw.githubusercontent.com/feibertguzman-dev/Project-DL1/main/assets/images/svg/neural.svg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyectar estilos CSS profesionales
inject_custom_css()

# Cargar clasificador en caché de recursos
@st.cache_resource(show_spinner="Inicializando clasificador convolucional Keras...")
def get_classifier():
    return RPSClassifier()

try:
    classifier = get_classifier()
except Exception as e:
    st.error(f"Fallo crítico al instanciar el clasificador neuronal: {e}")
    st.stop()

# Inicialización de estado de sesión
if "engine" not in st.session_state:
    st.session_state.engine = RPSEngine(target_score=3)
if "last_round" not in st.session_state:
    st.session_state.last_round = None
if "last_processed_img_id" not in st.session_state:
    st.session_state.last_processed_img_id = None

engine: RPSEngine = st.session_state.engine

# Barra Lateral de Navegación y Parámetros
with st.sidebar:
    st.markdown("### Parámetros de Ejecución")
    mode = st.radio(
        "Módulo Activo:",
        ["Partida vs Máquina", "Inspector de Inferencia", "Arquitectura & Documentación"],
        index=0
    )

    st.markdown("---")
    st.markdown("#### Configuración de Competencia")
    target_score = st.slider("Cota de victorias (meta):", min_value=1, max_value=5, value=engine.target_score)
    if target_score != engine.target_score:
        engine.target_score = target_score

    if st.button("Reiniciar Serie", use_container_width=True, type="secondary"):
        engine.reset()
        st.session_state.last_round = None
        st.session_state.last_processed_img_id = None
        st.rerun()

    st.markdown("---")
    st.markdown("#### Parámetros Óptimos de Adquisición")
    st.markdown(
        "<div style='font-size:0.85rem; color:#94A3B8; line-height:1.6;'>"
        "• Centrar la morfología de la mano en el sensor.<br>"
        "• Mantener contraste lumínico adecuado respecto al fondo.<br>"
        "• Definir el gesto estático antes de disparar el obturador.<br>"
        "• Clases admitidas: <strong>Piedra</strong>, <strong>Papel</strong> o <strong>Tijera</strong>."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown(
        "<div style='font-size:0.8rem; color:#64748B; text-align:center; line-height:1.4;'>"
        "<strong>Deep Learning 2026</strong><br>"
        "Universidad Católica del Norte<br>"
        "Investigador: Feibert Guzmán<br>"
        "<a href='https://github.com/feibertguzman-dev/Project-DL1.git' target='_blank' style='color:#60A5FA; text-decoration:none;'>Repositorio GitHub</a>"
        "</div>",
        unsafe_allow_html=True
    )

# Cabecera Institucional
render_hero()

# ==========================================
# MÓDULO 1: PARTIDA VS MÁQUINA
# ==========================================
if mode == "Partida vs Máquina":
    render_scoreboard(
        player_score=engine.player_score,
        computer_score=engine.computer_score,
        target_score=engine.target_score,
        round_num=engine.rounds_played
    )

    if engine.game_over:
        render_winner_banner(engine.winner)
        col_rst1, col_rst2, col_rst3 = st.columns([1, 2, 1])
        with col_rst2:
            if st.button("Comenzar Nueva Serie", type="primary", use_container_width=True):
                engine.reset()
                st.session_state.last_round = None
                st.session_state.last_processed_img_id = None
                st.rerun()

    col_cam, col_info = st.columns([1.1, 1], gap="large")

    with col_cam:
        st.markdown("### Adquisición de Muestra")
        tab_cam, tab_up = st.tabs(["Cámara Web (Stream)", "Cargar Imagen (Archivo)"])

        img_input = None
        with tab_cam:
            cam_file = st.camera_input("Capturar fotograma de la mano", key="game_cam")
            if cam_file:
                img_input = cam_file

        with tab_up:
            up_file = st.file_uploader("Subir imagen estática (JPG, PNG)", type=["jpg", "jpeg", "png"], key="game_up")
            if up_file:
                img_input = up_file

        if img_input is not None and not engine.game_over:
            file_id = f"{img_input.name}_{img_input.size}"
            if st.session_state.last_processed_img_id != file_id:
                try:
                    pil_img = Image.open(img_input)
                    pred = classifier.predict(pil_img)
                    detected_gesture = pred["label"]
                    confidence = pred["confidence"]

                    round_res = engine.play_round(detected_gesture)
                    round_res["confidence"] = confidence
                    round_res["probabilities"] = pred["probabilities"]
                    st.session_state.last_round = round_res
                    st.session_state.last_processed_img_id = file_id
                    st.rerun()
                except Exception as ex:
                    st.error(f"Error durante el preprocesamiento o inferencia: {ex}")

    with col_info:
        st.markdown("### Diagnóstico e Inferencia")
        if st.session_state.last_round:
            r = st.session_state.last_round
            render_duel_result(r)
            render_probabilities(r.get("probabilities", {}))
        else:
            q_svg = get_svg("question", width=56, height=56)
            st.markdown(f"""
            <div style="background:rgba(17,24,39,0.6); border:1px dashed rgba(255,255,255,0.12); border-radius:14px; padding:2.5rem 1.5rem; text-align:center; color:#94A3B8;">
                <div style="margin-bottom:0.8rem;">{q_svg}</div>
                <h4 style="color:#E2E8F0; margin-bottom:0.4rem; font-weight:700;">Canal de Inferencia en Espera</h4>
                <p style="font-size:0.9rem;">
                    Capture o suministre un fotograma para que la red convolucional extraiga las características
                    morfológicas e interactúe con el motor algorítmico.
                </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    render_history_list(engine.history)

# ==========================================
# MÓDULO 2: INSPECTOR DE INFERENCIA
# ==========================================
elif mode == "Inspector de Inferencia":
    st.markdown("### Inspector de Inferencia Neuronal")
    st.markdown("Evaluación detallada de la distribución Softmax y tensor de entrada normalizado.")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        tab_cam2, tab_up2 = st.tabs(["Cámara Web", "Cargar Archivo"])
        test_img = None
        with tab_cam2:
            c_input = st.camera_input("Adquirir para diagnóstico", key="inspect_cam")
            if c_input:
                test_img = c_input
        with tab_up2:
            u_input = st.file_uploader("Seleccionar imagen de prueba", type=["jpg", "jpeg", "png"], key="inspect_up")
            if u_input:
                test_img = u_input

    with col2:
        if test_img is not None:
            pil_img = Image.open(test_img)
            st.image(pil_img, caption="Tensor de Entrada Visual", use_container_width=True)
            
            with st.spinner("Procesando convolución feedforward..."):
                pred = classifier.predict(pil_img)

            top_label = pred["label"]
            conf = pred["confidence"] * 100.0
            svg_pred = get_svg(top_label, width=64, height=64)

            st.markdown(f"""
            <div style="background:rgba(17,24,39,0.8); border:1px solid rgba(59,130,246,0.3); border-radius:14px; padding:1.5rem; text-align:center; margin:1rem 0;">
                <div style="margin-bottom:0.5rem;">{svg_pred}</div>
                <div style="font-size:1.6rem; font-weight:800; color:#60A5FA;">{top_label}</div>
                <div style="font-size:1rem; color:#94A3B8;">Nivel de Confianza: <strong>{conf:.2f}%</strong></div>
            </div>
            """, unsafe_allow_html=True)

            render_probabilities(pred["probabilities"])
        else:
            st.info("Capture o cargue una imagen para desplegar el análisis tensorial.")

# ==========================================
# MÓDULO 3: ARQUITECTURA Y DOCUMENTACIÓN
# ==========================================
else:
    st.markdown("### Arquitectura de Software y Fundamentación Matemática")
    st.markdown("""
    El presente desarrollo desacopla de forma estricta la inferencia tensorial,
    el motor de reglas determinista y la interfaz gráfica de presentación.
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div style="background:rgba(17,24,39,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:1.4rem;">
            <h4 style="color:#60A5FA;">1. Capa de Aprendizaje Profundo</h4>
            <p style="font-size:0.88rem; color:#94A3B8;">
                • Módulo: <code>src/model/classifier.py</code><br>
                • Modelo serializado HDF5 (<code>keras_model.h5</code>).<br>
                • Preprocesamiento de entrada: Redimensión centrada a 224×224 píxeles RGB y normalización lineal en el intervalo [-1, 1].<br>
                • Activación final: Softmax multiclase.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div style="background:rgba(17,24,39,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:1.4rem;">
            <h4 style="color:#34D399;">2. Capa de Dominio (Motor de Reglas)</h4>
            <p style="font-size:0.88rem; color:#94A3B8;">
                • Módulo: <code>src/game/engine.py</code><br>
                • Álgebra formal del juego (relación de orden circular cíclico).<br>
                • Agente estocástico para la jugada adversaria.<br>
                • Control de victoria acumulada a 3 aciertos.<br>
                • Historial inmutable por ronda.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div style="background:rgba(17,24,39,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:1.4rem;">
            <h4 style="color:#C084FC;">3. Capa de Presentación (UI)</h4>
            <p style="font-size:0.88rem; color:#94A3B8;">
                • Módulo: <code>app.py</code> y <code>src/ui/components.py</code><br>
                • Interfaz reactiva en Streamlit.<br>
                • Adquisición por WebCam en tiempo real.<br>
                • Landing page desacoplada (<code>index.html</code>, CSS, JS) en la raíz.<br>
                • Iconografía vectorial SVG pura (sin emojis).
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Especificaciones Tensoriales")
    st.code("""
Tensor de Entrada: Shape (Batch, 224, 224, 3) | Tipo: float32
Ecuación de Normalización: X_norm = (X / 127.5) - 1.0  => Intervalo [-1.0, 1.0]
Tensor de Salida: Shape (Batch, 3) | Activación: Softmax(z_i) = exp(z_i) / sum(exp(z_j))
Clases del Dominio: [0: Piedra, 1: Papel, 2: Tijera]
Framework: TensorFlow 2.x / Keras / tf_keras
    """, language="text")
