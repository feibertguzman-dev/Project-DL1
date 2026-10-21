/**
 * Rock-Paper-Scissors AI | Landing Page Scripts
 * 100% Vector SVG Rendering - No Emojis
 * Autor: Feibert Alirio Guzmán Pérez
 * Repositorio: https://github.com/feibertguzman-dev/Project-DL1.git
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavbarScroll();
  initSimulator();
});

function initNavbarScroll() {
  const navbar = document.querySelector('.navbar');
  if (!navbar) return;
  
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.style.background = 'rgba(10, 14, 23, 0.95)';
      navbar.style.borderBottomColor = 'rgba(99, 102, 241, 0.2)';
    } else {
      navbar.style.background = 'rgba(10, 14, 23, 0.85)';
      navbar.style.borderBottomColor = 'rgba(255, 255, 255, 0.08)';
    }
  });
}

function initSimulator() {
  const choices = ['Piedra', 'Papel', 'Tijera'];
  
  const svgs = {
    'Piedra': `<svg class="svg-gesture" viewBox="0 0 64 64" fill="none"><path d="M22 28V20C22 17.79 23.79 16 26 16C28.21 16 30 17.79 30 20V24M30 20C30 17.79 31.79 16 34 16C36.21 16 38 17.79 38 20V24M38 22C38 19.79 39.79 18 42 18C44.21 18 46 19.79 46 22V32C46 41.94 39.94 48 30 48C20.06 48 16 41.94 16 36V28C16 25.79 17.79 24 20 24C22.21 24 24 25.79 24 28" stroke="#38BDF8" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="rgba(56, 189, 248, 0.12)"/><path d="M24 34H36M24 40H34" stroke="#93C5FD" stroke-width="2.5" stroke-linecap="round"/></svg>`,
    'Papel': `<svg class="svg-gesture" viewBox="0 0 64 64" fill="none"><path d="M20 28V14C20 12.34 21.34 11 23 11C24.66 11 26 12.34 26 14V26M26 14C26 12.34 27.34 11 29 11C30.66 11 32 12.34 32 14V26M32 16C32 14.34 33.34 13 35 13C36.66 13 38 14.34 38 16V26M38 19C38 17.34 39.34 16 41 16C42.66 16 44 17.34 44 19V34C44 43 38 49 29 49C20 49 16 43 16 36V28C16 26.34 17.34 25 19 25C20.66 25 22 26.34 22 28" stroke="#34D399" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="rgba(52, 211, 153, 0.12)"/><circle cx="29" cy="38" r="3" fill="#6EE7B7"/></svg>`,
    'Tijera': `<svg class="svg-gesture" viewBox="0 0 64 64" fill="none"><path d="M26 12L34 28M38 12L30 28" stroke="#C084FC" stroke-width="4" stroke-linecap="round"/><circle cx="24" cy="42" r="7" stroke="#C084FC" stroke-width="3.5" fill="rgba(192, 132, 252, 0.12)"/><circle cx="40" cy="42" r="7" stroke="#F472B6" stroke-width="3.5" fill="rgba(244, 114, 182, 0.12)"/><circle cx="32" cy="30" r="3" fill="#F472B6"/></svg>`
  };

  const rules = {
    'Piedra': 'Tijera',
    'Papel': 'Piedra',
    'Tijera': 'Papel'
  };

  const pGesture = document.getElementById('playerGesture');
  const pName = document.getElementById('playerName');
  const cGesture = document.getElementById('aiGesture');
  const cName = document.getElementById('aiName');
  const resultBadge = document.getElementById('simResult');
  const choiceBtns = document.querySelectorAll('.sim-choice-btn');

  if (!pGesture || !cGesture || !resultBadge) return;

  choiceBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const playerChoice = btn.getAttribute('data-choice');
      playSimRound(playerChoice);
    });
  });

  function playSimRound(playerChoice) {
    pGesture.innerHTML = svgs[playerChoice];
    pName.textContent = playerChoice;

    let count = 0;
    const interval = setInterval(() => {
      const rand = choices[Math.floor(Math.random() * choices.length)];
      cGesture.innerHTML = svgs[rand];
      cName.textContent = rand;
      count++;

      if (count > 6) {
        clearInterval(interval);
        finalizeSimRound(playerChoice);
      }
    }, 75);
  }

  function finalizeSimRound(playerChoice) {
    const aiChoice = choices[Math.floor(Math.random() * choices.length)];
    cGesture.innerHTML = svgs[aiChoice];
    cName.textContent = aiChoice;

    resultBadge.className = 'sim-result-badge';

    if (playerChoice === aiChoice) {
      resultBadge.classList.add('tie');
      resultBadge.textContent = `Empate: Ambos competidores eligieron ${playerChoice}.`;
      playTone(420, 'sine', 0.15);
    } else if (rules[playerChoice] === aiChoice) {
      resultBadge.classList.add('win');
      resultBadge.textContent = `Punto para el Jugador: ${playerChoice} neutraliza a ${aiChoice}.`;
      playTone(580, 'triangle', 0.2);
      setTimeout(() => playTone(820, 'triangle', 0.25), 140);
    } else {
      resultBadge.classList.add('lose');
      resultBadge.textContent = `Punto para la Máquina: ${aiChoice} neutraliza a ${playerChoice}.`;
      playTone(240, 'sawtooth', 0.25);
    }
  }
}

function playTone(freq, type = 'sine', duration = 0.2) {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    const ctx = new AudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = type;
    osc.frequency.setValueAtTime(freq, ctx.currentTime);

    gain.gain.setValueAtTime(0.06, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start();
    osc.stop(ctx.currentTime + duration);
  } catch (e) {
    // Autoplay restrictions or headless env
  }
}

function copyRunCommand() {
  navigator.clipboard.writeText('streamlit run app.py').then(() => {
    alert('Comando copiado al portapapeles: streamlit run app.py');
  });
}
