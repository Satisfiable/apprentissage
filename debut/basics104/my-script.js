for (let i = 0; i < 10; i++) {
  console.log(i);
}

let chiffres = [1,4,5,7,8,9]

for (let i = 0; i < chiffres.length; i++) {
  console.log(chiffres[i]);
}

let total = 0;

for (let indexnombre in chiffres) {
  console.log(indexnombre);
}

for (let nombre of chiffres) {
  console.log(nombre);
}

let utilisateur = {
  "prénom": "Alex",
  "nom": "Souza",
  "motdepasse": "72312187120",
  "email": "info@alexdesouza.com"
}

for (let x in utilisateur) {
  console.log(x);
}

for (let x in utilisateur) {
  console.log(utilisateur[x]);
}
