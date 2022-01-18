// Questions JavaScript

const question = document.querySelector('#question');
const choices = Array.from(document.querySelectorAll('.choice-text'));
const progressText = document.querySelector('#progressText');
const scoreText = document.querySelector('#score');

let currentQuestion = {};
let acceptingAnswers = true;
let score = 0;
let questionCounter = 0;
let availableQuestions = [];

// Available questions
let questions = [
    {
        question: 'How many values do we have?',
        choice1: '6',
        choice2: '5',
        choice3: '7',
        choice4: '4',
        answer: 2,
    },
    {
        question: 'What is our values?',
        choice1: 'Together we are stronger',
        choice2: 'We make it happen',
        choice3: 'We say how it is',
        choice4: 'All of the above',
        answer: 4,
    },
    {
        question: 'We believe that ______ makes us stronger as one.',
        choice1: 'Diversity',
        choice2: 'Teamwork',
        choice3: 'Communication',
        choice4: 'Skill',
        answer: 1,
    },
    {
        question: "How do we exceed our clients' expectations?",
        choice1: "By being committed",
        choice2: "By being trustworthy",
        choice3: "By being ambitious and brave",
        choice4: "None of the above",
        answer: 3,
    },
    {
        question: "Which behaviour has made us the business we are today?",
        choice1: "Open",
        choice2: "Reliable",
        choice3: "Trustworthy",
        choice4: "All of the above",
        answer: 4,
    }
]

// 50 points will be granted for every correct answer
const SCORE_POINTS = 50;
const MAX_QUESTIONS = 5;

startGame = () => {
    questionCounter = 0;
    score = 0;
    availableQuestions = [...questions]
    getNewQuestion();
}

// A function to generate a new question in random after the user answers the current question.
getNewQuestion = () => {
    if(availableQuestions.length === 0 || questionCounter > MAX_QUESTIONS) {
        localStorage.setItem('mostRecentScore', score);
        return window.location.assign('/endPage');
    }
    questionCounter++
    progressText.innerText = `Question ${questionCounter} of ${MAX_QUESTIONS}`;

    const questionsIndex = Math.floor(Math.random() * availableQuestions.length);
    currentQuestion = availableQuestions[questionsIndex];
    question.innerText = currentQuestion.question;

    choices.forEach(choice => {
        const number = choice.dataset['number'];
        choice.innerText = currentQuestion['choice' + number];
    })

    availableQuestions.splice(questionsIndex, 1);

    acceptingAnswers = true;
}

choices.forEach(choice => {
    choice.addEventListener('click', e => {
        if(!acceptingAnswers) return;

        acceptingAnswers = false;
        const selectedChoice = e.target;
        const selectedAnswer = selectedChoice.dataset['number'];

        let classToApply = selectedAnswer == currentQuestion.answer ? 'correct' : 'incorrect';

        if (classToApply === 'correct') {
            incrementScore(SCORE_POINTS);
        }

        selectedChoice.parentElement.classList.add(classToApply);

        setTimeout(() => {
            selectedChoice.parentElement.classList.remove(classToApply);
            getNewQuestion();
        }, 1000)
    })
})

incrementScore = num => {
    score += num;
    scoreText.innerText = score;
}

startGame();
