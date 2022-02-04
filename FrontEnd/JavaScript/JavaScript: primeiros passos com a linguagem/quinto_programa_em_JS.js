console.log("Melhorando as atribuições");

const idade = 25;
let nome = "Igor";
const sobrenome = "Esposito";

// console.log(nome + "" + sobrenome + "" + idade);
console.log(nome, sobrenome, idade);
console.log(`Testendo com crase ${nome}`); 


// A variavel const não pode ser alterada, ou seja, não pode ser reatribuida.
// Ex
// nome = nome + " " + sobrenome;
// Para isso, usamos a variavel let.

nome = nome + " " + sobrenome;
console.log(nome);