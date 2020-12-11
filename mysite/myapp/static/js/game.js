const question = document.querySelector('#question')
const choices = Array.from(document.querySelectorAll('.choice-text'))
const progressText = document.querySelector('#progressText')
const scoreText = document.querySelector('#score')
const progressBarFull = document.querySelector('#progressBarFull')

let currentQuestion = {}
let acceptingAnswers = true
let score = 0
let questionsCounter = 0
let availableQuestions = []

let questions = [
    {
        question: 'Which galaxy is home to the Solar system?',
        choice1: 'Cigar',
        choice2: 'Milky Way',
        choice3: 'NGC 1300',
        choice4: 'Snickers',
        answer: 2,
    },
    {
        question: 'Which object lost its status as a planet in 2006?',
        choice1: 'Mars',
        choice2: 'Pluto',
        choice3: 'Venus',
        choice4: 'Earth',
        answer: 2,
    },
    {
        question: 'what is the Oort cloud?',
        choice1: 'Space gas',
        choice2: 'A dense build up of planets',
        choice3: 'Space dust',
        choice4: 'A hypothetical reservoir for comets',
        answer: 4,
    },
    {
        question: 'What is the third brightest astronomical object in the sky?',
        choice1: 'Orions Belt',
        choice2: 'The north star',
        choice3: 'Venus',
        choice4: 'Jupiter',
        answer: 2,
    },
    {
        question: 'How many moons does Mars have?',
        choice1: '6',
        choice2: '4',
        choice3: '2',
        choice4: '17',
        answer: 3,
    },
    {
        question: 'Who discovered the four main moons of Jupiter in 1610?',
        choice1: 'Nicolaus Copernicus 1543',
        choice2: 'Johannes Kepler 1630',
        choice3: 'Tycho Brahe 1601',
        choice4: 'Galileo Galilei 1610',
        answer: 4,
    },
    {
        question: 'What is the Solar Cycle?',
        choice1: 'The path the sun takes around the galaxy',
        choice2: 'Polarity reverse of the Sun',
        choice3: 'The path planets take around the sun',
        choice4: 'path the galaxy takes in the universe',
        answer: 2,
    },
    {
        question: 'What is the Hubble constant?',
        choice1: 'A unit of measurement used to describe earths density',
        choice2: 'A unit of measurement used to describe the width of the universe',
        choice3: 'A unit of measurement used to describe the density of the sun',
        choice4: 'A unit of measurement used to describe the expansion of the Universe',
        answer: 4,
    },
    {
        question: 'Hydrogen and which other gas make up the majority of the Suns composition?',
        choice1: 'Helium',
        choice2: 'Oxygen',
        choice3: 'Argon',
        choice4: 'Neon',
        answer: 1,
    },
    {
        question: 'Which star is closest to the Sun?',
        choice1: 'UV Ceti A & B (4.24 light years)',
        choice2: 'Alpha Centauri (4.24 light years)',
        choice3: 'Wolf 359 (4.24 light years)',
        choice4: 'Proxima Centauri (4.24 light years)',
        answer: 4,
    },
    {
        question: 'Vesta is which type of heavenly body?',
        choice1: 'Asteroid',
        choice2: 'meteor',
        choice3: 'planet',
        choice4: 'star',
        answer: 1,
    },
    {
        question: 'The comet with the shortest orbital period of 3.3 years is named what?',
        choice1: 'Unicorn',
        choice2: 'Encke',
        choice3: 'Billy',
        choice4: 'CNx76',
        answer: 2,
    },
    {
        question: 'Which planet has the largest moon in the Solar system?',
        choice1: 'Earth (Moon)',
        choice2: 'Saturn (Gilda)',
        choice3: 'Uranus (Bertha)',
        choice4: 'Jupiter (Ganymede)',
        answer: 4,
    },
    {
        question: 'What is a pulsar?',
        choice1: 'A dead star',
        choice2: 'A highly magnetised rotating neutron star',
        choice3: 'A slowly rotating star',
        choice4: 'An exploding star',
        answer: 2,
    },
    {
        question: 'How many terrestrial planets are there in the Solar system?',
        choice1: '6',
        choice2: '2',
        choice3: '4',
        choice4: '17',
        answer: 3,
    },
    {
        question: 'How many named constellations are there?',
        choice1: '6',
        choice2: '4',
        choice3: '88',
        choice4: '17',
        answer: 3,
    },
    {
        question: 'What is the name of the largest volcano in the Solar system?',
        choice1: 'Sinister Hill (Venus)',
        choice2: 'Everest (Earth)',
        choice3: 'Mt.Konocti (Earth',
        choice4: 'Olympus Mons (Mars)',
        answer: 4,
    },
    {
        question: 'Which three stars make the Summer Triangle?',
        choice1: 'Sirius, Betelgeuse, Rigel',
        choice2: 'Vega, Deneb, Altair',
        choice3: 'Antares, Deneb, Rigel',
        choice4: 'Vega, Pleiades, Altair',
        answer: 2,
    },
    {
        question: 'Who was the last man on the Moon?',
        choice1: 'Eugene Cernan',
        choice2: 'Niel Armstrong',
        choice3: 'Buzz Aldrin',
        choice4: 'Alan Bean',
        answer: 1,
    },
    {
        question: 'What is a supernova?',
        choice1: 'A small Star explosion',
        choice2: 'A star birthing',
        choice3: 'A powerful Star explosion',
        choice4: 'Planets colliding',
        answer: 3,
    },
    {
        question: 'What is an astronomical unit?',
        choice1: 'A measure of distance - 1 astronomical unit equals 193,000,000 miles',
        choice2: 'A measure of distance - 1 astronomical unit equals 293,000,000 miles',
        choice3: 'A measure of distance - 1 astronomical unit equals 393,000,000 miles',
        choice4: 'A measure of distance - 1 astronomical unit equals 93,000,000 miles',
        answer: 4,
    },
    {
        question: 'What is a Coronal Mass Ejection?',
        choice1: 'A small release of plasma from the Sun',
        choice2: 'A massive release of lava from the Sun',
        choice3: 'A massive release of plasma from the Sun',
        choice4: 'A massive release of gama rays from the Sun',
        answer: 3,
    },
    {
        question: 'How many Ice giants are in the Solar system?',
        choice1: '2',
        choice2: '4',
        choice3: '21',
        choice4: '17',
        answer: 1,
    },
    {
        question: 'What is the orbital period of Halley’s comet?',
        choice1: '6 years',
        choice2: '4 years',
        choice3: '76 years',
        choice4: '17 years',
        answer: 3,
    },
    {
        question: 'What is the escape velocity from the Solar system at the distance of Earth?',
        choice1: '2 kilometers per second',
        choice2: '42 kilometers per second',
        choice3: '21 kilometers per second',
        choice4: '9 kilometers per second',
        answer: 2,
    }
]

const SCORE_POINTS = 100
const MAX_QUESTIONS = 5

startGame = () => {
    questionsCounter = 0;
    score = 0;
    availableQuestions = [...questions]
    getNewQuestion()
}

getNewQuestion = () => {
    if(availableQuestions.length === 0 || questionsCounter >= MAX_QUESTIONS){
        localStorage.setItem('mostRecentScore', score)
        axios.get('/setscore/' + score, {})
            .then(function (response) {
            return window.location.assign('/leaderboard/')
            console.log(response);
        })
            .catch(function (error) {
            console.log(error);
        });
    }

    questionsCounter++
    progressText.innerText = `Question ${questionsCounter} of ${MAX_QUESTIONS}`
    progressBarFull.style.width = `${(questionsCounter/MAX_QUESTIONS) * 100}%`

    const questionIndex = Math.floor(Math.random() * availableQuestions.length)
    currentQuestion = availableQuestions[questionIndex]
    question.innerText = currentQuestion.question

    choices.forEach(choice => {
        const number = choice.dataset['number']
        choice.innerText = currentQuestion['choice' + number]
    })

    availableQuestions.splice(questionIndex, 1)

    acceptingAnswers = true
}

choices.forEach( choice => {
    choice.addEventListener('click', e=>{
        if(!acceptingAnswers) return

        acceptingAnswers= false
        const selectedChoice = e.target
        const selectedAnswer = selectedChoice.dataset['number']

        let classToApply = selectedAnswer == currentQuestion.answer ? 'correct' :'incorrect'

        if(classToApply === 'correct'){
            incrementScore(SCORE_POINTS)
        }

        selectedChoice.parentElement.classList.add(classToApply)
        setTimeout(() => {
            selectedChoice.parentElement.classList.remove(classToApply)
            getNewQuestion()
        }, 1000)
    })
})

incrementScore = num => {
    score += num
    scoreText.innerText = score
}

startGame()