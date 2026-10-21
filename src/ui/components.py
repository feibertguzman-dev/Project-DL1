# -*- coding: utf-8 -*-
"""
Componentes de UI de Grado Académico / Doctoral para Streamlit
100% libre de emojis. Renderizado con gráficos vectoriales SVG escalables.
"""
import streamlit as st
from typing import Dict, Any, List
from src.ui.svg_icons import get_svg

def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* SVG Base Styling */
    .svg-icon {
        width: 20px;
        height: 20px;
        vertical-align: middle;
        display: inline-block;
    }

    .svg-gesture {
        width: 72px;
        height: 72px;
        display: block;
        margin: 0 auto;
        transition: transform 0.3s ease;
    }

    .svg-gesture:hover {
        transform: scale(1.08);
    }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.95) 0%, rgba(10, 14, 23, 0.98) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 2.2rem;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.5);
        text-align: center;
        position: relative;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #38BDF8 0%, #818CF8 50%, #C084FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #94A3B8;
        max-width: 720px;
        margin: 0 auto 1.2rem auto;
        line-height: 1.6;
    }

    .badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.35rem 0.9rem;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 600;
        background: rgba(59, 130, 246, 0.1);
        color: #93C5FD;
        border: 1px solid rgba(59, 130, 246, 0.25);
        margin: 0.2rem 0.3rem;
    }

    /* Scoreboard */
    .scoreboard-grid {
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        gap: 1.2rem;
        align-items: center;
        margin: 1.5rem 0;
    }

    .score-card {
        background: rgba(17, 24, 39, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.4rem;
        text-align: center;
        box-shadow: 0 8px 20px -5px rgba(0, 0, 0, 0.4);
    }

    .score-card.player { border-top: 3px solid #3B82F6; }
    .score-card.computer { border-top: 3px solid #EF4444; }

    .score-name {
        font-size: 0.85rem;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 1.2px;
        color: #94A3B8;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        margin-bottom: 0.4rem;
    }

    .score-value {
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1;
        font-family: 'JetBrains Mono', monospace;
    }

    .score-value.player { color: #60A5FA; }
    .score-value.computer { color: #F87171; }

    /* Duel Arena */
    .duel-arena {
        background: rgba(17, 24, 39, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.6rem;
        margin: 1.5rem 0;
        text-align: center;
    }

    .duel-hands-wrapper {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin: 1.2rem 0;
    }

    .hand-box {
        background: rgba(10, 14, 23, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 1.2rem 1.6rem;
        min-width: 140px;
    }

    .hand-title {
        font-weight: 700;
        font-size: 1rem;
        margin-top: 0.6rem;
        color: #F1F5F9;
    }

    .outcome-box {
        padding: 0.9rem 1.4rem;
        border-radius: 10px;
        font-weight: 700;
        font-size: 1.05rem;
        margin-top: 1rem;
    }

    .outcome-box.player {
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.35);
        color: #34D399;
    }

    .outcome-box.computer {
        background: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.35);
        color: #F87171;
    }

    .outcome-box.tie {
        background: rgba(245, 158, 11, 0.12);
        border: 1px solid rgba(245, 158, 11, 0.35);
        color: #FBBF24;
    }

    /* Winner Banner */
    .winner-banner {
        padding: 1.8rem;
        border-radius: 16px;
        text-align: center;
        margin: 1.5rem 0;
    }

    .winner-banner.player {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(5, 150, 105, 0.3) 100%);
        border: 1px solid #10B981;
    }

    .winner-banner.computer {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2) 0%, rgba(220, 38, 38, 0.3) 100%);
        border: 1px solid #EF4444;
    }

    /* History table */
    .history-card {
        background: rgba(17, 24, 39, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 10px;
        padding: 0.75rem 1.2rem;
        margin-bottom: 0.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.92rem;
    }

    .prob-bar-container {
        margin: 0.6rem 0;
    }
    .prob-label-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }
    .prob-bar-bg {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 9999px;
        height: 8px;
        overflow: hidden;
    }
    .prob-bar-fill {
        height: 100%;
        border-radius: 9999px;
    }
    </style>
    """, unsafe_allow_html=True)

def render_hero():
    neural_svg = get_svg("neural", width=22, height=22)
    st.markdown(f"""
    <div class="hero-container">
        <div>
            <span class="badge-pill">{neural_svg} UCN • Deep Learning 2026</span>
            <span class="badge-pill">TensorFlow / Keras</span>
            <span class="badge-pill">Autor: Feibert Guzmán</span>
        </div>
        <div class="hero-title">Sistema de Clasificación Convolucional</div>
        <div class="hero-subtitle">
            Duelo interactivo en tiempo real mediante visión artificial.
            La arquitectura procesa el flujo de fotogramas e infiere la categoría morfológica de la mano.
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_scoreboard(player_score: int, computer_score: int, target_score: int = 3, round_num: int = 0):
    user_svg = get_svg("user", width=18, height=18)
    robot_svg = get_svg("robot", width=18, height=18)
    vs_svg = get_svg("versus", width=42, height=42)

    st.markdown(f"""
    <div class="scoreboard-grid">
        <div class="score-card player">
            <div class="score-name">{user_svg} Jugador</div>
            <div class="score-value player">{player_score}</div>
            <div style="font-size:0.8rem; color:#94A3B8;">Objetivo: {target_score} victorias</div>
        </div>
        <div style="text-align:center;">
            {vs_svg}
            <div style="font-size:0.75rem; color:#64748B; margin-top:0.3rem; font-weight:700;">RONDA {round_num}</div>
        </div>
        <div class="score-card computer">
            <div class="score-name">{robot_svg} Máquina AI</div>
            <div class="score-value computer">{computer_score}</div>
            <div style="font-size:0.8rem; color:#94A3B8;">Objetivo: {target_score} victorias</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_duel_result(round_data: Dict[str, Any]):
    p_move = round_data.get("player_move", "Piedra")
    c_move = round_data.get("computer_move", "Piedra")
    outcome = round_data.get("outcome", "tie")
    msg = round_data.get("message", "")

    p_svg = get_svg(p_move, width=64, height=64)
    c_svg = get_svg(c_move, width=64, height=64)

    st.markdown(f"""
    <div class="duel-arena">
        <div style="color:#94A3B8; font-weight:600; text-transform:uppercase; letter-spacing:1px; font-size:0.8rem;">
            Resolución de la Ronda #{round_data.get('round', 1)}
        </div>
        <div class="duel-hands-wrapper">
            <div class="hand-box">
                {p_svg}
                <div class="hand-title">Jugador: {p_move}</div>
            </div>
            <div style="font-size:1.4rem; font-weight:800; color:#64748B;">vs</div>
            <div class="hand-box">
                {c_svg}
                <div class="hand-title">Máquina: {c_move}</div>
            </div>
        </div>
        <div class="outcome-box {outcome}">
            {msg}
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_winner_banner(winner: str):
    is_player = winner == "Jugador"
    banner_cls = "player" if is_player else "computer"
    trophy_svg = get_svg("trophy", width=36, height=36)
    title = "Victoria de la Serie: Jugador" if is_player else "Victoria de la Serie: Máquina AI"
    desc = "El modelo neuronal ha registrado la victoria del usuario frente al agente algorítmico." if is_player else "El agente algorítmico ha alcanzado la cota de 3 aciertos en primer lugar."

    st.markdown(f"""
    <div class="winner-banner {banner_cls}">
        <div style="margin-bottom:0.6rem; color:#FBBF24;">{trophy_svg}</div>
        <div style="font-size:1.8rem; font-weight:800; color:#FFFFFF; margin-bottom:0.3rem;">
            {title}
        </div>
        <div style="font-size:0.95rem; color:#E2E8F0;">
            {desc}
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_probabilities(probs: Dict[str, float]):
    colors = {"Piedra": "#3B82F6", "Papel": "#10B981", "Tijera": "#8B5CF6"}
    st.markdown("<h4 style='margin-top:1.2rem; font-weight:700;'>Vector de Probabilidades (Softmax)</h4>", unsafe_allow_html=True)
    for label, val in probs.items():
        pct = val * 100.0
        bar_color = colors.get(label, "#6366F1")
        svg_mini = get_svg(label, width=20, height=20)
        st.markdown(f"""
        <div class="prob-bar-container">
            <div class="prob-label-row">
                <span style="display:flex; align-items:center; gap:0.4rem;">{svg_mini} {label}</span>
                <span style="font-family:'JetBrains Mono', monospace;">{pct:.2f}%</span>
            </div>
            <div class="prob-bar-bg">
                <div class="prob-bar-fill" style="width: {pct:.2f}%; background-color: {bar_color};"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_history_list(history: List[Dict[str, Any]]):
    if not history:
        st.info("No se registran eventos aún. Inicie la captura para registrar la primera ronda.")
        return

    st.markdown("<h4 style='margin-top:1.5rem; font-weight:700;'>Registro Cronológico de Enfrentamientos</h4>", unsafe_allow_html=True)
    outcome_badges = {
        "player": ("#10B981", "Victoria"),
        "computer": ("#EF4444", "Derrota"),
        "tie": ("#EAB308", "Empate")
    }

    for r in reversed(history):
        col, txt = outcome_badges.get(r["outcome"], ("#64748B", "Ronda"))
        st.markdown(f"""
        <div class="history-card">
            <div>
                <strong style="color:#94A3B8;">Ronda {r['round']}</strong>: 
                Jugador [{r['player_move']}] vs Máquina [{r['computer_move']}]
            </div>
            <div>
                <span style="background:{col}20; color:{col}; border:1px solid {col}50; padding:0.2rem 0.6rem; border-radius:6px; font-size:0.78rem; font-weight:700;">
                    {txt}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
