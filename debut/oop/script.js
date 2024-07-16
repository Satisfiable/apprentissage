// Constructor

function Question(question_texte, réponses, bonne_réponse) { // this indicates a copy of the function since we're going to use this function for tens of questions
    this.question_texte = question_texte;
    this.réponses = réponses;
    this.bonne_réponse = bonne_réponse;
    // console.log(this); // this = Constructor'dan üretilecek olan her bir nesne
}

// Prototype (Tekrarı azaltır)

Question.prototype.controlerlaréponse = function(réponse) {
    return réponse === this.bonne_réponse;
} 

let questions = [new Question("1-Qu'est-ce que JavaScript exactement?", {a: "C'est un livre.", b: "C'est une personne", c: "C'est un langage de programmation."}, "c"), 
    new Question("2-Qu'est-ce que JavaScript exactement?", {a: "C'est un livre.", b: "C'est une personne", c: "C'est un langage de programmation."}, "c"), 
        new Question("3-Qu'est-ce que JavaScript exactement?", {a: "C'est un livre.", b: "C'est une personne", c: "C'est un langage de programmation."}, "c"), 
        new Question("4-Qu'est-ce que JavaScript exactement?", {a: "C'est un livre.", b: "C'est une personne", c: "C'est un langage de programmation."}, "c")]

// console.log(question1.question_texte)
// console.log(question1.réponses)
// console.log(question1.bonne_réponse)

function Quiz(questions) {
    this.questions = questions;
    this.question_index = 0;
}

Quiz.prototype.apporter_question = function() {
    return this.questions[this.question_index];
}

const quiz = new Quiz(questions);

document.querySelector(".btn_start").addEventListener("click", function() {
    document.querySelector(".quiz_box").classList.add("active");
    montrer_question(quiz.apporter_question());
});

document.querySelector(".next_btn").addEventListener("click", function() {
    if (quiz.questions.length != quiz.question_index + 1) {
        quiz.question_index += 1;
        montrer_question(quiz.apporter_question());
    }
    else {
        alert("QUESTIONNAIRE EST FINI!")
    }
})

function montrer_question(variable) {
    let question = `<span>${variable.question_texte}</span>`;
    let réponses = '';
    for (let réponse_index in variable.réponses) {
        réponses += `<div class="option">
                        <span><b>${réponse_index}</b>: ${variable.réponses[réponse_index]}
                     </div>`
    }
    document.querySelector(".question_text").innerHTML = question;
    document.querySelector(".option_list").innerHTML = réponses;
}

