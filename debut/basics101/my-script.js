console.log("C'est mon première code");

var rémunérationX = 750;
var rémunérationY = 900;

console.log(rémunérationX * 30);
console.log(rémunérationY * 30);

var nomdeproduit = "calculatrice"; // string
let prixdeproduit = 100; // number

console.log(typeof nomdeproduit);
console.log(typeof prixdeproduit);

var nombre1 = "1";
var nombre2 = "2";

console.log(Number(nombre1) + Number(nombre2));

var nombre3 = 3;
var nombre4 = 4;

console.log(nombre3.toString() + nombre4.toString());

let notedexamen = 52;
let succès = notedexamen >= 75;

console.log(succès);
console.log(typeof succès);

var id_étudiant555 = "22302955";
var motdepasse_étudiant555 = "723932";

var id_reçu = "223ada02955";
var motdepasse_reçu = "723932";

if (id_reçu == id_étudiant555) {
  if (motdepasse_reçu == motdepasse_étudiant555) {
    console.log("Bienvenue!");
  } else {
    console.log("Le mot de passe que tu es entré est faux. ");
  }
} else {
  console.log("Il n'y a pas d'utilisateur appelé " + id_reçu + ".");
}

var objet = "voiture";
var couleur = "bleu";

if (objet == "voiture" && couleur == "bleu") {
  console.log("Tu as gagné un voiture bleu.");
} else if (objet == "voiture" || couleur == "bleu") {
  console.log("Tu as gagné une bouteille bleu.");
} else {
  console.log("Tu n'as gagné aucun.");
}
