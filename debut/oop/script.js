const quiz = new Quiz(questions);
const ui = new UI();

ui.btn_start.addEventListener("click", function() {
  ui.quiz_box.classList.add("active");
  TimeLine();
  commencer_minuteur(10);
  montrer_question(quiz.apporter_question());
  nombre_de_questions(quiz.question_index + 1, quiz.questions.length);
  document.querySelector(".card-footer").classList.remove("montrer");
});

ui.next_btn.addEventListener("click", function() {
  if (quiz.questions.length != quiz.question_index + 1) {
      quiz.question_index += 1;
      clearInterval(counter);
      clearInterval(counterLine);
      commencer_minuteur(10);
      TimeLine();
      montrer_question(quiz.apporter_question());
      nombre_de_questions(quiz.question_index + 1, quiz.questions.length);
      document.querySelector(".card-footer").classList.remove("montrer");
  }
  else {
      clearInterval(counter);
      clearInterval(counterLine);
      document.querySelector(".score_box").classList.add("active");
      document.querySelector(".quiz_box").classList.remove("active");
      document.querySelector(".score_text").insertAdjacentHTML("beforeend", `<span class="span_text">Vous avez répondu vrai à ${quiz.nombredebonnesréponses} questions sur ${quiz.questions.length}.</span>`)
  }
})

ui.btn_terminer.addEventListener("click", function() {
  window.location.reload();
});

ui.btn_recommencer.addEventListener("click", function() {
  quiz.question_index = 0;
  quiz.nombredebonnesréponses = 0;
  ui.btn_start.click();
  document.querySelector(".score_box").classList.remove("active");
  document.querySelector(".span_text").remove();
});

function montrer_question(variable) {
  let question = `<span>${variable.question_texte}</span>`;
  let réponses = '';
  for (let réponse_index in variable.réponses) {
      réponses += `<div class="option">
                      <span><b>${réponse_index}</b>: ${variable.réponses[réponse_index]}
                   </div>`
  }
  ui.option_list.innerHTML = réponses;

  const réponse = ui.option_list.querySelectorAll(".option");

  for (let opt of réponse) {
    opt.setAttribute("onClick", "réponse_choisi(this)"); // this: div
  }

  document.querySelector(".question_text").innerHTML = question;
}

function réponse_choisi(réponse) {
  clearInterval(counter);
  clearInterval(counterLine);
  let répondre = réponse.querySelector("span b").textContent;
  let question = quiz.apporter_question();

  if (question.controlerlaréponse(répondre)) {
    quiz.nombredebonnesréponses += 1;
    réponse.classList.add("correct");
    réponse.insertAdjacentHTML("beforeend", ui.correctIcon);
  }
  else {
    réponse.classList.add("incorrect");
    réponse.insertAdjacentHTML("beforeend", ui.incorrectIcon);
  }

  for (let i=0; i < ui.option_list.children.length; i++) {
    ui.option_list.children[i].classList.add("disabled");
  }

  document.querySelector(".card-footer").classList.add("montrer");
}

function nombre_de_questions(tour, total) {
  let tag = `<span class="badge bg-warning">${tour} / ${total}</span>`
  document.querySelector(".quiz_box .question_index").innerHTML = tag;
}

let counter;

function commencer_minuteur (temps) {
  counter = setInterval(minuteur, 1000);

  function minuteur () {
    ui.time_duration.textContent = temps;
    temps--;

    if (temps < 0) {
      clearInterval(counter);
      ui.time_text.textContent = "le temps est terminé";

      var réponse = quiz.apporter_question().bonne_réponse;
      for (let opt of ui.option_list.children) {
        if (opt.querySelector("span b").textContent == réponse) {
          opt.classList.add("correct");
          opt.insertAdjacentHTML("beforeend", ui.correctIcon);
        }
        opt.classList.add("disabled");
      }
    document.querySelector(".card-footer").classList.add("montrer");
    }
  }
}

let counterLine;

function TimeLine() {
  let line_width = 0;

  counterLine = setInterval (timer, 100);
  
  function timer() {
    line_width += 4.65;
    ui.time_line.style.width = line_width + "px";

    if (line_width > 508) {
      clearInterval(counterLine);    
    }
  }
}
