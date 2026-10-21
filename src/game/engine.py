# -*- coding: utf-8 -*-
"""
Motor de Juego - Piedra, Papel o Tijera (Deep Learning Project)
Desacoplado, sin dependencias de fuentes o emojis de terceros.
"""
import random
from typing import Dict, Any, Tuple, List

CHOICES = ["Piedra", "Papel", "Tijera"]

RULES = {
    "Piedra": "Tijera",   # Piedra gana a Tijera
    "Papel": "Piedra",    # Papel gana a Piedra
    "Tijera": "Papel"     # Tijera gana a Papel
}

class RPSEngine:
    """
    Gestiona la lógica formal de juego, puntuaciones, historial de rondas
    y condiciones de victoria al mejor de 3 aciertos (o meta configurable).
    """
    def __init__(self, target_score: int = 3):
        self.target_score = target_score
        self.reset()

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds_played = 0
        self.history: List[Dict[str, Any]] = []
        self.game_over = False
        self.winner = None

    def computer_choose(self) -> str:
        return random.choice(CHOICES)

    def evaluate_round(self, player_move: str, computer_move: str) -> Tuple[str, str]:
        p = player_move.strip().capitalize()
        c = computer_move.strip().capitalize()

        if p not in CHOICES:
            return "invalid", f"Movimiento '{player_move}' no válido."

        if p == c:
            return "tie", f"Empate: Ambos competidores eligieron {p}."

        if RULES.get(p) == c:
            return "player", f"Punto para el Jugador: {p} neutraliza a {c}."
        else:
            return "computer", f"Punto para la Máquina: {c} neutraliza a {p}."

    def play_round(self, player_move: str, computer_move: str = None) -> Dict[str, Any]:
        if self.game_over:
            return {
                "error": "La serie ha finalizado. Reinicie para comenzar una nueva partida.",
                "game_over": True,
                "winner": self.winner
            }

        if computer_move is None:
            computer_move = self.computer_choose()

        outcome, message = self.evaluate_round(player_move, computer_move)

        if outcome == "player":
            self.player_score += 1
        elif outcome == "computer":
            self.computer_score += 1
        elif outcome == "tie":
            self.ties += 1

        self.rounds_played += 1

        if self.player_score >= self.target_score:
            self.game_over = True
            self.winner = "Jugador"
        elif self.computer_score >= self.target_score:
            self.game_over = True
            self.winner = "Máquina"

        round_data = {
            "round": self.rounds_played,
            "player_move": player_move,
            "computer_move": computer_move,
            "outcome": outcome,
            "message": message,
            "player_score": self.player_score,
            "computer_score": self.computer_score,
            "game_over": self.game_over,
            "winner": self.winner
        }
        self.history.append(round_data)
        return round_data

    def get_state(self) -> Dict[str, Any]:
        return {
            "player_score": self.player_score,
            "computer_score": self.computer_score,
            "ties": self.ties,
            "rounds_played": self.rounds_played,
            "target_score": self.target_score,
            "game_over": self.game_over,
            "winner": self.winner,
            "history": self.history
        }
