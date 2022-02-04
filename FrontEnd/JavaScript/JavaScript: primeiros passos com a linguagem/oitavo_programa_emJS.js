console.log("Fluxo de interação");


// const salvador = `Salvador`;
// const saoPaulo = `São Paulo`;
// const rioDeJaneiro = `Rio de Janeiro`;

// Criando uma lista para armazenar as cidades
const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);

const idadeComprador = 17;
const estaAcompanhada = true;
let temPassagemComprada = false;
const destino = `Salvador`;


console.log(listaDeDestinos);

const podeComprar = idadeComprador >= 18 || estaAcompanhada == true

let contador = 0;
let destinoExiste = false;

while (contador < 3) {
    if (listaDeDestinos[contador] == destino) {
        destinoExiste = true;
        break;
    } 
    contador = contador + 1;
}


console.log("Destino existente: ", destinoExiste);

if (podeComprar && destinoExiste) {
    console.log("Boa viagem!");
}else{
    console.log("Infelizmente não pode ir");
}

for (let i = 0; i < 3; i++) {
    if (listaDeDestinos[i] == destino) {
        destinoExiste = true;
    }
}