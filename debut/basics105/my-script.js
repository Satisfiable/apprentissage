function bonjour(msg) {
  console.log(msg);
}

bonjour("Salut!");
bonjour("Bonjour!");
bonjour("Je te souhaite une bonne journée.");

function calculationX(datedenaissance) {
  return new Date().getFullYear() - datedenaissance;
}

let agedoliver = calculationX(1975);
let agedemma =  calculationX(1999);

console.log(agedoliver, agedemma);

function retraite(datedenaissance, nom) {
  let age = calculationX(datedenaissance);
  let restedans = 65 - age;

  if (restedans > 0) {
    console.log(`Monsieur, Madame ${nom}; Il y a ${restedans} ans à vous retirer.`)
  }
  else {
    console.log(`Monsieur, Madame ${nom}; Vous vous êtes déjà retiré.`)
  }
}

retraite(1950, "Alicia");
retraite(1991, "Tommy");