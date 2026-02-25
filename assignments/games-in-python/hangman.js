(() => {
  const words = [
    'hangman','python','challenge','variable','function','iteration','condition','module','package','developer'
  ];

  let secret = '';
  let correct = new Set();
  let wrong = new Set();
  let attempts = 6;

  const wordEl = document.getElementById('word');
  const wrongEl = document.getElementById('wrong');
  const attemptsEl = document.getElementById('attempts');
  const guessInput = document.getElementById('guess');
  const submitBtn = document.getElementById('submit');
  const newBtn = document.getElementById('new');
  const picEl = document.getElementById('hangman-pic');

  function choose() {
    return words[Math.floor(Math.random()*words.length)];
  }

  function render() {
    const revealed = secret.split('').map(c => correct.has(c) ? c : '_').join(' ');
    wordEl.textContent = revealed;
    wrongEl.textContent = wrong.size ? Array.from(wrong).sort().join(', ') : 'None';
    attemptsEl.textContent = attempts;
    picEl.textContent = '';
  }

  function checkWin() {
    if (secret.split('').every(c => correct.has(c))) {
      setTimeout(()=> alert(`You win! The word was '${secret}'.`), 10);
      return true;
    }
    if (attempts <= 0) {
      setTimeout(()=> alert(`Game over. The word was '${secret}'.`), 10);
      return true;
    }
    return false;
  }

  function start() {
    secret = choose();
    correct = new Set();
    wrong = new Set();
    attempts = 6;
    render();
  }

  function handleGuess() {
    const raw = guessInput.value.trim().toLowerCase();
    if (!raw) return;
    if (!/^[a-z]+$/.test(raw)) { alert('Please enter only letters.'); return; }

    if (raw.length === 1) {
      if (correct.has(raw) || wrong.has(raw)) { alert('Already tried.'); return; }
      if (secret.includes(raw)) {
        correct.add(raw);
      } else {
        wrong.add(raw);
        attempts -= 1;
      }
    } else {
      // full-word guess
      if (raw === secret) {
        secret.split('').forEach(c => correct.add(c));
      } else {
        attempts -= 1;
      }
    }

    guessInput.value = '';
    render();
    checkWin();
  }

  submitBtn.addEventListener('click', handleGuess);
  guessInput.addEventListener('keydown', (e)=> { if (e.key === 'Enter') handleGuess(); });
  newBtn.addEventListener('click', start);

  start();
})();
