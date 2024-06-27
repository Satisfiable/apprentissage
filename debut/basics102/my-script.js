let prénom = "Berkay Yavuz";
let nom = "Göcek";
let age = 72;
let ville = "Ankara";

// ternary operators ilki true: ikincisi false
let retraite =
  65 - age > 0
    ? "Il'y a " + (65 - age) + " ans à me retirer."
    : "Je me suis déjà retiré.";

// backtickge} ans à me retire
let message = `Je m'appelle ${prénom} ${nom}. Je vis à ${ville}. ${retraite}`;

console.log(message);

let maintenant = new Date();

// GET METHODS
résultat = maintenant;
résultat = maintenant.getDate(); // Jour
résultat = maintenant.getDay(); // 0: Dimanche, 6: Samedi
résultat = maintenant.getFullYear();
résultat = maintenant.getHours();
résultat = maintenant.getTime();

// SET METHODS...
maintenant.setMonth(0);

console.log(maintenant.getMonth());

let date_de_naissance = new Date(2004, 0, 18);
résultat = maintenant.getFullYear() - date_de_naissance.getFullYear();
console.log(résultat);

let étudiants = ["Çınar", "Yiğit", "Tevfik"];
résultat = étudiants.length;
résultat = étudiants.toString();
résultat = étudiants.join(" ");

résultat = étudiants.pop(); // son eleman silinir ve konsola geri döner.
résultat = étudiants.shift(); // ilk eleman silinir ve konsola geri döner.

résultat = étudiants.push("Sena"); // sona eleman ekler.
résultat = étudiants.unshift("Aslı"); // başa eleman ekler.

let écoles = ["Bilkent", "Boğaziçi", "ODTÜ"];
résultat = étudiants.concat(écoles); // arrayler birleştirilir.

console.log(résultat);
console.log(étudiants);
