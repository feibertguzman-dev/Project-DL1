# -*- coding: utf-8 -*-
"""
Librería de Vectores SVG de Grado Académico / Doctoral
Sustituye completamente el uso de emojis por gráficos vectoriales profesionales,
escalables, estilizados y libres de artefactos de renderizado.
"""
import os

SVG_ICONS = {
    "Piedra": '''<svg class="svg-gesture svg-rock" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gradRock" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6"/>
      <stop offset="100%" stop-color="#06B6D4"/>
    </linearGradient>
    <filter id="glowRock" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#3B82F6" flood-opacity="0.35"/>
    </filter>
  </defs>
  <path d="M22 28V20C22 17.79 23.79 16 26 16C28.21 16 30 17.79 30 20V24M30 20C30 17.79 31.79 16 34 16C36.21 16 38 17.79 38 20V24M38 22C38 19.79 39.79 18 42 18C44.21 18 46 19.79 46 22V32C46 41.94 39.94 48 30 48C20.06 48 16 41.94 16 36V28C16 25.79 17.79 24 20 24C22.21 24 24 25.79 24 28" 
        stroke="url(#gradRock)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="rgba(59, 130, 246, 0.12)" filter="url(#glowRock)"/>
  <path d="M24 34H36M24 40H34" stroke="#93C5FD" stroke-width="2.5" stroke-linecap="round"/>
</svg>''',

    "Papel": '''<svg class="svg-gesture svg-paper" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gradPaper" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>
    <filter id="glowPaper" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#10B981" flood-opacity="0.35"/>
    </filter>
  </defs>
  <path d="M20 28V14C20 12.34 21.34 11 23 11C24.66 11 26 12.34 26 14V26M26 14C26 12.34 27.34 11 29 11C30.66 11 32 12.34 32 14V26M32 16C32 14.34 33.34 13 35 13C36.66 13 38 14.34 38 16V26M38 19C38 17.34 39.34 16 41 16C42.66 16 44 17.34 44 19V34C44 43 38 49 29 49C20 49 16 43 16 36V28C16 26.34 17.34 25 19 25C20.66 25 22 26.34 22 28" 
        stroke="url(#gradPaper)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="rgba(16, 185, 129, 0.12)" filter="url(#glowPaper)"/>
  <circle cx="29" cy="38" r="3" fill="#6EE7B7"/>
</svg>''',

    "Tijera": '''<svg class="svg-gesture svg-scissors" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gradScissors" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8B5CF6"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
    <filter id="glowScissors" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#8B5CF6" flood-opacity="0.35"/>
    </filter>
  </defs>
  <path d="M26 12L34 28M38 12L30 28" stroke="url(#gradScissors)" stroke-width="4" stroke-linecap="round"/>
  <circle cx="24" cy="42" r="7" stroke="url(#gradScissors)" stroke-width="3.5" fill="rgba(139, 92, 246, 0.12)" filter="url(#glowScissors)"/>
  <circle cx="40" cy="42" r="7" stroke="url(#gradScissors)" stroke-width="3.5" fill="rgba(236, 72, 153, 0.12)" filter="url(#glowScissors)"/>
  <circle cx="32" cy="30" r="3" fill="#F472B6"/>
</svg>''',

    "robot": '''<svg class="svg-icon svg-ai" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="3" y="11" width="18" height="10" rx="2"/>
  <circle cx="12" cy="5" r="2"/>
  <path d="M12 7v4"/>
  <line x1="8" y1="16" x2="8" y2="16"/>
  <line x1="16" y1="16" x2="16" y2="16"/>
</svg>''',

    "user": '''<svg class="svg-icon svg-user" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
  <circle cx="12" cy="7" r="4"/>
</svg>''',

    "trophy": '''<svg class="svg-icon svg-trophy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M6 9H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h2"/>
  <path d="M18 9h2a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2h-2"/>
  <path d="M4 22h16"/>
  <path d="M10 14.66V17c0 .55-.45 1-1 1H7c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1h10c.55 0 1-.45 1-1v-1c0-.55-.45-1-1-1h-2c-.55 0-1-.45-1-1v-2.34"/>
  <path d="M6 3h12v7a6 6 0 0 1-12 0V3z"/>
</svg>''',

    "neural": '''<svg class="svg-icon svg-neural" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="6" cy="6" r="3"/>
  <circle cx="6" cy="18" r="3"/>
  <circle cx="18" cy="12" r="3"/>
  <line x1="8.6" y1="7.3" x2="15.4" y2="10.7"/>
  <line x1="8.6" y1="16.7" x2="15.4" y2="13.3"/>
</svg>''',

    "camera": '''<svg class="svg-icon svg-cam" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/>
  <circle cx="12" cy="13" r="4"/>
</svg>''',

    "refresh": '''<svg class="svg-icon svg-refresh" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polyline points="23 4 23 10 17 10"/>
  <polyline points="1 20 1 14 7 14"/>
  <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>
</svg>''',

    "versus": '''<svg class="svg-icon svg-vs" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="24" cy="24" r="22" stroke="rgba(255,255,255,0.15)" stroke-width="2" fill="rgba(15,23,42,0.8)"/>
  <text x="24" y="29" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#CBD5E1" text-anchor="middle">VS</text>
</svg>''',

    "question": '''<svg class="svg-icon svg-question" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="32" cy="32" r="28" stroke="rgba(255,255,255,0.2)" stroke-width="3" stroke-dasharray="6 6"/>
  <text x="32" y="38" font-family="'Outfit', sans-serif" font-size="24" font-weight="700" fill="#64748B" text-anchor="middle">?</text>
</svg>'''
}

def get_svg(name: str, width: int = None, height: int = None) -> str:
    svg = SVG_ICONS.get(name, SVG_ICONS["question"])
    if width and height:
        svg = svg.replace('<svg ', f'<svg width="{width}" height="{height}" ', 1)
    return svg

def export_svg_files(target_dir: str):
    os.makedirs(target_dir, exist_ok=True)
    for name, content in SVG_ICONS.items():
        fname = f"{name.lower()}.svg"
        with open(os.path.join(target_dir, fname), "w", encoding="utf-8") as f:
            f.write(content)
