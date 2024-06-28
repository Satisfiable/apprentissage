// objects

let utilisateur437 = {
  "prénom": "Jean",
  "nom": "Roseaux",
  "age": 26,
  "adresse": {"pays": "France", "ville": "Paris"},
  "loisirs": ["lire de livres", "faire de la randonnée"]
}

let résultat;

résultat = utilisateur437.adresse.pays;
résultat = utilisateur437.loisirs[0];
console.log(résultat);

let utilisateur438 = {
  "prénom": "Marx",
  "nom": "Pompier",
  "age": 31,
  "adresse": {"pays": "France", "ville": "Lyon"},
  "loisirs": ["faire de la cuisine", "peindre"]
}

let utilisateurs =  [utilisateur437, utilisateur438]
console.log(utilisateurs[1].adresse.ville)

let produits = [
  {"nomdeproduit": "iphone 11", "prixdeproduit": 10000},
  {"nomdeproduit": "iphone 12", "prixdeproduit": 11200}
]

console.log(produits[0].nomdeproduit);
console.log(produits[1].prixdeproduit);