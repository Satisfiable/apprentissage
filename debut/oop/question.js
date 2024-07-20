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

