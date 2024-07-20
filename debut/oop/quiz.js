function Quiz(questions) {
  this.questions = questions;
  this.question_index = 0;
  this.nombredebonnesréponses = 0;
}

Quiz.prototype.apporter_question = function() {
  return this.questions[this.question_index];
}