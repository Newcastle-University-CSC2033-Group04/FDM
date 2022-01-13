const finalScore = document.querySelector('#scoreboard');
const mostRecentScore = localStorage.getItem('mostRecentScore');

finalScore.innerText = mostRecentScore;

function sendScore() {
    let userScore = {
        'score': mostRecentScore,
    }
    const request = new XMLHttpRequest()
    request.open('POST', `/processScore/${JSON.stringify(userScore)}`)
    request.onload = () => {
        const flaskMessage = request.responseText
        console.log(flaskMessage)
    }
    request.send()
}