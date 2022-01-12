const finalScore = document.querySelector('#scoreboard');
const mostRecentScore = localStorage.getItem('mostRecentScore');

finalScore.innerText = mostRecentScore;